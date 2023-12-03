def get_path_graph(lines):
    graph_dict = {}
    starting_position_array = []
    for line_index, line in enumerate(lines):
        line = line.replace("\n", "").strip()
        for char_index, char in enumerate(line):
            key = (line_index, char_index)
            if char == 'a':
                starting_position_array.append(key)
            graph_dict[key] = []
            char_value = letter_code(char)
            if char_index < len(line) - 1 and letter_code(line[char_index + 1]) <= char_value + 1:
                graph_dict[key].append((line_index, char_index + 1))
            if char_index > 0 and letter_code(line[char_index - 1]) <= char_value + 1:
                graph_dict[key].append((line_index, char_index - 1))
            if (line_index < len(lines) - 1 and
                    letter_code(lines[line_index + 1][char_index]) <= char_value + 1):
                graph_dict[key].append((line_index + 1, char_index))
            if line_index > 0 and letter_code(lines[line_index - 1][char_index]) <= char_value + 1:
                graph_dict[key].append((line_index - 1, char_index))
    return graph_dict, starting_position_array


def letter_code(char):
    if char == "E":
        return ord('z')
    if char == 'S':
        return ord('a')
    return ord(char)


def bfs_shortest_path(graph, start, end):
    queue = [(start, [start])]
    visited = set()
    while queue:
        current_node, path = queue.pop(0)
        if current_node == end:
            return path
        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph[current_node]:
                queue.append((neighbor, path + [neighbor]))
    return None


def part1(start, end):
    return len(bfs_shortest_path(get_path_graph(lines)[0], start, end)) - 1


def part2(end):
    min_length = None
    graph_dict, starting_position_array = get_path_graph(lines)
    for starting_position in starting_position_array:
        path = bfs_shortest_path(graph_dict, starting_position, end)
        if path and (min_length is None or len(path) - 1 < min_length):
            min_length = len(path) - 1
    return min_length


lines = open("./inputs/day12-input.txt", "r").readlines()

# 20 43 end
# 20 0 start
print("Q1:", part1((20, 0), (20, 43)))
print("Q2:", part2((20, 43)))
