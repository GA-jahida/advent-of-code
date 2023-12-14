def parse(lines):
    rows = []
    current_row = []
    for line in lines:
        if line.strip() == '':
            rows.append(current_row)
            current_row = []
        else:
            current_row.append(line.replace('\n', ''))
    
    cols = []
    for pattern_index, pattern in enumerate(rows):
        cols.append(['' for x in range(len(pattern[0]))])
        for line in pattern:
            for index, char in enumerate(line):
                cols[pattern_index][index] += char

    return rows, cols

def get_summary(rows, cols):
    summary = 0
    for pattern in rows:
       summary += 100 * check_reflection(pattern)
    
    for pattern in cols:
        summary += check_reflection(pattern)
    return summary

def check_reflection(pattern):
    for index in range(len(pattern) - 1):
        if pattern[index] == pattern[index + 1]:
            counter = 1
            if index == 0 or index + 1 == len(pattern) - 1:
                return index + 1
            while index - counter >= 0 and index + counter + 1 < len(pattern):
                if pattern[index - counter] != pattern[index + counter + 1]:
                    break
                if index - counter == 0 or index + counter + 1 == len(pattern) - 1:
                    return index + 1
                counter += 1
    return 0

def get_summary_difference(rows, cols):
    summary = 0
    for pattern in rows:
       summary += 100 * check_reflection_difference(pattern)
    
    for pattern in cols:
        summary += check_reflection_difference(pattern)
    return summary

def check_reflection_difference(pattern):
    for index in range(len(pattern) - 1):
        required_smudges = 0
        for i in range(len(pattern[index])):
            if pattern[index][i] != pattern[index + 1][i]:
                required_smudges += 1
        if required_smudges <= 1:
            counter = 1
            while index - counter >= 0 and index + counter + 1 < len(pattern):
                for i in range(len(pattern[index - counter])):
                    if pattern[index - counter][i] != pattern[index + counter + 1][i]:
                        required_smudges += 1
                if required_smudges == 1 and (index - counter == 0 or index + counter + 1 == len(pattern) - 1):
                    return index + 1
                counter += 1
            if (index == 0 or index + 1 == len(pattern) - 1) and required_smudges == 1:
                return index + 1
    return 0

def part1(lines):
    rows, cols = parse(lines)
    return get_summary(rows, cols)


def part2(lines):
    rows, cols = parse(lines)
    return get_summary_difference(rows, cols)


lines = open("./inputs/day13-input.txt", "r").readlines()
print("Q1:", part1(lines))
print("Q2:", part2(lines))