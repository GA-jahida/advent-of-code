def get_sum_extrapolated_values(lines):
    for line in lines:
        sequence = line.strip().split(" ")
        sequence = [int(x) for x in sequence]
        diff = get_diff_sequence(sequence)
        print(diff)


def get_diff_sequence(sequence):
    print(sequence)
    difference = []
    for index in range (0, len(sequence) - 1):
        diff = sequence[index + 1] - sequence[index]
        difference.append(diff)

    if len(set(difference)) == 1:
        return difference[0]
    else:
        updated_sequence = sequence.append(sequence[-1] + get_diff_sequence(difference))
    
    return updated_sequence[-1]

def part1(lines):
   return get_sum_extrapolated_values(lines)


def part2(lines):
    return

lines = open("./inputs/day9-input.txt", "r").readlines()
print("Q1:", part1(lines))
print("Q2:", part2(lines))