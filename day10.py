import statistics

def part1():
    with open('resources/input10.txt') as f:
        lines = f.readlines()
        total = 0
        for line in lines:
            chunk = []
            for char in line.strip():
                if char == '[':
                    chunk.append(']')
                elif char == '(':
                    chunk.append(')')
                elif char == '<':
                    chunk.append('>')
                elif char == '{':
                    chunk.append('}')
                elif char != chunk.pop():
                    if char == ')':
                        total += 3
                    elif char == ']':
                        total += 57
                    elif char == '}':
                        total += 1197
                    elif char == '>':
                        total += 25137

        print(total)


def part2():
    with open('resources/input10.txt') as f:
        lines = f.readlines()
        totals = list()
        for line in lines:
            chunk = []
            total = 0
            for char in line:
                if char == '[':
                    chunk.append(']')
                elif char == '(':
                    chunk.append(')')
                elif char == '<':
                    chunk.append('>')
                elif char == '{':
                    chunk.append('}')
                elif char == '\n':
                    while len(chunk) != 0:
                        total = total * 5
                        value = chunk.pop()
                        if value == ']':
                            total += 2
                        elif value == ')':
                            total += 1
                        elif value == '>':
                            total += 4
                        elif value == '}':
                            total += 3
                    totals.append(total)
                elif char != chunk.pop():
                    # corrupted line
                    break

    print(statistics.median(totals))

if __name__ == '__main__':
    part1()
    part2()
