"""
This file runs unit and integration tests for the SKINNY-AEAD class
"""

import sys
sys.path.append('..')
import unittest
from Skinny.skinnyaead import *
from Skinny.skinny import *


class TestApplyLFSR(unittest.TestCase):
    def setUp(self):
        # set up the SKINNY AEAD object(s)
        self.SKINNY_AEAD = SkinnyAead("M1", Skinny([128, 384, 56]))

    def test_apply_LFSR(self):
        """
        Unit test 1 for applying the LFSR -
        """

        lfsr = [0] * 15 + [1]
        correct = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]
        self.assertEqual(self.SKINNY_AEAD.apply_LFSR(lfsr), correct,
                         "Incorrect result")

    def test_apply_LFSR_2(self):
        """
        Unit test 2 for applying the LFSR -
        """

        lfsr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]
        correct = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4]
        self.assertEqual(self.SKINNY_AEAD.apply_LFSR(lfsr), correct,
                         "Incorrect result")


class TestGenerateLFSR(unittest.TestCase):
    """
    Unit tests for the generate LFSR method of the SKINNY AEAD class
    """

    def setUp(self):
        # set up the SKINNY AEAD object(s)
        self.SKINNY_AEAD = SkinnyAead("M1", Skinny([128,384, 56]))

    def test_apply_LFSR(self):
        """
        Unit test for applying the LFSR
        """

        correct = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        self.assertEqual(self.SKINNY_AEAD.generate_LFSR(), correct,
                         "Incorrect result")


class TestGetDomainSeparation(unittest.TestCase):
    """
    Unit tests for getting the correct domain separation byte
    """

    def setUp(self):
        # set up the SKINNY AEAD object(s)
        self.SKINNY_AEAD = SkinnyAead("M1", Skinny([128,384, 56]))

    def test_get_domain_separation(self):
        """
        Unit test 1 for getting the correct domain separation byte
        """

        d = 0
        correct = (0, 0)
        self.assertEqual(self.SKINNY_AEAD.get_domain_separation(d), correct,
                         "Incorrect result")

    def test_get_domain_separation_2(self):
        """
        Unit test 2 for getting the correct domain separation byte
        """

        d = 1
        correct = (0, 1)
        self.assertEqual(self.SKINNY_AEAD.get_domain_separation(d), correct,
                         "Incorrect result")

    def test_get_domain_separation_3(self):
        """
        Unit test 3 for getting the correct domain separation byte
        """

        d = 2
        correct = (0, 2)
        self.assertEqual(self.SKINNY_AEAD.get_domain_separation(d), correct,
                         "Incorrect result")

    def test_get_domain_separation_4(self):
        """
        Unit test 4 for getting the correct domain separation byte
        """

        d = 3
        correct = (0, 3)
        self.assertEqual(self.SKINNY_AEAD.get_domain_separation(d), correct,
                         "Incorrect result")

    def test_get_domain_separation_5(self):
        """
        Unit test 5 for getting the correct domain separation byte
        """

        d = 4
        correct = (0, 4)
        self.assertEqual(self.SKINNY_AEAD.get_domain_separation(d), correct,
                         "Incorrect result")

    def test_get_domain_separation_6(self):
        """
        Unit test 6 for getting the correct domain separation byte
        """

        d = 5
        correct = (0, 5)
        self.assertEqual(self.SKINNY_AEAD.get_domain_separation(d), correct,
                         "Incorrect result")


