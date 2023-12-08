import ast


def get_sum_pairs(lines):
    sum_pairs = 0
    for i in range(0, len(lines) - 1, 3):
        left = ast.literal_eval(lines[i].replace("\n",""))
        right = ast.literal_eval(lines[i+1].replace("\n",""))
        if is_right_order(left, right) == 1:
            sum_pairs += (i//3) + 1
    return sum_pairs

def is_right_order(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right: 
            return 1
        elif left > right:
            return -1
        else:
            return 0
    if isinstance(left, list) and isinstance(right, list):
        for index, value in enumerate(left):
            if index < len(right):
                x = is_right_order(value, right[index])
                if not x == 0:
                    return x
            if index == len(right):
                return -1
        if len(left) == len(right):
            return 0
        return 1
    if isinstance(left, list):
        return is_right_order(left, [right])
    if isinstance(right, list):
        return is_right_order([left], right)    
        
def decode(lines):
    first_index = 1
    second_index = 2
    for line in lines:
        if line.strip() != "":
            left = ast.literal_eval(line.replace("\n",""))
            if is_right_order(left, [[2]]) == 1:
                first_index += 1
                second_index += 1
            elif is_right_order(left, [[6]]) == 1:
                second_index += 1
    return first_index * second_index

def part1(lines):
    return get_sum_pairs(lines)


def part2(lines):
    return decode(lines)

lines = open("./inputs/day13-input.txt", "r").readlines()
print("Q1:", part1(lines))
print("Q2:", part2(lines))