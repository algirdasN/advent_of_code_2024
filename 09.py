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

    data_list = []
    for i in range(len(data)):
        size = int(data[i])
        if size == 0:
            continue

        value = i // 2 if i % 2 == 0 else -1
        data_list.append((value, size))

    r_pointer = 0
    while True:
        r_pointer -= 1
        if r_pointer < -len(data_list):
            break

        if data_list[r_pointer][0] == -1:
            continue

        size = data_list[r_pointer][1]

        for l_pointer in range(len(data_list) + r_pointer):
            if data_list[l_pointer][0] != -1:
                continue

            space = data_list[l_pointer][1]
            if size > space:
                continue

            data_list[l_pointer] = data_list[r_pointer]

            if size < space:
                data_list.insert(l_pointer + 1, (-1, space - size))

            if r_pointer + 1 < 0 and data_list[r_pointer + 1][0] == -1:
                size += data_list[r_pointer + 1][1]
                data_list.pop(r_pointer + 1)
                r_pointer += 1

            if data_list[r_pointer - 1][0] == -1:
                size += data_list[r_pointer - 1][1]
                data_list.pop(r_pointer - 1)

            data_list[r_pointer] = (-1, size)
            break

    bit_counter = 0
    checksum = 0
    for file in data_list:
        if file[0] > 0:
            checksum += file[0] * file[1] * (2 * bit_counter + file[1] - 1) // 2
        bit_counter += file[1]

    print(checksum)


if __name__ == "__main__":
    main()
