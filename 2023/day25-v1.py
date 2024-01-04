from itertools import combinations
import copy

def parse(lines):
    wire_dict = {}
    components = set()
    for line in lines:
        line = line.replace('\n','')
        component = line.split(':')[0]
        connections = set(line.split(':')[1][1:].split(' '))

        components.add(component)

        if component in wire_dict:
            for connection in connections:
                wire_dict[component].add(connection)
        else:
            wire_dict[component] = connections

        for connection in connections:
            components.add(connection)
            if connection in wire_dict:
                wire_dict[connection].add(component)
            else:
                wire_dict[connection] = set([component])
    return wire_dict, components


def bfs(graph, start, len_components):
    queue = [(start, [start])]
    while queue:
        current_node, path = queue.pop(0)
        for neighbour in graph[current_node]:
            if neighbour == start and len(path) == len_components:
                return False, len(path), path
            if neighbour not in path:
                new_path = path.copy()
                new_path.append(neighbour)
                queue.append((neighbour, new_path))
        
        if len(queue) == 0:
            return True, len(path), path
    return False, -1, []


def remove_edges(graph, edges):
    graph_copy = copy.deepcopy(graph)
    for edge in edges:
        graph_copy[edge[0]].remove(edge[1])
    return graph_copy


def iterate_graph_configurations(graph):
    all_edges = [(node, neighbor) for node, neighbors in graph.items() for neighbor in neighbors]
    
    for edges_to_remove in combinations(all_edges, 3):
        modified_graph = remove_edges(graph, edges_to_remove)
        yield modified_graph


def part1(lines):
    wire_dict, components = parse(lines)
    for component in components:
        print(component)
        configs = iterate_graph_configurations(wire_dict)
        for idx, config in enumerate(configs, start=1):
            result = bfs(config, component, len(components))
            if result[0]:
                print(result)
                return result[1] * (len(components) - result[1])
    return -1


def part2(lines):
    return

lines = open("./inputs/day25-input.txt", "r").readlines()
print("Q1:", part1(lines))
print("Q2:", part2(lines))