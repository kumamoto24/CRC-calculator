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


data_input = input("Enter the original binary data (e.g., 1101001) or hex (e.g., 0xAB): ")
poly_input = input("Enter the generator polynomial in binary (e.g., CRC-8: 100000111): ")

# Convert hexadecimal input to binary
if data_input.startswith("0x") or data_input.startswith("0X"):
    data_input = bin(int(data_input, 16))[2:]

# Input Validation
if not all(c in '01' for c in data_input + poly_input):
    print("Input must contain only binary digits 0 and 1!")
else:
    crc_rem = crc_generic(data_input, poly_input)
    print(f"Original data: {data_input}")
    print(f"Generator polynomial: {poly_input}")
    print(f"CRC remainder: {crc_rem}")
    print(f"Transmitted data: {data_input + crc_rem}")