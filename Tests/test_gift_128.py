"""
This file runs unit and integration tests for the GIFT-128 class and all
its methods
"""

import sys
sys.path.append('..')
import unittest
from Gift.gift_128 import *


class TestApplySBox(unittest.TestCase):
    """
    Unit tests for the s_box method of the GIFT-128 class.
    The three unit tests are taken from the 3 test vectors published on the
    official GIFT GitHub.
    """

    def setUp(self):
        # Set up GIFT-128 object
        self.gift128 = Gift128()

    def test_apply_s_box(self):
        """
        Test vector 1
        """

        state = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        correct = [1, 10, 4, 12, 6, 15, 3, 9, 2, 13, 11, 7, 5, 0, 8, 14,
                   1, 10, 4, 12, 6, 15, 3, 9, 2, 13, 11, 7, 5, 0, 8, 14]
        self.assertEqual(self.gift128.apply_s_box(state), correct,
                         "S-box not applied correctly")

    def test_apply_s_box2(self):
        """
        Test vector 2
        """

        state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        correct = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(self.gift128.apply_s_box(state), correct,
                         "S-box not applied correctly")

    def test_apply_s_box3(self):
        """
        Test vector 3
        """

        state = [1, 12, 6, 8, 15, 1, 9, 10, 6, 11, 5, 8, 10, 8, 0, 15, 3, 4,
                 10, 11, 13, 7, 5, 10, 15, 1, 4, 1, 12, 9, 3, 14]

        correct = [10, 5, 3, 2, 14, 10, 13, 11, 3, 7, 15, 2, 11, 2, 1, 14, 12,
                   6, 11, 7, 0, 9, 15, 11, 14, 10, 6, 10, 5, 13, 12, 8]
        self.assertEqual(self.gift128.apply_s_box(state), correct,
                         "S-box not applied correctly")


class TestApplyPBox(unittest.TestCase):
    """
    Unit tests for the p_box method of the GIFT-128 class.
    The three unit tests are taken from the 3 test vectors published on the
    official GIFT GitHub.
    """

    def setUp(self):
        # Set up GIFT-128 object
        self.gift128 = Gift128()

    def test_apply_p_box(self):
        """
        Test vector 1
        """

        state = [1, 10, 4, 12, 6, 15, 3, 9, 2, 13, 11, 7, 5, 0, 8, 14,
                 1, 10, 4, 12, 6, 15, 3, 9, 2, 13, 11, 7, 5, 0, 8, 14]

        correct = [15, 10, 0, 9, 15, 10, 0, 9, 0, 7, 15, 8, 0, 7, 15, 8, 8, 13,
                   11, 6, 8, 13, 11, 6, 4, 3, 7, 4, 4, 3, 7, 4]

        self.assertEqual(self.gift128.apply_p_box(state), correct,
                         "P-box not applied correctly")

    def test_apply_p_box2(self):
        """
        Test vector 2
        """

        state = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        correct = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(self.gift128.apply_p_box(state), correct,
                         "P-box not applied correctly")

    def test_apply_p_box3(self):
        """
        Test vector 3
        """

        state = [10, 5, 3, 2, 14, 10, 13, 11, 3, 7, 15, 2, 11, 2, 1, 14, 12,
                 6, 11, 7, 0, 9, 15, 11, 14, 10, 6, 10, 5, 13, 12, 8]
        correct = [0, 14, 7, 11, 2, 12, 14, 13, 6, 11, 14, 2, 13, 9, 2, 12, 3,
                   15, 3, 3, 7, 11, 14, 12, 11, 8, 3, 12, 14, 3, 10, 1]

        self.assertEqual(self.gift128.apply_p_box(state), correct,
                         "P-box not applied correctly")


