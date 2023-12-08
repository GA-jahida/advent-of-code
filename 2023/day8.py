import math

def get_graph_dict(lines):
    graph_dict = {}
    for line in lines:
        parts = line.strip().replace("(","").replace(")","").split(" = ")
        graph_dict[parts[0]] = (parts[1].split(", ")[0], parts[1].split(", ")[1])
    return graph_dict


def follow_instructions(instructions, graph_dict, current_node, end_func):
    steps = 0
    while end_func(current_node):
        for instruction in instructions:
            steps += 1
            if instruction == "L":
                current_node = graph_dict[current_node][0]
            else:
                current_node = graph_dict[current_node][1]
    return steps

def get_start_nodes(lines):
    start_nodes = []
    for line in lines:
        start_node = line.strip().replace("(","").replace(")","").split(" = ")[0]
        if start_node[2] == "A":
            start_nodes.append(start_node)
    return start_nodes

def part1(lines):
    instructions = lines[0].strip()
    graph_dict = get_graph_dict(lines[2:])
    return follow_instructions(instructions, graph_dict, 'AAA', lambda x: x != 'ZZZ')


def part2(lines):
    instructions = lines[0].strip()
    graph_dict = get_graph_dict(lines[2:])
    start_nodes = get_start_nodes(lines[2:])
    steps_list = []
    for start_node in start_nodes:
        steps = follow_instructions(instructions, graph_dict, start_node, lambda x: x[2] != 'Z')
        steps_list.append(steps)
    return math.lcm(*steps_list)

lines = open("./inputs/day8-input.txt", "r").readlines()
print("Q1:", part1(lines))
print("Q2:", part2(lines))