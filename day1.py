# Press the green button in the gutter to run the script.


def part1():
    count = 0
    prev = 99999
    with open('resources/input1.txt') as f:
        lines = f.readlines()
        for line in lines:
            val = int(line)
            if val > prev:
                count = count + 1
            prev = val

    print(count)


def part2():
    count = 0
    prev1 = 99999
    prev2 = 99999
    prev3 = 99999
    with open('resources/input1.txt') as f:
        lines = f.readlines()
        for line in lines:
            val = int(line)
            prevTotal = prev1 + prev2 + prev3
            total = val + prev1 + prev2
            if total > prevTotal:
                count = count + 1
            prev3 = prev2
            prev2 = prev1
            prev1 = val

    print(count)


if __name__ == '__main__':
    part1()
    part2()
