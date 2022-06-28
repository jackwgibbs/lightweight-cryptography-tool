"""
Module to implement the GIFT-64 version of the GIFT block cipher
"""
from utils import *


class Gift64:
    def __init__(self):
        # define number of rounds in GIFT-64
        self.num_rounds = 28

        # 4-bit s-box for GIFT-64
        self.s_box = [0x1, 0xa, 0x4, 0xc, 0x6, 0xf, 0x3, 0x9, 0x2, 0xd, 0xb,
                      0x7, 0x5, 0x0, 0x8, 0xe]

        # 4-bit inverse S-box for GIFT-64
        self.s_box_inv = [0xD, 0x0, 0x8, 0x6, 0x2, 0xC, 0x4, 0xB, 0xE, 0x7,
                          0x1, 0xA, 0x3, 0x9, 0xF, 0x5]

        # p-box for GIFT-64 bit permutation
        self.p_box = [0, 17, 34, 51, 48, 1, 18, 35, 32, 49, 2, 19, 16, 33, 50,
                      3, 4, 21, 38, 55, 52, 5, 22, 39, 36, 53, 6, 23, 20, 37,
                      54, 7, 8, 25, 42, 59, 56, 9, 26, 43, 40, 57, 10, 27, 24,
                      41, 58, 11, 12, 29, 46, 63, 60, 13, 30, 47, 44, 61, 14,
                      31, 28, 45, 62, 15]

        # inverse p-box for GIFT-64 bit permutation
        self.p_box_inv = [0, 5, 10, 15, 16, 21, 26, 31, 32, 37, 42, 47, 48, 53,
                          58, 63, 12, 1, 6, 11, 28, 17, 22, 27, 44, 33, 38, 43,
                          60, 49, 54, 59, 8, 13, 2, 7, 24, 29, 18, 23, 40, 45,
                          34, 39, 56, 61, 50, 55, 4, 9, 14, 3, 20, 25, 30, 19,
                          36, 41, 46, 35, 52, 57, 62, 51]

        # define round constants
        self.round_constants = [0x01, 0x03, 0x07, 0x0F, 0x1F, 0x3E, 0x3D, 0x3B,
                                0x37, 0x2F, 0x1E, 0x3C, 0x39, 0x33, 0x27, 0x0E,
                                0x1D, 0x3A, 0x35, 0x2B, 0x16, 0x2C, 0x18, 0x30,
                                0x21, 0x02, 0x05, 0x0B, 0x17, 0x2E, 0x1C, 0x38,
                                0x31, 0x23, 0x06, 0x0D, 0x1B, 0x36, 0x2D, 0x1A,
                                0x34, 0x29, 0x12, 0x24, 0x08, 0x11, 0x22, 0x04]

        # set steps to True to print intermediate steps of process (debugging)
        self.steps = False

    def set_steps(self):
        """
        Method to set the steps attribute to True - meaning intermediate
        steps of encryption/decryption are outputted to the console -
        useful for debugging
        Parameters: None
        Returns: None
        """

        self.steps = True

    def encrypt_block(self, state, key):
        """
        Method to encrypt one block of data using GIFT-64.
        Parameters: 64-bit block plaintext to encrypt and 128-bit key.
        Returns: the encrypted ciphertext.
        """

        round_num = 0
        for i in range(0, self.num_rounds):
            # Step 1: Non-linear - Apply s-box
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
        Method to decrypt one block of data using GIFT-64.
        Parameters: the 64 bit block ciphertext to decrypt and 128-bit key.
        Returns: the decrypted plaintext.
        """

        # As decrypting, we need to calculate the round keys for each round -
        # we need the key for round 27 first so must calculate the round keys
        # up front - calculate_round_keys will do this
        round_keys = self.calculate_round_keys(key)
        round_num = 27

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
        Parameters: the current cipher state.
        Returns: cipher state with s-box applied.
        """

        # iterate over each nibble in state and apply s-box
        for i in range(0, 16):
            state[i] = self.s_box[state[i]]

        return state

    def apply_inv_s_box(self, state):
        """
        Method to apply the inverse s-box to the cipher state. For each 4-bit
        nibble in the cipher state, swap it with the corresponding nibble in
        the inverse s-box
        Parameters: the current cipher state.
        Returns: cipher state with inverse s-box applied.
        """

        # iterate over each nibble in state and apply inverse s-box
        for i in range(0, 16):
            state[i] = self.s_box_inv[state[i]]

        return state

    def apply_p_box(self, state):
        """
        Method to apply the p-box to the cipher state. For each character in
        the state, move it to the specified bit location.
        Parameters: the current cipher state.
        Returns: the state with the p-box applied to it.
        """

        # create a new list to store the updated cipher state
        new_state = [0 for x in range(64)]

        # convert cipher state to bits
        bit_state = convert_to_bits_rev(state)

        # apply the p-box
        for i in range(0, 64):
            new_state[self.p_box[i]] = bit_state[i]

        # convert state from bits to hex
        state = convert_from_bits_rev(new_state, 64)

        return state

    def apply_inv_p_box(self, state):
        """
        Method to apply the inverse p-box to the cipher state. For each
        character in the state, move it to the specified bit location.
        Parameters: the current cipher state.
        Returns: the state with the inverse p-box applied to it.
        """

        # define new state and convert current state to bit representation
        new_state = [0 for x in range(64)]
        bit_state = convert_to_bits_rev(state)

        # apply p-box to the cipher state
        for i in range(0, 64):
            new_state[self.p_box_inv[i]] = bit_state[i]

        # convert new state back into hex from bits
        state = convert_from_bits_rev(new_state, 64)

        return state

    def apply_round_key(self, bit_state, key, round_num):
        """
        Method to apply the round key and the round constant to the current
        cipher state.
        Parameters: the current cipher state, the round key, and round number.
        Returns: the state with the round key and constant applied.
        """

        # convert key and cipher state to bit form
        key_bits = convert_to_bits_rev(key)
        bit_state = convert_to_bits_rev(bit_state)

        # extract the U and V round key from the key
        u = key_bits[16:32]
        v = key_bits[0:16]

        # add round key to cipher state
        for i in range(0, 16):
            bit_state[4 * i] ^= v[i]
            bit_state[4 * i + 1] ^= u[i]

        # get the round constant and convert it to bits
        round_constant = self.round_constants[round_num]
        round_constant_bits = convert_round_constant_to_bits(round_constant)

        # apply the round constant to cipher state
        bit_state[63] ^= 1
        bit_state[23] ^= round_constant_bits[5]
        bit_state[19] ^= round_constant_bits[4]
        bit_state[15] ^= round_constant_bits[3]
        bit_state[11] ^= round_constant_bits[2]
        bit_state[7] ^= round_constant_bits[1]
        bit_state[3] ^= round_constant_bits[0]

        # convert state from bits to hex
        state = convert_from_bits_rev(bit_state, 64)

        return state

    def update_key(self, key):
        """
        Method to update the key. Key is updated after each round.
        k7||k6||...||k1||k0 ← k1 ≫ 2||k0 ≫ 12||...||k3||k2.
        Parameters: the key state to update.
        Returns: the updated key state.
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

        num_rounds = 27
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
