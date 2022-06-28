"""
Module to implement the SKINNY block cipher and all six of its versions
"""
from utils import *


class Skinny:
    def __init__(self, version):
        # version contains [State size, key size, number of rounds]
        self.version = version
        # z is t/n (tweakey size / state size) - is either 1, 2 or 3
        self.z = self.version[1] // self.version[0]
        self.keys = []

        # SKINNY-64-X s-box
        self.s_box_64 = [12, 6, 9, 0, 1, 10, 2, 11, 3, 8, 5, 13, 4, 14, 7, 15]

        # SKINNY-128-X s-box
        self.s_box_128 = [0x65, 0x4c, 0x6a, 0x42, 0x4b, 0x63, 0x43, 0x6b, 0x55,
                          0x75, 0x5a, 0x7a, 0x53, 0x73, 0x5b, 0x7b, 0x35, 0x8c,
                          0x3a, 0x81, 0x89, 0x33, 0x80, 0x3b, 0x95, 0x25, 0x98,
                          0x2a, 0x90, 0x23, 0x99, 0x2b, 0xe5, 0xcc, 0xe8, 0xc1,
                          0xc9, 0xe0, 0xc0, 0xe9, 0xd5, 0xf5, 0xd8, 0xf8, 0xd0,
                          0xf0, 0xd9, 0xf9, 0xa5, 0x1c, 0xa8, 0x12, 0x1b, 0xa0,
                          0x13, 0xa9, 0x05, 0xb5, 0x0a, 0xb8, 0x03, 0xb0, 0x0b,
                          0xb9, 0x32, 0x88, 0x3c, 0x85, 0x8d, 0x34, 0x84, 0x3d,
                          0x91, 0x22, 0x9c, 0x2c, 0x94, 0x24, 0x9d, 0x2d, 0x62,
                          0x4a, 0x6c, 0x45, 0x4d, 0x64, 0x44, 0x6d, 0x52, 0x72,
                          0x5c, 0x7c, 0x54, 0x74, 0x5d, 0x7d, 0xa1, 0x1a, 0xac,
                          0x15, 0x1d, 0xa4, 0x14, 0xad, 0x02, 0xb1, 0x0c, 0xbc,
                          0x04, 0xb4, 0x0d, 0xbd, 0xe1, 0xc8, 0xec, 0xc5, 0xcd,
                          0xe4, 0xc4, 0xed, 0xd1, 0xf1, 0xdc, 0xfc, 0xd4, 0xf4,
                          0xdd, 0xfd, 0x36, 0x8e, 0x38, 0x82, 0x8b, 0x30, 0x83,
                          0x39, 0x96, 0x26, 0x9a, 0x28, 0x93, 0x20, 0x9b, 0x29,
                          0x66, 0x4e, 0x68, 0x41, 0x49, 0x60, 0x40, 0x69, 0x56,
                          0x76, 0x58, 0x78, 0x50, 0x70, 0x59, 0x79, 0xa6, 0x1e,
                          0xaa, 0x11, 0x19, 0xa3, 0x10, 0xab, 0x06, 0xb6, 0x08,
                          0xba, 0x00, 0xb3, 0x09, 0xbb, 0xe6, 0xce, 0xea, 0xc2,
                          0xcb, 0xe3, 0xc3, 0xeb, 0xd6, 0xf6, 0xda, 0xfa, 0xd3,
                          0xf3, 0xdb, 0xfb, 0x31, 0x8a, 0x3e, 0x86, 0x8f, 0x37,
                          0x87, 0x3f, 0x92, 0x21, 0x9e, 0x2e, 0x97, 0x27, 0x9f,
                          0x2f, 0x61, 0x48, 0x6e, 0x46, 0x4f, 0x67, 0x47, 0x6f,
                          0x51, 0x71, 0x5e, 0x7e, 0x57, 0x77, 0x5f, 0x7f, 0xa2,
                          0x18, 0xae, 0x16, 0x1f, 0xa7, 0x17, 0xaf, 0x01, 0xb2,
                          0x0e, 0xbe, 0x07, 0xb7, 0x0f, 0xbf, 0xe2, 0xca, 0xee,
                          0xc6, 0xcf, 0xe7, 0xc7, 0xef, 0xd2, 0xf2, 0xde, 0xfe,
                          0xd7, 0xf7, 0xdf, 0xff]

        # SKINNY-64-X Inverse s-box
        self.s_box_64_inv = [3, 4, 6, 8, 12, 10, 1, 14, 9, 2, 5, 7, 0, 11, 13,
                             15]

        # SKINNY-128-X Inverse s-box
        self.s_box_128_inv = [0xac, 0xe8, 0x68, 0x3c, 0x6c, 0x38, 0xa8, 0xec,
                              0xaa, 0xae, 0x3a, 0x3e, 0x6a, 0x6e, 0xea, 0xee,
                              0xa6, 0xa3, 0x33, 0x36, 0x66, 0x63, 0xe3, 0xe6,
                              0xe1, 0xa4, 0x61, 0x34, 0x31, 0x64, 0xa1, 0xe4,
                              0x8d, 0xc9, 0x49, 0x1d, 0x4d, 0x19, 0x89, 0xcd,
                              0x8b, 0x8f, 0x1b, 0x1f, 0x4b, 0x4f, 0xcb, 0xcf,
                              0x85, 0xc0, 0x40, 0x15, 0x45, 0x10, 0x80, 0xc5,
                              0x82, 0x87, 0x12, 0x17, 0x42, 0x47, 0xc2, 0xc7,
                              0x96, 0x93, 0x03, 0x06, 0x56, 0x53, 0xd3, 0xd6,
                              0xd1, 0x94, 0x51, 0x04, 0x01, 0x54, 0x91, 0xd4,
                              0x9c, 0xd8, 0x58, 0x0c, 0x5c, 0x08, 0x98, 0xdc,
                              0x9a, 0x9e, 0x0a, 0x0e, 0x5a, 0x5e, 0xda, 0xde,
                              0x95, 0xd0, 0x50, 0x05, 0x55, 0x00, 0x90, 0xd5,
                              0x92, 0x97, 0x02, 0x07, 0x52, 0x57, 0xd2, 0xd7,
                              0x9d, 0xd9, 0x59, 0x0d, 0x5d, 0x09, 0x99, 0xdd,
                              0x9b, 0x9f, 0x0b, 0x0f, 0x5b, 0x5f, 0xdb, 0xdf,
                              0x16, 0x13, 0x83, 0x86, 0x46, 0x43, 0xc3, 0xc6,
                              0x41, 0x14, 0xc1, 0x84, 0x11, 0x44, 0x81, 0xc4,
                              0x1c, 0x48, 0xc8, 0x8c, 0x4c, 0x18, 0x88, 0xcc,
                              0x1a, 0x1e, 0x8a, 0x8e, 0x4a, 0x4e, 0xca, 0xce,
                              0x35, 0x60, 0xe0, 0xa5, 0x65, 0x30, 0xa0, 0xe5,
                              0x32, 0x37, 0xa2, 0xa7, 0x62, 0x67, 0xe2, 0xe7,
                              0x3d, 0x69, 0xe9, 0xad, 0x6d, 0x39, 0xa9, 0xed,
                              0x3b, 0x3f, 0xab, 0xaf, 0x6b, 0x6f, 0xeb, 0xef,
                              0x26, 0x23, 0xb3, 0xb6, 0x76, 0x73, 0xf3, 0xf6,
                              0x71, 0x24, 0xf1, 0xb4, 0x21, 0x74, 0xb1, 0xf4,
                              0x2c, 0x78, 0xf8, 0xbc, 0x7c, 0x28, 0xb8, 0xfc,
                              0x2a, 0x2e, 0xba, 0xbe, 0x7a, 0x7e, 0xfa, 0xfe,
                              0x25, 0x70, 0xf0, 0xb5, 0x75, 0x20, 0xb0, 0xf5,
                              0x22, 0x27, 0xb2, 0xb7, 0x72, 0x77, 0xf2, 0xf7,
                              0x2d, 0x79, 0xf9, 0xbd, 0x7d, 0x29, 0xb9, 0xfd,
                              0x2b, 0x2f, 0xbb, 0xbf, 0x7b, 0x7f, 0xfb, 0xff]

        # round constants for SKINNY
        self.constants = [0x01, 0x03, 0x07, 0x0F, 0x1F, 0x3E, 0x3D, 0x3B,
                          0x37, 0x2F, 0x1E, 0x3C, 0x39, 0x33, 0x27, 0x0E,
                          0x1D, 0x3A, 0x35, 0x2B, 0x16, 0x2C, 0x18, 0x30,
                          0x21, 0x02, 0x05, 0x0B, 0x17, 0x2E, 0x1C, 0x38,
                          0x31, 0x23, 0x06, 0x0D, 0x1B, 0x36, 0x2D, 0x1A,
                          0x34, 0x29, 0x12, 0x24, 0x08, 0x11, 0x22, 0x04,
                          0x09, 0x13, 0x26, 0x0c, 0x19, 0x32, 0x25, 0x0a,
                          0x15, 0x2a, 0x14, 0x28, 0x10, 0x20]

        # key size, nonce size, tag size for each member version
        self.AEAD_sizes = {"M1": [128, 128, 128],
                           "M2": [128, 96, 128],
                           "M3": [128, 128, 64],
                           "M4": [128, 96, 64]}

        # set steps to True to print intermediate steps of process (debugging)
        self.steps = False

    def set_steps(self):
        """
        Method to set the steps attribute to True - meaning intermediate
        steps of encryption/decryption are outputted to the console -
        useful for debugging
        Parameters: none
        Returns: none
        """

        self.steps = True

    def encrypt_block(self, plaintext, key):
        """
        Method to encrypt one plaintext block with SKINNY
        Parameters: the plaintext block to encrypt and key
        Returns: the encrypted ciphertext
        """

        # initialise the plaintext and key into the cipher state (IS)
        # and key state
        IS = self.initialise_state(plaintext)
        key = self.initialise_key(key)

        for i in range(0, self.version[2]):

            IS = self.sub_cells(IS)
            if self.steps:
                print("Round " + str(i))
                print("State After SubCells: " + str(IS))

            IS = self.add_round_constant(IS, i)
            if self.steps:
                print("State After Add Constant: " + str(IS))

            IS = self.add_round_tweakey(IS, key)
            if self.steps:
                print("State After Add TK: " + str(IS))

            IS = self.shift_rows(IS)
            if self.steps:
                print("State After Shift Rows: " + str(IS))

            IS = self.mix_columns(IS)
            if self.steps:
                print("State After Mix Columns: ", str(IS))

            key = self.update_tweakey_arrays(key)
            if self.steps:
                print("Updated TK: ", str(key))
                print()

        IS = sum(IS, [])
        if self.version[0] == 128:
            IS = decimal_to_hex(IS)

        return IS

    def decrypt_block(self, plaintext, TK):
        """
        Method to decrypt one ciphertext block with SKINNY
        Parameters: the ciphertext block to decrypt and key
        Returns: the decrypted plaintext
        """

        # initialise the ciphertext and key into the cipher state (IS)
        # and key state
        IS = self.initialise_state(plaintext)
        TW = self.initialise_key(TK)

        # as decrypting need to generate the set of round keys
        self.keys = self.generate_round_keys(TW)

        for i in range(self.version[2] - 1, -1, -1):
            IS = self.mix_columns_inv(IS)
            if self.steps:
                print("Round " + str(i))
                print("State After Inv Mix Columns: ", str(IS))

            IS = self.shift_rows_inv(IS)
            if self.steps:
                print("State After Inv Shift Rows: " + str(IS))

            IS = self.add_round_tweakey(IS, self.keys[i])
            if self.steps:
                print("State After Add TK: " + str(IS))

            IS = self.add_round_constant(IS, i)
            if self.steps:
                print("State After Add Constant: " + str(IS))

            IS = self.sub_cells_inv(IS)
            if self.steps:
                print("State After SubCells: " + str(IS))
                print()

        IS = sum(IS, [])
        if self.version[0] == 128:
            IS = (decimal_to_hex(IS))

        return IS

    def initialise_key(self, key):
        """
        Method to initialise the key state. The key is stored in z 4x4 arrays,
        where z is t/n.
        Parameters: the key.
        Returns: The key initialised into tweakey arrays.
        """

        # if using SKINNY-64, each cell in the key state is 4 bits
        if self.version[0] == 64:
            keyNew = [[], [], []]
            for i in range(0, 16, 4):
                # initialise TK1
                keyNew[0].append(key[i:i + 4])

                # initialise TK2 if required
                if self.z == 2:
                    keyNew[1].append((key[16 + i:16 + i + 4]))

                # initialise TK2 and TK3 if required
                elif self.z == 3:
                    keyNew[1].append((key[16 + i:16 + i + 4]))
                    keyNew[2].append((key[32 + i:32 + i + 4]))

        elif self.version[0] == 128:
            # if using SKINNY-64, each cell in the key state is 8 bits
            decimal = hex_to_decimal(key)
            keyNew = []
            K1 = []
            K2 = []
            K3 = []

            for i in range(0, 4):
                K1.append(decimal[4 * i:4 * i + 4])
                if self.z == 2 or self.z == 3:
                    K2.append(decimal[4 * (i + 4):4 * (i + 4) + 4])
                if self.z == 3:
                    K3.append(decimal[4 * (i + 8):4 * (i + 8) + 8])

            keyNew.append(K1)
            keyNew.append(K2)
            keyNew.append(K3)

        return keyNew

    def initialise_state(self, state):
        """
        Method to load the state into the correct format as specified in the
        specification.
        Parameters: the plaintext block to encrypt/decrypt.
        Returns: the plaintext block initialised into a 4x4 array.
        """

        # 1. initialise the state of the cipher
        # (referred to as IS, as in the specification)
        IS = []

        # if using 64-bit block version:
        if self.version[0] == 64:
            for i in range(0, 16, 4):
                IS.append(state[i:i + 4])

        # if using 128-bit block version:
        elif self.version[0] == 128:
            state = hex_to_decimal(state)
            for i in range(0, 16, 4):
                IS.append(state[i:i + 4])

        return IS

    def update_tweakey_arrays(self, TW):
        """
        Method to perform the update function one each of the tweakey arrays.
        First, a permutation Pt is applied to each tweakey array, before an
        LFSR is applied to TK2 and TK3 (only first and second row).
        Parameters: the set of tweakey arrays.
        Returns: The tweakey arrays updated.
        """

        # first extract the three tweakey arrays from the key
        TK1, TK2, TK3 = extract_TK(TW, self.z)

        # next we apply the permutation to each tweakey array
        P = [9, 15, 8, 13, 10, 14, 12, 11, 0, 1, 2, 3, 4, 5, 6, 7]
        updated_TK1 = [0] * 16
        updated_TK2 = [0] * 16
        updated_TK3 = [0] * 16

        for i in range(0, 16):
            updated_TK1[i] = TK1[P[i]]
            if self.z == 2 or self.z == 3:
                updated_TK2[i] = TK2[P[i]]
            if self.z == 3:
                updated_TK3[i] = TK3[P[i]]

        # load tweakey arrays back into one larger array
        new_key = [[], [], []]
        for i in range(0, 16, 4):
            new_key[0].append(updated_TK1[i:i + 4])
            if self.z == 2 or self.z == 3:
                new_key[1].append(updated_TK2[i:i + 4])

            if self.z == 3:
                new_key[2].append(updated_TK3[i:i + 4])

        # lastly, we apply the LFSR to the second and third tweakey array
        if self.z == 2 or self.z == 3:
            # only update first and second row (i=2 rows, j=4 elements in row)
            for i in range(0, 2):
                for j in range(0, 4):
                    if self.version[0] == 64:
                        new_key[1][i][j] = LFSR(new_key[1][i][j], 2, 4)
                        if self.z == 3:
                            new_key[2][i][j] = LFSR(new_key[2][i][j], 3, 4)

                    else:
                        new_key[1][i][j] = LFSR(new_key[1][i][j], 2, 8)
                        if self.z == 3:
                            new_key[2][i][j] = LFSR(new_key[2][i][j], 3, 8)

        return new_key

    def generate_round_keys(self, key):
        """
        Method to generate a list of round keys. This is needed for decryption
        as the last round is run first, as opposed to encryption where rounds
        are run sequentially, and thus so too are the round keys.
        Parameters: the key state.
        Returns: a set of round keys.
        """

        # first round key is the original key (for use in round 0)
        round_keys = [key]
        for i in range(0, 56):
            # get the next updated round key and append to the round_keys list
            key = self.update_tweakey_arrays(key)
            round_keys.append(key)

        return round_keys

    def sub_cells(self, IS):
        """
        Method to apply an S-box to the current cipher state. A 4-bit s-box
        is applied when the plaintext size is 64 bits, and when the
        plaintext size is 128 bits, an 8-bit s-box is applied.
        Parameters: The current cipher state (4x4 matrix form).
        Returns: The current cipher state with the S-box applied.
        """

        # iterate over the 4x4 cipher state matrix and apply
        # s-box to each cell.
        for i in range(0, 4):
            for j in range(0, 4):
                if self.version[0] == 64:
                    # apply 4-bit S-box if plaintext size is 64 bits
                    IS[i][j] = self.s_box_64[IS[i][j]]
                elif self.version[0] == 128:
                    # apply 8-bit S-box if plaintext size is 128 bits
                    IS[i][j] = self.s_box_128[IS[i][j]]

        return IS

    def sub_cells_inv(self, IS):
        """
        Method to apply an inverse S-box to the current cipher state. A
        4-bit inverse s-box is applied when the plaintext size is 64 bits,
        and when the plaintext size is 128 bits, an inverse 8-bit s-box
        is applied.
        Parameters: the current cipher state (4x4 matrix form)
        Returns: the current cipher state with the inverse s-box applied
        """

        # iterate over the 4x4 cipher state matrix and apply
        # the inverse S-box to each cell.
        for i in range(0, 4):
            for j in range(0, 4):
                if self.version[0] == 64:
                    # apply inverse 4-bit S-box if plaintext size is 64 bits
                    IS[i][j] = self.s_box_64_inv[IS[i][j]]
                elif self.version[0] == 128:
                    # apply inverse 8-bit S-box if plaintext size is 128 bits
                    IS[i][j] = self.s_box_128_inv[IS[i][j]]

        return IS

    def add_round_constant(self, state, round_num):
        """
        Method to apply the round constants to the cipher state.
        Parameters: the current cipher state and the number of the round.
        Returns: the state after applying the round constants.
        """

        # define updated cells of the cipher state
        c0 = (self.constants[round_num] & 0xf)
        c1 = ((self.constants[round_num] >> 4) & 0x3)
        c2 = 0x2

        # apply the updated cells to the cipher state
        state[0][0] ^= c0
        state[1][0] ^= c1
        state[2][0] ^= c2

        return state

    def add_round_tweakey(self, state, TW):
        """
        Method to apply the round tweakey to the cipher state. The first and
        second rows of the tweakey arrays are xored to the cipher state.
        Parameters: The cipher state and array of tweakeys.
        Returns: The updated cipher state with the round tweakey added.
        """

        # iterate over first two rows of each tweakey array
        for i in range(0, 2):
            # iterate over each cell in the row
            for j in range(0, 4):
                # apply TK1
                state[i][j] ^= TW[0][i][j]

                # apply TK2 if required
                if self.z == 2:
                    state[i][j] ^= TW[1][i][j]

                # apply TK3 if required
                elif self.z == 3:
                    state[i][j] ^= TW[1][i][j]
                    state[i][j] ^= TW[2][i][j]

        return state

    def shift_rows(self, state):
        """
        Method to shift the rows of the cipher state.
        The permutation P = [0, 1, 2, 3, 7, 4, 5, 6, 10, 11, 8, 9, 13,
        14, 15, 12] is applied to shift the rows.
        Parameters: the cipher state.
        Returns: the cipher state with the rows shifted.
        """

        # define the updated state - initialised to zero
        updatedState = []
        updatedState.append([0, 0, 0, 0])
        updatedState.append([0, 0, 0, 0])
        updatedState.append([0, 0, 0, 0])
        updatedState.append([0, 0, 0, 0])

        # define how to shift the rows
        row1 = [0, 1, 2, 3]
        row2 = [3, 0, 1, 2]
        row3 = [2, 3, 0, 1]
        row4 = [1, 2, 3, 0]

        # apply the row shift
        for i in range(0, 4):
            updatedState[0][i] = state[0][row1[i]]
            updatedState[1][i] = state[1][row2[i]]
            updatedState[2][i] = state[2][row3[i]]
            updatedState[3][i] = state[3][row4[i]]

        return updatedState

    def shift_rows_inv(self, state):
        """
        Method to inverse shift the rows of the cipher state.
        Parameters: the cipher state with rows shifted.
        Returns: the cipher state with the rows inverse shifted.
        """

        # define the updated state - initialised to zero
        updatedState = []
        updatedState.append([0, 0, 0, 0])
        updatedState.append([0, 0, 0, 0])
        updatedState.append([0, 0, 0, 0])
        updatedState.append([0, 0, 0, 0])

        # define how to shift the rows
        row1 = [0, 1, 2, 3]
        row2 = [1, 2, 3, 0]
        row3 = [2, 3, 0, 1]
        row4 = [3, 0, 1, 2]

        # apply the row shift
        for i in range(0, 4):
            updatedState[0][i] = state[0][row1[i]]
            updatedState[1][i] = state[1][row2[i]]
            updatedState[2][i] = state[2][row3[i]]
            updatedState[3][i] = state[3][row4[i]]

        return updatedState

    def mix_columns(self, state):
        """
        Method to mix the columns of the cipher state.
        Parameters: the cipher state.
        Returns: the cipher state with the columns mixed.
        """

        # iterate over each column and mix columns
        for j in range(0, 4):
            state[1][j] ^= state[2][j]
            state[2][j] ^= state[0][j]
            state[3][j] ^= state[2][j]

            temp = state[3][j]
            state[3][j] = state[2][j]
            state[2][j] = state[1][j]
            state[1][j] = state[0][j]
            state[0][j] = temp

        return state

    def mix_columns_inv(self, state):
        """
        Method to inverse mix the columns of the cipher state.
        Parameters: the cipher state.
        Returns: the cipher state with the columns inverse mixed.
        """

        # iterate over each column and mix columns
        for j in range(0, 4):
            temp = state[3][j]
            state[3][j] = state[0][j]
            state[0][j] = state[1][j]
            state[1][j] = state[2][j]
            state[2][j] = temp

            state[3][j] ^= state[2][j]
            state[2][j] ^= state[0][j]
            state[1][j] ^= state[2][j]

        return state


