def part1():
    lantern_fish = list()
    with open('resources/input6.txt') as f:
        lines = f.readlines()
        entries = lines[0].strip().split(',')
        for entry in entries:
            lantern_fish.append(int(entry))

    for i in range(0, 80):
        fish_to_add = list()
        for fish in lantern_fish:
            if fish == 0:
                fish_to_add.append(8)
                lantern_fish[lantern_fish.index(fish)] = 6
            else:
                val = (lantern_fish[lantern_fish.index(fish)] - 1)
                lantern_fish[lantern_fish.index(fish)] = val
        lantern_fish += fish_to_add
    print(len(lantern_fish))


def part1_take2():
    lantern_fish = list()
    with open('resources/input6.txt') as f:
        lines = f.readlines()
        entries = lines[0].strip().split(',')
        for entry in entries:
            lantern_fish.append(int(entry))

    fish_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for fish in lantern_fish:
        fish_counts[fish] += 1

    for i in range(0, 80):
        new_entries = fish_counts[0]
        fish_counts[0] = fish_counts[1]
        fish_counts[1] = fish_counts[2]
        fish_counts[2] = fish_counts[3]
        fish_counts[3] = fish_counts[4]
        fish_counts[4] = fish_counts[5]
        fish_counts[5] = fish_counts[6]
        fish_counts[6] = fish_counts[7] + new_entries
        fish_counts[7] = fish_counts[8]
        fish_counts[8] = new_entries

    total = 0
    for count in fish_counts:
        total += count
    print(total)


def part2():
    lantern_fish = list()
    with open('resources/input6.txt') as f:
        lines = f.readlines()
        entries = lines[0].strip().split(',')
        for entry in entries:
            lantern_fish.append(int(entry))

    fish_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for fish in lantern_fish:
        fish_counts[fish] += 1

    for i in range(0, 256):
        new_entries = fish_counts[0]
        fish_counts[0] = fish_counts[1]
        fish_counts[1] = fish_counts[2]
        fish_counts[2] = fish_counts[3]
        fish_counts[3] = fish_counts[4]
        fish_counts[4] = fish_counts[5]
        fish_counts[5] = fish_counts[6]
        fish_counts[6] = fish_counts[7] + new_entries
        fish_counts[7] = fish_counts[8]
        fish_counts[8] = new_entries

    total = 0
    for count in fish_counts:
        total += count
    print(total)


if __name__ == '__main__':
    part1_take2()
    part2()
