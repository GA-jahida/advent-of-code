def get_sum_engine_schematic(lines):
    sum_engine_schematic = 0
    for line_index, line in enumerate(lines):
        line = line.replace("\n", "")
        current_number = ""
        for char_index, char in enumerate(line):
            if char.isnumeric():
                current_number += char
            if not char.isnumeric() or (char_index == len(line) - 1 and char.isnumeric()):
                if len(current_number) > 0:
                    start = max(0, line_index - 1)
                    if is_adjacent_symbol(lines[start : line_index + 2], line_index, char_index, len(current_number)):
                        sum_engine_schematic += int(current_number)
                current_number = ""
    return sum_engine_schematic


def is_adjacent_symbol(lines, line_index, char_index, number_length):
    for line in lines:
        line = line.replace("\n", "")
        start = max(0, char_index - number_length - 1)
        for char in line[start: char_index + 1]:
            if not (char.isnumeric() or char == "."):
                return True
    return False

def get_sum_product_gears(lines):
    sum_product_gears = 0
    for line_index, line in enumerate(lines):
        current_number = ""
        for char_index, char in enumerate(line):
            if char == "*":
                start = max(0, line_index - 1)
                sum_product_gears += get_adjacent_numbers(lines[start : line_index + 2], line_index, char_index)

    return sum_product_gears


def get_adjacent_numbers(lines, line_index, gear_index):
    numbers_dict = {
        0: {},
        1: {},
        2: {}
    }
    for line_index, line in enumerate(lines):
        start = max(0, gear_index - 1)
        i = 0
        for char_index in range(start, gear_index + 2):
            char = line[char_index]
            if char.isdigit():
                if i not in numbers_dict[line_index]:
                    numbers_dict[line_index][i] = ""
                numbers_dict[line_index][i] += char
                if char_index == start + 2:
                    count = 1
                    while line[char_index + count].isdigit():
                        numbers_dict[line_index][i] += line[char_index + count]
                        count += 1
                if char_index == start:
                    count = 1
                    while line[char_index - count].isdigit():
                        numbers_dict[line_index][i] = line[char_index - count] + numbers_dict[line_index][i]
                        count += 1
            else: 
                i += 1

    numbers_found = []
    for key, line_dict in numbers_dict.items():
        for key, number in line_dict.items():
            if number.isdigit():
               numbers_found.append(number)
    if len(numbers_found) == 2:
        return int(numbers_found[0]) * int(numbers_found[1])
    return 0


def part1(lines):
    return get_sum_engine_schematic(lines)


def part2(lines):
    return get_sum_product_gears(lines)


lines = open("./inputs/day3-input.txt", "r").readlines()
print("Q1:", part1(lines))
print("Q2:", part2(lines))