def LFSR(state, TK, s):
    """
    Function to apply the SKINNY LFSR.
    Parameters: the state to apply the LFSR to, the number of the TK array (2
    or 3) and s, the size of each cell in the array (4 or 8 bits).
    Returns: the state with the LFSR applied.
    """

    if TK == 2:
        if s == 4:
            # apply LFSR if tweakey is tweakey array 2 and size of each element
            # is 4 bits
            bits = convert_to_bits([state])

            updated_bits = [bits[1], bits[2], bits[3],
                            bits[0] ^ bits[1]]
            state = convert_from_bits(updated_bits, 4)[0]

        elif s == 8:
            # apply LFSR if tweakey is tweakey array 2 and size of each element
            # is 8 bits
            bits = convert_to_eight_bits([state])
            updated_bits = [bits[1], bits[2], bits[3], bits[4], bits[5],
                            bits[6], bits[7], bits[0] ^ bits[2]]

            state = convert_from_eight_bits(updated_bits, 8)[0]

    elif TK == 3:
        if s == 4:
            # apply LFSR if tweakey is tweakey array 3 and size of each element
            # is 4 bits
            bits = convert_to_bits([state])

            updated_bits = [bits[0] ^ bits[3], bits[0], bits[1],
                            bits[2]]
            state = convert_from_bits(updated_bits, 4)[0]

        elif s == 8:
            # apply LFSR if tweakey is tweakey array 3 and size of each element
            # is 8 bits
            bits = convert_to_eight_bits([state])
            updated_bits = [bits[7] ^ bits[1], bits[0], bits[1], bits[2], bits[3],
                            bits[4], bits[5], bits[6]]

            state = convert_from_eight_bits(updated_bits, 8)[0]

    return state


def extract_TK(TW, num_TKs):
    """
    Function to extract tweakey arrays TK1, TK2, TK3 from a key.
    Parameters: the key and number of TKs to extract (1-3).
    Returns: the tweakey arrays, number of which specified in the parameters.
    """

    # define empty tweakey arrays
    TK1 = []
    TK2 = []
    TK3 = []

    for i in range(0, 4):
        for j in range(0, 4):
            TK1.append(TW[0][i][j])
            if num_TKs == 2:
                TK2.append(TW[1][i][j])
            elif num_TKs == 3:
                TK2.append(TW[1][i][j])
                TK3.append(TW[2][i][j])

    return TK1, TK2, TK3
