"""
This file runs unit and integration tests for the GIFT-64 class and all
its methods
"""

import sys
sys.path.append('..')
import unittest
from Gift.gift_64 import *


class TestApplySBox(unittest.TestCase):
    """
    Unit tests for the s_box method of the GIFT-64 class.
    The three unit tests are taken from the 3 test vectors published on the
    official GIFT GitHub.
    """

    def setUp(self):
        # Set up GIFT-64 object
        self.gift64 = Gift64()

    def test_apply_s_box(self):
        """
        Test vector 1
        """

        state = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        correct = [1, 10, 4, 12, 6, 15, 3, 9, 2, 13, 11, 7, 5, 0, 8, 14]
        self.assertEqual(self.gift64.apply_s_box(state), correct,
                         "S-box not applied correctly")

    def test_apply_s_box2(self):
        """
        Test vector 2
        """

        state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        correct = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(self.gift64.apply_s_box(state), correct,
                         "S-box not applied correctly")

    def test_apply_s_box3(self):
        """
        Test vector 3
        """

        state = [13, 7, 10, 8, 11, 9, 10, 7, 2, 7, 7, 12, 0, 5, 4, 12]
        correct = [0, 9, 11, 2, 7, 13, 11, 9, 4, 9, 9, 5, 1, 15, 6, 5]
        self.assertEqual(self.gift64.apply_s_box(state), correct,
                         "S-box not applied correctly")


class TestApplyPBox(unittest.TestCase):
    """
    Unit tests for the p_box method of the GIFT-64 class.
    The three unit tests are taken from the 3 test vectors published on the
    official GIFT GitHub.
    """

    def setUp(self):
        # set up GIFT-64 object
        self.gift64 = Gift64()

    def test_apply_p_box(self):
        """
        Test vector 1
        """

        state = [1, 10, 4, 12, 6, 15, 3, 9, 2, 13, 11, 7, 5, 0, 8, 14]
        correct = [15, 10, 0, 9, 0, 7, 15, 8, 8, 13, 11, 6, 4, 3, 7, 4]
        self.assertEqual(self.gift64.apply_p_box(state), correct,
                         "P-box not applied correctly")

    def test_apply_p_box2(self):
        """
        Test vector 2
        """

        state = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        correct = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(self.gift64.apply_p_box(state), correct,
                         "P-box not applied correctly")

    def test_apply_p_box3(self):
        """
        Test vector 3
        """

        state = [0, 9, 11, 2, 7, 13, 11, 9, 4, 9, 9, 5, 1, 15, 6, 5]
        correct = [0, 9, 0, 7, 8, 15, 9, 5, 11, 13, 13, 8, 3, 3, 5, 7]

        self.assertEqual(self.gift64.apply_p_box(state), correct,
                         "P-box not applied correctly")


class TestAddingRoundKey(unittest.TestCase):
    """
    Unit tests for the apply_round_key method of the GIFT-64 class.
    The three unit tests are taken from the 3 test vectors published on the
    official GIFT GitHub.
    """

    def setUp(self):
        # set up GIFT-64 object
        self.gift64 = Gift64()

    def test_adding_round_key1(self):
        """
        Test vector 1
        """

        state = [15, 10, 0, 9, 0, 7, 15, 8, 8, 13, 11, 6, 4, 3, 7, 4]
        correct = [7, 10, 2, 9, 3, 7, 13, 8, 8, 14, 9, 6, 7, 0, 5, 12]
        round_key = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                     0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(self.gift64.apply_round_key(state, round_key, 0),
                         correct, "Round key not added correctly")

    def test_adding_round_key2(self):
        """
        Test vector 2
        """

        state = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        correct = [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9]
        round_key = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(self.gift64.apply_round_key(state, round_key, 0),
                         correct,
                         "Round key not added correctly")

    def test_adding_round_key3(self):
        """
        Test vector 3
        """

        state = [0, 9, 0, 7, 8, 15, 9, 5, 11, 13, 13, 8, 3, 3, 5, 7]
        correct = [9, 8, 1, 7, 10, 14, 10, 4, 9, 15, 14, 8, 3, 3, 6, 13]
        round_key = [7, 14, 4, 4, 0, 5, 7, 12, 15, 15, 6, 15, 9, 15, 1, 10, 3,
                     1, 7, 2, 12, 11, 6, 11, 14, 1, 3, 7, 1, 9, 13, 11]
        self.assertEqual(self.gift64.apply_round_key(state, round_key, 0),
                         correct,
                         "Round key not added correctly")


