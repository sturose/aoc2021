def part1():
    with open('resources/input8.txt') as f:
        lines = f.readlines()
        total = 0
        for line in lines:
            split = line.strip().split('|')
            code = split[0].strip().split(' ')
            output = split[1].strip().split(' ')
            for entry in output:
                if len(entry) == 2 or len(entry) == 3 or len(entry) == 4 or len(entry) == 7:
                    total += 1
        print(total)


def part2():

    with open('resources/input8.txt') as f:
        lines = f.readlines()
        total = 0
        for line in lines:
            split = line.strip().split('|')
            code = split[0].strip().split(' ')
            output = split[1].strip().split(' ')
            numbers = dict()
            values = dict()
            code.sort(key=len)
            for code_entry in code:
                sorted_code = "".join(sorted(code_entry))
                if len(sorted_code) == 2:
                    numbers[1] = sorted_code
                    values[sorted_code] = 1
                if len(sorted_code) == 3:
                    numbers[7] = sorted_code
                    values[sorted_code] = 7
                if len(sorted_code) == 4:
                    numbers[4] = sorted_code
                    values[sorted_code] = 4
                if len(sorted_code) == 7:
                    numbers[8] = sorted_code
                    values[sorted_code] = 8
                if len(sorted_code) == 5:
                    if contains_all_digits(sorted_code, numbers[1]):
                        numbers[3] = sorted_code
                        values[sorted_code] = 3
                    elif digits_contained(sorted_code, numbers[4]) == 3:
                        numbers[5] = sorted_code
                        values[sorted_code] = 5
                    else:
                        numbers[2] = sorted_code
                        values[sorted_code] = 2
                if len(sorted_code) == 6:
                    if contains_all_digits(sorted_code, numbers[4]):
                        numbers[9] = sorted_code
                        values[sorted_code] = 9
                    elif contains_all_digits(sorted_code, numbers[1]):
                        numbers[0] = sorted_code
                        values[sorted_code] = 0
                    else:
                        numbers[6] = sorted_code
                        values[sorted_code] = 6

            output_value = 0
            for output_entry in output:
                output_value = output_value * 10 + values["".join(sorted(output_entry))]

            total += output_value

        print(total)


def contains_all_digits(entry, input):
    for letter in input:
        if letter not in entry:
            return False
    return True


def digits_contained(entry, input):
    total = 0
    for letter in input:
        if letter in entry:
            total +=1
    return total


if __name__ == '__main__':
    part1()
    part2()
