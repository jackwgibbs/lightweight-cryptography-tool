"""
This file runs unit and integration tests for the SKINNY class and all its
methods
"""

import sys
sys.path.append('..')
import unittest
from Skinny.skinny import *


class TestApplySBox(unittest.TestCase):
    """
    Unit tests for the s_box method of the SKINNY class.
    """

    def test_apply_s_box_64_64(self):
        """
        Unit test for S-box of SKINNY-64-64
        """

        skinny = Skinny([64, 64, 32])
        state = [[0, 6, 0, 3], [4, 15, 9, 5],
                 [7, 7, 2, 4], [13, 1, 9, 13]]

        correct = [[12, 2, 12, 0], [1, 15, 8, 10],
                   [11, 11, 9, 1], [14, 6, 8, 14]]

        self.assertEqual(skinny.sub_cells(state), correct,
                         "S-box not applied correctly")

    def test_apply_s_box_64_128(self):
        """
        Unit test for S-box of SKINNY-64-128
        """

        skinny = Skinny([64, 128, 36])
        state = [[12, 15, 1, 6], [12, 15, 14, 8],
                 [15, 13, 0, 15], [9, 8, 10, 10]]

        correct = [[4, 15, 6, 2], [4, 15, 7, 3],
                   [15, 14, 12, 15], [8, 3, 5, 5]]

        self.assertEqual(skinny.sub_cells(state), correct,
                         "S-box not applied correctly")

    def test_apply_s_box_64_192(self):
        """
        Unit test for S-box of SKINNY-64-192
        """

        skinny = Skinny([64, 128, 40])
        state = [[5, 3, 0, 12], [6, 1, 13, 3],
                 [5, 14, 8, 6], [6, 3, 12, 3]]

        correct = [[10, 0, 12, 4], [2, 6, 14, 0],
                   [10, 7, 3, 2], [2, 0, 4, 0]]

        self.assertEqual(skinny.sub_cells(state), correct,
                         "S-box not applied correctly")

    def test_apply_s_box_128_128(self):
        """
        Unit test for S-box of SKINNY-128-128
        """

        skinny = Skinny([128, 128, 40])
        state = [[242, 10, 219, 14], [176, 139, 100, 138],
                 [59, 46, 238, 209], [240, 173, 218, 20]]

        correct = [[238, 90, 126, 91], [230, 40, 29, 154],
                   [184, 217, 15, 72], [226, 179, 94, 137]]

        self.assertEqual(skinny.sub_cells(state), correct,
                         "S-box not applied correctly")

    def test_apply_s_box_128_256(self):
        """
        Unit test for S-box of SKINNY-128-256
        """

        skinny = Skinny([128, 256, 48])
        state = [[58, 12, 71, 118], [122, 38, 166, 141],
                 [211, 130, 166, 149], [231, 2, 46, 37]]

        correct = [[10, 83, 61, 196], [220, 192, 16, 32],
                   [70, 56, 16, 96], [175, 106, 217, 224]]

        self.assertEqual(skinny.sub_cells(state), correct,
                         "S-box not applied correctly")

    def test_apply_s_box_128_384(self):
        """
        Unit test for S-box of SKINNY-128-384
        """

        skinny = Skinny([128, 384, 56])
        state = [[163, 153, 75, 102], [173, 133, 163, 69],
                 [159, 68, 233, 43], [8, 245, 80, 203]]

        correct = [[17, 118, 44, 20], [179, 48, 17, 52],
                   [121, 141, 178, 248], [85, 231, 98, 46]]

        self.assertEqual(skinny.sub_cells(state), correct,
                         "S-box not applied correctly")


class TestApplyInvSBox(unittest.TestCase):
    """
    Unit tests for the inverse s_box method of the SKINNY class.
    """

    def test_apply_s_box_inv_64_64(self):
        """
        Unit test for the inverse S-box method of SKINNY-64-64
        """

        skinny = Skinny([64, 64, 32])
        state = [[12, 2, 12, 0], [1, 15, 8, 10],
                 [11, 11, 9, 1], [14, 6, 8, 14]]

        correct = [[0, 6, 0, 3], [4, 15, 9, 5],
                   [7, 7, 2, 4], [13, 1, 9, 13]]

        self.assertEqual(skinny.sub_cells_inv(state), correct,
                         "S-box not applied correctly")

    def test_apply_s_box_inv_64_128(self):
        """
        Unit test for the inverse S-box method of SKINNY-64-128
        """

        skinny = Skinny([64, 128, 36])
        state = [[4, 15, 6, 2], [4, 15, 7, 3],
                 [15, 14, 12, 15], [8, 3, 5, 5]]

        correct = [[12, 15, 1, 6], [12, 15, 14, 8],
                   [15, 13, 0, 15], [9, 8, 10, 10]]

        self.assertEqual(skinny.sub_cells_inv(state), correct,
                         "S-box not applied correctly")

    def test_apply_s_box_inv_64_192(self):
        """
        Unit test for the inverse S-box method of SKINNY-64-192
        """

        skinny = Skinny([64, 128, 40])
        state = [[10, 0, 12, 4], [2, 6, 14, 0],
                 [10, 7, 3, 2], [2, 0, 4, 0]]

        correct = [[5, 3, 0, 12], [6, 1, 13, 3],
                   [5, 14, 8, 6], [6, 3, 12, 3]]

        self.assertEqual(skinny.sub_cells_inv(state), correct,
                         "S-box not applied correctly")

    def test_apply_s_box_inv_128_128(self):
        """
        Unit test for the inverse S-box method of SKINNY-128-128
        """

        skinny = Skinny([128, 128, 40])
        state = [[238, 90, 126, 91], [230, 40, 29, 154],
                 [184, 217, 15, 72], [226, 179, 94, 137]]

        correct = [[242, 10, 219, 14], [176, 139, 100, 138],
                   [59, 46, 238, 209], [240, 173, 218, 20]]

        self.assertEqual(skinny.sub_cells_inv(state), correct,
                         "S-box not applied correctly")

    def test_apply_s_box_inv_128_256(self):
        """
        Unit test for the inverse S-box method of SKINNY-128-256
        """

        skinny = Skinny([128, 256, 48])
        state = [[10, 83, 61, 196], [220, 192, 16, 32],
                 [70, 56, 16, 96], [175, 106, 217, 224]]

        correct = [[58, 12, 71, 118], [122, 38, 166, 141],
                   [211, 130, 166, 149], [231, 2, 46, 37]]

        self.assertEqual(skinny.sub_cells_inv(state), correct,
                         "S-box not applied correctly")

    def test_apply_s_box_inv_128_384(self):
        """
        Unit test for the inverse S-box method of SKINNY-128-384
        """

        skinny = Skinny([128, 384, 56])
        state = [[17, 118, 44, 20], [179, 48, 17, 52],
                 [121, 141, 178, 248], [85, 231, 98, 46]]

        correct = [[163, 153, 75, 102], [173, 133, 163, 69],
                   [159, 68, 233, 43], [8, 245, 80, 203]]

        self.assertEqual(skinny.sub_cells_inv(state), correct,
                         "S-box not applied correctly")