class TestAddingRoundKey(unittest.TestCase):
    """
    Unit tests for the apply_round_key method of the GIFT-128 class.
    The three unit tests are taken from the 3 test vectors published on the
    official GIFT GitHub.
    """

    def setUp(self):
        # Set up GIFT-128 object
        self.gift128 = Gift128()

    def test_adding_round_key1(self):
        """
        Test vector 1
        """

        state = [15, 10, 0, 9, 15, 10, 0, 9, 0, 7, 15, 8, 0, 7, 15, 8, 8, 13,
                 11, 6, 8, 13, 11, 6, 4, 3, 7, 4, 4, 3, 7, 4]
        correct = [7, 10, 0, 9, 9, 10, 0, 9, 0, 1, 15, 8, 6, 1, 15, 8, 8, 13,
                   13, 6, 14, 13, 13, 6, 4, 5, 1, 4, 2, 5, 1, 12]
        round_key = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                     0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(self.gift128.apply_round_key(state, round_key, 0),
                         correct, "Round key not added correctly")

    def test_adding_round_key2(self):
        """
        Test vector 2
        """

        state = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        correct = [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9]
        round_key = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(self.gift128.apply_round_key(state, round_key, 0),
                         correct,
                         "Round key not added correctly")

    def test_adding_round_key3(self):
        """
        Test vector 3
        """

        state = [0, 14, 7, 11, 2, 12, 14, 13, 6, 11, 14, 2, 13, 9, 2, 12, 3,
                 15, 3, 3, 7, 11, 14, 12, 11, 8, 3, 12, 14, 3, 10, 1]
        correct = [14, 14, 5, 13, 6, 12, 14, 9, 4, 9, 12, 0, 15, 13, 0, 12, 3,
                   15, 1, 5, 1, 15, 8, 8, 9, 12, 3, 10, 10, 1, 10, 15]
        round_key = [13, 0, 15, 5, 12, 5, 9, 10, 7, 7, 0, 0, 13, 3, 14, 7, 9,
                     9, 0, 2, 8, 15, 10, 9, 15, 9, 0, 10, 13, 8, 3, 7]
        self.assertEqual(self.gift128.apply_round_key(state, round_key, 0),
                         correct,
                         "Round key not added correctly")


class TestUpdateKey(unittest.TestCase):
    """
    Unit tests for the update_key method of the GIFT-128 class.
    The three unit tests are taken from the 3 test vectors published on the
    official GIFT GitHub.
    """

    def setUp(self):
        # Set up GIFT-128 object
        self.gift128 = Gift128()

    def test_update_key1(self):
        """
        Test vector 1
        """

        key = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
               0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        correct = [8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                   10, 11, 12, 13, 14, 15, 3, 0, 1, 2, 5, 9, 13, 1]
        self.assertEqual(self.gift128.update_key(key), correct,
                         "Key not updated correctly")

    def test_update_key2(self):
        """
        Test vector 2
        """

        key = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        correct = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(self.gift128.update_key(key), correct,
                         "Key not updated correctly")

    def test_update_key3(self):
        """
        Test vector 3
        """

        key = [7, 3, 8, 13, 10, 0, 9, 15, 9, 10, 15, 8, 2, 0, 9, 9, 7, 14, 3,
               13, 0, 0, 7, 7, 10, 9, 5, 12, 5, 15, 0, 13]
        correct = [9, 10, 15, 8, 2, 0, 9, 9, 7, 14, 3, 13, 0, 0, 7, 7, 10, 9,
                   5, 12, 5, 15, 0, 13, 13, 7, 3, 8, 2, 4, 14, 11]
        self.assertEqual(self.gift128.update_key(key), correct,
                         "Key not updated correctly")


