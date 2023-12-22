import numpy as np
import matplotlib.pyplot as plt
from collections import deque
from functools import cache
import asyncio


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


async def bfs_shortest_path_infinite(grid, start, max_steps, queue):
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


async def part2(lines):
    grid, start = parse(lines)
    queue = deque([(start, 0, start)])
    terms = []
    for i in range(0, 151, 1):
        queue = bfs_shortest_path_infinite(grid, start, i, queue)
        print(i, len(queue))
        terms.append(len(queue))
    print(terms)
    model = get_model(terms)
    return model(26501365)


def get_model(terms):
    x = [i for i in range(len(terms))]
    model = np.poly1d(np.polyfit(x, terms, 2))
    return model


lines = open("./inputs/day21-input.txt", "r").readlines()
print("Q1:", part1(lines)) # 3574
print("Q2:", asyncio.run(part2(lines))) # 600090522932119