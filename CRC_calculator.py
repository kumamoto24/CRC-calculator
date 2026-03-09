def crc_generic(data_bits, poly_bits):
    """
    General CRC calculator
    data_bits: binary string, e.g., "1101001"
    poly_bits: binary string of generator polynomial, e.g., "100000111" (CRC-8)
    Returns: CRC remainder as string
    """
    # CRC length = generator polynomial length - 1
    r = len(poly_bits) - 1

    # Append r zeros to the end of data
    padded_data = data_bits + '0' * r
    data = list(padded_data)

    poly_len = len(poly_bits)

    # Binary division
    for i in range(len(data) - r):
        # Only XOR when the highest bit is 1
        if data[i] == '1':
            for j in range(poly_len):
                data[i + j] = str(int(data[i + j]) ^ int(poly_bits[j])) #Update the result of each XOR division

    # CRC remainder = last r bits
    remainder = ''.join(data[-r:])
    return remainder
