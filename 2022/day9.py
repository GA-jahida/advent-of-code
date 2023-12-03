def get_total_visited(lines, tail_length):
    position_array = [[0, 0] for x in range(tail_length + 1)]
    visited = set({(0, 0)})
    for line in lines:
        instruction = line.replace("\n", "").split(" ")
        for i in range(int(instruction[1])):
            match instruction[0]:
                case "U":
                    position_array[0][0] += 1
                case "D":
                    position_array[0][0] -= 1
                case "L":
                    position_array[0][1] -= 1
                case "R":
                    position_array[0][1] += 1
            for i in range(0, len(position_array) - 1):
                update_position(position_array[i], position_array[i + 1],
                                visited, i == len(position_array) - 2)
    return len(visited)


def update_position(head_position, tail_position, visited, add_to_visited):
    row_diff = head_position[0] - tail_position[0]
    col_diff = head_position[1] - tail_position[1]

    if abs(row_diff) > 1 or abs(col_diff) > 1:
        if head_position[0] == tail_position[0]:
            tail_position[1] += col_diff/abs(col_diff)
        elif head_position[1] == tail_position[1]:
            tail_position[0] += row_diff/abs(row_diff)
        else:
            tail_position[0] += row_diff/abs(row_diff)
            tail_position[1] += col_diff/abs(col_diff)
            row_diff = head_position[0] - tail_position[0]
            col_diff = head_position[1] - tail_position[1]

        if add_to_visited:
            visited.add((tail_position[0], tail_position[1]))


lines = open("./inputs/day9-input.txt", "r").readlines()

print("Q1:", get_total_visited(lines, 1))
print("Q2:", get_total_visited(lines, 9))