class TestAddRoundConstant(unittest.TestCase):
    """
    Unit tests for the add_round_constant method for SKINNY
    """

    def test_add_round_constant_64_64(self):
        """
        Unit test for the add round constants method of SKINNY-64-64
        """

        skinny = Skinny([64, 64, 32])
        state = [[12, 2, 12, 0], [1, 15, 8, 10],
                 [11, 11, 9, 1], [14, 6, 8, 14]]

        correct = [[13, 2, 12, 0], [1, 15, 8, 10],
                   [9, 11, 9, 1], [14, 6, 8, 14]]

        self.assertEqual(skinny.add_round_constant(state, 0), correct,
                         "Round constant not added correctly")

    def test_add_round_constant_64_128(self):
        """
        Unit test for the add round constants method of SKINNY-64-128
        """

        skinny = Skinny([64, 128, 36])
        state = [[4, 15, 6, 2], [4, 15, 7, 3],
                 [15, 14, 12, 15], [8, 3, 5, 5]]

        correct = [[5, 15, 6, 2], [4, 15, 7, 3],
                   [13, 14, 12, 15], [8, 3, 5, 5]]

        self.assertEqual(skinny.add_round_constant(state, 0), correct,
                         "Round constant not added correctly")

    def test_add_round_constant_64_192(self):
        """
        Unit test for the add round constants method of SKINNY-64-192
        """

        skinny = Skinny([64, 192, 40])
        state = [[10, 0, 12, 4], [2, 6, 14, 0],
                 [10, 7, 3, 2], [2, 0, 4, 0]]

        correct = [[11, 0, 12, 4], [2, 6, 14, 0],
                   [8, 7, 3, 2], [2, 0, 4, 0]]

        self.assertEqual(skinny.add_round_constant(state, 0), correct,
                         "Round constant not added correctly")

    def test_add_round_constant_128_128(self):
        """
        Unit test for the add round constants method of SKINNY-128-128
        """

        skinny = Skinny([128, 128, 40])
        state = [[238, 90, 126, 91], [230, 40, 29, 154],
                 [184, 217, 15, 72], [226, 179, 94, 137]]

        correct = [[239, 90, 126, 91], [230, 40, 29, 154],
                   [186, 217, 15, 72], [226, 179, 94, 137]]

        self.assertEqual(skinny.add_round_constant(state, 0), correct,
                         "Round constant not added correctly")

    def test_add_round_constant_128_256(self):
        """
        Unit test for the add round constants method of SKINNY-128-256
        """

        skinny = Skinny([128, 256, 48])
        state = [[10, 83, 61, 196], [220, 192, 16, 32],
                 [70, 56, 16, 96], [175, 106, 217, 224]]

        correct = [[11, 83, 61, 196], [220, 192, 16, 32],
                   [68, 56, 16, 96], [175, 106, 217, 224]]

        self.assertEqual(skinny.add_round_constant(state, 0), correct,
                         "Round constant not added correctly")

    def test_add_round_constant_128_384(self):
        """
        Unit test for the add round constants method of SKINNY-128-384
        """

        skinny = Skinny([128, 384, 56])
        state = [[17, 118, 44, 20], [179, 48, 17, 52],
                 [121, 141, 178, 248], [85, 231, 98, 46]]

        correct = [[16, 118, 44, 20], [179, 48, 17, 52],
                   [123, 141, 178, 248], [85, 231, 98, 46]]

        self.assertEqual(skinny.add_round_constant(state, 0), correct,
                         "Round constant not added correctly")


class TestAddRoundTweakeys(unittest.TestCase):
    """
    Unit tests for the add round tweakey method
    """

    def test_add_tweakey_64_64(self):
        """
        Unit test for the add round tweakey of SKINNY-64-64
        """

        skinny = Skinny([64, 64, 32])
        state = [[13, 2, 12, 0], [1, 15, 8, 10],
                 [9, 11, 9, 1], [14, 6, 8, 14]]

        TW = [[[15, 5, 2, 6], [9, 8, 2, 6],
               [15, 12, 6, 8], [1, 2, 3, 8]], [], []]

        correct = [[2, 7, 14, 6], [8, 7, 10, 12],
                   [9, 11, 9, 1], [14, 6, 8, 14]]

        self.assertEqual(skinny.add_round_tweakey(state, TW), correct,
                         "Tweakey not added correctly")

    def test_add_tweakey_64_128(self):
        """
        Unit test for the add round tweakey of SKINNY-64-128
        """

        skinny = Skinny([64, 128, 36])

        state = [[5, 15, 6, 2], [4, 15, 7, 3],
                 [13, 14, 12, 15], [8, 3, 5, 5]]
        TW = [[[9, 14, 11, 9], [3, 6, 4, 0],
               [13, 0, 8, 8], [13, 10, 6, 3]],
              [[7, 6, 10, 3], [9, 13, 1, 12],
               [8, 11, 14, 10], [7, 1, 14, 1]], []]

        correct = [[11, 7, 7, 8], [14, 4, 2, 15],
                   [13, 14, 12, 15], [8, 3, 5, 5]]

        self.assertEqual(skinny.add_round_tweakey(state, TW), correct,
                         "Tweakey not added correctly")

    def test_add_tweakey_64_192(self):
        """
        Unit test for the add round tweakey of SKINNY-64-192
        """

        skinny = Skinny([64, 192, 40])

        state = [[11, 0, 12, 4], [2, 6, 14, 0],
                 [8, 7, 3, 2], [2, 0, 4, 0]]
        TW = [[[14, 13, 0, 0], [12, 8, 5, 11],
               [1, 2, 0, 13], [6, 8, 6, 1]],
              [[8, 7, 5, 3], [14, 2, 4, 11],
               [15, 13, 9, 0], [8, 15, 6, 0]],
              [[11, 2, 13, 11], [11, 4, 1, 11],
               [4, 2, 2, 13], [15, 12, 13, 0]]]

        correct = [[6, 8, 4, 12], [11, 8, 14, 11],
                   [8, 7, 3, 2], [2, 0, 4, 0]]

        self.assertEqual(skinny.add_round_tweakey(state, TW), correct,
                         "Tweakey not added correctly")

    def test_add_tweakey_128_128(self):
        """
        Unit test for the add round tweakey of SKINNY-128-128
        """

        skinny = Skinny([128, 128, 40])

        state = [[239, 90, 126, 91], [230, 40, 29, 154],
                 [186, 217, 15, 72], [226, 179, 94, 137]]

        TW = [[[79, 85, 207, 176], [82, 12, 172, 82],
               [253, 146, 193, 95], [55, 7, 62, 147]],
              [], []]

        correct = [[160, 15, 177, 235], [180, 36, 177, 200],
                   [186, 217, 15, 72], [226, 179, 94, 137]]

        self.assertEqual(skinny.add_round_tweakey(state, TW), correct,
                         "Tweakey not added correctly")

    def test_add_tweakey_128_256(self):
        """
        Unit test for the add round tweakey of SKINNY-128-256
        """

        skinny = Skinny([128, 256, 48])
        state = [[11, 83, 61, 196], [220, 192, 16, 32],
                 [68, 56, 16, 96], [175, 106, 217, 224]]

        TW = [[[0, 156, 236, 129], [96, 93, 74, 193],
               [210, 174, 158, 48], [133, 215, 161, 243]],
              [[26, 193, 35, 235], [252, 0, 253, 220],
               [240, 16, 70, 206], [237, 223, 202, 179]],
              []]

        correct = [[17, 14, 242, 174], [64, 157, 167, 61],
                   [68, 56, 16, 96], [175, 106, 217, 224]]

        self.assertEqual(skinny.add_round_tweakey(state, TW), correct,
                         "Tweakey not added correctly")

    def test_add_tweakey_128_384(self):
        """
        Unit test for the add round tweakey of SKINNY-128-384
        """

        skinny = Skinny([128, 384, 56])

        state = [[16, 118, 44, 20], [179, 48, 17, 52],
                 [123, 141, 178, 248], [85, 231, 98, 46]]

        TW = [[[223, 136, 149, 72], [207, 199, 234, 82],
               [210, 150, 51, 147], [1, 121, 116, 73]],
              [[171, 88, 138, 52], [164, 127, 26, 178],
               [223, 233, 200, 41], [63, 190, 169, 165]],
              [[171, 26, 250, 194, 97, 16, 18, 205],
               [97, 16, 18, 205, 140, 239, 149, 38],
               [140, 239, 149, 38, 24, 195, 235, 232],
               [24, 195, 235, 232]]]

        correct = [[207, 188, 201, 170], [185, 152, 243, 25],
                   [123, 141, 178, 248], [85, 231, 98, 46]]

        self.assertEqual(skinny.add_round_tweakey(state, TW), correct,
                         "Tweakey not added correctly")


