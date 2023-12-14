def parse(lines):
    for line_index, line in enumerate(lines):
        lines[line_index] = line.replace('\n', '')
    matrix = [[0 for x in range(len(lines[0]))] for y in range(len(lines))]
    
    for line_index, line in enumerate(lines):
        for char_index, char in enumerate(line):
            matrix[line_index][char_index] = char
    
    return matrix

def tilt_north(matrix, cycles):
    for i in range(1, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == 'O':
                for k in range(i - 1, -2, -1):
                    if matrix[k][j] == '.':
                        matrix[i][j] = '.'
                    if matrix[k][j] == '#' or matrix[k][j] == 'O' or k == -1:
                        matrix[k+1][j] = 'O'
                        break
    return matrix

def tilt(matrix, direction):
    for i in range(1, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == 'O':
                if direction[1] == 0:
                    for k in range(i + direction[0], -2, direction[0]):
                        if matrix[k][j] == '.':
                            matrix[i][j] = '.'
                        if matrix[k][j] == '#' or matrix[k][j] == 'O' or k == -1:
                            matrix[k+1][j] = 'O'
                            break
                else:
                    for k in range(j + direction[1], -2, direction[1]):
                        if matrix[i][k] == '.':
                            matrix[i][j] = '.'
                        if matrix[i][k] == '#' or matrix[i][k] == 'O' or k == -1:
                            matrix[i][k+1] = 'O'
                            break
    return matrix

def calc_load(matrix):
    load = 0
    for line_index, line in enumerate(matrix):
        count_rocks = len([i for i in line if i=='O'])
        load += (len(matrix) - line_index) * count_rocks
    return load

def part1(lines):
    matrix = parse(lines)
    matrix = tilt_north(matrix, len(matrix)*100)
    return calc_load(matrix)


def part2(lines):
    matrix = parse(lines)
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    cycles = 0
    while cycles < 1000000000:
        for direction in directions:
            tilt(matrix, direction)
            cycles += 1
    return calc_load(matrix)


lines = open("./inputs/day14-input.txt", "r").readlines()
print("Q1:", part1(lines))
print("Q2:", part2(lines))
