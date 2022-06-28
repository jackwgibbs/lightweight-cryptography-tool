"""
Module to determine time analysis of our implementations - function for
each construct, pass in the number of bytes to encrypt, and we find the time
taken to do so.
"""

import sys
sys.path.append('..')
from Gift.gift_128 import *
from Skinny.skinny import *
from Skinny.skinnyaead import *
from Gift.gift_cofb import *
from RC4 import *
import time


def experiment_gift_128(num_of_bytes):
    """
    Function to analyse time analysis of GIFT-128
    Parameter: num_of_bytes to encrypt under ECB mode
    Returns: elapsed time
    """

    cipher = Gift128()
    blocks = num_of_bytes // 8

    plaintext = "0123456789abcdef" * blocks
    key = "0123456789abcdef0123456789abcdef"
    plaintext = string_to_list(plaintext)
    key = string_to_list(key)

    blocks = divide_into_blocks(plaintext, 128, 1)
    c = []

    t = time.process_time()
    for block in blocks:
        c.append(cipher.encrypt_block(block, key[:]))
    elapsed_time = time.process_time() - t
    return elapsed_time


def experiment_skinny_128_384(num_of_bytes):
    """
    Function to analyse time analysis of SKINNY-128-384
    Parameter: num_of_bytes to encrypt under ECB mode
    Returns: elapsed time
    """

    cipher = Skinny([128, 384, 56])
    blocks = num_of_bytes // 8

    plaintext = "0123456789abcdef" * blocks
    key = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789" \
          "abcdef0123456789abcdef0123456789abcdef"
    plaintext = string_to_list(plaintext)
    key = string_to_list(key)

    blocks = divide_into_blocks(plaintext, 128, 1)
    c = []

    t = time.process_time()
    for block in blocks:
        c.append(cipher.encrypt_block(block, key))
    elapsed_time = time.process_time() - t
    return elapsed_time


def experiment_gift_128_b_s(num_of_bytes):
    """
    Function to analyse time analysis of GIFT-128 (bit-sliced implementation)
    Parameter: num_of_bytes to encrypt under ECB mode
    Returns: elapsed time
    """

    cipher = Gift128BitSliced()
    blocks = num_of_bytes // 16

    key = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    plaintext = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    blocks = [plaintext for i in range(blocks)]

    c = []

    t = time.process_time()
    for block in blocks:
        c.append(cipher.encrypt_block(block, key))
    elapsed_time = time.process_time() - t
    return elapsed_time


def experiment_gift_cofb(num_of_bytes):
    """
    Function to analyse time analysis of GIFT-COFB
    Parameter: num_of_bytes to encrypt
    Returns: elapsed time
    """

    cipher = GiftCofb()
    blocks = num_of_bytes // 8

    plaintext = "0123456789abcdef" * blocks
    key = "0123456789abcdef0123456789abcdef"
    nonce = "0123456789abcdef0123456789abcdef"
    a = "0123456789abcdef0123456789abcdef"
    plaintext = string_to_list(plaintext)
    key = string_to_list(key)
    nonce = string_to_list(nonce)
    a = string_to_list(a)

    blocks = divide_into_blocks(plaintext, 128, 1)
    a = divide_into_blocks(a, 128, 1)

    t = time.process_time()
    cipher.encrypt(blocks, key, a, nonce)
    elapsed_time = time.process_time() - t
    return elapsed_time


def experiment_skinny_aead(num_of_bytes):
    """
    Function to analyse time analysis of SKINNY-AEAD
    Parameter: num_of_bytes to encrypt
    Returns: elapsed time
    """

    cipher = SkinnyAead("M1", Skinny([128, 384, 56]))
    blocks = num_of_bytes // 8

    plaintext = "0123456789abcdef" * blocks
    key = "0123456789abcdef0123456789abcdef"
    nonce = "0123456789abcdef0123456789abcdef"
    a = "0123456789abcdef0123456789abcdef"
    plaintext = string_to_list(plaintext)
    key = string_to_list(key)
    nonce = string_to_list(nonce)
    a = string_to_list(a)

    blocks = divide_into_blocks(plaintext, 128, 1)
    a = divide_into_blocks(a, 128, 1)

    t = time.process_time()
    cipher.encrypt(blocks, key, a, nonce)
    elapsed_time = time.process_time() - t
    return elapsed_time