class TestShiftRows(unittest.TestCase):
    """
    Unit tests for the shift rows method of SKINNY
    """

    def test_shift_rows_64_64(self):
        """
        Unit test for the shift rows method of SKINNY-64-64
        """

        skinny = Skinny([64, 64, 32])

        state = [[2, 7, 14, 6], [8, 7, 10, 12],
                 [9, 11, 9, 1], [14, 6, 8, 14]]

        correct = [[2, 7, 14, 6], [12, 8, 7, 10],
                   [9, 1, 9, 11], [6, 8, 14, 14]]

        self.assertEqual(skinny.shift_rows(state), correct,
                         "Rows not shifted correctly")

    def test_shift_rows_64_128(self):
        """
        Unit test for the shift rows method of SKINNY-64-128
        """

        skinny = Skinny([64, 128, 36])

        state = [[11, 7, 7, 8], [14, 4, 2, 15],
                 [13, 14, 12, 15], [8, 3, 5, 5]]

        correct = [[11, 7, 7, 8], [15, 14, 4, 2],
                   [12, 15, 13, 14], [3, 5, 5, 8]]

        self.assertEqual(skinny.shift_rows(state), correct,
                         "Rows not shifted correctly")

    def test_shift_rows_64_192(self):
        """
        Unit test for the shift rows method of SKINNY-64-192
        """

        skinny = Skinny([64, 192, 40])

        state = [[6, 8, 4, 12], [11, 8, 14, 11],
                 [8, 7, 3, 2], [2, 0, 4, 0]]

        correct = [[6, 8, 4, 12], [11, 11, 8, 14],
                   [3, 2, 8, 7], [0, 4, 0, 2]]

        self.assertEqual(skinny.shift_rows(state), correct,
                         "Rows not shifted correctly")

    def test_shift_rows_128_128(self):
        """
        Unit test for the shift rows method of SKINNY-128-128
        """

        skinny = Skinny([128, 128, 40])

        state = [[160, 15, 177, 235], [180, 36, 177, 200],
                 [186, 217, 15, 72], [226, 179, 94, 137]]

        correct = [[160, 15, 177, 235], [200, 180, 36, 177],
                   [15, 72, 186, 217], [179, 94, 137, 226]]

        self.assertEqual(skinny.shift_rows(state), correct,
                         "Rows not shifted correctly")

    def test_shift_rows_128_256(self):
        """
        Unit test for the shift rows method of SKINNY-128-256
        """

        skinny = Skinny([128, 256, 48])

        state = [[17, 14, 242, 174], [64, 157, 167, 61],
                 [68, 56, 16, 96], [175, 106, 217, 224]]

        correct = [[17, 14, 242, 174], [61, 64, 157, 167],
                   [16, 96, 68, 56], [106, 217, 224, 175]]

        self.assertEqual(skinny.shift_rows(state), correct,
                         "Rows not shifted correctly")

    def test_shift_rows_128_384(self):
        """
        Unit test for the shift rows method of SKINNY-128-256
        """

        skinny = Skinny([128, 384, 56])

        state = [[207, 188, 201, 170], [185, 152, 243, 25],
                 [123, 141, 178, 248], [85, 231, 98, 46]]

        correct = [[207, 188, 201, 170], [25, 185, 152, 243],
                   [178, 248, 123, 141], [231, 98, 46, 85]]

        self.assertEqual(skinny.shift_rows(state), correct,
                         "Rows not shifted correctly")


