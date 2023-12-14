def parse(lines):
    for line_index, line in enumerate(lines):
        lines[line_index] = line.replace('\n', '')
    matrix = [[0 for x in range(len(lines[0]))] for y in range(len(lines))]
    
    for line_index, line in enumerate(lines):
        for char_index, char in enumerate(line):
            matrix[line_index][char_index] = char
    
    return matrix


def tilt_north(matrix, cycles):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == 'O':
                for k in range(i - 1, -2, -1):
                    if matrix[k][j] == '.':
                        matrix[i][j] = '.'
                    if matrix[k][j] == '#' or matrix[k][j] == 'O' or k == -1:
                        matrix[k+1][j] = 'O'
                        break
    return matrix


def calc_load(matrix):
    load = 0
    for line_index, line in enumerate(matrix):
        count_rocks = len([i for i in line if i=='O'])
        load += (len(matrix) - line_index) * count_rocks
    return load


def tilt_track_bottom(matrix, direction):
    if direction[1] == 0:
        if direction[0] == 1:
            bottom = [(0, x) for x in range(len(matrix[0]))] 
            start = 1
            end = len(matrix)
        else:
            bottom = [(len(matrix) - 1, x) for x in range(len(matrix[0]))] 
            start = len(matrix) - 1
            end = -1
        for i in range(start, end, direction[0]):
            for j in range(0, len(matrix[0])):
                if (i, j) == bottom[j]:
                    continue
                if matrix[i][j] == '#':
                    bottom[j] = (i, j)
                elif matrix[i][j] == 'O':
                    if matrix[bottom[j][0]][bottom[j][1]] == '.':
                        matrix[bottom[j][0]][bottom[j][1]] = 'O'
                        bottom[j] = (bottom[j][0] + direction[0], bottom[j][1] + direction[1])
                        matrix[i][j] = '.'
                    else:
                        bottom[j] = (bottom[j][0] + direction[0], bottom[j][1] + direction[1]) 
                        
                        matrix[i][j] = '.' 
                        matrix[bottom[j][0]][bottom[j][1]] = 'O'       
    else:
        if direction[1] == 1:
            bottom = [(x, 0) for x in range(len(matrix))] 
            start = 1
            end = len(matrix[0])
        else:
            bottom = [(x, len(matrix) - 1) for x in range(len(matrix))] 
            start = len(matrix[0]) - 1
            end = -1
        for j in range(start, end, direction[1]):
            for i in range(0, len(matrix)):
                if (i, j) == bottom[i]:
                    continue
                if matrix[i][j] == '#':
                    bottom[i] = (i, j)
                elif matrix[i][j] == 'O':
                    if matrix[bottom[i][0]][bottom[i][1]] == '.':
                        matrix[bottom[i][0]][bottom[i][1]] = 'O'
                        bottom[i] = (bottom[i][0] + direction[0], bottom[i][1] + direction[1])
                        matrix[i][j] = '.'
                    else:
                        bottom[i] = (bottom[i][0] + direction[0], bottom[i][1] + direction[1]) 
                        matrix[i][j] = '.' 
                        matrix[bottom[i][0]][bottom[i][1]] = 'O'
    return matrix


def matrix_to_set(matrix):
    return tuple(tuple(row) for row in matrix)

def run_cycles(max_cycles, matrix):
    matrix_set = set()
    cycles = 0
    required_cycles = None
    loads = []
    while cycles < max_cycles and required_cycles is None:
        set_length = len(matrix_set)
        matrix = run_cycle(matrix)
        matrix_set.add(matrix_to_set(matrix))
        loads.append(calc_load(matrix))
        cycles += 1
        if len(matrix_set) == set_length:
            required_cycles = cycles

    cycle_end = len(loads)
    loads = []
    matrix_set = set()
    for i in range(required_cycles * 2):
        set_length = len(matrix_set)
        matrix = run_cycle(matrix)
        matrix_set.add(matrix_to_set(matrix))
        loads.append(calc_load(matrix))
        if len(matrix_set) == set_length:
            break
        
    return cycle_end - len(loads), len(loads) - 1


def run_cycle(matrix):
    directions = [(1, 0),(0, 1), (-1, 0), (0, -1)]
    for direction in directions:
        matrix = tilt_track_bottom(matrix, direction)
    return matrix


def part1(lines):
    matrix = parse(lines)
    matrix = tilt_north(matrix, len(matrix)*100)
    return calc_load(matrix)


def part2(lines):
    cycle_start, cycle_loop = run_cycles(1000000000, parse(lines))
    matrix = parse(lines)
    print(cycle_start, cycle_loop)
    print((1000000000 - cycle_start) % cycle_loop + cycle_start)
    for i in range((1000000000 - cycle_start) % cycle_loop + cycle_start):
        matrix = run_cycle(matrix)
    return calc_load(matrix)
  
 
lines = open("./inputs/day14-input.txt", "r").readlines()
print("Q1:", part1(lines))
print("Q2:", part2(lines))