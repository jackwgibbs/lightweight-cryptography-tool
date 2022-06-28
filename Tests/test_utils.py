"""
This file runs unit for the utils files functions
"""

import sys
sys.path.append('..')
import unittest
from utils import *


class TestPlaintextLength(unittest.TestCase):
    """
    Unit tests for plaintext length function
    """

    def test_plaintext_length_1(self):
        """
        Unit test 1 for plaintext length function - tests negative input length
        """

        plaintext_length_ = 32
        input_length = -56
        correct = 32

        self.assertEqual(plaintext_length(plaintext_length_, input_length),
                         correct, "Incorrect plaintext length")

    def test_plaintext_length_2(self):
        """
        Unit test 2 for plaintext length function - tests too large
        input length
        """

        plaintext_length_ = 32
        input_length = 40
        correct = 32

        self.assertEqual(plaintext_length(plaintext_length_, input_length),
                         correct, "Incorrect plaintext length")


class TestIncrementByte(unittest.TestCase):
    """
    Unit tests for increment byte function - used by CTR mode
    """

    def test_increment_byte_1(self):
        """
        Unit test 1 for increment byte function - boundary case!
        """
        byte = [15, 15]
        correct = [0, 0]
        self.assertEqual(increment_byte(byte), correct,
                         "Incorrect plaintext length")

    def test_increment_byte_2(self):
        """
        Unit test 2 for increment byte function
        """

        byte = [13, 12]
        correct = [13, 13]
        self.assertEqual(increment_byte(byte), correct,
                         "Incorrect plaintext length")