class TestInvShiftRows(unittest.TestCase):
    """
    Unit tests for the inverse shift rows method of SKINNY
    """

    def test_shift_rows_inv_64_64(self):
        """
        Unit test for the inverse shift rows method of SKINNY-64-64
        """

        skinny = Skinny([64, 64, 32])

        state = [[2, 7, 14, 6], [12, 8, 7, 10],
                 [9, 1, 9, 11], [6, 8, 14, 14]]

        correct = [[2, 7, 14, 6], [8, 7, 10, 12],
                   [9, 11, 9, 1], [14, 6, 8, 14]]

        self.assertEqual(skinny.shift_rows_inv(state), correct,
                         "Rows not inverse shifted correctly")

    def test_shift_rows_inv_64_128(self):
        """
        Unit test for the inverse shift rows method of SKINNY-64-128
        """
        skinny = Skinny([64, 128, 36])

        state = [[11, 7, 7, 8], [15, 14, 4, 2],
                 [12, 15, 13, 14], [3, 5, 5, 8]]

        correct = [[11, 7, 7, 8], [14, 4, 2, 15],
                   [13, 14, 12, 15], [8, 3, 5, 5]]
        self.assertEqual(skinny.shift_rows_inv(state), correct,
                         "Rows not inverse shifted correctly")

    def test_shift_rows_inv_64_192(self):
        """
        Unit test for the inverse shift rows method of SKINNY-64-192
        """

        skinny = Skinny([64, 192, 40])

        state = [[6, 8, 4, 12], [11, 11, 8, 14],
                 [3, 2, 8, 7], [0, 4, 0, 2]]

        correct = [[6, 8, 4, 12], [11, 8, 14, 11],
                   [8, 7, 3, 2], [2, 0, 4, 0]]

        self.assertEqual(skinny.shift_rows_inv(state), correct,
                         "Rows not inverse shifted correctly")

    def test_shift_rows_inv_128_128(self):
        """
        Unit test for the inverse shift rows method of SKINNY-128-128
        """

        skinny = Skinny([128, 128, 40])

        state = [[160, 15, 177, 235], [200, 180, 36, 177],
                 [15, 72, 186, 217], [179, 94, 137, 226]]

        correct = [[160, 15, 177, 235], [180, 36, 177, 200],
                   [186, 217, 15, 72], [226, 179, 94, 137]]

        self.assertEqual(skinny.shift_rows_inv(state), correct,
                         "Rows not inverse shifted correctly")

    def test_shift_rows_inv_128_256(self):
        """
        Unit test for the inverse shift rows method of SKINNY-128-256
        """

        skinny = Skinny([128, 128, 48])

        state = [[17, 14, 242, 174], [61, 64, 157, 167],
                 [16, 96, 68, 56], [106, 217, 224, 175]]

        correct = [[17, 14, 242, 174], [64, 157, 167, 61],
                   [68, 56, 16, 96], [175, 106, 217, 224]]

        self.assertEqual(skinny.shift_rows_inv(state), correct,
                         "Rows not inverse shifted correctly")

    def test_shift_rows_inv_128_384(self):
        """
        Unit test for the inverse shift rows method of SKINNY-128-384
        """

        skinny = Skinny([128, 384, 56])

        state = [[207, 188, 201, 170], [25, 185, 152, 243],
                 [178, 248, 123, 141], [231, 98, 46, 85]]

        correct = [[207, 188, 201, 170], [185, 152, 243, 25],
                   [123, 141, 178, 248], [85, 231, 98, 46]]

        self.assertEqual(skinny.shift_rows_inv(state), correct,
                         "Rows not inverse shifted correctly")


class TestMixColumns(unittest.TestCase):
    """
    Unit tests for the mix columns method of SKINNY
    """

    def test_mix_columns_64_64(self):
        """
        Unit test for the mix columns method of SKINNY-64-64
        """

        skinny = Skinny([64, 64, 32])

        state = [[2, 7, 14, 6], [12, 8, 7, 10],
                 [9, 1, 9, 11], [6, 8, 14, 14]]

        correct = [[13, 14, 9, 3], [2, 7, 14, 6],
                   [5, 9, 14, 1], [11, 6, 7, 13]]

        self.assertEqual(skinny.mix_columns(state), correct,
                         "Columns not mixed correctly")

    def test_mix_columns_64_128(self):
        """
        Unit test for the mix columns method of SKINNY-64-128
        """

        skinny = Skinny([64, 128, 36])

        state = [[11, 7, 7, 8], [15, 14, 4, 2],
                 [12, 15, 13, 14], [3, 5, 5, 8]]

        correct = [[4, 13, 15, 14], [11, 7, 7, 8],
                   [3, 1, 9, 12], [7, 8, 10, 6]]

        self.assertEqual(skinny.mix_columns(state), correct,
                         "Columns not mixed correctly")

    def test_mix_columns_64_192(self):
        """
        Unit test for the mix columns method of SKINNY-64-192
        """

        skinny = Skinny([64, 192, 40])

        state = [[6, 8, 4, 12], [11, 11, 8, 14],
                 [3, 2, 8, 7], [0, 4, 0, 2]]

        correct = [[5, 14, 12, 9], [6, 8, 4, 12],
                   [8, 9, 0, 9], [5, 10, 12, 11]]

        self.assertEqual(skinny.mix_columns(state), correct,
                         "Columns not mixed correctly")

    def test_mix_columns_128_128(self):
        """
        Unit test for the mix columns method of SKINNY-128-128
        """

        skinny = Skinny([128, 128, 40])

        state = [[160, 15, 177, 235], [200, 180, 36, 177],
                 [15, 72, 186, 217], [179, 94, 137, 226]]

        correct = [[28, 25, 130, 208], [160, 15, 177, 235],
                   [199, 252, 158, 104], [175, 71, 11, 50]]

        self.assertEqual(skinny.mix_columns(state), correct,
                         "Columns not mixed correctly")

    def test_mix_columns_128_256(self):
        """
        Unit test for the mix columns method of SKINNY-128-256
        """

        skinny = Skinny([128, 256, 48])

        state = [[17, 14, 242, 174], [61, 64, 157, 167],
                 [16, 96, 68, 56], [106, 217, 224, 175]]

        correct = [[107, 183, 86, 57], [17, 14, 242, 174],
                   [45, 32, 217, 159], [1, 110, 182, 150]]

        self.assertEqual(skinny.mix_columns(state), correct,
                         "Columns not mixed correctly")

    def test_mix_columns_128_384(self):
        """
        Unit test for the mix columns method of SKINNY-128-384
        """

        skinny = Skinny([128, 384, 56])

        state = [[207, 188, 201, 170], [25, 185, 152, 243],
                 [178, 248, 123, 141], [231, 98, 46, 85]]

        correct = [[154, 38, 156, 114], [207, 188, 201, 170],
                   [171, 65, 227, 126], [125, 68, 178, 39]]

        self.assertEqual(skinny.mix_columns(state), correct,
                         "Columns not mixed correctly")


