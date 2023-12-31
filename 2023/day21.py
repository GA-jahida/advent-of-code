import numpy as np
from collections import deque
from functools import cache
import asyncio
from numpy.polynomial.polynomial import Polynomial
from math import ceil


directions =  [
    (1,0),
    (-1, 0),
    (0,1),
    (0,-1)
]


def parse(lines):
    start = 0
    grid = [[x for x in line.replace("\n", "").strip()] for line in lines]
    for line_index, line in enumerate(grid):
        if  'S' in line:
            for char_index, char in enumerate(line):
                if char == 'S':
                    start = (line_index, char_index)
    return grid, start


def bfs_shortest_path(grid, start, max_steps):
    queue = [(start, 0)]
    while queue:
        current_node, distance = queue.pop(0)

        if distance == max_steps:
            return len(set(queue)) + 1
        
        for direction in directions:
            x = current_node[0] + direction[0]
            y = current_node[1] + direction[1]
            if len(grid) > x >= 0 and len(grid[0]) > y >= 0:
                if grid[x][y] == '.' or grid[x][y] == 'S':
                    if ((x, y), distance + 1) not in queue:
                        queue.append(((x, y), distance + 1))
    return None


def bfs_shortest_path_infinite(grid, start, max_steps, queue):
    visited = set([start, 0])
    while queue:
        current_node, distance, coordinate = queue.popleft()

        if distance == max_steps:
            queue.append((current_node, distance, coordinate))
            return queue
        
        for direction in directions:
            cx = current_node[0] + direction[0]
            cy = current_node[1] + direction[1]
            if ((cx, cy), distance + 1) not in visited:
                visited.add(((cx, cy), distance + 1))
                x = cx % (len(grid))
                y = cy % (len(grid[0]))
                if grid[x][y] == '.' or grid[x][y] == 'S':
                    if ((cx, cy), distance + 1, (x,y)) not in queue:
                        queue.append(((cx, cy), distance + 1,(x,y)))
    return queue


def visualise(current_nodes, grid):
    for node in current_nodes:
        if grid[node[0]][node[1]] == '.' or grid[node[0]][node[1]] == 'S':
            grid[node[0]][node[1]] = 'O'
    for line in grid:
        print(''.join(line))


def part1(lines):
    grid, start = parse(lines)
    return bfs_shortest_path(grid, start, 6)


def part2(lines, steps):
    grid, start = parse(lines)
    queue = deque([(start, 0, start)])
    m = steps % len(grid)
    queue =  bfs_shortest_path_infinite(grid, start, m, queue)
    a0 = len(queue)
    queue = bfs_shortest_path_infinite(grid, start, m + len(grid), queue)
    a1 = len(queue)
    queue = bfs_shortest_path_infinite(grid, start, m + 2 * len(grid), queue)
    a2 = len(queue)

    model = get_model([a0, a1, a2])
    print(model(ceil(steps / len(grid))))

    quadratic_func = quadratic(a0, a1, a2)
    return quadratic_func(ceil(steps / len(grid)))


def quadratic(a0, a1, a2):
    first_diff = a1 - a0
    second_diff = a2 - a1
    third_diff = second_diff - first_diff

    A = third_diff // 2
    B = first_diff - 3 * A
    C = a0 - B - A
    return lambda n: A*n**2 + B*n + C


def get_model(terms):
    x = [i for i in range(len(terms))]
    model = np.poly1d(np.polyfit(x, terms, 2))
    return model


lines = open("./inputs/day21-input.txt", "r").readlines()
print("Q1:", part1(lines))
print("Q2:", part2(lines, 26501365))