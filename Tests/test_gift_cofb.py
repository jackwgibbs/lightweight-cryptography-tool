"""
This file runs unit and integration tests for the GIFT-COFB class
"""

import sys
sys.path.append('..')
import unittest
from Gift.gift_cofb import *


class TestRho1(unittest.TestCase):
    """
    Unit tests for the rho1 method of GIFT-COFB
    """

    def test_rho1(self):
        """
        Unit test for the rho1 method of GIFT-COFB
        """

        c = GiftCofb()
        Y = [10, 9, 4, 10, 15, 7, 15, 9, 11, 10, 1, 8, 1, 13, 15, 9, 11, 2,
             11, 0, 0, 14, 11, 7, 13, 11, 15, 10, 9, 3, 13, 15]
        M = [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        correct = [3, 2, 11, 0, 0, 14, 11, 7, 13, 11, 15, 10, 9, 3, 13, 15,
                   5, 2, 9, 5, 14, 15, 15, 3, 7, 4, 3, 0, 3, 11, 15, 3]

        self.assertEqual(c.pho1(Y, M), correct, "Rho1 incorrectly applied")


class TestRho(unittest.TestCase):
    """
    Unit tests for the rho method of GIFT-COFB
    """
    def test_rho(self):
        """
        Unit test for the rho method of GIFT-COFB
        """

        c = GiftCofb()
        Y = [5, 13, 5, 8, 5, 13, 12, 3, 0, 14, 3, 5, 9, 5, 0, 6, 7, 9, 9, 2,
             3, 10, 10, 6, 9, 2, 6, 0, 7, 12, 0, 0]
        M = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0,
             10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        correct = ([7, 9, 9, 3, 3, 8, 10, 5, 9, 6, 6, 5, 7, 10, 0, 7, 11, 2,
                    11, 9, 11, 1, 8, 13, 1, 0, 6, 6, 2, 4, 0, 3],
                   [5, 13, 5, 9, 5, 15, 12, 0, 0, 10, 3, 0, 9, 3, 0, 1, 7, 1,
                    9, 11, 3, 0, 10, 13, 9, 14, 6, 13, 7, 2, 0, 15])

        self.assertEqual(c.pho(Y, M), correct, "Rho incorrectly applied")


class TestRhoPrime(unittest.TestCase):
    """
    Unit tests for the rho prime method of GIFT-COFB (used for decryption)
    """

    def test_rho_prime(self):
        """
        Unit test for the rho prime method of GIFT-COFB
        """

        c = GiftCofb()
        Y = [11, 10, 15, 4, 6, 1, 12, 5, 0, 11, 11, 11, 13, 11, 12, 2, 6, 14,
             2, 0, 9, 15, 15, 15, 12, 10, 7, 5, 11, 0, 8, 15]
        M = [11, 10, 15, 5, 6, 3, 12, 6, 0, 15, 11, 14, 13, 13, 12, 5, 6, 6,
              2, 9, 9, 5, 15, 4, 12, 6, 7, 8, 11, 14, 8, 0]

        correct = ([6, 14, 2, 1, 9, 13, 15, 12, 12, 14, 7, 0, 11, 6, 8, 8,
                     7, 13, 14, 1, 12, 9, 8, 1, 1, 11, 7, 10, 11, 9, 8, 10],
                    [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0,
                     9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15])
        self.assertEqual(c.phoprime(Y, M), correct, "Rho prime incorrect")


class TestDouble(unittest.TestCase):
    """
    Unit tests for the double method of GIFT-COFB
    """

    def test_double(self):
        """
        Unit test for the double method of GIFT-COFB
        """

        c = GiftCofb()
        L = [10, 9, 4, 10, 15, 7, 15, 9, 11, 10, 1, 8, 1, 13, 15, 9]
        correct = [5, 2, 9, 5, 14, 15, 15, 3, 7, 4, 3, 0, 3, 11, 14, 9]
        self.assertEqual(c.double(L), correct, "Double incorrectly applied")


class TestTriple(unittest.TestCase):
    """
    Unit tests for the triple method of GIFT-COFB
    """

    def test_triple(self):
        """
        Unit test for the triple method of GIFT-COFB
        """

        c = GiftCofb()
        L = [10, 9, 4, 10, 15, 7, 15, 9, 11, 10, 1, 8, 1, 13, 15, 9]
        correct = [15, 11, 13, 15, 1, 8, 0, 10, 12, 14, 2, 8, 2, 6, 1, 0]
        self.assertEqual(c.triple(L), correct, "Triple applied incorrectly")


class TestG(unittest.TestCase):
    """
    Unit tests for the G method of GIFT-COFB
    """

    def test_G(self):
        """
        Unit tests for the G method of GIFT-COFB
        """

        c = GiftCofb()
        Y = [10, 9, 4, 10, 15, 7, 15, 9, 11, 10, 1, 8, 1, 13, 15, 9, 11, 2,
             11, 0, 0, 14, 11, 7, 13, 11, 15, 10, 9, 3, 13, 15]
        correct = [11, 2, 11, 0, 0, 14, 11, 7, 13, 11, 15, 10, 9, 3, 13, 15,
                   5, 2, 9, 5, 14, 15, 15, 3, 7, 4, 3, 0, 3, 11, 15, 3]
        self.assertEqual(c.G(Y), correct, "G applied incorrectly")


# INTEGRATION TESTS
class TestEncrypt(unittest.TestCase):
    """
    Integration tests for the GIFT COFB class
    """

    def test_encrypt_1(self):
        """
        Integration tests 1 - encrypt empty P and AD
        """

        c = GiftCofb()
        K = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        N = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        M = [[]]
        A = [[]]

        correct = ([], [3, 6, 8, 9, 6, 5, 8, 3, 6, 13, 3, 6, 6, 1, 4, 13, 14,
                2, 15, 12, 2, 4, 13, 0, 15, 8, 0, 1, 11, 9, 10, 15])

        self.assertEqual(c.encrypt(M, K, A, N), correct,
                         "Incorrect result")

    def test_encrypt_2(self):
        """
        Integration tests 2 - encrypt empty P and incomplete AD
        """

        c = GiftCofb()
        K = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        N = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        M = [[]]
        A = [[0,0]]

        correct = ([], [10, 14, 5, 13, 12, 13, 13, 1, 2, 8, 5, 13, 5, 1, 7, 7,
                15, 14, 2, 5, 1, 13, 14, 11, 9, 9, 13, 7, 2, 7, 13, 12])

        self.assertEqual(c.encrypt(M, K, A, N), correct,
                         "Incorrect result")

    def test_encrypt_3(self):
        """
        Integration tests 3 - encrypt incomplete P and complete AD
        """

        c = GiftCofb()
        K = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        N = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        M = [[0,0]]
        A = [[0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0,
              10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15]]

        correct = ([[3, 11]], [8, 10, 8, 5, 6, 6, 2, 0, 0, 5, 10, 9, 11, 2,
                10, 2, 10, 4, 1, 0, 8, 14, 1, 2, 12, 15, 5, 8, 9, 2, 8, 8])

        self.assertEqual(c.encrypt(M, K, A, N), correct,
                         "Incorrect result")

    def test_encrypt_4(self):
        """
        Integration tests 4 - encrypt incomplete P and AD
        """

        c = GiftCofb()
        K = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        N = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        M = [[0,0,0,1]]
        A = [[0, 0, 0, 1, 0, 2, 0, 3, 0, 4]]

        correct = ([[12, 4, 3, 9]], [14, 8, 4, 2, 3, 14, 2, 7, 0, 7, 4, 1, 0,
            9, 5, 6, 12, 12, 3, 11, 3, 10, 1, 14, 0, 7, 10, 12, 6, 14, 14, 2])

        self.assertEqual(c.encrypt(M, K, A, N), correct,
                         "Incorrect result")

    def test_encrypt_5(self):
        """
        Integration tests 5 - encrypt empty complete P and AD
        """

        c = GiftCofb()
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

        correct = ([[11, 10, 15, 5, 6, 3, 12, 6, 0, 15, 11, 14, 13, 13, 12, 5,
          6, 6, 2, 9, 9, 5, 15, 4, 12, 6, 7, 8, 11, 14, 8, 0], [10, 7, 15, 7,
        13, 14, 9, 11, 3, 10, 13, 8, 12, 9, 7, 10, 10, 6, 12, 10, 1, 7, 0, 1,
        6, 13, 2, 10, 14, 6, 5, 0]], [8, 14, 6, 15, 11, 3, 15, 7, 9, 11, 4, 1,
        2, 10, 1, 6, 2, 7, 10, 11, 7, 13, 15, 10, 7, 5, 5, 14, 0, 10, 2, 2])

        self.assertEqual(c.encrypt(M, K, A, N), correct,
                         "Incorrect result")


class TestVerify(unittest.TestCase):
    """
    Integration tests for the GIFT COFB class
    """

    def test_verify_1(self):
        """
        Integration tests 1 - decrypt empty P and AD
        """

        c = GiftCofb()
        K = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        N = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        C = [[]]
        A = [[]]
        T = [3, 6, 8, 9, 6, 5, 8, 3, 6, 13, 3, 6, 6, 1, 4, 13, 14,
                2, 15, 12, 2, 4, 13, 0, 15, 8, 0, 1, 11, 9, 10, 15]

        correct = []

        self.assertEqual(c.verify(C, K, A, N, T), correct,
                         "Incorrect result")

    def test_verify_2(self):
        """
        Integration tests 2 - decrypt empty P and incomplete AD
        """

        c = GiftCofb()
        K = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        N = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        C = [[]]
        A = [[0,0]]
        T = [10, 14, 5, 13, 12, 13, 13, 1, 2, 8, 5, 13, 5, 1, 7, 7,
                15, 14, 2, 5, 1, 13, 14, 11, 9, 9, 13, 7, 2, 7, 13, 12]

        correct = []

        self.assertEqual(c.verify(C, K, A, N, T), correct,
                         "Incorrect result")

    def test_verify_3(self):
        """
        Integration tests 3 - decrypt incomplete P and complete AD
        """

        c = GiftCofb()
        K = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        N = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        C = [[3, 11]]
        A = [[0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0,
              10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15]]
        T = [8, 10, 8, 5, 6, 6, 2, 0, 0, 5, 10, 9, 11, 2,
                10, 2, 10, 4, 1, 0, 8, 14, 1, 2, 12, 15, 5, 8, 9, 2, 8, 8]

        correct = [[0,0]]

        self.assertEqual(c.verify(C, K, A, N, T), correct,
                         "Incorrect result")

    def test_verify_4(self):
        """
        Integration tests 4 - decrypt incomplete P and AD
        """

        c = GiftCofb()
        K = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        N = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        C = [[12, 4, 3, 9]]
        A = [[0, 0, 0, 1, 0, 2, 0, 3, 0, 4]]
        T = [14, 8, 4, 2, 3, 14, 2, 7, 0, 7, 4, 1, 0,
            9, 5, 6, 12, 12, 3, 11, 3, 10, 1, 14, 0, 7, 10, 12, 6, 14, 14, 2]

        correct =  [[0,0,0,1]]

        self.assertEqual(c.verify(C, K, A, N, T), correct,
                         "Incorrect result")

    def test_verify_5(self):
        """
        Integration tests 5 - decrypt empty complete P and AD
        """

        c = GiftCofb()
        K = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        N = [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15]
        C = [[11, 10, 15, 5, 6, 3, 12, 6, 0, 15, 11, 14, 13, 13, 12, 5,
          6, 6, 2, 9, 9, 5, 15, 4, 12, 6, 7, 8, 11, 14, 8, 0], [10, 7, 15, 7,
        13, 14, 9, 11, 3, 10, 13, 8, 12, 9, 7, 10, 10, 6, 12, 10, 1, 7, 0, 1,
        6, 13, 2, 10, 14, 6, 5, 0]]
        A = [
            [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15],
            [1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10,
             1, 11, 1, 12, 1, 13, 1, 14, 1, 15]]

        T = [8, 14, 6, 15, 11, 3, 15, 7, 9, 11, 4, 1,
        2, 10, 1, 6, 2, 7, 10, 11, 7, 13, 15, 10, 7, 5, 5, 14, 0, 10, 2, 2]

        correct =[
            [0, 0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10,
             0, 11, 0, 12, 0, 13, 0, 14, 0, 15],
            [1, 0, 1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10,
             1, 11, 1, 12, 1, 13, 1, 14, 1, 15]]

        self.assertEqual(c.verify(C, K, A, N, T), correct,
                         "Incorrect result")


if __name__ == '__main__':
    unittest.main()