class TestInvMixColumns(unittest.TestCase):
    """
    Unit tests for the inverse mix columns method of SKINNY
    """

    def test_mix_columns_inv_64_64(self):
        """
        Unit test for the inverse mix columns method of SKINNY-64-64
        """

        skinny = Skinny([64, 64, 32])

        state = [[13, 14, 9, 3], [2, 7, 14, 6], [5, 9, 14, 1], [11, 6, 7, 13]]
        correct = [[2, 7, 14, 6], [12, 8, 7, 10], [9, 1, 9, 11],
                   [6, 8, 14, 14]]
        self.assertEqual(skinny.mix_columns_inv(state), correct,
                         "Columns not inverse mixed correctly")

    def test_mix_columns_inv_64_128(self):
        """
        Unit test for the inverse mix columns method of SKINNY-64-128
        """

        skinny = Skinny([64, 128, 36])

        state = [[4, 13, 15, 14], [11, 7, 7, 8], [3, 1, 9, 12], [7, 8, 10, 6]]
        correct = [[11, 7, 7, 8], [15, 14, 4, 2], [12, 15, 13, 14],
                   [3, 5, 5, 8]]
        self.assertEqual(skinny.mix_columns_inv(state), correct,
                         "Columns not inverse mixed correctly")

    def test_mix_columns_inv_64_192(self):
        """
        Unit test for the inverse mix columns method of SKINNY-64-192
        """

        skinny = Skinny([64, 192, 40])

        state = [[5, 14, 12, 9], [6, 8, 4, 12], [8, 9, 0, 9], [5, 10, 12, 11]]
        correct = [[6, 8, 4, 12], [11, 11, 8, 14], [3, 2, 8, 7], [0, 4, 0, 2]]
        self.assertEqual(skinny.mix_columns_inv(state), correct,
                         "Columns not inverse mixed correctly")

    def test_shift_rows_inv_128_128(self):
        """
        Unit test for the inverse mix columns method of SKINNY-128-128
        """

        skinny = Skinny([128, 128, 40])

        state = [[28, 25, 130, 208], [160, 15, 177, 235], [199, 252, 158, 104],
                 [175, 71, 11, 50]]
        correct = [[160, 15, 177, 235], [200, 180, 36, 177],
                   [15, 72, 186, 217], [179, 94, 137, 226]]
        self.assertEqual(skinny.mix_columns_inv(state), correct,
                         "Columns not inverse mixed correctly")

    def test_mix_columns_inv_128_256(self):
        """
        Unit test for the inverse mix columns method of SKINNY-128-256
        """

        skinny = Skinny([128, 256, 48])

        state = [[107, 183, 86, 57], [17, 14, 242, 174], [45, 32, 217, 159],
                 [1, 110, 182, 150]]
        correct = [[17, 14, 242, 174], [61, 64, 157, 167], [16, 96, 68, 56],
                   [106, 217, 224, 175]]
        self.assertEqual(skinny.mix_columns_inv(state), correct,
                         "Columns not inverse mixed correctly")

    def test_mix_columns_inv_128_384(self):
        """
        Unit test for the inverse mix columns method of SKINNY-128-384
        """

        skinny = Skinny([128, 384, 56])

        state = [[154, 38, 156, 114], [207, 188, 201, 170],
                 [171, 65, 227, 126], [125, 68, 178, 39]]
        correct = [[207, 188, 201, 170], [25, 185, 152, 243],
                   [178, 248, 123, 141], [231, 98, 46, 85]]
        self.assertEqual(skinny.mix_columns_inv(state), correct,
                         "Columns not inverse mixed correctly")


class TestUpdateTweakey(unittest.TestCase):
    """
    Unit tests for the update tweakey method of SKINNY
    """

    def test_update_tweakey_arrays_64_64(self):
        """
        Unit test for the update tweakey arrays method of SKINNY-64-64
        """

        skinny = Skinny([64, 64, 32])

        TW = [[[15, 5, 2, 6], [9, 8, 2, 6],
               [15, 12, 6, 8], [1, 2, 3, 8]],
              [], []]

        correct = [[[12, 8, 15, 2], [6, 3, 1, 8],
                    [15, 5, 2, 6], [9, 8, 2, 6]], [], []]

        self.assertEqual(skinny.update_tweakey_arrays(TW), correct,
                         "Tweakey not updated correctly")

    def test_update_tweakey_arrays_64_128(self):
        """
        Unit test for the update tweakey arrays method of SKINNY-64-128
        """

        skinny = Skinny([64, 128, 36])

        TW = [[[9, 14, 11, 9], [3, 6, 4, 0],
               [13, 0, 8, 8], [13, 10, 6, 3]],
              [[7, 6, 10, 3], [9, 13, 1, 12],
               [8, 11, 14, 10], [7, 1, 14, 1]], []]

        correct = [[[0, 3, 13, 10], [8, 6, 13, 8],
                    [9, 14, 11, 9], [3, 6, 4, 0]],
                   [[7, 2, 1, 2], [12, 12, 15, 5],
                    [7, 6, 10, 3], [9, 13, 1, 12]], []]

        self.assertEqual(skinny.update_tweakey_arrays(TW), correct,
                         "Tweakey not updated correctly")

    def test_update_tweakey_arrays_64_192(self):
        """
        Unit test for the update tweakey arrays method of SKINNY-64-192
        """

        skinny = Skinny([64, 192, 40])

        TW = [[[14, 13, 0, 0], [12, 8, 5, 11],
               [1, 2, 0, 13], [6, 8, 6, 1]],
              [[8, 7, 5, 3], [14, 2, 4, 11],
               [15, 13, 9, 0], [8, 15, 6, 0]],
              [[11, 2, 13, 11], [11, 4, 1, 11],
               [4, 2, 2, 13], [15, 12, 13, 0]]]

        correct = [[[2, 1, 1, 8], [0, 6, 6, 13],
                    [14, 13, 0, 0], [12, 8, 5, 11]],
                   [[10, 0, 14, 14], [3, 13, 1, 0],
                    [8, 7, 5, 3], [14, 2, 4, 11]],
                   [[1, 0, 2, 14], [1, 6, 7, 6],
                    [11, 2, 13, 11], [11, 4, 1, 11]]]

        self.assertEqual(skinny.update_tweakey_arrays(TW), correct,
                         "Tweakey not updated correctly")

    def test_update_tweakey_arrays_128_128(self):
        """
        Unit test for the update tweakey arrays method of SKINNY-128-128
        """

        skinny = Skinny([128, 128, 40])
        TW = [[[79, 85, 207, 176], [82, 12, 172, 82],
               [253, 146, 193, 95], [55, 7, 62, 147]], [], []]

        correct = [[[146, 147, 253, 7], [193, 62, 55, 95],
                    [79, 85, 207, 176], [82, 12, 172, 82]], [], []]

        self.assertEqual(skinny.update_tweakey_arrays(TW), correct,
                         "Tweakey not updated correctly")

    def test_update_tweakey_arrays_128_256(self):
        """
        Unit test for the update tweakey arrays method of SKINNY-128-256
        """

        skinny = Skinny([128, 256, 48])

        TW = [[[0, 156, 236, 129], [96, 93, 74, 193],
               [210, 174, 158, 48], [133, 215, 161, 243]],
              [[26, 193, 35, 235], [252, 0, 253, 220],
               [240, 16, 70, 206], [237, 223, 202, 179]], []]

        correct = [[[174, 243, 210, 215], [158, 161, 133, 48],
                    [0, 156, 236, 129], [96, 93, 74, 193]],
                   [[32, 102, 224, 191], [140, 149, 218, 157],
                    [26, 193, 35, 235], [252, 0, 253, 220]], []]

        self.assertEqual(skinny.update_tweakey_arrays(TW), correct,
                         "Tweakey not updated correctly")

    def test_update_tweakey_arrays_128_384(self):
        """
        Unit test for the update tweakey arrays method of SKINNY-128-384
        """

        skinny = Skinny([128, 384, 56])

        TW = [[[223, 136, 149, 72], [207, 199, 234, 82],
               [210, 150, 51, 147], [1, 121, 116, 73]],
              [[171, 88, 138, 52], [164, 127, 26, 178],
               [223, 233, 200, 41], [63, 190, 169, 165]],
              [[171, 26, 250, 194, 97, 16, 18, 205],
               [97, 16, 18, 205, 140, 239, 149, 38],
               [140, 239, 149, 38, 24, 195, 235, 232],
               [24, 195, 235, 232]]]

        correct = [[[150, 73, 210, 121], [51, 116, 1, 147],
                    [223, 136, 149, 72], [207, 199, 234, 82]],
                   [[210, 74, 191, 124], [145, 82, 127, 83],
                    [171, 88, 138, 52], [164, 127, 26, 178]],
                   [[119, 244, 70, 97], [202, 117, 12, 19],
                    [171, 26, 250, 194], [97, 16, 18, 205]]]

        self.assertEqual(skinny.update_tweakey_arrays(TW), correct,
                         "Tweakey not updated correctly")


