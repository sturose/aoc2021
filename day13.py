def part1():
    with open('resources/input13.txt') as f:
        lines = f.readlines()
        matrix = list(list())
        for i in range(0, 1500):
            row = list()
            for i2 in range(0, 1500):
                row.append('.')
            matrix.append(row)

        for line in lines:
            line = line.strip()
            if "=" in line:
                split = line.split('=')
                fold(split[0], int(split[1]), matrix)
                break
            else:
                split = line.split(',')
                x = int(split[0])
                y = int(split[1])
                matrix[x][y] = '#'

        total = 0
        for row in matrix:
            for value in row:
                if value == '#':
                    total +=1
        print(total)


def fold(axis, value, matrix):
    if axis == 'y':
        for i in range(1, value+1):
            to_y = value-i
            from_y = value+i
            for x in range(0, len(matrix)):
                if matrix[x][from_y] == '#':
                    matrix[x][to_y] = '#'
                    matrix[x][from_y] = '.'
    if axis == 'x':
        for i in range(1, value+1):
            for y in range(0, len(matrix[i])):
                if matrix[value + i][y] == '#':
                    matrix[value - i][y] = '#'
                    matrix[value + i][y] = '.'


def part2():
    with open('resources/input13.txt') as f:
        lines = f.readlines()
        matrix = list(list())
        for i in range(0, 1500):
            row = list()
            for i2 in range(0, 1500):
                row.append('.')
            matrix.append(row)

        for line in lines:
            line = line.strip()
            if "=" in line:
                split = line.split('=')
                fold(split[0], int(split[1]), matrix)
            else:
                split = line.split(',')
                x = int(split[0])
                y = int(split[1])
                matrix[x][y] = '#'

        total = 0
        for x in range(0, 7):
            for y in range(0, 45):
                print(matrix[y][x], end='')
            print()
        print(total)

if __name__ == '__main__':
    part1()
    part2()
