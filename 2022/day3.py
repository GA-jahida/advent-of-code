def get_priority_dict():
    priority_dict = {}
    for i in range(26):
        letter = chr(ord('a') + i)
        priority_dict[letter] = i + 1

    for i in range(26):
        letter = chr(ord('A') + i)
        priority_dict[letter] = i + 27

    return priority_dict


def get_priority_sum(lines, priority_dict):
    priority_sum = 0
    for line in lines:
        first_compartment, second_compartment = line[:len(
            line)//2], set(line[len(line)//2:])
        checked_letters = set()
        for letter in first_compartment:
            if not letter in checked_letters:
                if letter in second_compartment:
                    priority_sum += priority_dict.get(letter)
                    break
                checked_letters.add(letter)
    return priority_sum

# could be improved by using set intersection, as the size of each string is different


def get_badge_priority_sum(lines, priority_dict):
    priority_sum = 0
    for i in range(0, len(lines)-2, 3):
        first_bag, second_bag, third_bag = lines[i].strip(), set(
            lines[i+1].strip()), set(lines[i+2].strip())
        checked_letters = set()
        for letter in first_bag:
            if not letter in checked_letters:
                if letter in second_bag and letter in third_bag:
                    priority_sum += priority_dict.get(letter)
                    break
                checked_letters.add(letter)
    return priority_sum


lines = open("./inputs/day3-input.txt", "r").readlines()
print('Q1:', get_priority_sum(lines, get_priority_dict()))
print('Q2:', get_badge_priority_sum(lines, get_priority_dict()))
