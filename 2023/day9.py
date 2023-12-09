def get_sum_extrapolated_values(lines, reverse):
    sum_extrapolated_values = 0
    for line in lines:
        sequence = line.strip().split(" ")
        if reverse:
            sequence.reverse()
        sequence = [int(x) for x in sequence]
        sum_extrapolated_values += get_diff_sequence(sequence)
    return sum_extrapolated_values


def get_diff_sequence(sequence):
    difference = []
    for index in range(0, len(sequence) - 1):
        diff = sequence[index + 1] - sequence[index]
        difference.append(diff)
    if len(set(difference)) == 1:
        return sequence[-1] + difference[0]

    return sequence[-1] + get_diff_sequence(difference)


def part1(lines):
    return get_sum_extrapolated_values(lines, False)


def part2(lines):
    return get_sum_extrapolated_values(lines, True)


lines = open("./inputs/day9-input.txt", "r").readlines()
print("Q1:", part1(lines))
print("Q2:", part2(lines))
