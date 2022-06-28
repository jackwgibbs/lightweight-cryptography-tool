"""
Module to run the tool - includes main menu logic as well as the code to
call the relevant code constructs
"""

from Gift.gift_64 import *
from Gift.gift_128 import *
from Skinny.skinny import *
from Gift.gift_cofb import *
from Skinny.skinnyaead import *
from RC4 import *
from utils import *
from os import path

# descriptions of constructs implemented by the tool
# Block, Key, Nonce, AD, note -1 refers to N/A (where it is not required)
descriptions = {"GIFT-64": [64, 128, -1, -1, -1],
                "GIFT-128": [128, 128, -1, -1, -1],
                "SKINNY-64-64": [64, 64, -1, -1, -1],
                "SKINNY-64-128": [64, 128, -1, -1, -1],
                "SKINNY-64-192": [64, 192, -1, -1, -1],
                "SKINNY-128-128": [128, 128, -1, -1, -1],
                "SKINNY-128-256": [128, 256, -1, -1, -1],
                "SKINNY-128-384": [128, 384, -1, -1, -1],
                "GIFT-COFB": [128, 128, 128, 128, 128],
                "SKINNY-AEAD-M1": [128, 128, 128, 128],
                "SKINNY-AEAD-M2": [128, 128, 96, 128, 128],
                "SKINNY-AEAD-M3": [128, 128, 128, 128, 64],
                "SKINNY-AEAD-M4": [128, 128, 96, 128, 64]}


class Menu:
    def __init__(self):
        # main menu options
        self.mainMenu = {"1": "Encrypt", "2": "Decrypt", "3": "Generate MAC",
                         "4": "Verify MAC", "5": "AEAD", "6": "Verify AEAD"}

        # ciphers implemented
        self.ciphers = {"1": "GIFT-64", "2": "GIFT-128", "3": "SKINNY-64-64",
                        "4": "SKINNY-64-128", "5": "SKINNY-64-192",
                        "6": "SKINNY-128-128", "7": "SKINNY-128-256",
                        "8": "SKINNY-128-384"}

        # BC modes implemented
        self.options = {"1": "ECB", "2": "CTR (Inverse Free)", "3": "CBC"}

        # AEAD modes implemented
        self.AEAD = {"1": "GIFT-COFB (Inverse Free)", "2": "SKINNY-AEAD-M1",
                     "3": "SKINNY-AEAD-M2", "4": "SKINNY-AEAD-M3",
                     "5": "SKINNY-AEAD-M4"}

    @staticmethod
    def display(question):
        """
        Static method to display the prompt for the question.
        Parameters: the question to ask.
        Returns: none.
        """

        for key in question:
            print(key + ": " + question[key])

    @staticmethod
    def get_answer(valid_answer_list):
        """
        Static method to get the input from the user.
        Parameters: list of correct inputs from the user (not valid
        if input not in list).
        Returns: the answer/input from user.
        """

        choice = ""
        while choice not in valid_answer_list:
            choice = input("Your choice: ")
            if choice.lower() == "q":
                quit()
        print("\n")

        return choice

    def run_main_menu(self):
        """
        Method to run the main menu and collect options from user.
        Parameters: none.
        Returns: function (e.g. encrypt or AEAD), mode (e.g. ECB),
        BC (e.g. GIFT-64) and construct_name (e.g. GIFT-64).
        """

        completed = False
        while not completed:
            # Get which functionality the user wishes to use
            print()
            print("Select your option: ")
            self.display(self.mainMenu)
            function = self.get_answer(["1", "2", "3", "4", "5", "6", "s"])
            if function == "s":
                # check if user wishes to start over
                continue

            # if functionality to encrypt/decrypt is selected:
            if function == "1" or function == "2":

                # get the mode of encryption
                print("Select your mode of encryption/decryption:")
                self.display(self.options)
                mode = self.get_answer(["1", "2", "3", "s"])
                if mode == "s":
                    # check if user wishes to start over
                    continue

                # get the lightweight BC
                print("Select your lightweight cipher:")
                self.display(self.ciphers)
                BC = self.get_answer(
                    ["1", "2", "3", "4", "5", "6", "7", "8", "s"])
                if BC == "s":
                    # check if user wishes to start over
                    continue

                # determine the lightweight BCs name
                construct_name = self.ciphers[BC]

            # if functionality to generate/verify MAC is selected:
            elif function == "3" or function == "4":

                # get the lightweight BC to use
                print("Select your lightweight cipher:")
                self.display(self.ciphers)
                BC = self.get_answer(
                    ["1", "2", "3", "4", "5", "6", "7", "8", "s"])
                if BC == "s":
                    # check if user wishes to start over
                    continue
                mode = "1"

                # determine the lightweight BCs name
                construct_name = self.ciphers[BC]

            # if functionality to generate/verify AEAD is selected:
            elif function == "5" or function == "6":

                # get the AEAD mode to use
                print("Select your AEAD mode:")
                self.display(self.AEAD)
                mode = self.get_answer(["1", "2", "3", "4", "5", "s"])
                if mode == "s":
                    # check if user wishes to start over
                    continue
                if mode == "1":
                    BC = "2"
                    construct_name = "GIFT-COFB"
                else:
                    BC = "8"
                    construct_name = self.AEAD[mode]

            return function, mode, BC, construct_name