class TestRev64(unittest.TestCase):
    """
    Unit tests for testing the rev64 method which reverses bytes in a list
    """

    def setUp(self):
        # set up the SKINNY AEAD object(s)
        self.SKINNY_AEAD = SkinnyAead("M1", Skinny([128,384, 56]))

    def test_rev64_1(self):
        """
        Unit test 1 for reversing byte list
        """

        LFSR = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        correct = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(self.SKINNY_AEAD.rev64(LFSR), correct,
                         "Incorrect result")

    def test_rev64_2(self):
        """
        Unit test 2 for reversing byte list
        """

        LFSR = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4]
        correct = [0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(self.SKINNY_AEAD.rev64(LFSR), correct,
                         "Incorrect result")


class TestGenerateTK(unittest.TestCase):
    """
    Unit tests for generating the TK to use in the BC call
    """

    def setUp(self):
        # set up the SKINNY AEAD object(s)
        self.SKINNY_AEAD = SkinnyAead("M1", Skinny([128,384, 56]))
        self.SKINNY_AEAD.nonce = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6,
                                  0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0,
                                  13, 0, 14, 0, 15]
        self.SKINNY_AEAD.key = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0,
                                7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13,
                                0, 14, 0, 15]

    def test_generate_tk(self):
        """
        Unit test 1 generating the TK
        """

        d = 0
        LFSR = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        correct = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2,
                   0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11,
                   0, 12, 0, 13, 0, 14, 0, 15, 0, 0, 0, 1, 0, 2, 0, 3, 0, 4,
                   0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13,
                   0, 14, 0, 15]
        self.assertEqual(self.SKINNY_AEAD.generate_tweakey(d, LFSR), correct,
                         "Incorrect result")

    def test_generate_tk(self):
        """
        Unit test 2 generating the TK
        """

        d = 2
        LFSR = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4]
        correct = [0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 2,
                   0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0,
                   12, 0, 13, 0, 14, 0, 15, 0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0,
                   5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0,
                   14, 0, 15]
        self.assertEqual(self.SKINNY_AEAD.generate_tweakey(d, LFSR), correct,
                         "Incorrect result")


class TestGetSigma(unittest.TestCase):
    """
    Unit tests for generating sigma (xor of all blocks)
    """

    def setUp(self):
        # set up the SKINNY AEAD object(s)
        self.SKINNY_AEAD = SkinnyAead("M1", Skinny([128,384, 56]))

    def test_get_sigma(self):
        """
        Unit test 1 generating sigma
        """

        blocks = [[0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9,
                   0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15],
            [1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10,
             1, 11, 1, 12, 1, 13, 1, 14, 1, 15]]

        correct = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,
                   0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        self.assertEqual(self.SKINNY_AEAD.calculate_sigma(blocks), correct,
                         "Incorrect result")

    def test_get_sigma_2(self):
        """
        Unit test 2 generating sigma
        """

        blocks = [[]]
        correct = [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(self.SKINNY_AEAD.calculate_sigma(blocks), correct,
                         "Incorrect result")


class TestProcessAD(unittest.TestCase):
    """
    Unit tests for processing associated data blocks - tests a variety of
    possibilities - such as empty AD, incomplete AD, complete AD...
    """

    def setUp(self):
        # set up the SKINNY AEAD object(s)
        self.SKINNY_AEAD = SkinnyAead("M1", Skinny([128, 384, 56]))
        self.SKINNY_AEAD.nonce = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0,
                                  7, 0, 8, 0, 9, 0, 10,
                                  0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        self.SKINNY_AEAD.key = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7,
                                0, 8, 0, 9, 0, 10,
                                0, 11, 0, 12, 0, 13, 0, 14, 0, 15]

    def test_process_AD(self):
        """
        Unit test 1 processing associated data (empty block)
        """

        AD = [[]]
        correct = [0] * 128
        self.assertEqual(self.SKINNY_AEAD.process_ad(AD), correct,
                         "Incorrect result")

    def test_process_AD_2(self):
        """
        Unit test 2 processing associated data (complete block)
        """

        AD = [[0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0,
               10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15]]

        correct = [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1,
                   0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1,
                   0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1,
                   0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1,
                   0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1,
                   1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1,
                   1, 0, 0, 1, 0, 0, 0, 0]

        self.assertEqual(self.SKINNY_AEAD.process_ad(AD), correct,
                         "Incorrect result")

    def test_process_AD_3(self):
        """
        Unit test 1 processing associated data (Incomplete block)
        """

        AD = [[0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9]]
        correct = [1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1,
                   0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
                   0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0,
                   1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0,
                   0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1,
                   1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]

        self.assertEqual(self.SKINNY_AEAD.process_ad(AD), correct,
                         "Incorrect result")

    def test_process_AD_4(self):
        """
        Unit test 2 processing associated data (two full blocks)
        """

        AD = [
            [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15],
            [1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10,
             1, 11, 1, 12, 1, 13, 1, 14, 1, 15]]
        correct = [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0,
                   1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0,
                   0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1,
                   0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0,
                   0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0,
                   0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0,
                   1, 1, 0, 0, 0, 0, 1, 0]

        self.assertEqual(self.SKINNY_AEAD.process_ad(AD), correct,
                         "Incorrect result")


