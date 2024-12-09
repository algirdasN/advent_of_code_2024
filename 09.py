def main():
    with open("data/09.txt") as file:
        data = file.readline()

    l_pointer = 0
    r_pointer = len(data) - 1
    l_bits = int(data[0])
    r_bits = int(data[-1])
    bit_counter = 0
    checksum = 0

    while l_pointer < r_pointer:
        if l_pointer % 2 == 0:
            checksum += bit_counter * (l_pointer // 2)
            l_bits -= 1
        else:
            checksum += bit_counter * (r_pointer // 2)
            l_bits -= 1
            r_bits -= 1

        bit_counter += 1

        while l_bits == 0:
            l_pointer += 1
            l_bits = int(data[l_pointer])
        while r_bits == 0:
            r_pointer -= 2
            r_bits = int(data[r_pointer])

    while r_bits > 0:
        checksum += bit_counter * (r_pointer // 2)
        r_bits -= 1
        bit_counter += 1

    print(checksum)


if __name__ == "__main__":
    main()
