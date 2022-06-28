"""
This file runs integration tests for the GIFT-128 Bit-Sliced class
"""

import sys
sys.path.append('..')
import unittest
from Gift.gift128bitsliced import Gift128BitSliced
from utils import hex_to_decimal


class TestEncryptBlock(unittest.TestCase):
    """
    Integration tests for the encrypt_block method of the
    class.
    The three integration tests are taken from the 3 test vectors published on
    the official GIFT GitHub.
    """

    def setUp(self):
        # Set up GIFT-128-bit-sliced object
        self.gift_128_bit_sliced = Gift128BitSliced()

    def test_encrypt_block(self):
        """
        Official test vector 1
        """

        state = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        key = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        correct = [10, 9, 4, 10, 15, 7, 15, 9, 11, 10, 1, 8, 1, 13, 15, 9, 11,
                   2, 11, 0, 0, 14, 11, 7, 13, 11, 15, 10, 9, 3, 13, 15]

        self.assertEqual(self.gift_128_bit_sliced.encrypt_block(state, key),
                         correct, "Block not encrypted correctly")

    def test_encrypt_block2(self):
        """
        Official test vector 2
        """

        key = [14, 0, 8, 4, 1, 15, 8, 15, 11, 9, 0, 7, 8, 3, 1, 3, 6, 10, 10,
               8, 11, 7, 15, 1, 9, 2, 15, 5, 12, 4, 7, 4]
        key = hex_to_decimal(key)
        state = [14, 4, 9, 1, 12, 6, 6, 5, 5, 2, 2, 0, 3, 1, 12, 15, 0, 3, 3,
                 11, 15, 7, 1, 11, 9, 9, 8, 9, 14, 12, 11, 3]
        state = hex_to_decimal(state)
        correct = [3, 3, 3, 1, 14, 15, 12, 3, 10, 6, 6, 0, 4, 15, 9, 5, 9, 9,
                   14, 13, 4, 2, 11, 7, 13, 11, 12, 0, 2, 10, 3, 8]

        self.assertEqual(self.gift_128_bit_sliced.encrypt_block(state, key),
                         correct, "Block not encrypted correctly")


if __name__ == '__main__':
    unittest.main()