class TestApplySBoxInv(unittest.TestCase):
    """
    Unit tests for the apply_inv_s_box method of the GIFT-128 class.
    The three unit tests are taken from the 3 test vectors published on the
    official GIFT GitHub.
    """

    def setUp(self):
        # Set up GIFT-128 object
        self.gift128 = Gift128()

    def test_apply_s_box_inv(self):
        """
        Test vector 1
        """

        state = [1, 10, 4, 12, 6, 15, 3, 9, 2, 13, 11, 7, 5, 0, 8, 14,
                 1, 10, 4, 12, 6, 15, 3, 9, 2, 13, 11, 7, 5, 0, 8, 14]
        correct = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                   0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(self.gift128.apply_inv_s_box(state), correct,
                         "Inverse S-box not applied correctly")

    def test_apply_s_box_inv2(self):
        """
        Test vector 2
        """

        state = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        correct = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(self.gift128.apply_inv_s_box(state), correct,
                         "Inverse S-box not applied correctly")

    def test_apply_s_box_inv3(self):
        """
        Test vector 3
        """

        state = [10, 5, 3, 2, 14, 10, 13, 11, 3, 7, 15, 2, 11, 2, 1, 14, 12,
                 6, 11, 7, 0, 9, 15, 11, 14, 10, 6, 10, 5, 13, 12, 8]

        correct = [1, 12, 6, 8, 15, 1, 9, 10, 6, 11, 5, 8, 10, 8, 0, 15, 3, 4,
                   10, 11, 13, 7, 5, 10, 15, 1, 4, 1, 12, 9, 3, 14]
        self.assertEqual(self.gift128.apply_inv_s_box(state), correct,
                         "Inverse S-box not applied correctly")


class TestApplyPBoxInv(unittest.TestCase):
    """
    Unit tests for the apply_inv_p_box method of the GIFT-128 class.
    The three unit tests are taken from the 3 test vectors published on the
    official GIFT GitHub.
    """

    def setUp(self):
        # Set up GIFT-128 object
        self.gift128 = Gift128()

    def test_apply_inv_p_box(self):
        """
        Test vector 1
        """

        state = [15, 10, 0, 9, 15, 10, 0, 9, 0, 7, 15, 8, 0, 7, 15, 8, 8, 13,
                 11, 6, 8, 13, 11, 6, 4, 3, 7, 4, 4, 3, 7, 4]

        correct = [1, 10, 4, 12, 6, 15, 3, 9, 2, 13, 11, 7, 5, 0, 8, 14,
                   1, 10, 4, 12, 6, 15, 3, 9, 2, 13, 11, 7, 5, 0, 8, 14]

        self.assertEqual(self.gift128.apply_inv_p_box(state), correct,
                         "Inverse P-box not applied correctly")

    def test_apply_inv_p_box2(self):
        """
        Test vector 2
        """

        state = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        correct = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(self.gift128.apply_inv_p_box(state), correct,
                         "Inverse P-box not applied correctly")

    def test_apply_inv_p_box3(self):
        """
        Test vector 3
        """

        state = [0, 14, 7, 11, 2, 12, 14, 13, 6, 11, 14, 2, 13, 9, 2, 12, 3,
                 15, 3, 3, 7, 11, 14, 12, 11, 8, 3, 12, 14, 3, 10, 1]
        correct = [10, 5, 3, 2, 14, 10, 13, 11, 3, 7, 15, 2, 11, 2, 1, 14, 12,
                   6, 11, 7, 0, 9, 15, 11, 14, 10, 6, 10, 5, 13, 12, 8]

        self.assertEqual(self.gift128.apply_inv_p_box(state), correct,
                         "Inverse P-box not applied correctly")


