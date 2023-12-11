def get_galaxy_positions(lines, expansion_value):
    galaxy_positions = []
    row_extra = 0
    for line_index, line in enumerate(lines):
        lines[line_index] = line.strip().replace('\n', '')
    for line_index, line in enumerate(lines):
        if '#' not in line:
            row_extra += expansion_value
            continue
        col_extra = 0
        for char_index, char in enumerate(line):
            if char == '.':
                for i in range(len(lines)):
                    if lines[i][char_index] == '#':
                        break
                    if i == len(lines) - 1:
                        col_extra += expansion_value
            else:
                galaxy_positions.append((line_index + row_extra, char_index + col_extra))
    return galaxy_positions
        

def manhattan_distance(galaxy_1, galaxy_2):
    x1, y1 = galaxy_1
    x2, y2 = galaxy_2
    return abs(x2 - x1) + abs(y2 - y1)


def get_sum_min_dist(galaxy_positions):
    sum_min_dist = 0
    for i in range(1, len(galaxy_positions)):
        sum_min_dist += manhattan_distance(galaxy_positions[0], galaxy_positions[i])
    return sum_min_dist


def part1(lines):
    galaxy_positions = get_galaxy_positions(lines, 1)
    sum_shortest_path = 0
    for i in range(len(galaxy_positions) - 1):
        sum_shortest_path += get_sum_min_dist(galaxy_positions[i:])
    return sum_shortest_path


def part2(lines):
    galaxy_positions = get_galaxy_positions(lines, 1000000-1)
    sum_shortest_path = 0
    for i in range(len(galaxy_positions) - 1):
        sum_shortest_path += get_sum_min_dist(galaxy_positions[i:])
    return sum_shortest_path


lines = open("./inputs/day11-input.txt", "r").readlines()
print("Q1:", part1(lines))
print("Q2:", part2(lines))