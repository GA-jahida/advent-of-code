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
        start = max(0, char_index - number_length - 1)
        for char in line[start: char_index + 1]:
            if not (char.isnumeric() or char == "."):
                return True
    return False

def get_sum_product_gears(lines):
    sum_product_gears = 0
    for line_index, line in enumerate(lines):
        line = line.replace("\n", "")
        current_number = ""
        for char_index, char in enumerate(line):
            if char == "*":
                start = max(0, line_index - 1)
                get_adjacent_numbers(lines[start : line_index + 2], line_index, char_index)

    return sum_product_gears


def get_adjacent_numbers(lines, line_index, char_index):
    numbers_dict = {
        0: [""]
    }
    for line_index, line in enumerate(lines):
        start = max(0, char_index - 1)
        print(line[start: char_index + 2])
        i = 0
        numbers_dict[line_index] = [""]
        for char in line[start: char_index + 2]:
            if char.isnumeric():
                counter = 0
                print(char, line[char_index + counter - start + 1])
                while line[char_index + counter].isnumeric() and len(line) - 1 >= char_index:
                    numbers_dict[line_index][i] += char
                    counter += 1
            else:
                numbers_dict[line_index].append("")
                i += 1
        
        # print(numbers_dict)
    return False


def part1(lines):
    return get_sum_engine_schematic(lines)


def part2(lines):
    return get_sum_product_gears(lines)


lines = open("./inputs/day3-input.txt", "r").readlines()
print("Q1:", part1(lines))
print("Q2:", part2(lines))