class TestEncryptBlock(unittest.TestCase):
    """
    Integration tests for the encrypt_block method of the GIFT-128 class.
    The three integration tests are taken from the 3 test vectors published on
    the official GIFT GitHub.
    """

    def setUp(self):
        # Set up GIFT-128 object
        self.gift128 = Gift128()

    def test_encrypt_block(self):
        """
        Test vector 1
        """

        state = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        key = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
               0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        correct = [2, 5, 1, 0, 14, 14, 9, 0, 4, 8, 6, 4, 15, 10, 6, 4, 3, 9,
                   10, 5, 15, 11, 13, 6, 10, 1, 4, 2, 2, 2, 4, 8]

        self.assertEqual(self.gift128.encrypt_block(state, key), correct,
                         "Block not encrypted correctly")

    def test_encrypt_block2(self):
        """
        Test vector 2
        """

        state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        key = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        correct = [2, 9, 15, 15, 6, 11, 14, 12, 6, 3, 10, 5, 1, 11, 8, 6, 6,
                   15, 3, 13, 10, 8, 8, 3, 8, 3, 7, 13, 11, 0, 13, 12]

        self.assertEqual(self.gift128.encrypt_block(state, key), correct,
                         "Block not encrypted correctly")

    def test_encrypt_block3(self):
        """
        Test vector 3
        """

        state = [1, 12, 6, 8, 15, 1, 9, 10, 6, 11, 5, 8, 10, 8, 0, 15, 3, 4,
                 10, 11, 13, 7, 5, 10, 15, 1, 4, 1, 12, 9, 3, 14]
        key = [7, 3, 8, 13, 10, 0, 9, 15, 9, 10, 15, 8, 2, 0, 9, 9, 7, 14, 3,
               13, 0, 0, 7, 7, 10, 9, 5, 12, 5, 15, 0, 13]

        correct = [10, 14, 5, 6, 2, 7, 7, 9, 6, 13, 2, 6, 10, 0, 0, 4, 15, 11,
                   13, 3, 12, 12, 13, 11, 12, 7, 6, 14, 13, 14, 3, 1]

        self.assertEqual(self.gift128.encrypt_block(state, key), correct,
                         "Block not encrypted correctly")


class TestDecryptBlock(unittest.TestCase):
    """
    Integration tests for the decrypt_block method of the GIFT-64 class.
    The three integration tests are taken from the 3 test vectors published on
    the official GIFT GitHub.
    """

    def setUp(self):
        # Set up GIFT-128 object
        self.gift128 = Gift128()

    def test_decrypt_block(self):
        """
        Test vector 1
        """

        state = [2, 5, 1, 0, 14, 14, 9, 0, 4, 8, 6, 4, 15, 10, 6, 4, 3, 9,
                 10, 5, 15, 11, 13, 6, 10, 1, 4, 2, 2, 2, 4, 8]
        key = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
               0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        correct = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                   0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

        self.assertEqual(self.gift128.decrypt_block(state, key), correct,
                         "Block not decrypted correctly")

    def test_decrypt_block2(self):
        """
        Test vector 2
        """

        state = [2, 9, 15, 15, 6, 11, 14, 12, 6, 3, 10, 5, 1, 11, 8, 6, 6,
                 15, 3, 13, 10, 8, 8, 3, 8, 3, 7, 13, 11, 0, 13, 12]
        key = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        correct = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.assertEqual(self.gift128.decrypt_block(state, key), correct,
                         "Block not decrypted correctly")

    def test_decrypt_block3(self):
        """
        Test vector 3
        """

        state = [10, 14, 5, 6, 2, 7, 7, 9, 6, 13, 2, 6, 10, 0, 0, 4, 15, 11,
                 13, 3, 12, 12, 13, 11, 12, 7, 6, 14, 13, 14, 3, 1]
        key = [7, 3, 8, 13, 10, 0, 9, 15, 9, 10, 15, 8, 2, 0, 9, 9, 7, 14, 3,
               13, 0, 0, 7, 7, 10, 9, 5, 12, 5, 15, 0, 13]

        correct = [1, 12, 6, 8, 15, 1, 9, 10, 6, 11, 5, 8, 10, 8, 0, 15, 3, 4,
                   10, 11, 13, 7, 5, 10, 15, 1, 4, 1, 12, 9, 3, 14]

        self.assertEqual(self.gift128.decrypt_block(state, key), correct,
                         "Block not decrypted correctly")


if __name__ == '__main__':
    unittest.main()
