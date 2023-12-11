import sys
sys.setrecursionlimit(10000000)
def get_rock_matrix(lines):
    min_right = None
    max_right = None
    min_down = None
    max_down = None
    for line in lines:
        coords = line.strip().split(" -> ")
        for coord in coords:
            right = int(coord.split(",")[0])
            down = int(coord.split(",")[1])
            if min_right is None or right < min_right:
                min_right = right
            if max_right is None or right > max_right:
                max_right = right
            if min_down is None or down < min_down:
                min_down = down
            if max_down is None or down > max_down:
                max_down = down          
    matrix = [[0 for x in range(min_right, max_right + 1)] for y in range(0, max_down + 1)]

    for line in lines:
        coords = line.strip().split(" -> ")
        for coord_index in range(0, len(coords) - 1):
            right = int(coords[coord_index].split(",")[0])
            down = int(coords[coord_index].split(",")[1])
            next_right = int(coords[coord_index + 1].split(",")[0])
            next_down = int(coords[coord_index + 1].split(",")[1])
            for i in range(min(right, next_right), max(right + 1, next_right + 1)):
                matrix[down][i - min_right] = 1
            for i in range(min(down, next_down), max(down + 1, next_down + 1)):
                matrix[i][right - min_right] = 1
    return matrix, min_right

def get_sand_matrix(rock_matrix, sand_position, min_right, sum_sand):
    if sand_position[0] + 1 < len(rock_matrix) and sand_position[1] + 1 < len(rock_matrix[0]) and sand_position[1] - 1 >= 0:
        if rock_matrix[sand_position[0] + 1][sand_position[1]] == 0:
            sand_position = [sand_position[0] + 1, sand_position[1]]
            return get_sand_matrix(rock_matrix, sand_position, min_right, sum_sand)
        elif rock_matrix[sand_position[0] + 1][sand_position[1] - 1] == 0:
            sand_position = [sand_position[0] + 1, sand_position[1] - 1]
            return get_sand_matrix(rock_matrix, sand_position, min_right, sum_sand)
        elif rock_matrix[sand_position[0] + 1][sand_position[1] + 1] == 0:
            sand_position = [sand_position[0] + 1, sand_position[1] + 1]
            return get_sand_matrix(rock_matrix, sand_position, min_right, sum_sand)
        else:
            sum_sand += 1
            rock_matrix[sand_position[0]][sand_position[1]] = 2
            return get_sand_matrix(rock_matrix, [0, 500 - min_right], min_right, sum_sand)
    return rock_matrix, sum_sand

def get_sand_matrix_2(rock_matrix, sand_position, min_right, sum_sand):
    if rock_matrix[0][500 - min_right] != 2:
        if  sand_position[1] + 1 < len(rock_matrix[0]) and sand_position[1] - 1 >= 0:  
            if rock_matrix[sand_position[0] + 1][sand_position[1]] == 0:
                sand_position = [sand_position[0] + 1, sand_position[1]]
                return get_sand_matrix_2(rock_matrix, sand_position, min_right, sum_sand)
            elif rock_matrix[sand_position[0] + 1][sand_position[1] - 1] == 0:
                sand_position = [sand_position[0] + 1, sand_position[1] - 1]
                return get_sand_matrix_2(rock_matrix, sand_position, min_right, sum_sand)
            elif rock_matrix[sand_position[0] + 1][sand_position[1] + 1] == 0:
                sand_position = [sand_position[0] + 1, sand_position[1] + 1]
                return get_sand_matrix_2(rock_matrix, sand_position, min_right, sum_sand)
            else:
                sum_sand += 1
                rock_matrix[sand_position[0]][sand_position[1]] = 2
                return get_sand_matrix_2(rock_matrix, [0, 500 - min_right], min_right, sum_sand)
        else:
            for index, row in enumerate(rock_matrix):
                if index == len(rock_matrix) - 1:
                    row.append(1)
                    row.insert(0, 1)
                else:
                    row.append(0)
                    row.insert(0, 0)
            return get_sand_matrix_2(rock_matrix, [0, 500 - min_right + 1], min_right - 1, sum_sand)
    return rock_matrix, sum_sand

def part1(lines):
    rock_matrix, min_right = get_rock_matrix(lines)
    final_matrix, sum_sand = get_sand_matrix(rock_matrix, [0, 500 - min_right], min_right, 0)
    return sum_sand


def part2(lines):
    rock_matrix, min_right = get_rock_matrix(lines)
    rock_matrix.append([0 for x in rock_matrix[0]])
    rock_matrix.append([1 for x in rock_matrix[0]])
    final_matrix, sum_sand = get_sand_matrix_2(rock_matrix, [0, 500 - min_right], min_right, 0)
    return sum_sand

lines = open("./inputs/day14-input.txt", "r").readlines()
print("Q1:", part1(lines))
print("Q2:", part2(lines))