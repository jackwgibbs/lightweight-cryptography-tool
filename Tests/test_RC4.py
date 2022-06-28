"""
This file runs integration tests for the RC4 function
"""

import sys
sys.path.append('..')
import unittest
from RC4 import *


class TestRC4(unittest.TestCase):
    """
    Run integration tests on the RC4 algorithm
    """

    def test_RC4_1(self):
        key = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        no_bytes = 32
        correct = [233, 156, 64, 249, 71, 226, 25, 204, 6, 219, 151, 198,
                   14, 221, 42, 79, 211, 113, 129, 95, 242, 183, 66, 238,
                   143, 158, 165, 217, 249, 55, 227, 2]

        self.assertEqual(algorithm(key, no_bytes), correct, "Incorrect RC4")


if __name__ == '__main__':
    unittest.main()
