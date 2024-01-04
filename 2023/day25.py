from itertools import combinations
import copy
import heapq
import random

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


def bfs(graph, pair, len_components):
    queue = [(pair[0], [pair[0]])]
    visited = set()
    while queue:
        current_node, path = heapq.heappop(queue)
        for neighbour in graph[current_node]:
            if neighbour == pair[1]:
                path.append(neighbour)
                return path
            if neighbour not in visited:
                visited.add(neighbour)
                new_path = path.copy()
                new_path.append(neighbour)
                heapq.heappush(queue, (neighbour, new_path))
        if len(queue) == 0:
            return path
    return []


def bfs_2(graph, pair, len_components):
    queue = [(pair[0], [pair[0]])]
    visited = set()
    while queue:
        current_node, path = heapq.heappop(queue)
        for neighbour in graph[current_node]:
            if neighbour not in path:
                visited.add(neighbour)
                new_path = path.copy()
                new_path.append(neighbour)
                heapq.heappush(queue, (neighbour, new_path))
        if len(queue) == 0:
            return path
    return []

def dfs(graph, pair, len_components):
    queue = [(-1, pair[0], [pair[0]])]
    while queue:
        _, current_node, path = heapq.heappop(queue)
        for neighbour in graph[current_node]:
            if neighbour not in path:
                new_path = path.copy()
                new_path.append(neighbour)
                heapq.heappush(queue, (-len(new_path), neighbour, new_path))
        if len(queue) == 0:
            return path
    return []


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


def get_combinations(components):
    for edges in combinations(components, 2):
        yield edges


def get_tally(components):
    pairs = get_combinations(components)
    tally = {}
    for pair in pairs:
        key = tuple(sorted([pair[0], pair[1]]))
        tally[key] = 0
    return tally


def get_random_combination(components):
    combo_list = list(combinations(components, 2))
    while True:
        yield random.choice(combo_list)


def part1(lines):
    wire_dict, components = parse(lines)
    random_pair_generator = get_random_combination(components)
    for _ in range(3):
        j = 0
        tally = get_tally(components)
        for _ in range(300):
            pair = next(random_pair_generator)
            path = bfs(wire_dict, pair, len(components))
            for i in range(len(path) - 1):
                key = tuple(sorted([path[i], path[i+1]]))
                tally[key] += 1
            j += 1
        wire_to_remove = sorted(tally, key=tally.get, reverse=True)
        print(wire_to_remove[0])
        wire_dict[wire_to_remove[0][0]].discard(wire_to_remove[0][1])
        wire_dict[wire_to_remove[0][1]].discard(wire_to_remove[0][0])

    # wires_to_remove = [('hfx', 'pzl'), ('bvb', 'cmg'), ('nvd', 'jqt')]

    # for wire_to_remove in wires_to_remove:
    #     wire_dict[wire_to_remove[0]].discard(wire_to_remove[1])
    #     wire_dict[wire_to_remove[1]].discard(wire_to_remove[0])

    path = bfs_2(wire_dict, ('jqt', 'jqt'), len(components))
    print(path)
    return len(set(path)) * (len(components) - len(set(path)))


def part2(lines):
    return

lines = open("./inputs/day25-input.txt", "r").readlines()
print("Q1:", part1(lines)) #543256
print("Q2:", part2(lines))