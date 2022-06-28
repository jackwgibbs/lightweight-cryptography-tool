"""
Module to implement the SKINNY-AEAD construct, including versions M1, M2
M3 and M4
"""

from utils import *

domain_separation = {"M1": [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1],
                            [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 1],
                            [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1]
                            ],

                     "M2": [[0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1],
                            [0, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 1, 1],
                            [0, 0, 0, 1, 0, 1, 0, 0],
                            [0, 0, 0, 1, 0, 1, 0, 1]],

                     "M3": [[0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 1],
                            [0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 1, 0, 1, 1],
                            [0, 0, 0, 0, 1, 1, 0, 0],
                            [0, 0, 0, 0, 1, 1, 0, 1]],

                     "M4": [[0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 1],
                            [0, 0, 0, 1, 1, 0, 1, 0], [0, 0, 0, 1, 1, 0, 1, 1],
                            [0, 0, 0, 1, 1, 1, 0, 0],
                            [0, 0, 0, 1, 1, 1, 0, 1]]}


class SkinnyAead:
    def __init__(self, member, skinny):
        """
        Constructor method.
        Parameters: the member of SKINNY (M1-M4), and the SKINNY BC object.
        Returns: none.
        """
        self.member = member[-2:]  # member (1-4), i.e. version of SKINNY-AEAD
        self.skinny = skinny  # skinny object
        self.nonce = []
        self.key = []
        self.nonce_size = -1
        self.key_size = -1

    def encrypt(self, plaintext, key, associated_data, nonce):
        """
        Method to encrypt plaintext message and generate a tag using
        authenticated data.
        Parameters: the plaintext to encrypt, the key, associated data, and
        nonce.
        Return: the ciphertext and the tag.
        """

        self.nonce = nonce  # the nonce
        self.key = key  # the key
        self.nonce_size = len(nonce) * 4  # size of the nonce (bits)
        self.key_size = len(key) * 4  # size of the key (bits)

        # process the authenticated data and the plaintext blocks
        auth = self.process_ad(associated_data)
        ciphertext, tag = self.process_plaintext(plaintext)

        # generate the tag by xoring auth with the tag
        tag = xor_bits(convert_to_bits(tag), auth)
        tag = convert_from_bits(tag, 128)

        # if using M3 or M4 SKINNY-AEAD truncate tag to 64 bits
        if self.member == "M3" or self.member == "M4":
            tag = tag[0:16]

        return ciphertext, tag

    def verify(self, ciphertext, key, associated_data, nonce, tag_to_verify):
        """
        Method to decrypt ciphertext with the provided authenticated data
        Parameters: The ciphertext to decrypt, the associated data and the tag
        Returns: If the tag matches the tag provided, returns the plaintext,
        if not, an empty list.
        Parameters: the ciphertext to decrypt, the associated data and the
        tag that is to be verified.
        Returns: the plaintext if tag is verified, [-1] otherwise.
        """

        self.nonce = nonce  # the nonce
        self.key = key  # the key
        self.nonce_size = len(nonce) * 4  # size of the nonce (bits)
        self.key_size = len(key) * 4  # size of the key (bits)

        # process the authenticated data and the plaintext blocks
        auth = self.process_ad(associated_data)
        plaintext, tag = self.process_plaintext_dec(ciphertext)

        # generate the tag by xoring auth with the tag
        tag = xor_bits(convert_to_bits(tag), auth)
        tag = convert_from_bits(tag, 128)

        # if using M3 or M4 SKINNY-AEAD truncate tag to 64 bits
        if self.member == "M3" or self.member == "M4":
            tag = tag[0:16]

        # if generated tag matches provided one, return plaintext
        if tag_to_verify == tag:
            return plaintext
        else:
            return [-1]

    def apply_LFSR(self, lfsr):
        """
        Method to update the LFSR.
        Parameters: LFSR (the state of the current LFSR in hexadecimal.
        Returns: updated LFSR (in hexadecimal).
        """

        # First convert the current lfsr into its bit representation
        lfsr = convert_to_bits(lfsr)

        # Calculate final four bits of the updated lfsr
        updatedLFSR = []
        y0 = lfsr[0]
        y1 = lfsr[63] ^ lfsr[0]
        y2 = lfsr[62]
        y3 = lfsr[61] ^ lfsr[0]
        y4 = lfsr[60] ^ lfsr[0]

        #  Rest of the bits are shifted by 1
        for i in range(0, 59):
            updatedLFSR.append(lfsr[i + 1])

        # Append the final four bits to the updated lfsr
        updatedLFSR.append(y4)
        updatedLFSR.append(y3)
        updatedLFSR.append(y2)
        updatedLFSR.append(y1)
        updatedLFSR.append(y0)

        # Convert the updated lfsr back to hex
        updatedLFSR = convert_from_bits(updatedLFSR, 64)

        return updatedLFSR

    def rev64(self, lfsr):
        """
        Method to reverse the order of the bytes in the LFSR.
        Parameters: current state of the LFSR in hexadecimal.
        Returns: the reversed LFSR in hex where bytes have been reversed.
        """

        reversedLFSR = []
        for i in range(len(lfsr) - 1, 0, -2):
            reversedLFSR.append(lfsr[i - 1])
            reversedLFSR.append(lfsr[i])
        return reversedLFSR

    def generate_LFSR(self):
        """"
        Method to initialise the LFSR - its initial value is 0*63 || 1.
        Method then converts it to hex representation.
        Parameters: none.
        Returns: initialised LFSR.
        """

        lfsr = [0] * 63 + [1]
        lfsr = convert_from_bits(lfsr, 64)

        return lfsr

    def get_domain_separation(self, d):
        """
        Method to return the domain separation byte.
        Parameters: d - number of the domain separation byte to use.
        Returns: the byte in two nibbles (hex).
        """

        x = domain_separation[self.member][d]
        x = convert_from_bits(x, 8)

        return x[0], x[1]

    def generate_tweakey(self, d, lfsr):
        """
        Method to generate the TK for a given block.
        Parameters: d - the domain separation to use, and the
        LFSR value (in hexadecimal).
        Returns: the TK.
        """

        TK = []
        # Get the domain separation byte (returned as two nibbles)
        d1, d2 = self.get_domain_separation(d)

        # Reverse the bytes order of the LFSR
        lfsr = self.rev64(lfsr)

        # Add the LFSR to the TK
        TK += lfsr

        # Add 0*56 bits to the TK (14 nibbles)
        for i in range(0, 14):
            TK.append(0)

        # Add the domain separation to the TK
        TK.append(d1)
        TK.append(d2)

        # Finally, add the nonce and key to the TK
        TK += self.nonce

        if self.member == "M2" or self.member == "M4":
            # Add 0*56 bits to the TK (14 nibbles)
            for i in range(0, 8):
                TK.append(0)

        TK += self.key

        return TK

    def calculate_sigma(self, blocks):
        """
        Sigma is all of the blocks in the plaintext XOR'ed together
        (with the last block padded if necessary). Method calculates Sigma.
        Parameters: list of plaintext blocks.
        Returns: sigma
        """

        # Initialise sigma
        sigma = [0] * 128

        # If there is no plaintext, return 0*128
        if blocks == []:
            return [0] * 128

        # XOR all blocks (excluding last one)
        for i in range(0, len(blocks) - 1):
            bits = convert_to_bits(blocks[i])
            sigma = xor_bits(bits, sigma)

        # Get the last block in the list of plaintext blocks
        lastBlock = blocks[-1]

        # If the final block is a full block, no padding needs to be applied
        if len(lastBlock) == 32:
            bits = convert_to_bits(lastBlock)
            sigma = xor_bits(bits, sigma)

        # Otherwise, apply padding before XORing    
        else:
            lastBlock = apply_padding(lastBlock[:], 128)
            bits = convert_to_bits(lastBlock)
            sigma = xor_bits(bits, sigma)

        # Return sigma in hex representation
        return convert_from_bits(sigma, 128)

    def process_ad(self, blocksAD):
        """
        Method to process the authenticated data and calculate
        the auth variable which is later XORed with sigma to generate
        the tag.
        Parameters: authenticated data blocks.
        Returns: auth variable.
        """

        # Initialise auth to 0*128
        auth = [0] * 128

        # Initialise the LFSR and generate the first TK value
        lfsr = self.generate_LFSR()
        TK = self.generate_tweakey(2, lfsr)

        # First check if authenticated data is not empty -
        # if it is, the initialised auth is returned
        if blocksAD != [[]]:

            # Iterate over all but the last block of authenticated data 
            for i in range(0, len(blocksAD) - 1):
                # Encrypt each block under the tweakey TK and
                # XOR it to the auth variable
                encryptedBlock = self.skinny.encrypt_block(blocksAD[i], TK)
                auth = xor_bits(auth, convert_to_bits(encryptedBlock))

                # Update the LFSR and generate the new TK
                lfsr = self.apply_LFSR(lfsr)
                TK = self.generate_tweakey(2, lfsr)

            # Get the last block of authenticated data
            lastBlock = blocksAD[-1]

            # If the last block of authenticated data is not full,
            # it needs to be padded
            if len(lastBlock) != 32:

                # Pad the last block and specify domain separation 3 for the TK
                padLastBlock = apply_padding(lastBlock, 128)
                TK = self.generate_tweakey(3, lfsr)

                # Encrypt the padded associated data and XOR it
                # to the auth variable
                cipher = self.skinny.encrypt_block(padLastBlock, TK)
                auth = xor_bits(auth, convert_to_bits(cipher))

            else:
                cipher = self.skinny.encrypt_block(lastBlock, TK)
                auth = xor_bits(auth, convert_to_bits(cipher))
        return auth

    def process_plaintext(self, blocks):
        """
        Method to process the plaintext blocks during encryption.
        Parameters: the plaintext blocks
        Returns: the ciphertext and T
        """

        # Initialise the LFSR and ciphertext list
        lfsr = self.generate_LFSR()
        ciphertext = []

        # First check whether the plaintext is empty
        if blocks == [[]]:
            # If no plaintext is supplied, generate the TK and encrypt
            # 0*128 under it
            TK = self.generate_tweakey(4, lfsr)
            T = self.skinny.encrypt_block([0] * 128, TK)

        else:
            # Loop over all but the last plaintext  block
            for i in range(0, len(blocks) - 1):
                # Generate the TK with domain separation d0 and
                # encrypt each plaintext block
                TK = self.generate_tweakey(0, lfsr)
                C = self.skinny.encrypt_block(blocks[i], TK)
                ciphertext.append(C)

                # Update the LFSR
                lfsr = self.apply_LFSR(lfsr)

            # Get the final block in the plaintext
            lastBlock = blocks[-1]

            if len(lastBlock) != 32:

                # If the last block is not full
                TK = self.generate_tweakey(1, lfsr)

                # Encrypt 0*128
                R = self.skinny.encrypt_block([0] * 32, TK)

                # Truncate R such that it is the same length
                # as the plaintext block,
                # then XOR R and the plaintext block together
                mBits = convert_to_bits(lastBlock)
                R = convert_to_bits(R)
                trunct = len(mBits)
                clm = xor_bits(R[0:trunct], mBits)
                clm = convert_from_bits(clm, len(lastBlock) * 4)
                ciphertext.append(clm)

                # Update LFSR
                lfsr = self.apply_LFSR(lfsr)
                TK = self.generate_tweakey(5, lfsr)

                # Encrypt sigma under the TK
                T = self.skinny.encrypt_block(self.calculate_sigma(blocks), TK)

            else:
                # If final block is full
                TK = self.generate_tweakey(0, lfsr)
                C = self.skinny.encrypt_block(lastBlock, TK)
                ciphertext.append(C)

                # Update LFSR and encrypt sigma
                lfsr = self.apply_LFSR(lfsr)
                TK = self.generate_tweakey(4, lfsr)
                T = self.skinny.encrypt_block(self.calculate_sigma(blocks), TK)

        return ciphertext, T

    def process_plaintext_dec(self, blocks):
        """
        Method to process the plaintext blocks during decryption.
        Parameters: the ciphertext blocks.
        Returns: the plaintext and T.
        """

        # Initialise the LFSR and ciphertext list
        lfsr = self.generate_LFSR()
        plaintext = []

        # First check whether the plaintext is empty
        if blocks == [[]]:
            # If no plaintext is supplied, generate the TK and encrypt
            # 0*128 under it
            TK = self.generate_tweakey(4, lfsr)
            T = self.skinny.encrypt_block([0] * 128, TK)

        else:
            # Loop over all but the last plaintext  block
            for i in range(0, len(blocks) - 1):
                # Generate the TK with domain separation d0 and
                # encrypt each plaintext block
                TK = self.generate_tweakey(0, lfsr)
                C = self.skinny.decrypt_block(blocks[i], TK)
                plaintext.append(C)

                # Update the LFSR
                lfsr = self.apply_LFSR(lfsr)

            # Get the final block in the plaintext
            lastBlock = blocks[-1]

            if len(lastBlock) != 32:
                # If final block not full
                TK = self.generate_tweakey(1, lfsr)

                # Encrypt 0*128
                R = self.skinny.encrypt_block([0] * 32, TK)

                # Truncate R such that it is the same length
                # as the plaintext block, then XOR R and the
                # plaintext block together
                mBits = convert_to_bits(lastBlock)
                R = convert_to_bits(R)

                trunct = len(mBits)
                clm = xor_bits(R[0:trunct], mBits)
                clm = convert_from_bits(clm, len(lastBlock) * 4)
                plaintext.append(clm)

                # Update LFSR
                lfsr = self.apply_LFSR(lfsr)
                TK = self.generate_tweakey(5, lfsr)
                T = self.skinny.encrypt_block(self.calculate_sigma(
                    plaintext[:]), TK)



            else:
                # If final block is full
                TK = self.generate_tweakey(0, lfsr)
                C = self.skinny.decrypt_block(lastBlock, TK)
                plaintext.append(C)

                # Update LFSR and encrypt sigma
                lfsr = self.apply_LFSR(lfsr)
                TK = self.generate_tweakey(4, lfsr)
                T = self.skinny.encrypt_block(self.calculate_sigma(
                    plaintext), TK)

        return plaintext, T
