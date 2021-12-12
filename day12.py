def part1():
    with open('resources/input12.txt') as f:
        lines = f.readlines()
        connections = {}
        for line in lines:
            line = line.strip()
            split = line.split('-')
            if split[0] not in connections:
                connections[split[0]] = list()
            if split[1] not in connections:
                connections[split[1]] = list()
            connections.get(split[0]).append(split[1])
            connections.get(split[1]).append(split[0])

        chain = list()
        chain.append("start")
        print(find_path(connections["start"], connections, chain))


def find_path(node, connections, chain):
    found = 0
    for value in node:
        new_chain = list()
        new_chain.extend(chain)
        if value == "end":
            found += 1
        elif value == "start":
            continue
        elif value.islower() and value in new_chain:
            continue
        else:
            new_chain.append(value)
            found += find_path(connections[value], connections, new_chain)
    return found


def part2():
    with open('resources/input12.txt') as f:
        lines = f.readlines()
        connections = {}
        for line in lines:
            line = line.strip()
            split = line.split('-')
            if split[0] not in connections:
                connections[split[0]] = list()
            if split[1] not in connections:
                connections[split[1]] = list()
            connections.get(split[0]).append(split[1])
            connections.get(split[1]).append(split[0])

        chain = list()
        chain.append("start")
        print(find_path2(connections["start"], connections, chain))


def find_path2(node, connections, chain):
    found = 0
    for value in node:
        new_chain = list()
        new_chain.extend(chain)
        if value == "end":
            found += 1
        elif value == "start":
            continue
        elif value.islower():
            duplicate_already_used = False
            seen = set()
            dupes = [x for x in new_chain if x in seen or seen.add(x)]
            for entry in dupes:
                if entry.islower():
                    duplicate_already_used = True
                    break
            if duplicate_already_used and value in new_chain:
                continue
            else:
                new_chain.append(value)
                found += find_path2(connections[value], connections, new_chain)
        else:
            new_chain.append(value)
            found += find_path2(connections[value], connections, new_chain)
    return found


if __name__ == '__main__':
    #part1()
    part2()
