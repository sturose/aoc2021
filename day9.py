def part1():
    with open('resources/input9.txt') as f:
        lines = f.readlines()
        map = list(list())
        first_row = list()
        last_row = list()
        for i in range(0, len(lines[0])):
            first_row.append(9)
            last_row.append(9)
        map.append(first_row)
        for line in lines:
            row = list()
            row.append(9)
            line = line.strip()
            for char in line:
                row.append((int(char)))
            row.append(9)
            map.append(row)
        map.append(last_row)

        risk_level_sum = 0
        for x in range(1, len(map)-1):
            for y in range(1, len(map[x])-1):
                if lowest_point(x, y, map):
                    risk_level_sum += (map[x][y] + 1)

        print(risk_level_sum)


def lowest_point(x, y, map):
    val = map[x][y]
    if val < map[x-1][y] and val < map[x+1][y] and val < map[x][y-1] and val < map[x][y+1]:
        return True
    return False


def part2():
    with open('resources/input9.txt') as f:
        lines = f.readlines()
        map = list(list())
        first_row = list()
        last_row = list()
        for i in range(0, len(lines[0])):
            first_row.append(False)
            last_row.append(False)
        map.append(first_row)
        for line in lines:
            row = list()
            row.append(False)
            line = line.strip()
            for char in line:
                val = int(char)
                if val == 9:
                    row.append(False)
                else:
                    row.append(True)
            row.append(False)
            map.append(row)
        map.append(last_row)

        basin_sizes = list()
        for x in range(1, len(map)-1):
            for y in range(1, len(map[x])-1):
                if map[x][y]:
                    basin_sizes.append(get_basin_size(x, y, map))
        sorted_sizes = sorted(basin_sizes)
        print(sorted_sizes.pop() * sorted_sizes.pop() * sorted_sizes.pop())


def get_basin_size(x, y, map):
    if not map[x][y]:
        return 0
    map[x][y] = False
    if map[x-1][y] or map[x+1][y] or map[x][y-1] or map[x][y+1]:
        return 1 + get_basin_size(x-1, y, map) + get_basin_size(x+1, y, map) + get_basin_size(x, y-1, map) + get_basin_size(x, y + 1, map)

    return 1


if __name__ == '__main__':
    part1()
    part2()
