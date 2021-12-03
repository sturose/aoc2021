def part1():
    with open('resources/input3.txt') as f:
        lines = f.readlines()
        total0 = list()
        total1 = list()

        for line in lines:
            index = 0
            for char in line:
                if len(total1) < index + 1:
                    total1.append(0)
                    total0.append(0)
                if char == '1':
                    total1[index] = total1[index] + 1
                else:
                    total0[index] = total0[index] + 1
                index += 1

        gamma_rate_list = list()
        epsilon_rate_list = list()
        for index in range(0, len(total1)-1):
            if total0[index] > total1[index]:
                gamma_rate_list.append("0")
                epsilon_rate_list.append("1")
            else:
                gamma_rate_list.append("1")
                epsilon_rate_list.append("0")

    print(gamma_rate_list)
    gamma_rate_string = "".join(gamma_rate_list)
    epsilon_rate_string = "".join(epsilon_rate_list)
    gamma_rate = binaryToDecimal(int(gamma_rate_string))
    epsilon_rate = binaryToDecimal(int(epsilon_rate_string))
    print(gamma_rate * epsilon_rate)


def binaryToDecimal(binary):
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


def part2():
    with open('resources/input3.txt') as f:
        lines = f.readlines()
        oxygen_running_list = lines
        co2_running_list = lines
        total0 = list()
        total1 = list()
        entry_length = 0

        for line in lines:
            entry_length = len(line)

        for index in range(0, entry_length):
            if len(total1) < index + 1:
                total1.append(0)
                total0.append(0)

            for line in oxygen_running_list:
                char = line[index]
                if char == '1':
                    total1[index] = total1[index] + 1
                else:
                    total0[index] = total0[index] + 1
            value = "1"
            if total1[index] < total0[index]:
                value = "0"
            oxygen_running_list = filterValues(oxygen_running_list, index, value)
            index += 1

        oxygen_list = list()
        for index in range(0, len(total1)):
            if total0[index] <= total1[index]:
                oxygen_list.append("1")
            else:
                oxygen_list.append("0")

    oxygen_string = findEntry(oxygen_running_list, entry_length, 1)
    oxygen = binaryToDecimal(int(oxygen_string))

    co2_string = findEntry(co2_running_list, entry_length, 0)
    co2 = binaryToDecimal(int(co2_string))

    print(oxygen)
    print(co2)

    print(co2 * oxygen)


def filterValues(running_list, index, value):
    new_list = list()
    for entry in running_list:
        if entry[index] == value:
            new_list.append(entry)
    return new_list


def findEntry(running_list, entry_length, find_larger):
    for index in range(0, entry_length):
        total1 = 0
        total0 = 0
        for line in running_list:
            char = line[index]
            if char == '1':
                total1 += 1
            else:
                total0 += 1

        value = "0"
        if find_larger:
            value = "1"
            if total1 < total0:
                value = "0"
        else:
            if total1 < total0:
                value = "1"
        running_list = filterValues(running_list, index, value)
        index += 1
        if len(running_list) == 1:
            return running_list[0]



if __name__ == '__main__':
    part1()
    part2()
