from collections import Counter


def part1():
    with open('resources/input14.txt') as f:
        lines = f.readlines()
        template = lines[0].strip()
        insertions = {}

        for line in lines:
            line = line.strip()
            if "->" in line:
                split = line.split(' -> ')
                insertions[split[0]] = split[1]

        for _ in range(0, 10):
            template = insert(insertions, template)

        counter = Counter(template)
        most_common = counter.most_common()
        print(most_common[0][1] - most_common.pop()[1])


def insert(insertions, template):
    new_template = []
    prev_char = ' '
    for char in template:
        char_pair = prev_char + char
        if char_pair in insertions:
            new_template.append(insertions[char_pair])
        new_template.append(char)
        prev_char = char
    return new_template


def part2():
    with open('resources/input14.txt') as f:
        lines = f.readlines()
        template = lines[0].strip()
        template_pairs = {}
        prev_char = None
        for char in template:
            if prev_char is not None:
                char_pair = prev_char + char
                if char_pair in template_pairs:
                    template_pairs[char_pair] +=1
                else:
                    template_pairs[char_pair] = 1
            prev_char = char

        insertions = {}

        for line in lines:
            line = line.strip()
            if "->" in line:
                split = line.split(' -> ')
                insertions[split[0]] = (split[0][0] + split[1], split[1] + split[0][1])

        for _ in range(0, 40):
            template_pairs = insert2(insertions, template_pairs)

        print(template_pairs)
        counts = calculate_counts(template_pairs, template[0], template[len(template)-1])
        sorted_counts = sorted(counts.values())

        print(abs(sorted_counts[0] - sorted_counts.pop()))


def insert2(insertions, template_pairs):
    new_template_pairs = {}
    for entry in template_pairs:
        if entry in insertions:
            increment(insertions[entry][0], new_template_pairs, template_pairs[entry])
            increment(insertions[entry][1], new_template_pairs, template_pairs[entry])
        else:
            increment(entry, new_template_pairs, 1)
    return new_template_pairs


def increment(key, dict, count):
    if key in dict:
        dict[key] += count
    else:
        dict[key] = count


def calculate_counts(template_pairs, start, end):
    counts = {}
    for entry in template_pairs:
        for char in entry:
            increment(char, counts, template_pairs[entry])
    counts[start] += 1
    counts[end] += 1
    for count in counts:
        counts[count] /= 2
    return counts

if __name__ == '__main__':
    part1()
    part2()