class TestDivideIntoBlocks(unittest.TestCase):
    """
    Unit tests for the dividing into blocks function
    """

    def test_divide_into_blocks_1(self):
        """
        Unit test 1 for the dividing into blocks function - three complete
        blocks in encryption mode so padded extra block too
        """

        plaintext = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0,
                     1, 2, 3, 4, 5, 6, 7,
                     8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7, 8,
                     9, 10, 11, 12, 13,
                     14, 15]

        correct = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                   [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.assertEqual(divide_into_blocks(plaintext, 64, 1), correct,
                         "Incorrect plaintext length")

    def test_divide_into_blocks_2(self):
        """
        Unit test 2 for the dividing into blocks function - three complete
        blocks in mode 3 - so no extra padding
        """

        plaintext = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0,
                     1, 2, 3, 4, 5, 6, 7,
                     8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7, 8,
                     9, 10, 11, 12, 13,
                     14, 15]

        correct = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]

        self.assertEqual(divide_into_blocks(plaintext, 64, 3), correct,
                         "Incorrect plaintext length")

    def test_divide_into_blocks_3(self):
        """
        Unit test 3 for the dividing into blocks function - empty plaintext
        """

        plaintext = []
        correct = [[]]
        self.assertEqual(divide_into_blocks(plaintext, 64, 1), correct,
                         "Incorrect plaintext length")

    def test_divide_into_blocks_4(self):
        """
        Unit test 4 for the dividing into blocks function - incomplete
        block - padding needs to be applied
        """

        plaintext = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                     0, 1, 2, 3, 4, 5, 6, 7,
                     8, 9, 10, 11, 12, 13, 14, 15, 0, 1, 2]

        correct = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                   [0, 1, 2, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.assertEqual(divide_into_blocks(plaintext, 64, 1), correct,
                         "Incorrect plaintext length")


class TestApplyPadding(unittest.TestCase):
    """
    Unit tests for applying the injective padding
    """

    def test_apply_padding(self):
        """
        Unit test 1 for applying the injective padding - incomplete block -
        64 bits
        """

        block = [0, 1, 2, 3]
        correct = [0, 1, 2, 3, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.assertEqual(apply_padding(block, 64), correct,
                         "Padding not applied correctly")

    def test_apply_padding_2(self):
        """
        Unit test 2 for applying the injective padding - incomplete block -
        128 bits
        """

        block = [0, 1, 2, 3]
        correct = [0, 1, 2, 3, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.assertEqual(apply_padding(block, 128), correct,
                         "Padding not applied correctly")

    def test_apply_padding_3(self):
        """
        Unit test 3 for applying the injective padding - empty block
        """

        block = []
        correct = [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.assertEqual(apply_padding(block, 64), correct,
                         "Padding not applied correctly")


class TestDecimalToHex(unittest.TestCase):
    """
    Unit tests for the decimal to hex conversion function
    """

    def test_decimal_to_hex(self):
        """
        Unit test for the decimal to hex conversion function
        """

        decimal = [56, 120, 255, 12, 8, 0, 45]
        correct = [3, 8, 7, 8, 15, 15, 0, 12, 0, 8, 0, 0, 2, 13]

        self.assertEqual(decimal_to_hex(decimal), correct,
                         "Decimal to hex conversion incorrect")


class TestHexToDecimal(unittest.TestCase):
    """
    Unit tests for the hex to decimal conversion function
    """

    def test_hex_to_decimal(self):
        """
        Unit test 1 for the hex to decimal conversion function
        """
        decimal = [3, 8, 7, 8, 15, 15, 0, 12, 0, 8, 0, 0, 2, 13]
        correct = [56, 120, 255, 12, 8, 0, 45]

        self.assertEqual(hex_to_decimal(decimal), correct,
                         "Hex to decimal conversion incorrect")


class TestStringToList(unittest.TestCase):
    """
    Unit tests for the string to list representation function
    """

    def test_string_to_list(self):
        """
        Unit test for the string to list representation function
        """

        string = "0123456789ABCDEF"
        correct = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

        self.assertEqual(string_to_list(string), correct,
                         "String to list conversion incorrect")


class TestListToString(unittest.TestCase):
    """
    Unit tests for the list to string representation function
    """

    def test_list_to_string(self):
        """
        Unit test for the list to string representation function
        """
        list_to_convert = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                           15]
        correct = "0123456789ABCDEF"

        self.assertEqual(list_to_string(list_to_convert), correct,
                         "List to string conversion incorrect")


class TestXorBits(unittest.TestCase):
    """
    Unit tests for the xor function
    """

    def test_xor_bits_1(self):
        """
        Unit test for the xor function
        """

        a = [0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0]
        b = [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1]
        correct = [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1]

        self.assertEqual(xor_bits(a, b), correct,
                         "XOR incorrect")


class TestConvertFromBitsRev(unittest.TestCase):
    """
    Unit tests for the convert from bits reverse function
    """

    def test_convert_from_bits_rev(self):
        """
        Unit tests for the convert from bits reverse function
        """

        a = [0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0]
        correct = [10, 5, 4, 3]

        self.assertEqual(convert_from_bits_rev(a, 16), correct,
                         "XOR incorrect")


class TestConvertToBitsRev(unittest.TestCase):
    """
    Unit tests for the convert to bits reverse function
    """

    def test_convert_to_bits_rev(self):
        """
        Unit test for the convert to bits reverse function
        """

        a = [10, 5, 4, 3]
        correct = [0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0]

        self.assertEqual(convert_to_bits_rev(a), correct,
                         "XOR incorrect")


class TestConvertToEightBits(unittest.TestCase):
    """
    Unit tests for convert to eight bits function
    """

    def test_convert_to_eight_bits(self):
        """
        Unit test for convert to eight bits function
        """

        hex = [10, 5, 4, 3]
        correct = [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0,
                   0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]

        self.assertEqual(convert_to_eight_bits(hex), correct,
                         "Conversion incorrect")


class TestConvertFromEightBits(unittest.TestCase):
    """
    Unit tests for convert from eight bits function
    """

    def test_convert_from_eight_bits(self):
        """
        Unit test for convert from eight bits function
        """

        bits = [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0,
                0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
        correct = [10, 5, 4, 3]

        self.assertEqual(convert_from_eight_bits(bits, 32), correct,
                         "Conversion incorrect")


class TestConvertToBits(unittest.TestCase):
    """
    Unit tests for the convert to bits function
    """

    def test_convert_to_bits(self):
        """
        Unit test for the convert to bits function
        """

        hex = [10, 5, 4, 3]
        correct = [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1]

        self.assertEqual(convert_to_bits(hex), correct,
                         "Conversion incorrect")


class TestConvertFromBits(unittest.TestCase):
    """
    Unit tests for the convert from bits function
    """

    def test_convert_from_bits(self):
        """
        Unit tests for the convert from bits function
        """

        bits = [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1]
        correct = [10, 5, 4, 3]

        self.assertEqual(convert_from_bits(bits, 16), correct,
                         "Conversion incorrect")


class TestCheckInputValidity(unittest.TestCase):
    """
    Unit tests for the s_box method of the skinny class.
    """

    def test_check_input_validity(self):
        """
        Unit test 1 for checking input validity - test valid input
        """

        variables_dictionary = {'P': '000102030405060708090A0B0C0D0E0F10'
                                     '1112131415161718191A1B1C1D1E1F\n',
                                'A': '000102030405060708090A0B0C0D0E0F10111'
                                     '2131415161718191A1B1C1D1E1F\n',
                                'N': '000102030405060708090A0B0C0D0E0F\n',
                                'K': '000102030405060708090A0B0C0D0E0F\n',
                                'C': 'BAF563C60FBEDDC5662995F4C678BE80A7F7DE9'
                                     'B3AD8C97AA6CA17016D2AE650\n',
                                'T': '8E6FB3F79B412A1627AB7DFA755E0A22\n'}

        variable_conditions = {'C': [True, 0, False], 'K': [False, 32, True],
                               'N': [False, 32, True], 'A': [True, 0, False],
                               'T': [False, 32, True]}

        self.assertEqual(check_input_validity(variables_dictionary,
                                              variable_conditions), True,
                         "Incorrect validity")

    def test_check_input_validity_2(self):
        """
        Unit test 2 for checking input validity - no key
        """

        variables_dictionary = {'P': '000102030405060708090A0B0C0D0E0F10'
                                     '1112131415161718191A1B1C1D1E1F\n',
                                'A': '000102030405060708090A0B0C0D0E0F10111'
                                     '2131415161718191A1B1C1D1E1F\n',
                                'N': '000102030405060708090A0B0C0D0E0F\n',
                                'C': 'BAF563C60FBEDDC5662995F4C678BE80A7F7DE9'
                                     'B3AD8C97AA6CA17016D2AE650\n',
                                'T': '8E6FB3F79B412A1627AB7DFA755E0A22\n'}

        variable_conditions = {'C': [True, 0, False], 'K': [False, 32, True],
                               'N': [False, 32, True], 'A': [True, 0, False],
                               'T': [False, 32, True]}

        self.assertEqual(check_input_validity(variables_dictionary,
                                              variable_conditions), False,
                         "Incorrect validity")

    def test_check_input_validity_3(self):
        """
        Unit test 3 for checking input validity - incorrect key length
        """

        variables_dictionary = {'P': '000102030405060708090A0B0C0D0E0F10'
                                     '1112131415161718191A1B1C1D1E1F\n',
                                'A': '000102030405060708090A0B0C0D0E0F10111'
                                     '2131415161718191A1B1C1D1E1F\n',
                                'N': '000102030405060708090A0B0C0D0E0F\n',
                                'K': '000102030405060708090A0B0C0D0\n',
                                'C': 'BAF563C60FBEDDC5662995F4C678BE80A7F7DE9'
                                     'B3AD8C97AA6CA17016D2AE650\n',
                                'T': '8E6FB3F79B412A1627AB7DFA755E0A22\n'}

        variable_conditions = {'C': [True, 0, False], 'K': [False, 32, True],
                               'N': [False, 32, True], 'A': [True, 0, False],
                               'T': [False, 32, True]}

        self.assertEqual(check_input_validity(variables_dictionary,
                                              variable_conditions), False,
                         "Incorrect validity")

    def test_check_input_validity_4(self):
        """
        Unit test 4 for checking input validity - empty key
        """

        variables_dictionary = {'P': '000102030405060708090A0B0C0D0E0F10'
                                     '1112131415161718191A1B1C1D1E1F\n',
                                'A': '000102030405060708090A0B0C0D0E0F10111'
                                     '2131415161718191A1B1C1D1E1F\n',
                                'N': '000102030405060708090A0B0C0D0E0F\n',
                                'K': '\n',
                                'C': 'BAF563C60FBEDDC5662995F4C678BE80A7F7DE9'
                                     'B3AD8C97AA6CA17016D2AE650\n',
                                'T': '8E6FB3F79B412A1627AB7DFA755E0A22\n'}

        variable_conditions = {'C': [True, 0, False], 'K': [False, 32, True],
                               'N': [False, 32, True], 'A': [True, 0, False],
                               'T': [False, 32, True]}

        self.assertEqual(check_input_validity(variables_dictionary,
                                              variable_conditions), False,
                         "Incorrect validity")

    def test_check_input_validity_5(self):
        """
        Unit test 5 for checking input validity - invalid character
        """

        variables_dictionary = {'P': '000102030405060708090A0B0C0D0E0F10'
                                     '1112131415161718191A1B1C1D1E1F\n',
                                'A': '000102030405060708090A0B0C0D0E0F10111'
                                     '2131415161718191A1B1C1D1E1F\n',
                                'N': '000102030405060708090A0B0C0D0E0F\n',
                                 'K': '000102030405060708090A0B0C0D0E0G\n',
                                'C': 'BAF563C60FBEDDC5662995F4C678BE80A7F7DE9'
                                     'B3AD8C97AA6CA17016D2AE650\n',
                                'T': '8E6FB3F79B412A1627AB7DFA755E0A22\n'}

        variable_conditions = {'C': [True, 0, False], 'K': [False, 32, True],
                               'N': [False, 32, True], 'A': [True, 0, False],
                               'T': [False, 32, True]}

        self.assertEqual(check_input_validity(variables_dictionary,
                                              variable_conditions), False,
                         "Incorrect validity")


class TestExtractInputs(unittest.TestCase):
    """
    Unit tests for the s_box method of the skinny class.
    """

    def test_extract_inputs(self):
        """
        Unit test for extracting inputs
        """

        variables_dictionary = {'A': '000102030405060708090A0B0C0D0E0F10111'
                                     '2131415161718191A1B1C1D1E1F\n',
                                'N': '000102030405060708090A0B0C0D0E0F\n',
                                'K': '000102030405060708090A0B0C0D0E0F\n',
                                'C': 'BAF563C60FBEDDC5662995F4C678BE80A7F7DE9'
                                     'B3AD8C97AA6CA17016D2AE650\n',
                                'T': '8E6FB3F79B412A1627AB7DFA755E0A22\n'}

        correct = ['BAF563C60FBEDDC5662995F4C678BE80A7'
                   'F7DE9B3AD8C97AA6CA17016D2AE650',
                   '000102030405060708090A0B0C0D0E0F1'
                   '01112131415161718191A1B1C1D1E1F',
                   '000102030405060708090A0B0C0D0E0F',
                   '000102030405060708090A0B0C0D0E0F',
                   '8E6FB3F79B412A1627AB7DFA755E0A22']

        self.assertEqual(extract_inputs(variables_dictionary,
                                        ["C", "A", "N", "K", "T"]), correct,
                         "Incorrect validity")


if __name__ == '__main__':
    unittest.main()