class TestInitialiseKey(unittest.TestCase):
    """
    Unit tests for the initialise key method of SKINNY
    """

    def test_initialise_key_64_64(self):
        """
        Unit test for the initialise key method of SKINNY-64-64
        """

        skinny = Skinny([64, 64, 32])

        key = [15, 5, 2, 6, 9, 8, 2, 6, 15, 12, 6, 8, 1, 2, 3, 8]

        correct = [[[15, 5, 2, 6], [9, 8, 2, 6],
                    [15, 12, 6, 8], [1, 2, 3, 8]], [], []]

        self.assertEqual(skinny.initialise_key(key), correct,
                         "Key not initialised correctly")

    def test_initialise_key_64_128(self):
        """
        Unit test for the initialise key  method of SKINNY-64-128
        """

        skinny = Skinny([64, 128, 36])

        key = [9, 14, 11, 9, 3, 6, 4, 0, 13, 0, 8, 8, 13, 10, 6, 3, 7, 6, 10,
               3, 9, 13, 1, 12, 8, 11, 14, 10, 7, 1, 14, 1]

        correct = [[[9, 14, 11, 9], [3, 6, 4, 0],
                    [13, 0, 8, 8], [13, 10, 6, 3]],
                   [[7, 6, 10, 3], [9, 13, 1, 12],
                    [8, 11, 14, 10], [7, 1, 14, 1]], []]

        self.assertEqual(skinny.initialise_key(key), correct,
                         "Key not initialised correctly")

    def test_initialise_key_64_192(self):
        """
        Unit test for the initialise key  method of SKINNY-64-128
        """

        skinny = Skinny([64, 192, 40])

        key = [14, 13, 0, 0, 12, 8, 5, 11, 1, 2, 0, 13, 6, 8, 6, 1, 8, 7, 5,
               3, 14, 2, 4, 11, 15, 13, 9, 0, 8, 15, 6, 0, 11, 2, 13, 11,
               11, 4, 1, 11, 4, 2, 2, 13, 15, 12, 13, 0]
        correct =[[[14, 13, 0, 0], [12, 8, 5, 11],
                   [1, 2, 0, 13], [6, 8, 6, 1]],
                  [[8, 7, 5, 3], [14, 2, 4, 11],
                   [15, 13, 9, 0], [8, 15, 6, 0]],
                  [[11, 2, 13, 11], [11, 4, 1, 11],
                   [4, 2, 2, 13], [15, 12, 13, 0]]]

        self.assertEqual(skinny.initialise_key(key), correct,
                         "Key not initialised correctly")

    def test_initialise_key_128_128(self):
        """
        Unit test for the initialise key  method of SKINNY-128-128
        """

        skinny = Skinny([128, 128, 40])

        key = [4, 15, 5, 5, 12, 15, 11, 0, 5, 2, 0, 12, 10, 12, 5, 2, 15, 13,
               9, 2, 12, 1, 5, 15, 3, 7, 0, 7, 3, 14, 9, 3]

        correct = [[[79, 85, 207, 176], [82, 12, 172, 82],
                    [253, 146, 193, 95], [55, 7, 62, 147]], [], []]

        self.assertEqual(skinny.initialise_key(key), correct,
                         "Key not initialised correctly")

    def test_initialise_key_128_256(self):
        """
        Unit test for the initialise key  method of SKINNY-128-256
        """

        skinny = Skinny([128, 256, 48])

        key = [0, 0, 9, 12, 14, 12, 8, 1, 6, 0, 5, 13, 4, 10, 12, 1, 13, 2, 10,
               14, 9, 14, 3, 0, 8, 5, 13, 7, 10, 1, 15, 3, 1, 10, 12, 1, 2, 3,
               14, 11, 15, 12, 0, 0, 15, 13, 13, 12, 15, 0, 1, 0, 4, 6, 12,
               14, 14, 13, 13, 15, 12, 10, 11, 3]

        correct = [[[0, 156, 236, 129], [96, 93, 74, 193],
                    [210, 174, 158, 48], [133, 215, 161, 243]],
                   [[26, 193, 35, 235], [252, 0, 253, 220],
                    [240, 16, 70, 206], [237, 223, 202, 179]], []]

        self.assertEqual(skinny.initialise_key(key), correct,
                         "Key not initialised correctly")

    def test_initialise_key_128_384(self):
        """
        Unit test for the initialise key method of SKINNY-128-384
        """

        skinny = Skinny([128, 384, 56])

        key = [13, 15, 8, 8, 9, 5, 4, 8, 12, 15, 12, 7, 14, 10, 5, 2, 13, 2,
               9, 6, 3, 3, 9, 3, 0, 1, 7, 9, 7, 4, 4, 9, 10, 11, 5, 8, 8, 10,
               3, 4, 10, 4, 7, 15, 1, 10, 11, 2, 13, 15, 14, 9, 12, 8, 2, 9,
               3, 15, 11, 14, 10, 9, 10, 5, 10, 11, 1, 10, 15, 10, 12, 2, 6,
               1, 1, 0, 1, 2, 12, 13, 8, 12, 14, 15, 9, 5, 2, 6, 1, 8, 12, 3,
               14, 11, 14, 8]

        correct = [[[223, 136, 149, 72], [207, 199, 234, 82],
                    [210, 150, 51, 147], [1, 121, 116, 73]],
                   [[171, 88, 138, 52], [164, 127, 26, 178],
                    [223, 233, 200, 41], [63, 190, 169, 165]],
                   [[171, 26, 250, 194, 97, 16, 18, 205],
                    [97, 16, 18, 205, 140, 239, 149, 38],
                    [140, 239, 149, 38, 24, 195, 235, 232],
                    [24, 195, 235, 232]]]

        self.assertEqual(skinny.initialise_key(key), correct,
                         "Key not initialised correctly")


class TestInitialiseState(unittest.TestCase):
    """
    Unit tests for the initialise state method of SKINNY
    """

    def test_initialise_state_64_64(self):
        """
        Unit test for the initialise state method of SKINNY-64-64
        """

        skinny = Skinny([64, 64, 32])

        plaintext = [0, 6, 0, 3, 4, 15, 9, 5, 7, 7, 2, 4, 13, 1, 9, 13]

        correct =[[0, 6, 0, 3], [4, 15, 9, 5], [7, 7, 2, 4], [13, 1, 9, 13]]

        self.assertEqual(skinny.initialise_state(plaintext), correct,
                         "State not initialised correctly")

    def test_initialise_state_128_128(self):
        """
        Unit test for the initialise state method of SKINNY-128-128
        """

        skinny = Skinny([128, 128, 40])

        plaintext = [15, 2, 0, 10, 13, 11, 0, 14, 11, 0, 8, 11, 6, 4, 8, 10,
                     3, 11, 2, 14, 14, 14, 13, 1, 15, 0, 10, 13, 13, 10, 1, 4]
        correct = [[242, 10, 219, 14], [176, 139, 100, 138],
                   [59, 46, 238, 209], [240, 173, 218, 20]]

        self.assertEqual(skinny.initialise_state(plaintext), correct,
                         "State not initialised correctly")


