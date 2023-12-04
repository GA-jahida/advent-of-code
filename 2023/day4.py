def get_sum_points(lines):
    sum_points = 0
    for line in lines:
        card = line.split(":")[1].replace("\n", "").split("|")
        winning_numbers = set(card[0].strip().split(" "))
        selected_numbers = card[1].strip().split(" ")
        selected_winning_numbers = get_sum_winning_numbers(
            selected_numbers, winning_numbers)
        if selected_winning_numbers > 0:
            sum_points += pow(2, (selected_winning_numbers-1))
    return sum_points


def get_sum_winning_numbers(selected_numbers, winning_numbers):
    sum_winning_numbers = 0
    for number in selected_numbers:
        if number in winning_numbers:
            if number.isdigit():
                sum_winning_numbers += 1
    return sum_winning_numbers


def get_sum_copies(lines):
    copy_array = [1 for x in range(len(lines))]
    for line_index, line in enumerate(lines):
        card = line.split(":")[1].replace("\n", "").split("|")
        winning_numbers = set(card[0].strip().split(" "))
        selected_numbers = card[1].strip().split(" ")
        selected_winning_numbers = 0
        selected_winning_numbers = get_sum_winning_numbers(
            selected_numbers, winning_numbers)
        for i in range(1, selected_winning_numbers + 1):
            if line_index + i < len(lines):
                copy_array[line_index + i] += 1 * copy_array[line_index]
    return sum(copy_array)


def part1(lines):
    return get_sum_points(lines)


def part2(lines):
    return get_sum_copies(lines)


lines = open("./inputs/day4-input.txt", "r").readlines()
print("Q1:", part1(lines))
print("Q2:", part2(lines))