class TestProcessPlaintext(unittest.TestCase):
    """
    Unit tests to process the plaintext (a variety of tests for empty
    plaintext, incomplete plaintext, full plaintext etc...
    """

    def setUp(self):
        # set up the SKINNY AEAD object(s)
        self.SKINNY_AEAD = SkinnyAead("M1", Skinny([128, 384, 56]))
        self.SKINNY_AEAD.nonce = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0,
                                  7, 0, 8, 0, 9, 0, 10,
                                  0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        self.SKINNY_AEAD.key = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7,
                                0, 8, 0, 9, 0, 10,
                                0, 11, 0, 12, 0, 13, 0, 14, 0, 15]

    def test_process_plaintext(self):
        """
        Unit test 1 processing plaintext (empty block)
        """

        plaintext = [[]]
        correct = ([], [9, 9, 12, 14, 6, 8, 14, 15, 7, 11, 5, 2, 10, 10, 13,
                        0, 14, 1, 1, 12, 6, 14, 2, 15, 12, 7, 2, 2, 4, 2,
                        6, 13])

        self.assertEqual(self.SKINNY_AEAD.process_plaintext(plaintext), correct,
                         "Incorrect result")

    def test_process_plaintext_2(self):
        """
        Unit test 2 processing plaintext (full block)
        """

        plaintext = [[0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0,
                      9, 0, 10,  0, 11, 0, 12, 0, 13, 0, 14, 0, 15]]
        correct = ([[2, 4, 1, 15, 0, 13, 10, 12, 2, 12, 5, 13, 13, 10, 4, 8,
                     8, 15, 0, 14, 6, 8, 12, 10, 13, 11, 15, 2, 12, 12, 9,
                     15]], [11, 5, 12, 3, 5, 11, 9, 14, 0, 8, 7, 7, 4, 0, 4,
                    10, 4, 4, 7, 2, 0, 6, 10, 13, 8, 2, 1, 5, 13, 4, 1, 1])

        self.assertEqual(self.SKINNY_AEAD.process_plaintext(plaintext), correct,
                         "Incorrect result")

    def test_process_plaintext_3(self):
        """
        Unit test 3 processing plaintext (incomplete block)
        """

        plaintext = [[0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8,
                      0, 9]]
        correct = ([[8, 5, 11, 11, 14, 10, 14, 2, 0, 8, 11, 7, 0, 13, 6, 1, 5,
                    12, 4, 5]], [1, 8, 11, 11, 0, 10, 10, 0, 14, 7, 8, 8, 11,
                    6, 14, 9, 12, 9, 14, 9, 9, 5, 11, 14, 13, 12, 10, 4, 9,
                    10, 0, 8])

        self.assertEqual(self.SKINNY_AEAD.process_plaintext(plaintext), correct,
                         "Incorrect result")

    def test_process_plaintext_4(self):
        """
        Unit test 1 processing plaintext (complete two blocks)
        """

        plaintext = [
            [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15],
            [1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10,
             1, 11, 1, 12, 1, 13, 1, 14, 1, 15]]

        correct = ([[2, 4, 1, 15, 0, 13, 10, 12, 2, 12, 5, 13, 13, 10, 4, 8,
                     8, 15, 0, 14, 6, 8, 12, 10, 13, 11, 15, 2, 12, 12, 9, 15],
                    [6, 7, 14, 15, 4, 0, 6, 4, 10, 3, 14, 13, 5, 15, 3, 6, 12,
                     12, 0, 11, 10, 7, 4, 13, 1, 9, 2, 7, 3, 6, 3, 5]], [9,
                     11, 0, 7, 4, 12, 2, 3, 9, 9, 1, 15, 1, 3, 10, 13, 9, 15,
                    12, 3, 11, 0, 6, 10, 10, 12, 5, 6, 10, 10, 8, 11])
        self.assertEqual(self.SKINNY_AEAD.process_plaintext(plaintext), correct,
                         "Incorrect result")


