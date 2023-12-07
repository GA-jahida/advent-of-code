def parse(lines):

    bids = [int(lines[0].split(" ")[1])]

    for index, line in enumerate(lines):
        hand = list(line.split(" ")[0])
        bid = int(line.split(" ")[1])
        next_hand = list(lines[index+1].split(" ")[0])
        next_bid = int(lines[index+1].split(" ")[1])
        hand_type = get_hand_type(hand)
        next_hand_type = get_hand_type(next_hand)
        if hand_type < next_hand_type:
            bids.insert(0, next_bid)
        elif hand_type == next_hand_type:
            for index, char in enumerate(hand):
                if char < next_hand[index]:
                    bids.insert(0, next_bid)
                elif char > next_hand[index]:
                    bids.append(next_bid)
        else:
            bids.append(next_bid)
        print(bids)
    return prod(bids)


def get_hand_type(hand):
    set_hand = set(hand)
    if len(set_hand) == 1: # Five of a kind
        return 6
    elif len(set_hand) == 2: # Four of a kind or full house
        duplicates = [card for card in hand if hand.count(card) > 1]
        removed_cards = list(set(duplicates))
        if len(removed_cards) == 1:
            return 5
        else:
            return 4
    elif len(set_hand) == 3: # three of a kind or 2 pair
        duplicates = [card for card in hand if hand.count(card) > 1]
        removed_cards = list(set(duplicates))
        if len(removed_cards) == 1:
            return 3
        else:
            return 2
    elif len(set_hand) == 4:  # one pair
        return 1
    else:
        return 0

def part1(lines):
    return parse(lines)


def part2(lines):
    return 

lines = open("./inputs/day7-input.txt", "r").readlines()
print("Q1:", part1(lines))
print("Q2:", part2(lines))