def experiment_gift_128_cbc(num_of_bytes):
    """
    Function to analyse time analysis of GIFT-128 with CBC
    Parameter: num_of_bytes to encrypt
    Returns: elapsed time
    """

    cipher = Gift128()
    blocks = num_of_bytes // 8

    plaintext = "0123456789abcdef" * blocks
    key = "0123456789abcdef0123456789abcdef"
    plaintext = string_to_list(plaintext)
    key = string_to_list(key)

    blocks = divide_into_blocks(plaintext, 128, 1)

    c = []
    t = time.process_time()

    IV = run_RC4(key, 128 // 8)

    # initialise CBC mode
    x = xor_bits(blocks[0], IV)
    y = cipher.encrypt_block(x, key)
    c.append(y)

    # iterate over each plaintext block
    for i in range(1, len(blocks)):
        # XOR the current plaintext block and the result of the
        # previous encryption
        x = xor_bits(blocks[i], y)

        # Encrypt the xored plaintext block and previous encryption result
        y = cipher.encrypt_block(x, key)
        c.append(y)

    elapsed_time = time.process_time() - t
    return elapsed_time


def experiment_skinny_128_384_cbc(num_of_bytes):
    """
    Function to analyse time analysis of SKINNY-128-384 with CBC
    Parameter: num_of_bytes to encrypt
    Returns: elapsed time
    """

    cipher = Skinny([128, 384, 56])
    blocks = num_of_bytes // 8

    plaintext = "0123456789abcdef" * blocks
    key = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789" \
          "abcdef0123456789abcdef0123456789abcdef"
    plaintext = string_to_list(plaintext)
    key = string_to_list(key)

    blocks = divide_into_blocks(plaintext, 128, 1)

    c = []
    t = time.process_time()

    IV = run_RC4(key, 128 // 8)

    # initialise CBC mode
    x = xor_bits(blocks[0], IV)
    y = cipher.encrypt_block(x, key)
    c.append(y)

    # iterate over each plaintext block
    for i in range(1, len(blocks)):
        # XOR the current plaintext block and the result of the
        # previous encryption
        x = xor_bits(blocks[i], y)

        # Encrypt the xored plaintext block and previous encryption result
        y = cipher.encrypt_block(x, key)
        c.append(y)

    elapsed_time = time.process_time() - t
    return elapsed_time


def experiment_gift_128_ctr(num_of_bytes):
    """
    Function to analyse time analysis of GIFT-128 with CTR
    Parameter: num_of_bytes to encrypt
    Returns: elapsed time
    """

    cipher = Gift128()
    blocks = num_of_bytes // 8

    plaintext = "0123456789abcdef" * blocks
    key = "0123456789abcdef0123456789abcdef"
    plaintext = string_to_list(plaintext)
    key = string_to_list(key)

    blocks = divide_into_blocks(plaintext, 128, 1)

    c = []
    t = time.process_time()

    # generate the IV using the RC4 algorithm
    IV = run_RC4(key, 128 // 8)

    # iterate over each block, encrypt the IV and xor to the block
    for block in blocks:
        x = xor_bits(block, cipher.encrypt_block(IV[:], key))
        c.append(x)

        # increment last byte of the IV
        IV[-2:] = increment_byte(IV[-2:])

    elapsed_time = time.process_time() - t
    return elapsed_time


def experiment_skinny_128_384_ctr(num_of_bytes):
    """
    Function to analyse time analysis of SKINNY-128-384 with CTR
    Parameter: num_of_bytes to encrypt
    Returns: elapsed time
    """

    cipher = Skinny([128, 384, 56])
    blocks = num_of_bytes // 8

    plaintext = "0123456789abcdef" * blocks
    key = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789" \
          "abcdef0123456789abcdef0123456789abcdef"
    plaintext = string_to_list(plaintext)
    key = string_to_list(key)

    blocks = divide_into_blocks(plaintext, 128, 1)

    c = []
    t = time.process_time()

    # generate the IV using the RC4 algorithm
    IV = run_RC4(key, 128 // 8)

    # iterate over each block, encrypt the IV and xor to the block
    for block in blocks:
        x = xor_bits(block, cipher.encrypt_block(IV[:], key))
        c.append(x)

        # increment last byte of the IV
        IV[-2:] = increment_byte(IV[-2:])

    elapsed_time = time.process_time() - t
    return (elapsed_time)


def experiment_gift_128_cbcmac(num_of_bytes):
    """
    Function to analyse time analysis of GIFT-128 with CBC-MAC
    Parameter: num_of_bytes to encrypt
    Returns: elapsed time
    """

    cipher = Gift128()
    blocks = num_of_bytes // 8

    plaintext = "0123456789abcdef" * blocks
    key = "0123456789abcdef0123456789abcdef"
    plaintext = string_to_list(plaintext)
    key = string_to_list(key)

    blocks = divide_into_blocks(plaintext, 128, 1)

    c = []
    t = time.process_time()

    # initialise CBC MAC mode
    x = xor_bits(blocks[0], [0] * (128 // 4))
    y = cipher.encrypt_block(x, key)

    # iterate over each block
    for i in range(1, len(blocks)):
        # xor the current plaintext block and the result of the
        # previous encryption
        x = xor_bits(blocks[i], y)

        # encrypt the xored plaintext block and previous encryption result
        y = cipher.encrypt_block(x, key)

    elapsed_time = time.process_time() - t
    return (elapsed_time)


def experiment_skinny_128_384_cbcmac(num_of_bytes):
    """
    Function to analyse time analysis of SKINNY-128-384 with CBC-MAC
    Parameter: num_of_bytes to encrypt
    Returns: elapsed time
    """

    cipher = Skinny([128, 384, 56])
    blocks = num_of_bytes // 8

    plaintext = "0123456789abcdef" * blocks
    key = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789" \
          "abcdef0123456789abcdef0123456789abcdef"
    plaintext = string_to_list(plaintext)
    key = string_to_list(key)

    blocks = divide_into_blocks(plaintext, 128, 1)

    c = []
    t = time.process_time()

    # initialise CBC MAC mode
    x = xor_bits(blocks[0], [0] * (128 // 4))
    y = cipher.encrypt_block(x, key)

    # iterate over each block
    for i in range(1, len(blocks)):
        # xor the current plaintext block and the result of the
        # previous encryption
        x = xor_bits(blocks[i], y)

        # encrypt the xored plaintext block and previous encryption result
        y = cipher.encrypt_block(x, key)

    elapsed_time = time.process_time() - t
    return elapsed_time


if __name__ == "__main__":
    # determine CBC-MAC overhead with SKINNY-128-384
    num_of_bytes = 256
    x = experiment_skinny_128_384_cbcmac(num_of_bytes)
    y = experiment_skinny_128_384(num_of_bytes)
    print(x - y)