class TestUpdateKey(unittest.TestCase):
    """
    Unit tests for the update_key method of the GIFT-64 class.
    The three unit tests are taken from the 3 test vectors published on the
    official GIFT GitHub.
    """

    def setUp(self):
        # set up GIFT-64 object
        self.gift64 = Gift64()

    def test_update_key1(self):
        """
        Test vector 1
        """

        key = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        correct = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(self.gift64.update_key(key), correct,
                         "Key not updated correctly")

    def test_update_key2(self):
        """
        Test vector 2
        """

        key = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
               0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

        correct = [8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                   10, 11, 12, 13, 14, 15, 3, 0, 1, 2, 5, 9, 13, 1]
        self.assertEqual(self.gift64.update_key(key), correct,
                         "Key not updated correctly")

    def test_update_key3(self):
        """
        Test vector 3
        """

        key = [7, 14, 4, 4, 0, 5, 7, 12, 15, 15, 6, 15, 9, 15, 1, 10, 3, 1, 7,
               2, 12, 11, 6, 11, 14, 1, 3, 7, 1, 9, 13, 11]
        correct = [15, 15, 6, 15, 9, 15, 1, 10, 3, 1, 7, 2, 12, 11, 6, 11, 14,
                   1, 3, 7, 1, 9, 13, 11, 4, 7, 14, 4, 4, 13, 1, 3]
        self.assertEqual(self.gift64.update_key(key), correct,
                         "Key not updated correctly")


class TestApplySBoxInv(unittest.TestCase):
    """
    Unit tests for the apply_inv_s_box method of the GIFT-64 class.
    The three unit tests are taken from the 3 test vectors published on the
    official GIFT GitHub.
    """

    def setUp(self):
        # set up GIFT-64 object
        self.gift64 = Gift64()

    def test_apply_s_box_inv(self):
        """
        Test vector 1
        """

        correct = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        state = [1, 10, 4, 12, 6, 15, 3, 9, 2, 13, 11, 7, 5, 0, 8, 14]
        self.assertEqual(self.gift64.apply_inv_s_box(state), correct,
                         "Inv S-box not applied correctly")

    def test_apply_s_box_inv2(self):
        """
        Test vector 2
        """

        correct = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        state = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(self.gift64.apply_inv_s_box(state), correct,
                         "Inv S-box not applied correctly")

    def test_apply_s_box_inv3(self):
        """
        Test vector 3
        """

        correct = [13, 7, 10, 8, 11, 9, 10, 7, 2, 7, 7, 12, 0, 5, 4, 12]
        state = [0, 9, 11, 2, 7, 13, 11, 9, 4, 9, 9, 5, 1, 15, 6, 5]
        self.assertEqual(self.gift64.apply_inv_s_box(state), correct,
                         "Inv S-box not applied correctly")


class TestApplyPBoxInv(unittest.TestCase):
    """
    Unit tests for the apply_inv_p_box method of the GIFT-64 class.
    The three unit tests are taken from the 3 test vectors published on the
    official GIFT GitHub.
    """

    def setUp(self):
        # set up GIFT-64 object
        self.gift64 = Gift64()

    def test_apply_inv_p_box(self):
        """
        Test vector 1
        """

        correct = [1, 10, 4, 12, 6, 15, 3, 9, 2, 13, 11, 7, 5, 0, 8, 14]
        state = [15, 10, 0, 9, 0, 7, 15, 8, 8, 13, 11, 6, 4, 3, 7, 4]
        self.assertEqual(self.gift64.apply_inv_p_box(state), correct,
                         "Inv p-box not applied correctly")

    def test_apply_inv_p_box2(self):
        """
        Test vector 2
        """

        correct = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        state = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(self.gift64.apply_inv_p_box(state), correct,
                         "Inv p-box not applied correctly")

    def test_apply_inv_p_box3(self):
        """
        Test vector 3
        """

        correct = [0, 9, 11, 2, 7, 13, 11, 9, 4, 9, 9, 5, 1, 15, 6, 5]
        state = [0, 9, 0, 7, 8, 15, 9, 5, 11, 13, 13, 8, 3, 3, 5, 7]
        self.assertEqual(self.gift64.apply_inv_p_box(state), correct,
                         "Inv p-box not applied correctly")