class TestProcessPlaintextDec(unittest.TestCase):
    """
    Unit tests to process plaintext blocks when decrypting - a range of unit
    tests for empty, complete or incomplete blocks
    """

    def setUp(self):
        # set up the SKINNY AEAD object(s)
        self.SKINNY_AEAD = SkinnyAead("M1", Skinny([128, 384, 56]))
        self.SKINNY_AEAD.nonce = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0,
                                  7, 0, 8, 0, 9, 0, 10,
                                  0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        self.SKINNY_AEAD.key = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7,
                                0, 8, 0, 9, 0, 10,
                                0, 11, 0, 12, 0, 13, 0, 14, 0, 15]

    def test_process_plaintext_dec(self):
        """
        Unit test 1 processing plaintext (empty block)
        """

        plaintext = [[]]
        correct = correct = ([], [9, 9, 12, 14, 6, 8, 14, 15, 7, 11, 5, 2, 10,
                                  10, 13, 0, 14, 1, 1, 12, 6, 14, 2, 15, 12,
                                  7, 2, 2, 4, 2, 6, 13])
        self.assertEqual(self.SKINNY_AEAD.process_plaintext_dec(plaintext),
                         correct, "Incorrect result")

    def test_process_plaintext_dec_2(self):
        """
        Unit test 2 processing plaintext (complete block)
        """

        plaintext = [[2, 4, 1, 15, 0, 13, 10, 12, 2, 12, 5, 13, 13, 10, 4, 8,
                    8, 15, 0, 14, 6, 8, 12, 10, 13, 11, 15, 2, 12, 12, 9, 15]]
        correct = ([[0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0,
                     9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15]], [11, 5,
                    12, 3, 5, 11, 9, 14, 0, 8, 7, 7, 4, 0, 4, 10, 4, 4, 7, 2,
                    0, 6, 10, 13, 8, 2, 1, 5, 13, 4, 1, 1])

        self.assertEqual(self.SKINNY_AEAD.process_plaintext_dec(plaintext),
                         correct, "Incorrect result")

    def test_process_plaintext_dec_3(self):
        """
        Unit test 3 processing plaintext (incomplete block)
        """

        plaintext = [[8, 5, 11, 11, 14, 10, 14, 2, 0, 8, 11, 7, 0, 13, 6, 1,
                      5, 12, 4, 5]]
        correct = ([[0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8,
                     0, 9]], [1, 8, 11, 11, 0, 10, 10, 0, 14, 7, 8, 8, 11, 6,
                     14, 9, 12, 9, 14, 9, 9, 5, 11, 14, 13, 12, 10,
                    4, 9, 10, 0, 8])

        self.assertEqual(self.SKINNY_AEAD.process_plaintext_dec(plaintext),
                         correct, "Incorrect result")

    def test_process_plaintext_dec_4(self):
        """
        Unit test 4 processing plaintext (two complete blocks)
        """

        plaintext = [[2, 4, 1, 15, 0, 13, 10, 12, 2, 12, 5, 13, 13, 10, 4, 8,
                      8, 15, 0, 14, 6, 8, 12, 10, 13, 11, 15, 2, 12, 12, 9,
                      15],
                    [6, 7, 14, 15, 4, 0, 6, 4, 10, 3, 14, 13, 5, 15, 3, 6, 12,
                     12, 0, 11, 10, 7, 4, 13, 1, 9, 2, 7, 3, 6, 3, 5]]

        correct = ([[0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0,
                     9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15], [1, 0, 1,
                    1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10,
                    1, 11, 1, 12, 1, 13, 1, 14, 1, 15]], [9, 11, 0, 7, 4, 12,
                    2, 3, 9, 9, 1, 15, 1, 3, 10, 13, 9, 15, 12, 3, 11, 0, 6,
                    10, 10, 12, 5, 6, 10, 10, 8, 11])
        self.assertEqual(self.SKINNY_AEAD.process_plaintext_dec(plaintext),
                         correct, "Incorrect result")


