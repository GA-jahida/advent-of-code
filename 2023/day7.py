def get_winnings(lines, card_dict, useJoker):
    hands_and_bids = [(list(lines[0].split(" ")[0]), int(lines[0].split(" ")[1]))]
    for line_index in range(1, len(lines)):
            hand = list(lines[line_index].split(" ")[0])
            bid = int(lines[line_index].split(" ")[1])
            for index, hand_and_bid in enumerate(hands_and_bids):
                if is_right_order(hand, hand_and_bid[0], card_dict, useJoker):
                    hands_and_bids.insert(index, (hand, bid))
                    break
                if index == len(hands_and_bids) - 1:
                    hands_and_bids.append((hand, bid))
                    break
    winnings = 0            
    for index, hand_and_bid in enumerate(hands_and_bids):
        winnings += (index + 1) * hand_and_bid[1]
    return winnings


def is_right_order(first_hand, second_hand, card_dict, useJoker):
    first_hand_type = get_hand_type(first_hand, card_dict, useJoker)
    second_hand_type = get_hand_type(second_hand, card_dict, useJoker)
    if first_hand_type < second_hand_type:
        return True
    elif first_hand_type == second_hand_type:
        for index, char in enumerate(first_hand):
            if card_dict[char] < card_dict[second_hand[index]]:
                return True
            elif card_dict[char] > card_dict[second_hand[index]]:
                return False
    return False
            

def get_hand_type(hand, card_dict, useJoker):
    temp = []
    if useJoker and "J" in hand:
        duplicates = set([card for card in hand if hand.count(card) > 1])
        max_char = ""
        if len(duplicates) == 0 or (len(duplicates) == 1 and "J" in duplicates):
            for char in hand:
                if max == "" or card_dict[char] > card_dict[max_char]:
                    max_char = char
        else:
            for duplicate in duplicates:
                if max == "" or card_dict[duplicate] > card_dict[max_char]:
                    max_char = duplicate
        for index, char in enumerate(hand):
            if char == "J":
                temp.append(max_char)
            else:
                temp.append(char)
        hand = temp
    set_hand = set(hand)
    if len(set_hand) == 1: 
        return 6 # 5 of a kind
    elif len(set_hand) == 2: 
        duplicates = set([card for card in hand if hand.count(card) > 1])
        if len(duplicates) == 1:
            return 5 # 4 of a kind
        else:
            return 4 # Full house
    elif len(set_hand) == 3:
        duplicates = set([card for card in hand if hand.count(card) > 1])
        if len(duplicates) == 1:
            return 3 # 3 of a kind
        else:
            return 2 # 2 pair
    elif len(set_hand) == 4: 
        return 1  # 1 pair
    else:
        return 0 # High card

def part1(lines):
    card_dict = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, '': 0}
    return get_winnings(lines, card_dict, False)


def part2(lines):
    card_dict = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1 , '': 0}
    return get_winnings(lines, card_dict, True)

lines = open("./inputs/day7-input.txt", "r").readlines()
print("Q1:", part1(lines))
print("Q2:", part2(lines))