# INTEGRATION TESTS
class TestEncryptBlock(unittest.TestCase):
    """
    Integration tests for the encrypt_block method of the GIFT-64 class.
    The three integration tests are taken from the 3 test vectors published on
    the official GIFT GitHub.
    """

    def setUp(self):
        # set up GIFT-64 object
        self.gift64 = Gift64()

    def test_encrypt_block(self):
        """
        Test vector 1
        """

        state = [13, 7, 10, 8, 11, 9, 10, 7, 2, 7, 7, 12, 0, 5, 4, 12]
        key = [7, 14, 4, 4, 0, 5, 7, 12, 15, 15, 6, 15, 9, 15, 1, 10, 3, 1, 7,
               2, 12, 11, 6, 11, 14, 1, 3, 7, 1, 9, 13, 11]
        correct = [11, 8, 10, 11, 4, 9, 10, 15, 5, 8, 8, 2, 7, 2, 3, 14]
        self.assertEqual(self.gift64.encrypt_block(state, key), correct,
                         "Block not encrypted correctly")

    def test_encrypt_block2(self):
        """
        Test vector 2
        """

        state = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        key = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
               0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        correct = [7, 8, 5, 15, 15, 0, 6, 1, 6, 6, 15, 1, 7, 11, 1, 12]

        self.assertEqual(self.gift64.encrypt_block(state, key), correct,
                         "Block not encrypted correctly")

    def test_encrypt_block3(self):
        """
        Test vector 3
        """

        state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        key = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        correct = [12, 10, 5, 7, 7, 15, 4, 3, 15, 14, 3, 12, 11, 2, 6, 15]

        self.assertEqual(self.gift64.encrypt_block(state, key), correct,
                         "Block not encrypted correctly")


class TestDecryptBlock(unittest.TestCase):
    """
    Integration tests for the decrypt_block method of the GIFT-64 class.
    The three integration tests are taken from the 3 test vectors published on
    the official GIFT GitHub.
    """

    def setUp(self):
        # set up GIFT-64 object
        self.gift64 = Gift64()

    def test_decrypt_block(self):
        """
        Test vector 1
        """

        correct = [13, 7, 10, 8, 11, 9, 10, 7, 2, 7, 7, 12, 0, 5, 4, 12]
        key = [7, 14, 4, 4, 0, 5, 7, 12, 15, 15, 6, 15, 9, 15, 1, 10, 3, 1, 7,
               2, 12, 11, 6, 11, 14, 1, 3, 7, 1, 9, 13, 11]
        state = [11, 8, 10, 11, 4, 9, 10, 15, 5, 8, 8, 2, 7, 2, 3, 14]
        self.assertEqual(self.gift64.decrypt_block(state, key), correct,
                         "Block not decrypted correctly")

    def test_decrypt_block2(self):
        """
        Test vector 2
        """

        correct = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        key = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
               0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        state = [7, 8, 5, 15, 15, 0, 6, 1, 6, 6, 15, 1, 7, 11, 1, 12]

        self.assertEqual(self.gift64.decrypt_block(state, key), correct,
                         "Block not decrypted correctly")

    def test_decrypt_block3(self):
        """
        Test vector 3
        """

        correct = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        key = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        state = [12, 10, 5, 7, 7, 15, 4, 3, 15, 14, 3, 12, 11, 2, 6, 15]

        self.assertEqual(self.gift64.decrypt_block(state, key), correct,
                         "Block not decrypted correctly")


if __name__ == '__main__':
    unittest.main()
