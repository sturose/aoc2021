def part1():
    with open('resources/input4.txt') as f:
        lines = f.readlines()
        input = lines.pop(0).split(',')
        lines.pop(0)
        cards = get_cards(lines)

        for number in input:
            for card in cards:
                for row in card:
                    for spot in row:
                        if spot[0] == number:
                            spot[1] = True
            winnerFound = findWinner(cards)
            if winnerFound:
                unmarkedTotal = get_unmarked_total(winnerFound)
                print(unmarkedTotal * int(number))
                break


def get_cards(lines):
    cards = list()
    card = list()
    for line in lines:
        if not line.strip():
            cards.append(card)
            card = list()
        else:
            entries = line.strip().replace("  ", " ").split(" ")
            row = list()
            for entry in entries:
                value = list()
                value.append(entry)
                value.append(False)
                row.append(value)
            card.append(row)
    cards.append(card)
    return cards


def findWinner(cards):

    for card in cards:
        for x in range(0, len(card)):
            y_good = True
            x_good = True
            for y in range(0, len(card)):
                if not card[x][y][1]:
                    x_good = False
                if not card[y][x][1]:
                    y_good = False
            if y_good or x_good:
                return card
    return None


def get_unmarked_total(card):
    total = 0
    for row in card:
        for entry in row:
            if not entry[1]:
                total += int(entry[0])
    return total


def part2():
    with open('resources/input4.txt') as f:
        lines = f.readlines()
        input = lines.pop(0).split(',')
        lines.pop(0)
        cards = get_cards(lines)

        for number in input:
            for card in cards:
                for row in card:
                    for spot in row:
                        if spot[0] == number:
                            spot[1] = True
            winnerFound = findWinner(cards)
            while winnerFound:
                cards.remove(winnerFound)
                if len(cards) == 0:
                    unmarkedTotal = get_unmarked_total(winnerFound)
                    print(unmarkedTotal * int(number))
                winnerFound = findWinner(cards)

if __name__ == '__main__':
    part1()
    part2()
