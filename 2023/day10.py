import sys
sys.setrecursionlimit(10000)

pipe_connection_dict = {
    "|": {
        (-1, 0): ['7', 'F', 'S', '|'],
        (1, 0): ['L', 'J', 'S', '|']
    },
    "-": {
        (0, -1): ['L', 'F', 'S', '-'],
        (0, 1): ['J', '7', 'S', '-']
    },
    "L": {
        (-1, 0): ['7', 'F', 'S', '|'],
        (0, 1): ['J', '7', 'S', '-']
    },
    "J": {
        (-1, 0): ['7', 'F', 'S', '|'],
        (0, -1): ['L', 'F', 'S', '-'],
    },
    "7": {
        (0, -1): ['L', 'F', 'S', '-'],
        (1, 0): ['L', 'J', 'S', '|']
    },
    "F": {
        (0, 1): ['J', '7', 'S', '-'],
        (1, 0): ['L', 'J', 'S', '|']
    },
    "S": {
        (-1, 0): ['7', 'F', 'S', '|'],
        (1, 0): ['L', 'J', 'S', '|'],
        (0, -1): ['L', 'F', 'S', '-'],
        (0, 1): ['J', '7', 'S', '-']
    }
}

def get_pipe_dict(lines):
    pipe_dict = {}
    start_index = None
    for line_index, line in enumerate(lines):
        lines[line_index] = line.replace("\n", "")
        if line.find('S') != -1:
            start_index = (line_index, line.find('S'))
    for line_index, line in enumerate(lines):
        for char_index, char in enumerate(line):
            pipe_dict[line_index, char_index] = []
            if char != ".":
                for key, value in pipe_connection_dict[char].items():
                    if line_index + key[0] < len(lines) and char_index + key[1] < len(line):
                        if lines[line_index + key[0]][char_index + key[1]] in value:
                            pipe_dict[line_index, char_index].append((line_index + key[0], char_index + key[1]))
    return pipe_dict, start_index


def get_farthest_point(pipe_dict, paths):
    path_ends = set()
    for path in paths:
        path_ends_len = len(path_ends)
        path_ends.add(path[-1])
        if len(path_ends) == path_ends_len:
            return len(path) - 1, paths
    new_paths = []
    for path in paths:
        a = pipe_dict[path[-1]]
        for pipe in pipe_dict[path[-1]]:
            if pipe not in path:
                new_paths.append(path + [pipe])
    
    return get_farthest_point(pipe_dict, new_paths)


def get_min_max(paths):
    min_node = None
    max_node = None
    for path in paths:
        for pipe in path:
            if min_node is None or (pipe[0] <= min_node[0] and pipe[1] <= min_node[1]):
                min_node = pipe
            if max_node is None or (pipe[0] >= max_node[0] and pipe[1] >= max_node[1]):
                max_node = pipe  
    return min_node, max_node

def get_pipe_matrix(path, lines):
    pipe_matrix = []
    for line_index, line in enumerate(lines):
        lines[line_index] = line.replace("\n", "")
        pipe_matrix.append([])
    for line_index, line in enumerate(lines):
        for char_index, char in enumerate(line):
            if (line_index, char_index) in path:
                pipe_matrix[line_index].append(char)
            else:
                pipe_matrix[line_index].append(0)
    return pipe_matrix


def is_enclosed(matrix, row, col):
    pipes_to_check = []
    hits = 0
    while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
        if matrix[row][col] in ['|', 'L', 'J', 'S'] :
            hits += 1
        row += 0
        col += +1
    return hits % 2 == 1


def part1(lines):
    pipe_dict, start_node = get_pipe_dict(lines)
    return get_farthest_point(pipe_dict, [[start_node]])[0]


def part2(lines):
    pipe_dict, start_node = get_pipe_dict(lines)
    paths = get_farthest_point(pipe_dict, [[start_node]])[1]
    pipe_matrix = get_pipe_matrix({pipe for path in paths for pipe in path}, lines)
    enclosed_zeros = []
    for i in range(len(pipe_matrix)):
        for j in range(len(pipe_matrix[0])):
            if pipe_matrix[i][j] == 0 and is_enclosed(pipe_matrix, i, j):
                enclosed_zeros.append((i, j))
    return len(enclosed_zeros)


lines = open("./inputs/day10-input.txt", "r").readlines()
print("Q1:", part1(lines))
print("Q2:", part2(lines))