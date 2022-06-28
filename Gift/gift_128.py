"""
Module to implement the GIFT-128 version of the GIFT block cipher
"""
from utils import *


class Gift128:
    def __init__(self):
        # define number of rounds in GIFT-128
        self.num_rounds = 40

        # 4-bit S-box for GIFT-128
        self.s_box = [0x1, 0xa, 0x4, 0xc, 0x6, 0xf, 0x3, 0x9, 0x2, 0xd,
                      0xb, 0x7, 0x5, 0x0, 0x8, 0xe]

        # 4-bit inverse S-box for GIFT-128
        self.s_box_inv = [0xD, 0x0, 0x8, 0x6, 0x2, 0xC, 0x4, 0xB, 0xE, 0x7,
                          0x1, 0xA, 0x3, 0x9, 0xF, 0x5]

        # p-box for GIFT-128
        self.p_box = [0, 33, 66, 99, 96, 1, 34, 67, 64, 97, 2, 35, 32, 65,
                      98, 3, 4, 37, 70, 103, 100, 5, 38, 71, 68, 101, 6, 39,
                      36, 69, 102, 7, 8, 41, 74, 107, 104, 9, 42, 75, 72, 105,
                      10, 43, 40, 73, 106, 11, 12, 45, 78, 111, 108, 13, 46,
                      79, 76, 109, 14, 47, 44, 77, 110, 15, 16, 49, 82, 115,
                      112, 17, 50, 83, 80, 113, 18, 51, 48, 81, 114, 19, 20,
                      53, 86, 119, 116, 21, 54, 87, 84, 117, 22, 55, 52, 85,
                      118, 23, 24, 57, 90, 123, 120, 25, 58, 91, 88, 121, 26,
                      59, 56, 89, 122, 27, 28, 61, 94, 127, 124, 29, 62, 95,
                      92, 125, 30, 63, 60, 93, 126, 31]

        # inverse p-box for GIFT-128
        self.p_box_inv = [0, 5, 10, 15, 16, 21, 26, 31, 32, 37, 42, 47, 48,
                          53, 58, 63, 64, 69, 74, 79, 80, 85, 90, 95, 96, 101,
                          106, 111, 112, 117, 122, 127, 12, 1, 6, 11, 28, 17,
                          22, 27, 44, 33, 38, 43, 60, 49, 54, 59, 76, 65, 70,
                          75, 92, 81, 86, 91, 108, 97, 102, 107, 124, 113, 118,
                          123, 8, 13, 2, 7, 24, 29, 18, 23, 40, 45, 34, 39, 56,
                          61, 50, 55, 72, 77, 66, 71, 88, 93, 82, 87, 104, 109,
                          98, 103, 120, 125, 114, 119, 4, 9, 14, 3, 20, 25, 30,
                          19, 36, 41, 46, 35, 52, 57, 62, 51, 68, 73, 78, 67,
                          84, 89, 94, 83, 100, 105, 110, 99, 116, 121, 126, 115]

        # define round constants
        self.round_constants = [0x01, 0x03, 0x07, 0x0F, 0x1F, 0x3E, 0x3D,
                                0x3B, 0x37, 0x2F, 0x1E, 0x3C, 0x39, 0x33,
                                0x27, 0x0E, 0x1D, 0x3A, 0x35, 0x2B, 0x16,
                                0x2C, 0x18, 0x30, 0x21, 0x02, 0x05, 0x0B,
                                0x17, 0x2E, 0x1C, 0x38, 0x31, 0x23, 0x06,
                                0x0D, 0x1B, 0x36, 0x2D, 0x1A]

        # set steps to True to print intermediate steps of process (debugging)
        self.steps = False

    def set_steps(self):
        """
        Method to set the steps attribute to True - meaning intermediate
        steps of encryption/decryption are outputted to the console -
        useful for debugging.
        Parameters: none.
        Returns: none.
        """

        self.steps = True

    def encrypt_block(self, state, key):
        """
        Method to encrypt one block of data using GIFT-128.
        Parameters: 128-bit block plaintext to encrypt and 128-bit key.
        Returns: the encrypted ciphertext.
        """

        round_num = 0
        for i in range(0, self.num_rounds):
            # Step 1: Non-linear - Apply the s-box
            state = self.apply_s_box(state)
            if self.steps:
                print("Round " + str(round_num) + ":")
                print("1. Apply S-box: " + str(state))

            # Step 2: Linear - Apply bit permutation
            state = self.apply_p_box(state)
            if self.steps:
                print("2. Apply P-box: " + str(state))

            # Step 3: Apply the round key and round constant
            state = self.apply_round_key(state, key, round_num)
            if self.steps:
                print("3. Add round key and constant: " + str(state))

            # Step 4: Update the key
            key = self.update_key(key)
            if self.steps:
                print("4. The Updated Key: " + str(key))
                print()
    
            round_num += 1

        return state

    def decrypt_block(self, state, key):
        """
        Method to decrypt one block of data using GIFT-128.
        Parameters: 128-bit block ciphertext to decrypt and 128-bit key.
        Returns: the decrypted plaintext.
        """

        # As decrypting, we need to calculate the round keys for each round -
        # we need the key for round 27 first so must calculate the round keys
        # up front - calculate_round_keys will do this
        round_keys = self.calculate_round_keys(key)
        round_num = 39

        for i in range(0, self.num_rounds):

            # get the round key for this round
            key = round_keys[round_num]

            # Step 1: Apply the round key and round constant
            state = self.apply_round_key(state, key, round_num)
            if self.steps:
                print("Round " + str(round_num) + ":")
                print("1. Add round key and constant: " + str(state))

            # Step 2: Linear - Apply perm bits
            state = self.apply_inv_p_box(state)
            if self.steps:
                print("2. Apply inverse P-box: " + str(state))

            # Step 3: Non-Linear - Apply S box
            state = self.apply_inv_s_box(state)
            if self.steps:
                print("3. Apply inverse S-box: " + str(state))
                print()

            round_num -= 1

        return state

    def apply_s_box(self, state):
        """
        Method to apply the S-box to the cipher state. For each 4-bit nibble
        in the cipher state, swap it with the corresponding nibble in the
        s-box.
        Parameters: cipher state.
        Returns: cipher state with s-box applied.
        """

        # iterate over each nibble in state and apply s-box
        for i in range(0, 32):
            state[i] = self.s_box[state[i]]

        return state

    def apply_inv_s_box(self, state):
        """
        Method to apply the inverse S-box to the cipher state. For each 4-bit
        nibble in the cipher state, swap it with the corresponding nibble in
        the inverse s-box.
        Parameters: cipher state.
        Returns: cipher state with inverse s-box applied.
        """

        # iterate over each nibble in state and apply inverse s-box
        for i in range(0, 32):
            state[i] = self.s_box_inv[state[i]]

        return state

    def apply_p_box(self, state):
        """
        Method to apply the p-box to the cipher state. For each character in
        the state, move it to the specified bit location.
        Parameters: the current cipher state.
        Returns: the cipher state with the p-box applied to it.
        """

        # create a new list to store the updated cipher state
        new_state = [0 for x in range(128)]

        # convert cipher state to bits
        bit_state = convert_to_bits_rev(state)

        # apply the p-box
        for i in range(0, 128):
            new_state[self.p_box[i]] = bit_state[i]

        # convert state from bits to hex
        state = convert_from_bits_rev(new_state, 128)

        return state

    def apply_inv_p_box(self, state):
        """
        Method to apply the inverse p-box to the cipher state. For each
        character in the state, move it to the specified bit location.
        Parameters: the current cipher state.
        Returns: the cipher state with the inverse p-box applied to it.
        """

        # define new state and convert current state to bit representation
        new_state = [0 for x in range(128)]
        bit_state = convert_to_bits_rev(state)

        # apply p-box to the cipher state
        for i in range(0, 128):
            new_state[self.p_box_inv[i]] = bit_state[i]

        # convert new state back into hex from bits
        state = convert_from_bits_rev(new_state, 128)

        return state

    def apply_round_key(self, state, key, round_num):
        """
        Method to apply the round key and the round constant to the current
        cipher state.
        Parameters: the current cipher state, the key, and round number.
        Returns: the state with the round key and constant applied.
        """

        # convert the key and the cipher state to their bit representation
        key_bits = convert_to_bits_rev(key)
        bit_state = convert_to_bits_rev(state)

        # extract the U and V round key from the key
        u = key_bits[64:96]
        v = key_bits[0:32]

        # add round key to cipher state
        for i in range(0, 32):
            bit_state[4 * i + 1] ^= v[i]
            bit_state[4 * i + 2] ^= u[i]

        # Get the round constant and convert it to its bit representation
        round_constant = self.round_constants[round_num]
        round_constant_bits = convert_round_constant_to_bits(round_constant)

        # apply the round constant to the cipher state
        bit_state[23] ^= round_constant_bits[5]
        bit_state[19] ^= round_constant_bits[4]
        bit_state[15] ^= round_constant_bits[3]
        bit_state[11] ^= round_constant_bits[2]
        bit_state[7] ^= round_constant_bits[1]
        bit_state[3] ^= round_constant_bits[0]
        bit_state[127] ^= 1

        # convert state from bits to hex
        state = convert_from_bits_rev(bit_state, 128)

        return state

    def update_key(self, key):
        """
        Method to update the key. Key is updated after each round.
        k7||k6||...||k1||k0 ← k1 ≫ 2||k0 ≫ 12||...||k3||k2.
        Parameters: The key state to update.
        Returns: The updated key state.
        """

        # apply k0 >>> 12
        k0 = [0 for x in range(4)]
        k0[0] = key[3]
        k0[1] = key[0]
        k0[2] = key[1]
        k0[3] = key[2]

        # apply k1 >>> 2
        k1_bits = [0 for x in range(16)]
        key_bits = convert_to_bits_rev(key[4:8])

        for i in range(0, 16):
            k1_bits[i] = key_bits[(i + 2) % 16]
        k1 = convert_from_bits_rev(k1_bits, 16)

        # shift k >>> 32
        updated_key = [0 for x in range(32)]
        for i in range(0, 32):
            updated_key[i] = key[(i + 8) % 32]

        # combine key together
        updated_key[24:48] = k0
        updated_key[28:32] = k1

        return updated_key

    def calculate_round_keys(self, key):
        """
        Method to determine all round keys and return them in a list.
        Parameters: the original key.
        Returns: a list of round keys where index position is the round key
        for that round.
        """

        num_rounds = 39
        round_keys = [0 for x in range(num_rounds + 1)]

        # round key for round 0 is the original key
        round_keys[0] = key[:]

        for round_num in range(1, num_rounds + 1):
            # get the next round key by updating the key
            key = self.update_key(key)

            # add to the keys list where position represents round number
            round_keys[round_num] = key[:]

        return round_keys


def convert_round_constant_to_bits(round_constant):
    """
    Function to convert the round constant to its bit representation.
    Parameter: the round constant.
    Returns: the round constant in its bit representation.
    """

    round_constant_bits = [0 for x in range(6)]
    for i in range(0, 6):
        round_constant_bits[i] = round_constant >> i & 0x1

    return round_constant_bits
