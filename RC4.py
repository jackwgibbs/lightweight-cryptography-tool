"""
Module to implement the RC4 pseudo-random number generation algorithm
"""

from utils import decimal_to_hex, hex_to_decimal


def initialisation(key):
    """
    Function to initialise RC4 algorithm.
    Parameters: key.
    Returns: initialised list s.
    """

    j = 0
    s = []

    # initialise s list to [0, 1, ... 255]
    for i in range(0, 256):
        s.append(i)

    # j = j + s[i] + key[i mod len(key)] mod 256
    # then swap s[i] and s[j]
    for i in range(0, 256):
        j = (j + s[i] + key[i % len(key)]) % 256
        s[i], s[j] = s[j], s[i]

    return s


def algorithm(key, num_of_bytes):
    """
    Function to run the RC4 algorithm to produce a random list of bytes.
    Parameters: key and number of bytes to generate.
    Returns: list of bytes.
    """

    stream = []

    # initialise s list using the initialisation function
    s = initialisation(key)

    i = 0
    j = 0

    # run the algorithm, each iteration add character to stream list
    # repeat for the number of bytes specified
    for k in range(0, num_of_bytes):
        i = (i+1) % 256
        j = (j+s[i]) % 256
        s[i], s[j] = s[j], s[i]
        t = s[(s[i] + s[j]) % 256]
        stream.append(t)

    return stream


def run_RC4(key, num_of_bytes):
    """
    Function to generate a random stream of bytes using RC4 algorithm.
    Parameters: key and number of bytes.
    Returns: list of hex (converted from list of bytes from RC4).
    """

    # first convert the key from hex to byte format
    key = hex_to_decimal(key)
    result = algorithm(key, num_of_bytes)

    # return result as a list of hex converted from bytes
    result = decimal_to_hex(result)

    return result
