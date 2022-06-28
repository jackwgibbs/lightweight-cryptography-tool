"""
This module runs integration tests for ECB, CTR, CBC and CBC-MAC modes (code
in the main.py file - extracted here for tests without I/O)
"""

import sys
sys.path.append('..')
import unittest
from Gift.gift_64 import *
from RC4 import *


class TestECBMode(unittest.TestCase):
    """
    Integration test for ECB mode - tests extracted encrypt and decrypt block
    of code - test whether encrypted and decrypted block matches original
    plaintext
    """

    def setUp(self):
        # Set up GIFT-64 object
        self.gift64 = Gift64()

    def test_ecb_mode(self):
        """
        Test vector 1
        """

        c = Gift64()

        state = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]

        key = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
               0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

        ciphertext = []

        # run ECB mode - code block extracted from encrypt_ecb method
        for block in state:
            ciphertext.append(c.encrypt_block(block[:], key))

        plaintext = []

        # for every ciphertext block, decrypt the block and add to
        # plaintext list
        for block in ciphertext:
            plaintext.append(c.decrypt_block(block[:], key))

        self.assertEqual(state, plaintext,
                         "Decrypted message does not equal original message")

    def test_ctr_mode(self):
        """
        Integration test for CTR mode-tests extracted encrypt and decrypt block
        of code - test whether encrypted and decrypted block matches original
        plaintext
        """

        c = Gift64()

        state = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]

        key = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
               0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

        ciphertext = []

        # generate the IV using the RC4 algorithm
        IV = run_RC4(key, 64 // 8)

        # iterate over each block, encrypt the IV and xor to the block
        for block in state:
            x = xor_bits(block, c.encrypt_block(IV[:], key))
            ciphertext.append(x)

            # increment last byte of the IV
            IV[-2:] = increment_byte(IV[-2:])

        plaintext = []

        # generate the IV using the RC4 algorithm
        IV = run_RC4(key, 64 // 8)

        # iterate over each block, encrypt the IV and xor to the block
        for block in ciphertext:
            x = xor_bits(block, c.encrypt_block(IV[:], key))
            plaintext.append(x)

            # increment last byte of the IV
            IV[-2:] = increment_byte(IV[-2:])

        self.assertEqual(state, plaintext,
                         "Decrypted message does not equal original message")

    def test_cbc_mode(self):
        """
        Integration test for CBC mode-tests extracted encrypt and decrypt block
        of code - test whether encrypted and decrypted block matches original
        plaintext
        """

        c = Gift64()

        state = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]

        key = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
               0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

        ciphertext = []

        IV = run_RC4(key, 64 // 8)

        # initialise CBC mode
        x = xor_bits(state[0], IV)
        y = c.encrypt_block(x, key)
        ciphertext.append(y)

        # iterate over each plaintext block
        for i in range(1, len(state)):
            # XOR the current plaintext block and the result of the
            # previous encryption
            x = xor_bits(state[i], y)

            # Encrypt the xored plaintext block and previous encryption result
            y = c.encrypt_block(x, key)
            ciphertext.append(y)

        plaintext = []

        IV = run_RC4(key, 64 // 8)

        # initialise CBC MAC mode
        y = c.decrypt_block(ciphertext[0], key)
        x = xor_bits(y, IV)
        plaintext.append(x)

        # iterate over each block
        for i in range(1, len(ciphertext)):
            # xor the current plaintext block and the result of the
            # previous encryption
            y = c.decrypt_block(ciphertext[i], key)
            x = xor_bits(ciphertext[i - 1], y)

            # Encrypt the xored plaintext block and previous encryption result
            plaintext.append(x)

        self.assertEqual(state, plaintext,
                         "Decrypted message does not equal original message")

    def test_cbcmac_mode(self):
        """
        Integration test for CBC-MAC mode - tests extracted encrypt and decrypt
         block of code - test whether encrypted and decrypted block matches
         original plaintext
        """

        c = Gift64()

        state = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]

        key = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
               0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

        tag = []

        # initialise CBC MAC mode
        x = xor_bits(state[0], [0] * (64 // 4))
        tag = c.encrypt_block(x, key)

        # iterate over each block
        for i in range(1, len(state)):
            # xor the current plaintext block and the result of the
            # previous encryption
            x = xor_bits(state[i], tag)

            # encrypt the xored plaintext block and previous encryption result
            tag = c.encrypt_block(x, key)

        verified_tag = []

        # initialise CBC MAC mode
        x = xor_bits(state[0], [0] * (64 // 4))
        verified_tag = c.encrypt_block(x, key)

        # iterate over each block
        for i in range(1, len(state)):
            # xor the current plaintext block and the result of the previous
            # encryption
            x = xor_bits(state[i], verified_tag)

            # Encrypt the xored plaintext block and previous encryption result
            verified_tag = c.encrypt_block(x, key)

        self.assertEqual(tag, verified_tag,
                         "Decrypted message does not equal original message")


if __name__ == '__main__':
    unittest.main()
