import statistics


def part1():
    positions = list()
    with open('resources/input7.txt') as f:
        lines = f.readlines()
        entries = lines[0].strip().split(',')
        for entry in entries:
            positions.append(int(entry))

    prev_fuel_cost = 99999999
    for i in range(1, 1300):
        fuel_cost = calculate_fuel_cost(positions, i)
        if fuel_cost < prev_fuel_cost:
            prev_fuel_cost = fuel_cost
        else:
            print(str(i) + " : " + str(prev_fuel_cost))
            break


def calculate_fuel_cost(postisions, i):
    total = 0
    for position in postisions:
        total += abs(position - i)
    return total


def part2():
    positions = list()
    with open('resources/input7.txt') as f:
        lines = f.readlines()
        entries = lines[0].strip().split(',')
        for entry in entries:
            positions.append(int(entry))

    prev_fuel_cost = 99999999999999
    for i in range(1, 1300):
        fuel_cost = calculate_fuel_cost2(positions, i)
        if fuel_cost < prev_fuel_cost:
            prev_fuel_cost = fuel_cost
        else:
            print(str(i) + " : " + str(prev_fuel_cost))
            break


def calculate_fuel_cost2(postisions, i):
    total = 0
    for position in postisions:
        for value in range(1, abs(position - i)+1):
            total += value
    return total


if __name__ == '__main__':
    part1()
    part2()
