# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

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
        (-1, 0): ['7', 'F', 'S', '|'],
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

def parse(lines):
    pipe_dict = {}
    for line_index, line in enumerate(lines):
        lines[line_index] = line.replace("\n", "")
    for line_index, line in enumerate(lines):
        for char_index, char in enumerate(line):
            pipe_dict[line_index, char_index] = []
            if char != ".":
                for key, value in pipe_connection_dict[char].items():
                    if lines[line_index + key[0]][char_index + key[1]] in value:
                        pipe_dict[line_index, char_index].append((line_index + key[0], char_index + key[1]))
    return pipe_dict


# def get_adjacent_pipes(pipes_array):


def part1(lines):
    return parse(lines)


def part2(lines):
    return


lines = open("./inputs/day10-input.txt", "r").readlines()
print("Q1:", part1(lines))
print("Q2:", part2(lines))