class lightweightTool:
    def __init__(self):
        # initialise options
        self.option = -1
        self.mode = -1
        self.cipher = -1
        self.filename = ""
        self.construct = ""
        self.construct_name = ""

    def run(self):
        """
        Main method to run the tool - calls the necessary construction.
        Parameters: none.
        Returns: none.
        """

        # run the main menu to get the user inputs
        menu = Menu()
        self.option, self.mode, self.cipher, \
            self.construct_name = menu.run_main_menu()

        # get the filename which contains the data
        valid = False
        while not valid:
            self.filename = input("Enter filename: ")
            if self.filename[-4:] != ".txt":
                self.filename += ".txt"
            valid = path.isfile(self.filename)
            if not valid:
                print("File not found, try again")
            print()

        # create cipher object
        if self.cipher == "1":
            self.construct = Gift64()
        elif self.cipher == "2":
            self.construct = Gift128()
        else:
            # anything else is SKINNY
            # define SKINNY versions
            skinny_versions = [[64, 64, 32], [64, 128, 36], [64, 192, 40],
                               [128, 128, 40], [128, 256, 48], [128, 384, 56]]

            # create skinny object with the correct version
            self.construct = Skinny(skinny_versions[int(self.cipher) - 3])

        # option 1 is to encrypt
        if self.option == "1":
            if self.mode == "1":
                # encrypt in ECB mode
                self.encrypt_ecb()

            elif self.mode == "2":
                # encrypt in CTR (inverse-free) mode - 1 means encrypting
                self.encrypt_ctr(1)

            elif self.mode == "3":
                # encrypt in CBC mode
                self.encrypt_cbc()

        # option 2 is to decrypt
        elif self.option == "2":
            if self.mode == "1":
                # decrypt in ECB mode
                self.decrypt_ecb()

            elif self.mode == "2":
                # decrypt in CTR (inverse-free) mode - 2 means decrypting
                self.encrypt_ctr(2)

            elif self.mode == "3":
                # decrypt in CBC mode
                self.decrypt_cbc()

        # option 3 is to generate MAC
        elif self.option == "3":
            # generate MAC
            self.encrypt_cbcmac()

        # option 4 is to verify MAC
        elif self.option == "4":
            # verify MAC
            self.verify_cbcmac()

        # option 5 is to run GIFT-COFB
        elif self.option == "5":
            if self.mode == "1":
                # run GIFT-COFB
                self.construct = GiftCofb()
            else:
                # run SKINNY-AEAD
                self.construct = SkinnyAead(self.construct_name,
                                            Skinny([128, 384, 56]))

            self.encrypt_aead()

        # option 6 is to verify GIFT-COFB
        elif self.option == "6":
            if self.mode == "1":
                # run GIFT-COFB verification
                self.construct = GiftCofb()
            else:
                # run SKINNY-AEAD verification
                self.construct = SkinnyAead(self.construct_name,
                                            Skinny([128, 384, 56]))

            self.verify_aead()

    def encrypt_ecb(self):
        """
        Method to encrypt under ECB mode.
        Parameters: none.
        Returns: none.
        """

        ciphertext = []

        # read in parameters from file and check their validity
        block_size = descriptions[self.construct_name][0]
        key_size = descriptions[self.construct_name][1]
        variables_dictionary = read_from_file(self.filename)
        variable_conditions = {"P": [False, 0, False],
                               "K": [False, key_size//4, True]}
        valid = check_input_validity(variables_dictionary, variable_conditions)
        if not valid:
            return

        # if inputs are checked to be valid, extract them into variables
        # and convert parameters from string to list formats
        inputs = extract_inputs(variables_dictionary, ["P", "K"])
        plaintext = inputs[0]
        key = inputs[1]
        plaintextList = string_to_list(plaintext)
        keyList = string_to_list(key)
        m_len = len(plaintextList)

        # split plaintext into 128-bit blocks
        blocks = divide_into_blocks(plaintextList, block_size, 1)

        # run ECB mode
        for block in blocks:
            ciphertext.append(self.construct.encrypt_block(block, keyList))

        # format data ready to be written to file
        data = {"Note": " Encrypted in ECB mode with " +
                str(self.construct_name), "P": plaintext, "K": key,
                "C": list_to_string(ciphertext), "L": str(m_len)}

        # write data to file
        write_to_file(self.filename, data)

    def decrypt_ecb(self):
        """
        Method to decrypt under ECB mode.
        Parameters: none.
        Returns: none.
        """

        plaintext = []

        # read in parameters from file and check their validity
        block_size = descriptions[self.construct_name][0]
        key_size = descriptions[self.construct_name][1]
        variables_dictionary = read_from_file(self.filename)
        variable_conditions = {"C": [False, 0, False],
                               "K": [False, key_size//4, True],
                               "L": [False, -1, True]}

        valid = check_input_validity(variables_dictionary, variable_conditions)
        if not valid:
            return

        # if inputs are checked to be valid, extract them into variables
        # and convert parameters from string to list formats
        inputs = extract_inputs(variables_dictionary, ["C", "K", "L"])
        ciphertext = inputs[0]
        key = inputs[1]
        m_len_input = inputs[2]
        m_len = plaintext_length(len(ciphertext), int(m_len_input))
        ciphertextList = string_to_list(ciphertext)
        keyList = string_to_list(key)

        # split plaintext into 128-bit blocks
        blocks = divide_into_blocks(ciphertextList, block_size, 2)

        # for every ciphertext block, decrypt the block and add to
        # plaintext list
        for block in blocks:
            plaintext.append(self.construct.decrypt_block(block, keyList))

        # format data ready to be written to file
        data = {"Note": " Decrypted in ECB mode with " +
                str(self.construct_name), "C": ciphertext, "K": key,
                "P": list_to_string(plaintext)[0:m_len], "L": str(m_len)}

        # write data to file
        write_to_file(self.filename, data)

    def encrypt_cbc(self):
        """
        Method to encrypt under CBC mode.
        Parameters: none.
        Returns: none.
        """

        ciphertext_blocks = []

        # read in parameters from file and check their validity
        block_size = descriptions[self.construct_name][0]
        key_size = descriptions[self.construct_name][1]
        variables_dictionary = read_from_file(self.filename)
        variable_conditions = {"P": [False, 0, False],
                               "K": [False, key_size // 4, True]}

        valid = check_input_validity(variables_dictionary, variable_conditions)
        if not valid:
            return

        # if inputs are checked to be valid, extract them into variables
        # and convert parameters from string to list formats
        inputs = extract_inputs(variables_dictionary, ["P", "K"])
        plaintext = inputs[0]
        key = inputs[1]
        plaintextList = string_to_list(plaintext)
        keyList = string_to_list(key)
        m_len = len(plaintextList)

        # split plaintext into 128-bit blocks
        blocks = divide_into_blocks(plaintextList, block_size, 1)
        IV = run_RC4(keyList, block_size//8)

        # initialise CBC mode
        x = xor_bits(blocks[0], IV)
        y = self.construct.encrypt_block(x, keyList)
        ciphertext_blocks.append(y)

        # iterate over each plaintext block
        for i in range(1, len(blocks)):
            # XOR the current plaintext block and the result of the
            # previous encryption
            x = xor_bits(blocks[i], y)

            # Encrypt the xored plaintext block and previous encryption result
            y = self.construct.encrypt_block(x, keyList)
            ciphertext_blocks.append(y)

        # format data ready to be written to file
        data = {"Note": " Encrypted with CBC mode and "
                + str(self.construct_name), "P": plaintext, "K": key,
                "C": list_to_string(ciphertext_blocks), "L": str(m_len)}

        # write data to file
        write_to_file(self.filename, data)

    def decrypt_cbc(self):
        """
        Method to decrypt under CBC mode.
        Parameters: none.
        Returns: none.
        """

        plaintext_blocks = []

        # read in parameters from file and check their validity
        block_size = descriptions[self.construct_name][0]
        key_size = descriptions[self.construct_name][1]
        variables_dictionary = read_from_file(self.filename)
        variable_conditions = {"C": [False, 0, False],
                               "K": [False, key_size // 4, True]}

        valid = check_input_validity(variables_dictionary, variable_conditions)
        if not valid:
            return

        # if inputs are checked to be valid, extract them into variables
        # and convert parameters from string to list formats
        inputs = extract_inputs(variables_dictionary, ["C", "K", "L"])
        ciphertext = inputs[0]
        key = inputs[1]
        m_len = inputs[2]
        m_len_input = inputs[2]
        m_len = plaintext_length(len(ciphertext), int(m_len_input))
        ciphertext_list = string_to_list(ciphertext)
        keyList = string_to_list(key)

        # split plaintext into 128-bit blocks
        blocks = divide_into_blocks(ciphertext_list, block_size, 2)
        IV = run_RC4(keyList, block_size // 8)

        # initialise CBC MAC mode
        y = self.construct.decrypt_block(blocks[0], keyList)
        x = xor_bits(y, IV)
        plaintext_blocks.append(x)

        # iterate over each block
        for i in range(1, len(blocks)):
            # xor the current plaintext block and the result of the
            # previous encryption
            y = self.construct.decrypt_block(blocks[i], keyList)
            x = xor_bits(blocks[i - 1], y)

            # Encrypt the xored plaintext block and previous encryption result
            plaintext_blocks.append(x)

        # format data ready to be written to file
        data = {"Note": " Decrypted with CBC mode and "
                + str(self.construct_name), "C": ciphertext, "K": key,
                "P": list_to_string(plaintext_blocks)[0:m_len],
                "L": str(m_len)}

        # format data ready to be written to file
        write_to_file(self.filename, data)

    def encrypt_ctr(self, operation):
        """
        Method to encrypt/decrypt under CTR mode. Note CTR is inverse-free.
        Parameters: operation, 1 for encryption, 2 for decryption.
        Returns: none.
        """

        ciphertext_blocks = []

        # read in parameters from file and check their validity
        block_size = descriptions[self.construct_name][0]
        key_size = descriptions[self.construct_name][1]
        variables_dictionary = read_from_file(self.filename)

        # specify variable conditions - note different variables (P or C)
        # for encrypting and decrypting
        if operation == 1:
            variable_conditions = {"P": [False, 0, False],
                                   "K": [False, key_size // 4, True]}
        else:
            variable_conditions = {"C": [False, 0, False],
                                   "K": [False, key_size // 4, True]}

        valid = check_input_validity(variables_dictionary, variable_conditions)
        if not valid:
            return

        # if inputs are checked to be valid, extract them into variables
        # and convert parameters from string to list formats
        if operation == 1:
            inputs = extract_inputs(variables_dictionary, ["P", "K"])
        else:
            inputs = extract_inputs(variables_dictionary, ["C", "K", "L"])

        plaintext = inputs[0]
        key = inputs[1]
        plaintextList = string_to_list(plaintext)
        keyList = string_to_list(key)

        if operation == 2:
            m_len_input = inputs[2]
            m_len = plaintext_length(len(plaintext), int(m_len_input))
        else:
            m_len = len(plaintextList)

        # split plaintext into 64-bit blocks
        blocks = divide_into_blocks(plaintextList, block_size, operation)

        # generate the IV using the RC4 algorithm
        IV = run_RC4(keyList, block_size//8)

        # iterate over each block, encrypt the IV and xor to the block
        for block in blocks:
            x = xor_bits(block, self.construct.encrypt_block(IV[:], keyList))
            ciphertext_blocks.append(x)

            # increment last byte of the IV
            IV[-2:] = increment_byte(IV[-2:])

        # format data ready to be written to file (note different message
        # for encrypting/decrypting
        if operation == 1:
            data = {"Note": " Encrypted in CTR mode with " +
                self.construct_name, "P": plaintext, "K": key,
                    "C": list_to_string(ciphertext_blocks), "L": str(m_len)}
        else:
            data = {"Note": " Decrypted in CTR mode with " +
                    self.construct_name, "C": plaintext, "K": key,
                    "P": list_to_string(ciphertext_blocks)[0:m_len],
                    "L": str(m_len)}

        # format data ready to be written to file
        write_to_file(self.filename, data)

    def encrypt_cbcmac(self):
        """
        Method to generate an authentication tag (MAC) using CBC-MAC mode.
        Parameters: none.
        Returns: none.
        """

        # read in parameters from file and check their validity
        block_size = descriptions[self.construct_name][0]
        key_size = descriptions[self.construct_name][1]
        variables_dictionary = read_from_file(self.filename)
        variable_conditions = {"P": [False, 0, False],
                               "K": [False, key_size // 4, True]}

        valid = check_input_validity(variables_dictionary, variable_conditions)
        if not valid:
            return

        # if inputs are checked to be valid, extract them into variables
        # and convert parameters from string to list formats
        inputs = extract_inputs(variables_dictionary, ["P", "K"])
        plaintext = inputs[0]
        key = inputs[1]
        plaintextList = string_to_list(plaintext)
        keyList = string_to_list(key)

        # split plaintext into 128-bit blocks
        blocks = divide_into_blocks(plaintextList, block_size, 1)

        # initialise CBC MAC mode
        x = xor_bits(blocks[0], [0]*(block_size//4))
        y = self.construct.encrypt_block(x, keyList)

        # iterate over each block
        for i in range(1, len(blocks)):
            # xor the current plaintext block and the result of the
            # previous encryption
            x = xor_bits(blocks[i], y)

            # encrypt the xored plaintext block and previous encryption result
            y = self.construct.encrypt_block(x, keyList)

        # format data ready to be written to file
        data = {"Note": "Generated MAC with CBC-MAC and " +
                self.construct_name, "P": plaintext, "K": key,
                "T": list_to_string(y)}

        # format data ready to be written to file
        write_to_file(self.filename, data)

    def verify_cbcmac(self):
        """
        Method to verify an authentication tag (MAC) using CBC-MAC mode.
        Parameters: none.
        Returns: none.
        """

        # read in parameters from file and check their validity
        block_size = descriptions[self.construct_name][0]
        key_size = descriptions[self.construct_name][1]
        variables_dictionary = read_from_file(self.filename)
        variable_conditions = {"P": [False, 0, False],
                               "K": [False, key_size // 4, True],
                               "T": [False, block_size // 4, True]}

        valid = check_input_validity(variables_dictionary, variable_conditions)
        if not valid:
            return

        # if inputs are checked to be valid, extract them into variables
        # and convert parameters from string to list formats
        inputs = extract_inputs(variables_dictionary, ["P", "K", "T"])
        plaintext = inputs[0]
        key = inputs[1]
        tag = inputs[2]
        plaintextList = string_to_list(plaintext)
        keyList = string_to_list(key)
        tagList = string_to_list(tag)

        # split plaintext into 128-bit blocks
        blocks = divide_into_blocks(plaintextList, block_size, 1)

        # initialise CBC MAC mode
        x = xor_bits(blocks[0], [0]*(block_size//4))
        y = self.construct.encrypt_block(x, keyList)

        # iterate over each block
        for i in range(1, len(blocks)):
            # xor the current plaintext block and the result of the previous
            # encryption
            x = xor_bits(blocks[i], y)

            # Encrypt the xored plaintext block and previous encryption result
            y = self.construct.encrypt_block(x, keyList)

        # format data ready to be written to file
        if y == tagList:
            data = {"Note": " Verified MAC with CBC-MAC mode and " +
                    self.construct_name, "P": plaintext, "K": key,
                    "T": list_to_string(y)}
        else:
            data = {"Note": " NOT verified MAC with CBC-MAC and " +
                    self.construct_name, "P": plaintext, "K": key,
                    "T": list_to_string(y)}

        # format data ready to be written to file
        write_to_file(self.filename, data)

    def encrypt_aead(self):
        """
        Method to run AEAD encryption.
        Parameters: none.
        Returns: none.
        """

        # read in parameters from file and check their validity
        block_size = descriptions[self.construct_name][0]
        key_size = descriptions[self.construct_name][1]
        nonce_size = descriptions[self.construct_name][2]
        variables_dictionary = read_from_file(self.filename)
        variable_conditions = {"P": [True, 0, False],
                               "K": [False, key_size // 4, True],
                               "N": [False, nonce_size // 4, True],
                               "A": [True, 0, False],
                               }

        valid = check_input_validity(variables_dictionary, variable_conditions)
        if not valid:
            return

        # if inputs are checked to be valid, extract them into variables
        inputs = extract_inputs(variables_dictionary, ["P", "A", "N", "K"])
        plaintext = inputs[0]
        AD = inputs[1]
        N = inputs[2]
        K = inputs[3]

        # convert parameters from string to list formats
        plaintextList = string_to_list(plaintext)
        ADList = string_to_list(AD)
        NList = string_to_list(N)
        KList = string_to_list(K)

        p_blocks = divide_into_blocks(plaintextList, block_size, 3)
        a_blocks = divide_into_blocks(ADList, block_size, 3)

        c, t = self.construct.encrypt(p_blocks, KList, a_blocks, NList)

        # format data ready to be written to file
        data = {"Note": " Encrypted with " + self.construct_name,
                "P": plaintext, "A": AD, "N": N, "K": K,
                "C": list_to_string(c), "T": list_to_string(t)}

        # write data to file
        write_to_file(self.filename, data)

    def verify_aead(self):
        """
        Method to run AEAD verification.
        Parameters: none.
        Returns: none.
        """

        block_size = descriptions[self.construct_name][0]
        key_size = descriptions[self.construct_name][1]
        nonce_size = descriptions[self.construct_name][2]
        tag_size = descriptions[self.construct_name][3]

        # read in parameters from file and check their validity
        variables_dictionary = read_from_file(self.filename)
        variable_conditions = {"C": [True, 0, False],
                               "K": [False, key_size // 4, True],
                               "N": [False, nonce_size // 4, True],
                               "A": [True, 0, False],
                               "T": [False, tag_size // 4, True]}

        valid = check_input_validity(variables_dictionary, variable_conditions)
        if not valid:
            return

        # if inputs are checked to be valid, extract them into variables
        inputs = extract_inputs(variables_dictionary,
                                ["C", "A", "N", "K", "T"])
        plaintext = inputs[0]
        AD = inputs[1]
        N = inputs[2]
        K = inputs[3]
        T = inputs[4]

        # convert parameters from string to list formats
        plaintextList = string_to_list(plaintext)
        ADList = string_to_list(AD)
        NList = string_to_list(N)
        KList = string_to_list(K)
        TList = string_to_list(T)
        p_blocks = divide_into_blocks(plaintextList, block_size, 3)
        a_blocks = divide_into_blocks(ADList, block_size, 3)

        p = self.construct.verify(p_blocks, KList, a_blocks, NList, TList)

        # format data ready to be written to file
        if p != [-1]:
            data = {"Note": " Verified and decrypted with " +
                    self.construct_name, "C": plaintext, "A": AD, "N": N,
                    "K": K, "P": list_to_string(p), "T": T}
        else:
            data = {"Note": " Decryption failed", "P": "", "A": AD, "N": N,
                    "K": K, "C": plaintext, "T": T}

        # write data to file
        write_to_file(self.filename, data)


if __name__ == '__main__':
    print("Welcome to this tool. Using this tool you can "
          "encrypt/decrypt, generate MACs, or apply AEAD encryption "
          "using the implemented lightweight constructs.")
    print("This tool implements: GIFT and SKINNY Block Ciphers, and "
          "a variety of encryption/AEAD modes")
    print("Type s to start over at any point or q to quit.")

    lightweightTool = lightweightTool()

    running = True
    while running:
        lightweightTool.run()
        run = input("Would you like to re-run the tool? (y/n)")
        if run.lower() == "n":
            running = False