class TestLFSR(unittest.TestCase):
    """
    Unit tests for LFSR in SKINNY
    """

    def test_LFSR(self):
        """
        Unit test for LFSR
        """

        TW = 15
        correct = 14

        self.assertEqual(LFSR(TW, 2, 4), correct,
                         "LFSR not applied correctly")

    def test_LFSR_2(self):
        """
        Unit test for the LFSR - 2
        """

        TW = 255
        correct = 254

        self.assertEqual(LFSR(TW, 2, 8), correct,
                         "LFSR not applied correctly")

    def test_LFSR_3(self):
        """
        Unit test for the LFSR - 3
        """

        TW = 0
        correct = 0

        self.assertEqual(LFSR(TW, 3, 8), correct,
                         "LFSR not applied correctly")


# INTEGRATION TESTS
class TestEncryptBlock(unittest.TestCase):
    """
    Integration tests for the encrypt_block method of the SKINNY class.
    Each version of skinny is tested
    """

    def test_encrypt_block_64_64(self):
        """
        Integration test for encrypting SKINNY-64-64
        """

        skinny = Skinny([64, 64, 32])

        plaintext = [0, 6, 0, 3, 4, 15, 9, 5, 7, 7, 2, 4, 13, 1, 9, 13]
        key = [15, 5, 2, 6, 9, 8, 2, 6, 15, 12, 6, 8, 1, 2, 3, 8]
        correct = [11, 11, 3, 9, 13, 15, 11, 2, 4, 2, 9, 11, 8, 10, 12, 7]

        self.assertEqual(skinny.encrypt_block(plaintext, key), correct,
                         "Block not encrypted correctly")

    def test_encrypt_block_64_128(self):
        """
        Integration test for encrypting SKINNY-64-128
        """

        skinny = Skinny([64, 128, 36])

        plaintext = [12, 15, 1, 6, 12, 15, 14, 8, 15, 13, 0, 15, 9, 8, 10, 10]
        key = [9, 14, 11, 9, 3, 6, 4, 0, 13, 0, 8, 8, 13, 10, 6, 3, 7, 6, 10,
               3, 9, 13, 1, 12, 8, 11, 14, 10, 7, 1, 14, 1]
        correct = [6, 12, 14, 13, 10, 1, 15, 4, 3, 13, 14, 9, 2, 11, 9, 14]

        self.assertEqual(skinny.encrypt_block(plaintext, key), correct,
                         "Block not encrypted correctly")

    def test_encrypt_block_64_192(self):
        """
        Integration test for encrypting SKINNY-64-192
        """

        skinny = Skinny([64, 192, 40])

        plaintext = [5, 3, 0, 12, 6, 1, 13, 3, 5, 14, 8, 6, 6, 3, 12, 3]
        key = [14, 13, 0, 0, 12, 8, 5, 11, 1, 2, 0, 13, 6, 8, 6, 1, 8, 7, 5,
               3, 14, 2, 4, 11, 15, 13, 9, 0, 8, 15, 6, 0, 11, 2, 13, 11,
               11, 4, 1, 11, 4, 2, 2, 13, 15, 12, 13, 0]
        correct = [13, 13, 2, 12, 15, 1, 10, 8, 15, 3, 3, 0, 3, 0, 3, 12]
        self.assertEqual(skinny.encrypt_block(plaintext, key), correct,
                         "Block not encrypted correctly")

    def test_encrypt_block_128_128(self):
        """
        Integration test for encrypting SKINNY-128-128
        """

        skinny = Skinny([128, 128, 40])
        plaintext = [15, 2, 0, 10, 13, 11, 0, 14, 11, 0, 8, 11, 6, 4, 8, 10,
                     3, 11, 2, 14, 14, 14, 13, 1, 15, 0, 10, 13, 13, 10, 1, 4]
        key = [4, 15, 5, 5, 12, 15, 11, 0, 5, 2, 0, 12, 10, 12, 5, 2, 15, 13,
               9, 2, 12, 1, 5, 15, 3, 7, 0, 7, 3, 14, 9, 3]
        correct = [2, 2, 15, 15, 3, 0, 13, 4, 9, 8, 14, 10, 6, 2, 13, 7, 14,
                   4, 5, 11, 4, 7, 6, 14, 3, 3, 6, 7, 5, 11, 7, 4]
        self.assertEqual(skinny.encrypt_block(plaintext, key), correct,
                         "Block not encrypted correctly")

    def test_encrypt_block_128_256(self):
        """
        Integration test for encrypting SKINNY-128-256
        """

        skinny = Skinny([128, 256, 48])
        plaintext = [3, 10, 0, 12, 4, 7, 7, 6, 7, 10, 2, 6, 10, 6, 8, 13, 13,
                     3, 8, 2, 10, 6, 9, 5, 14, 7, 0, 2, 2, 14, 2, 5]
        key = [0, 0, 9, 12, 14, 12, 8, 1, 6, 0, 5, 13, 4, 10, 12, 1, 13, 2, 10,
               14, 9, 14, 3, 0, 8, 5, 13, 7, 10, 1, 15, 3, 1, 10, 12, 1, 2, 3,
               14, 11, 15, 12, 0, 0, 15, 13, 13, 12, 15, 0, 1, 0, 4, 6, 12,
               14, 14, 13, 13, 15, 12, 10, 11, 3]
        correct = [11, 7, 3, 1, 13, 9, 8, 10, 4, 11, 13, 14, 1, 4, 7, 10, 7,
                   14, 13, 4, 10, 6, 15, 1, 6, 11, 9, 11, 5, 8, 7, 15]

        self.assertEqual(skinny.encrypt_block(plaintext, key), correct,
                         "Block not encrypted correctly")

    def test_encrypt_block_128_384(self):
        """
        Integration test for encrypting SKINNY-128-384
        """

        skinny = Skinny([128, 384, 56])

        plaintext = [10, 3, 9, 9, 4, 11, 6, 6, 10, 13, 8, 5, 10, 3, 4, 5, 9,
                     15, 4, 4, 14, 9, 2, 11, 0, 8, 15, 5, 5, 0, 12, 11]
        key = [13, 15, 8, 8, 9, 5, 4, 8, 12, 15, 12, 7, 14, 10, 5, 2, 13, 2,
               9, 6, 3, 3, 9, 3, 0, 1, 7, 9, 7, 4, 4, 9, 10, 11, 5, 8, 8, 10,
               3, 4, 10, 4, 7, 15, 1, 10, 11, 2, 13, 15, 14, 9, 12, 8, 2, 9,
               3, 15, 11, 14, 10, 9, 10, 5, 10, 11, 1, 10, 15, 10, 12, 2, 6,
               1, 1, 0, 1, 2, 12, 13, 8, 12, 14, 15, 9, 5, 2, 6, 1, 8, 12, 3,
               14, 11, 14, 8]
        correct = [9, 4, 14, 12, 15, 5, 8, 9, 14, 2, 0, 1, 7, 12, 6, 0, 1, 11,
                   3, 8, 12, 6, 3, 4, 6, 10, 1, 0, 13, 12, 15, 10]

        self.assertEqual(skinny.encrypt_block(plaintext, key), correct,
                         "Block not encrypted correctly")


