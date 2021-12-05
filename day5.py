def part1():
    matrix = list()
    for i in range(1000):
        row = list()
        for i2 in range(1000):
            row.append(0)
        matrix.append(row)

    with open('resources/input5.txt') as f:
        lines = f.readlines()
        for line in lines:
            pairs = line.split(" -> ")
            first = True
            start = None
            end = None
            for pair in pairs:
                values = pair.split(",")
                x = int(values[1].strip())
                y = int(values[0].strip())
                int_pair = (x, y)
                if first:
                    start = int_pair
                    first = False
                else:
                    end = int_pair
            if use_line(start, end):
                if start[0] == end[0]:
                    low_high = get_low_and_high(start[1], end[1])
                    for i in range(low_high[0], low_high[1] + 1):
                        matrix[start[0]][i] += 1
                else:
                    low_high = get_low_and_high(start[0], end[0])
                    for i in range(low_high[0], low_high[1] + 1):
                        matrix[i][start[1]] += 1

    overlap_line_count = 0
    for row in matrix:
        for val in row:
            if val > 1:
                overlap_line_count += 1

    print(overlap_line_count)


def use_line(start, end):
    if start[0] == end[0]:
        return True
    if start[1] == end[1]:
        return True
    return False


def get_low_and_high(val1, val2):
    low = val1
    high = val1
    if val2 > val1:
        high = val2
    else:
        low = val2
    return low, high


def part2():
    matrix = list()
    for i in range(1000):
        row = list()
        for i2 in range(1000):
            row.append(0)
        matrix.append(row)

    with open('resources/input5.txt') as f:
        lines = f.readlines()
        for line in lines:
            pairs = line.split(" -> ")
            first = True
            start = None
            end = None
            for pair in pairs:
                values = pair.split(",")
                x = int(values[1].strip())
                y = int(values[0].strip())
                int_pair = (x, y)
                if first:
                    start = int_pair
                    first = False
                else:
                    end = int_pair
            if use_line2(start, end):
                if start[0] == end[0]:
                    low_high = get_low_and_high(start[1], end[1])
                    for i in range(low_high[0], low_high[1] + 1):
                        matrix[start[0]][i] += 1
                else:
                    if start[1] == end[1]:
                        low_high = get_low_and_high(start[0], end[0])
                        for i in range(low_high[0], low_high[1] + 1):
                            matrix[i][start[1]] += 1
                    else:
                        x_mod = 1
                        if end[0] < start[0]:
                            x_mod = -1

                        y_mod = 1
                        if end[1] < start[1]:
                            y_mod = -1

                        x_val = start[0]
                        y_val = start[1]

                        low_high1 = get_low_and_high(start[0], end[0])
                        for i in range(0, low_high1[1] - low_high1[0] + 1):
                            matrix[x_val][y_val] += 1
                            x_val += x_mod
                            y_val += y_mod

    overlap_line_count = 0
    for row in matrix:
        for val in row:
            if val > 1:
                overlap_line_count += 1

    print(overlap_line_count)


def use_line2(start, end):
    if start[0] == end[0]:
        return True
    if start[1] == end[1]:
        return True
    if abs(start[0] - end[0]) == abs(start[1] - end[1]):
        return True
    return False


if __name__ == '__main__':
    part1()
    part2()