# INTEGRATION TESTS
class TestEncrypt(unittest.TestCase):
    """
    Integration tests for encrypting with SKINNY-AEAD
    """

    def setUp(self):
        # set up the SKINNY AEAD object(s)
        self.SKINNY_AEAD = SkinnyAead("M1", Skinny([128,384, 56]))
        self.SKINNY_AEAD_M2 = SkinnyAead("M2", Skinny([128, 384, 56]))
        self.SKINNY_AEAD_M3 = SkinnyAead("M3", Skinny([128, 384, 56]))
        self.SKINNY_AEAD_M4 = SkinnyAead("M4", Skinny([128, 384, 56]))

    def test_encrypt(self):
        """
        Integration test 1 for SKINNY-AEAD - full blocks of AD and plaintext
        """

        K = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]

        N = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        M = [
            [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15],
            [1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10,
             1, 11, 1, 12, 1, 13, 1, 14, 1, 15]]
        A = [
            [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15],
            [1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10,
             1, 11, 1, 12, 1, 13, 1, 14, 1, 15]]

        correct =([[2, 4, 1, 15, 0, 13, 10, 12, 2, 12, 5, 13, 13, 10, 4, 8, 8,
                    15, 0, 14, 6, 8, 12, 10, 13, 11, 15, 2, 12, 12, 9, 15],
                   [6, 7, 14, 15, 4, 0, 6, 4, 10, 3, 14, 13, 5, 15, 3, 6, 12,
                    12, 0, 11, 10, 7, 4, 13, 1, 9, 2, 7, 3, 6, 3, 5]],
                  [3, 4, 15, 2, 8, 0, 13, 12, 0, 7, 2, 0, 10, 0, 1, 10, 14, 8,
                   10, 9, 12, 1, 7, 6, 14, 15, 6, 4, 1, 14, 4, 9])


        self.assertEqual(self.SKINNY_AEAD .encrypt(M, K, A, N), correct,
                         "Incorrect result")

    def test_encrypt_2(self):
        """
        Integration test 2 for SKINNY-AEAD - empty AD and plaintext
        """


        K = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        N = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        M = [[]]
        A = [[]]
        correct = ([], [9, 9, 12, 14, 6, 8, 14, 15, 7, 11, 5, 2, 10, 10, 13, 0,
                        14, 1, 1, 12, 6, 14, 2, 15, 12, 7, 2, 2, 4, 2, 6, 13])


        self.assertEqual(self.SKINNY_AEAD .encrypt(M, K, A, N), correct,
                         "Incorrect result")

    def test_encrypt_3(self):
        """
        Integration test 3 for SKINNY-AEAD - empty plaintext, incomplete AD
        """

        K = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        N = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        M = [[]]
        A = [[0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0,
              10,   0, 11, 0, 12]]
        correct = ([], [7, 2, 12, 13, 0, 10, 8, 5, 15, 1, 9, 10, 15, 6, 15,
                6, 13, 1, 15, 13, 11, 4, 10, 12, 15, 15, 6, 6, 15, 12, 10, 9])


        self.assertEqual(self.SKINNY_AEAD .encrypt(M, K, A, N), correct,
                         "Incorrect result")

    def test_encrypt_4(self):
        """
        Integration test 4 for SKINNY-AEAD - incomplete plaintext,
        complete AD
        """

        K = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0,
             10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        N = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0,
             10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        M = [[0,0]]
        A = [[0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0,
             10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15]]
        correct = ([[8, 5]], [2, 9, 6, 13, 2, 2, 8, 4, 11, 1, 12, 0, 12, 11
            , 8, 9, 14, 14, 0, 3, 11, 6, 12, 0, 15, 6, 10, 5, 12, 3, 6, 6])

        self.assertEqual(self.SKINNY_AEAD.encrypt(M, K, A, N), correct,
                         "Incorrect result")


    def test_encrypt_5(self):
        """
        Integration test 5 for SKINNY-AEAD - One complete and one incomplete
        plaintext and AD
        """

        K = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0,
             10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        N = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0,
             10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        M = [
            [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15],
            [1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9]]
        A = [
            [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15],
            [1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9]]

        correct = ([[2, 4, 1, 15, 0, 13, 10, 12, 2, 12, 5, 13, 13, 10, 4, 8,
                     8, 15, 0, 14, 6, 8, 12, 10, 13, 11, 15, 2, 12, 12, 9, 15],
                    [9, 10, 1, 5, 6, 2, 11, 4, 1, 13, 15, 12, 0, 9, 10, 15,
                     6, 12, 5, 5]], [2, 5, 6, 13, 12, 8, 5, 6, 14, 4, 5, 10,
                    8, 3, 4, 12, 11, 3, 1, 12, 8, 8, 1, 9, 11, 10, 7, 15,
                    13, 11, 1, 8])

        self.assertEqual(self.SKINNY_AEAD.encrypt(M, K, A, N), correct,
                         "Incorrect result")

    def test_encrypt_M2(self):
        """
        Integration test 6 for SKINNY-AEAD - M2 version
        """

        K = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        N = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11]
        M = [
            [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15],
            [1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10,
             1, 11, 1, 12, 1, 13, 1, 14, 1, 15]]
        A = [
            [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15],
            [1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10,
             1, 11, 1, 12, 1, 13, 1, 14, 1, 15]]

        correct =([[6, 0, 0, 11, 10, 4, 3, 11, 15, 2, 10, 4, 9, 11, 11, 8, 9,
                    7, 3, 1, 4, 4, 0, 13, 7, 8, 2, 5, 9, 12, 0, 10], [12, 2,
                    5, 0, 3, 15, 12, 13, 8, 8, 0, 5, 11, 9, 2, 6, 6, 11, 0, 8,
                9, 2, 4, 12, 9, 0, 7, 7, 14, 10, 11, 4]], [14, 11, 12, 11, 4,
                6, 7, 7, 13, 8, 12, 8, 0, 8, 4, 14, 2, 6, 2, 9, 1, 0, 9, 10,
                    14, 3, 6, 1, 9, 4, 12, 12])

        self.assertEqual(self.SKINNY_AEAD_M2.encrypt(M, K, A, N), correct,
                         "Incorrect result")

    def test_encrypt_M3(self):
        """
        Integration test 7 for SKINNY-AEAD - M3 version
        """

        K = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        N = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        M = [
            [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15],
            [1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10,
             1, 11, 1, 12, 1, 13, 1, 14, 1, 15]]
        A = [
            [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15],
            [1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10,
             1, 11, 1, 12, 1, 13, 1, 14, 1, 15]]

        correct = ([[6, 7, 1, 11, 10, 5, 5, 1, 12, 15, 2, 11, 14, 12, 5, 10,
                     13, 2, 14, 9, 9, 11, 10, 15, 7, 6, 12, 9, 11, 11, 2, 5],
                    [11, 9, 10, 10, 8, 7, 12, 2, 5, 8, 3, 9, 9, 3, 7, 9, 4,
                     15, 15, 13, 2, 5, 12, 2, 1, 12, 15, 11, 6, 5, 5, 9]],
                   [6, 8, 12, 7, 0, 5, 11, 2, 12, 13, 1, 7, 14, 8, 0, 7])
        self.assertEqual(self.SKINNY_AEAD_M3.encrypt(M, K, A, N), correct,
                         "Incorrect result")

    def test_encrypt_M4(self):
        """
        Integration test 7 for SKINNY-AEAD - M4 version
        """


        K = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        N = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11]
        M = [
            [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15],
            [1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10,
             1, 11, 1, 12, 1, 13, 1, 14, 1, 15]]
        A = [
            [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15],
            [1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10,
             1, 11, 1, 12, 1, 13, 1, 14, 1, 15]]

        correct = ([[4, 10, 7, 2, 2, 9, 3, 9, 14, 1, 4, 2, 4, 9, 9, 6, 8, 0,
                     12, 1, 1, 7, 4, 6, 5, 1, 13, 4, 5, 4, 3, 0], [8, 9, 4, 8,
                    0, 2, 6, 11, 0, 1, 14, 5, 8, 3, 8, 14, 10, 3, 8, 0, 15, 5,
                    2, 7, 9, 11, 15, 9, 4, 8, 14, 11]], [10, 11, 15, 2, 1, 2,
                    15, 9, 7, 1, 13, 15, 12, 13, 7, 11])

        self.assertEqual(self.SKINNY_AEAD_M4.encrypt(M, K, A, N), correct,
                         "Incorrect result")


