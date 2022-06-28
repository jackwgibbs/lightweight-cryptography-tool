# Lightweight Cryptography Tool

This Lightweight Cryptography Tool (LCT) implements a selection of lightweight
cryptographic designs which feature in the NIST lightweight
standardisation process. 

This tool implements the following two lightweight Block Ciphers (BC):
* GIFT
  * GIFT-64
  * GIFT-128
  * GIFT-128 (bit sliced implementation)
* SKINNY
  * SKINNY-64-64
  * SKINNY-64-128
  * SKINNY-64-192
  * SKINNY-128-128
  * SKINNY-128-256
  * SKINNY-128-384

The tool implements two lightweight Authenticated Encryption with 
Associated Data (AEAD) constructs which instantiate one of the two lightweight
BCs
* GIFT-COFB (instantiates GIFT-128 (bit sliced implementation))
* SKINNY-AEAD (instantiates SKINNY-128-384)
  * M1
  * M2
  * M3
  * M4

## What can you do with this tool?
There are three main functionalities of this tool:
1. Encrypt / decrypt using lightweight BCs (encryption modes ECB, CTR and CBC)
2. Generate / verify MAC using lightweight BCs (authenticion mode CBC-MAC)
3. Encrypt / verify AEAD encryption using lightweight AEAD schemes
(authenticated encryption)

## How to use the tool
To run the tool run the main.py script. You will be presented with a menu 
driven interface to select your use of the tool. You will be prompted several
questions as to which functionality / lightweight construct to use, as well
as supply a filename containing the data.


## Data formatting - how to format the input file
Each line in the text-file represents a different input, with the 
first character describing the type of input, followed by a colon, followed
by the input itself (note no spaces). For example:

P:0123456789ABCDEF

There are seven types of input:
* P - plaintext
* K - key
* C - ciphertext
* A - associated data
* N - nonce
* T - tag
* L - length of plaintext 

For encrypting / decrypting the following needs to be supplied:
* P (or C)
* K
* L (if decryping provide length of plaintext)

For generating / verifying a MAC, the following needs to be supplied:
* P
* K
* T (if verifying)

For generating / verifying AEAD encryption, the following needs to be supplied:
* P (or C)
* K
* N
* A
* T (if verifying)

# Testing
The tool has unit and integration tests written for all functions and
lightweight constructs. To run the tests, run the following command from the 
root directory:

python -m unittest discover Tests