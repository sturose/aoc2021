def part1():
    x = 0
    y = 0
    with open('resources/input2.txt') as f:
        lines = f.readlines()
        for line in lines:
            split = line.split(" ")
            val = int(split[1])
            if split[0] == 'forward':
                x = x + val
            if split[0] == 'up':
                y = y - val
            if split[0] == 'down':
                y = y + val

    print(x, y)
    print(x * y)


def part2():
    aim = 0
    x = 0
    y = 0
    with open('resources/input2.txt') as f:
        lines = f.readlines()
        for line in lines:
            split = line.split(" ")
            val = int(split[1])
            if split[0] == 'forward':
                x = x + val
                y = y + (val * aim)
            if split[0] == 'up':
                aim = aim - val
            if split[0] == 'down':
                aim = aim + val

    print(aim, x, y)
    print(x * y)


if __name__ == '__main__':
    part1()
    part2()
