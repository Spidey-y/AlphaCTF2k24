def read_byte_file(filename):
    with open(filename, "rb") as f:
        byte_data = f.read()
    left= []
    right= []
    for b in range(len(byte_data)):
        if b%2 == 0:
            left.append(byte_data[b])
        else:
            right.append(byte_data[b])
    left+=right
    return left
    # return byte_data


def byte_to_binary(byte):
    return format(
        byte, "08b"
    )  # Convert byte to binary string, padded with zeros to 8 digits


def bytes_to_matrix(byte_data):
    matrix = []
    for byte in byte_data:
        binary_str = byte_to_binary(byte)
        row = [
            int(bit) for bit in binary_str
        ]  # Convert binary string to list of integers
        matrix.append(row)
    return matrix


def main():
    filename = "output.bin"  # Change this to your file name
    byte_data = read_byte_file(filename)
    matrix = bytes_to_matrix(byte_data)
    chunk = []
    for row in matrix:
        if len(chunk) != 8:
            chunk.append(row)
        else:
            # transpose chunk matrix
            transposed_chunk = list(zip(*chunk))
            # join transposed tuples
            joined_transposed = ["".join(map(str, t)) for t in transposed_chunk]
            for i in joined_transposed:
                print(chr(int(i, 2)), end="")
            chunk = []
            chunk.append(row)
    #treat the last chunk
    transposed_chunk = list(zip(*chunk))
    joined_transposed = ["".join(map(str, t)) for t in transposed_chunk]
    for i in joined_transposed:
        print(chr(int(i, 2)), end="")

if __name__ == "__main__":
    main()
