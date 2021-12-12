import statistics


def part1():
    with open('resources/input11.txt') as f:
        lines = f.readlines()
        map = list(list())

        first_row = list()
        last_row = list()
        # buffers to avoid out of range index error
        for i in range(0, 12):
            first_row.append(-1)
            last_row.append(-1)
        map.append(first_row)

        for line in lines:
            row = list()
            row.append(-1)  # buffer
            line = line.strip()
            for char in line:
                row.append((int(char)))
            row.append(-1)  # buffer
            map.append(row)

        map.append(last_row)

        flash_count = 0
        for _ in range(0, 100):
            # increment all by 1
            for x in range(1, 11):
                for y in range(1, 11):
                    map[x][y] += 1

            # adjust for flashes
            for x in range(1, 11):
                for y in range(1, 11):
                    flash(map, x, y)

            for x in range(1, 11):
                for y in range(1, 11):
                    if map[x][y] > 9:
                        flash_count += 1
                        map[x][y] = 0
        print(flash_count)


def flash(map, x, y):
    if map[x][y] != 10:
        return
    else:
        map[x][y] += 1
        increment_and_flash(map, x, y+1)
        increment_and_flash(map, x, y-1)
        increment_and_flash(map, x-1, y+1)
        increment_and_flash(map, x-1, y-1)
        increment_and_flash(map, x+1, y+1)
        increment_and_flash(map, x+1, y-1)
        increment_and_flash(map, x-1, y)
        increment_and_flash(map, x+1, y)


def increment_and_flash(map, x, y):
    if map[x][y] == -1:
        return
    # check if should flash before and after incrementing
    flash(map, x, y)
    map[x][y] += 1
    if map[x][y] == 10:
        flash(map, x, y)



def part2():
    with open('resources/input11.txt') as f:
        lines = f.readlines()
        map = list(list())

        first_row = list()
        last_row = list()
        # buffers to avoid out of range index error
        for i in range(0, 12):
            first_row.append(-1)
            last_row.append(-1)
        map.append(first_row)

        for line in lines:
            row = list()
            row.append(-1)  # buffer
            line = line.strip()
            for char in line:
                row.append((int(char)))
            row.append(-1)  # buffer
            map.append(row)

        map.append(last_row)

        attempt = 1
        while True:
            # increment all by 1
            flash_count = 0
            for x in range(1, 11):
                for y in range(1, 11):
                    map[x][y] += 1

            # adjust for flashes
            for x in range(1, 11):
                for y in range(1, 11):
                    flash(map, x, y)

            for x in range(1, 11):
                for y in range(1, 11):
                    if map[x][y] > 9:
                        flash_count += 1
                        map[x][y] = 0
            if(flash_count == 100):
                print(attempt)
                break
            else:
                attempt += 1


if __name__ == '__main__':
    part1()
    part2()