class TestDecryptBlock(unittest.TestCase):
    """
    Integration tests for the decrypt_block method of the SKINNY class.
    Each version of skinny is tested
    """

    def test_decrypt_block_64_64(self):
        """
        Integration test for encrypting SKINNY-64-64
        """

        skinny = Skinny([64, 64, 32])

        plaintext = [11, 11, 3, 9, 13, 15, 11, 2, 4, 2, 9, 11, 8, 10, 12, 7]
        key = [15, 5, 2, 6, 9, 8, 2, 6, 15, 12, 6, 8, 1, 2, 3, 8]
        correct = [0, 6, 0, 3, 4, 15, 9, 5, 7, 7, 2, 4, 13, 1, 9, 13]

        self.assertEqual(skinny.decrypt_block(plaintext, key), correct,
                         "Block not decrypted correctly")

    def test_decrypt_block_64_128(self):
        """
        Integration test for encrypting SKINNY-64-128
        """

        skinny = Skinny([64, 128, 36])

        plaintext = [6, 12, 14, 13, 10, 1, 15, 4, 3, 13, 14, 9, 2, 11, 9, 14]
        key = [9, 14, 11, 9, 3, 6, 4, 0, 13, 0, 8, 8, 13, 10, 6, 3, 7, 6, 10,
               3, 9, 13, 1, 12, 8, 11, 14, 10, 7, 1, 14, 1]
        correct = [12, 15, 1, 6, 12, 15, 14, 8, 15, 13, 0, 15, 9, 8, 10, 10]

        self.assertEqual(skinny.decrypt_block(plaintext, key), correct,
                         "Block not decrypted correctly")

    def test_decrypt_block_64_192(self):
        """
        Integration test for encrypting SKINNY-64-192
        """

        skinny = Skinny([64, 192, 40])

        plaintext = [13, 13, 2, 12, 15, 1, 10, 8, 15, 3, 3, 0, 3, 0, 3, 12]
        key = [14, 13, 0, 0, 12, 8, 5, 11, 1, 2, 0, 13, 6, 8, 6, 1, 8, 7, 5,
               3, 14, 2, 4, 11, 15, 13, 9, 0, 8, 15, 6, 0, 11, 2, 13, 11,
               11, 4, 1, 11, 4, 2, 2, 13, 15, 12, 13, 0]
        correct = [5, 3, 0, 12, 6, 1, 13, 3, 5, 14, 8, 6, 6, 3, 12, 3]

        self.assertEqual(skinny.decrypt_block(plaintext, key), correct,
                         "Block not decrypted correctly")

    def test_decrypt_block_128_128(self):
        """
        Integration test for encrypting SKINNY-128-128
        """

        skinny = Skinny([128, 128, 40])

        plaintext = [2, 2, 15, 15, 3, 0, 13, 4, 9, 8, 14, 10, 6, 2, 13, 7, 14,
                     4, 5, 11, 4, 7, 6, 14, 3, 3, 6, 7, 5, 11, 7, 4]
        key = [4, 15, 5, 5, 12, 15, 11, 0, 5, 2, 0, 12, 10, 12, 5, 2, 15, 13,
               9, 2, 12, 1, 5, 15, 3, 7, 0, 7, 3, 14, 9, 3]
        correct = [15, 2, 0, 10, 13, 11, 0, 14, 11, 0, 8, 11, 6, 4, 8, 10,
                   3, 11, 2, 14, 14, 14, 13, 1, 15, 0, 10, 13, 13, 10, 1, 4]

        self.assertEqual(skinny.decrypt_block(plaintext, key), correct,
                         "Block not decrypted correctly")

    def test_decrypt_block_128_256(self):
        """
        Integration test for encrypting SKINNY-128-256
        """

        skinny = Skinny([128, 256, 48])

        plaintext = [11, 7, 3, 1, 13, 9, 8, 10, 4, 11, 13, 14, 1, 4, 7, 10, 7,
                     14, 13, 4, 10, 6, 15, 1, 6, 11, 9, 11, 5, 8, 7, 15]
        key = [0, 0, 9, 12, 14, 12, 8, 1, 6, 0, 5, 13, 4, 10, 12, 1, 13, 2, 10,
               14, 9, 14, 3, 0, 8, 5, 13, 7, 10, 1, 15, 3, 1, 10, 12, 1, 2, 3,
               14, 11, 15, 12, 0, 0, 15, 13, 13, 12, 15, 0, 1, 0, 4, 6, 12,
               14, 14, 13, 13, 15, 12, 10, 11, 3]
        correct = [3, 10, 0, 12, 4, 7, 7, 6, 7, 10, 2, 6, 10, 6, 8, 13, 13,
                   3, 8, 2, 10, 6, 9, 5, 14, 7, 0, 2, 2, 14, 2, 5]

        self.assertEqual(skinny.decrypt_block(plaintext, key), correct,
                         "Block not decrypted correctly")

    def test_decrypt_block_128_384(self):
        """
        Integration test for encrypting SKINNY-128-384
        """

        skinny = Skinny([128, 384, 56])

        plaintext = [9, 4, 14, 12, 15, 5, 8, 9, 14, 2, 0, 1, 7, 12, 6, 0, 1,
                     11, 3, 8, 12, 6, 3, 4, 6, 10, 1, 0, 13, 12, 15, 10]
        key = [13, 15, 8, 8, 9, 5, 4, 8, 12, 15, 12, 7, 14, 10, 5, 2, 13, 2,
               9, 6, 3, 3, 9, 3, 0, 1, 7, 9, 7, 4, 4, 9, 10, 11, 5, 8, 8, 10,
               3, 4, 10, 4, 7, 15, 1, 10, 11, 2, 13, 15, 14, 9, 12, 8, 2, 9,
               3, 15, 11, 14, 10, 9, 10, 5, 10, 11, 1, 10, 15, 10, 12, 2, 6,
               1, 1, 0, 1, 2, 12, 13, 8, 12, 14, 15, 9, 5, 2, 6, 1, 8, 12, 3,
               14, 11, 14, 8]
        correct = [10, 3, 9, 9, 4, 11, 6, 6, 10, 13, 8, 5, 10, 3, 4, 5, 9,
                   15, 4, 4, 14, 9, 2, 11, 0, 8, 15, 5, 5, 0, 12, 11]

        self.assertEqual(skinny.decrypt_block(plaintext, key), correct,
                         "Block not decrypted correctly")


if __name__ == '__main__':
    unittest.main()