class TestVerify(unittest.TestCase):
    """
    Integration tests for verifying SKINNY-AEAD
    """

    def setUp(self):
        # set up the SKINNY AEAD object(s)
        self.SKINNY_AEAD = SkinnyAead("M1", Skinny([128, 384, 56]))
        self.SKINNY_AEAD_M2 = SkinnyAead("M2", Skinny([128, 384, 56]))
        self.SKINNY_AEAD_M3 = SkinnyAead("M3", Skinny([128, 384, 56]))
        self.SKINNY_AEAD_M4 = SkinnyAead("M4", Skinny([128, 384, 56]))

    def test_verify(self):
        """
        Integration test 1 for SKINNY-AEAD
        """

        K = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        N = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        C = [[2, 4, 1, 15, 0, 13, 10, 12, 2, 12, 5, 13, 13, 10, 4, 8, 8, 15,
              0, 14, 6, 8, 12, 10, 13, 11, 15, 2, 12, 12, 9, 15],
                   [6, 7, 14, 15, 4, 0, 6, 4, 10, 3, 14, 13, 5, 15, 3, 6, 12,
                    12, 0, 11, 10, 7, 4, 13, 1, 9, 2, 7, 3, 6, 3, 5]]
        A = [
            [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15],
            [1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10,
             1, 11, 1, 12, 1, 13, 1, 14, 1, 15]]

        T =  [3, 4, 15, 2, 8, 0, 13, 12, 0, 7, 2, 0, 10, 0, 1, 10, 14, 8, 10,
              9, 12, 1, 7, 6, 14, 15, 6, 4, 1, 14, 4, 9]

        correct =[
            [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15],
            [1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10,
             1, 11, 1, 12, 1, 13, 1, 14, 1, 15]]


        self.assertEqual(self.SKINNY_AEAD .verify(C, K, A, N, T), correct,
                         "Incorrect result")

    def test_verify_2(self):
        """
        Integration test 2 for SKINNY-AEAD
        """

        K = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        N = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        C = [[]]
        A = [[]]
        T = [9, 9, 12, 14, 6, 8, 14, 15, 7, 11, 5, 2, 10, 10, 13, 0, 14,
             1, 1, 12, 6, 14, 2, 15, 12, 7, 2, 2, 4, 2, 6, 13]
        correct = []


        self.assertEqual(self.SKINNY_AEAD .verify(C, K, A, N, T), correct,
                         "Incorrect result")

    def test_verify_3(self):
        """
        Integration test 3 for SKINNY-AEAD
        """

        K = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        N = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        C = [[]]
        A = [[0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0,
              10,
             0, 11, 0, 12]]
        T = [7, 2, 12, 13, 0, 10, 8, 5, 15, 1, 9, 10, 15, 6, 15, 6, 13, 1, 15,
             13, 11, 4, 10, 12, 15, 15, 6, 6, 15, 12, 10, 9]
        correct = []


        self.assertEqual(self.SKINNY_AEAD .verify(C, K, A, N, T), correct,
                         "Incorrect result")

    def test_verify_4(self):
        """
        Integration test 4 for SKINNY-AEAD
        """

        K = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0,
             10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        N = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0,
             10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        C = [[8, 5]]
        A = [[0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0,
             10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15]]
        T = [2, 9, 6, 13, 2, 2, 8, 4, 11, 1, 12, 0, 12, 11, 8, 9, 14, 14, 0,
             3, 11, 6, 12, 0, 15, 6, 10, 5, 12, 3, 6, 6]
        correct = [[0,0]]

        self.assertEqual(self.SKINNY_AEAD.verify(C, K, A, N, T), correct,
                         "Incorrect result")


    def test_verify_5(self):
        """
        Integration test 5 for SKINNY-AEAD
        """

        K = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0,
             10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        N = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0,
             10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        C = [[2, 4, 1, 15, 0, 13, 10, 12, 2, 12, 5, 13, 13, 10, 4, 8, 8, 15, 0,
              14, 6, 8, 12, 10, 13, 11, 15, 2, 12, 12, 9, 15],
             [9, 10, 1, 5, 6, 2, 11, 4, 1, 13, 15, 12, 0, 9, 10, 15, 6, 12, 5,
              5]]
        A = [
            [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15],
            [1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9]]

        T =  [2, 5, 6, 13, 12, 8, 5, 6, 14, 4, 5, 10, 8, 3, 4, 12, 11, 3, 1,
              12, 8, 8, 1, 9, 11, 10, 7, 15, 13, 11, 1, 8]

        correct = [
            [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15],
            [1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9]]


        self.assertEqual(self.SKINNY_AEAD.verify(C, K, A, N, T), correct,
                         "Incorrect result")

    def test_verify_M2(self):
        """
        Integration test 6 for SKINNY-AEAD
        """

        K = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        N = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11]
        C = [[6, 0, 0, 11, 10, 4, 3, 11, 15, 2, 10, 4, 9, 11, 11, 8, 9,
                     7, 3, 1, 4, 4, 0, 13, 7, 8, 2, 5, 9, 12, 0, 10],
                    [12, 2, 5, 0, 3, 15, 12, 13, 8, 8, 0, 5, 11, 9, 2, 6, 6,
                     11, 0, 8, 9, 2, 4, 12, 9, 0, 7, 7, 14, 10, 11, 4]]
        A = [
            [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15],
            [1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10,
             1, 11, 1, 12, 1, 13, 1, 14, 1, 15]]

        T = [14, 11, 12, 11, 4, 6, 7, 7, 13, 8, 12, 8, 0, 8, 4, 14, 2,
                    6, 2, 9, 1, 0, 9, 10, 14, 3, 6, 1, 9, 4, 12, 12]

        correct = [[0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0,
                    9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15],
                   [1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1,
                    9, 1, 10, 1, 11, 1, 12, 1, 13, 1, 14, 1, 15]]


        self.assertEqual(self.SKINNY_AEAD_M2.verify(C, K, A, N, T), correct,
                         "Incorrect result")

    def test_encrypt_M3(self):
        """
        Integration test 7 for SKINNY-AEAD
        """

        K = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        N = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        C = [[6, 7, 1, 11, 10, 5, 5, 1, 12, 15, 2, 11, 14, 12, 5, 10,
                     13, 2, 14, 9, 9, 11, 10, 15, 7, 6, 12, 9, 11, 11, 2, 5],
                    [11, 9, 10, 10, 8, 7, 12, 2, 5, 8, 3, 9, 9, 3, 7, 9, 4, 15,
                     15, 13, 2, 5, 12, 2, 1, 12, 15, 11, 6, 5, 5, 9]]
        A = [
            [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15],
            [1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10,
             1, 11, 1, 12, 1, 13, 1, 14, 1, 15]]

        T = [6, 8, 12, 7, 0, 5, 11, 2, 12, 13, 1, 7, 14, 8, 0, 7]
        correct = [[0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0,
                    9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15],
                   [1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8,
                    1, 9, 1, 10, 1, 11, 1, 12, 1, 13, 1, 14, 1, 15]]
        print(self.SKINNY_AEAD_M3.verify(C, K, A, N, T))
        self.assertEqual(self.SKINNY_AEAD_M3.verify(C, K, A, N, T), correct,
                         "Incorrect result")

    def test_encrypt_M4(self):
        """
        Integration test 8 for SKINNY-AEAD
        """

        K = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        N = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11]
        C = [[4, 10, 7, 2, 2, 9, 3, 9, 14, 1, 4, 2, 4, 9, 9, 6, 8, 0, 12, 1,
              1, 7, 4, 6, 5, 1, 13, 4, 5, 4, 3, 0],
             [8, 9, 4, 8, 0, 2, 6, 11, 0, 1, 14, 5, 8, 3, 8, 14, 10, 3, 8,
              0, 15, 5, 2, 7, 9, 11, 15, 9, 4, 8, 14, 11]]
        A = [
            [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15],
            [1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10,
             1, 11, 1, 12, 1, 13, 1, 14, 1, 15]]

        T = [10, 11, 15, 2, 1, 2, 15, 9, 7, 1, 13, 15, 12, 13, 7, 11]

        correct = [[0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0,
                    9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15],
                   [1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8,
                    1, 9, 1, 10, 1, 11, 1, 12, 1, 13, 1, 14, 1, 15]]
        print(self.SKINNY_AEAD_M4.verify(C, K, A, N, T))
        self.assertEqual(self.SKINNY_AEAD_M4.verify(C, K, A, N, T), correct,
                         "Incorrect result")


if __name__ == '__main__':
    unittest.main()
