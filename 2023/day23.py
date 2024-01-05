import heapq
import copy

def parse(lines):
    for i, line in enumerate(lines):
        lines[i] = line.replace("\n", "").strip()
    grid = [[x for x in line[1:len(line)-1]] for line in lines]
    return grid


def parse_2(lines):
    graph = {}
    for i, line in enumerate(lines):
        lines[i] = line.replace('>', '.').replace('<', '.').replace('^', '.').replace('v', '.').replace("\n", "").strip()
    grid = [[x for x in line[1:len(line)-1]] for line in lines]
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            graph[(i, j)] = []
            if i + 1 < len(lines) and lines[i+1][j] == '.':
                graph[(i, j)].append((i+1, j))
            if i - 1 >= 0 and lines[i-1][j] == '.':
                graph[(i, j)].append((i-1, j))
            if j + 1 < len(line) and lines[i][j+1] == '.':
                graph[(i, j)].append((i, j+1))
            if j - 1 >= 0 and lines[i][j-1] == '.':
                graph[(i, j)].append((i, j-1))
    return graph


def dfs(grid, start, end):
    queue = [(0, start, [start])]
    max_steps = 0
    max_path = []
    while queue:
        steps, node, path = heapq.heappop(queue)
        x, y = node
        if node == end and -steps > max_steps:
            max_steps = -steps
            max_path = path
        else:
            if grid[x][y] in ['>', '<', '^', 'v']:
                match grid[x][y]:
                    case '>':
                        if y + 1 < len(grid[0]) and grid[x][y + 1] != '#' and (x, y + 1) not in path:
                            heapq.heappush(queue, (steps - 1, (x, y + 1), path + [(x, y + 1)]))
                    case '<':
                        if y - 1 >= 0 and grid[x][y - 1] != '#' and (x, y - 1) not in path:
                            heapq.heappush(queue, (steps - 1, (x, y - 1), path + [(x, y - 1)]))
                    case '^':
                        if x - 1 >= 0 and grid[x - 1][y] != '#' and (x - 1, y) not in path:
                            heapq.heappush(queue, (steps - 1, (x - 1, y), path + [(x - 1, y)]))
                    case 'v':
                        if x + 1 < len(grid) and grid[x + 1][y] != '#' and (x + 1, y) not in path:
                            heapq.heappush(queue, (steps - 1, (x + 1, y), path + [(x + 1, y)]))
            else:
                if x + 1 < len(grid) and grid[x + 1][y] != '#' and (x + 1, y) not in path:
                    heapq.heappush(queue, (steps - 1, (x + 1, y), path + [(x + 1, y)]))
                if x - 1 >= 0 and grid[x - 1][y] != '#' and (x - 1, y) not in path:
                    heapq.heappush(queue, (steps - 1, (x - 1, y), path + [(x - 1, y)]))
                if y + 1 < len(grid[0]) and grid[x][y + 1] != '#' and (x, y + 1) not in path:
                    heapq.heappush(queue, (steps - 1, (x, y + 1), path + [(x, y + 1)]))
                if y - 1 >= 0 and grid[x][y - 1] != '#' and (x, y - 1) not in path:
                    heapq.heappush(queue, (steps - 1, (x, y - 1), path + [(x, y - 1)]))
    return max_steps, max_path
                

def dfs_graph(graph, start, end):
    queue = [(0, start, [start])]
    max_steps = 0
    max_path = []
    while queue:
        steps, node, path = heapq.heappop(queue)
        x, y = node
        if node == end and -steps > max_steps:
            max_steps = -steps
            print(max_steps - 1)
            max_path = path
        else:
            for neighbour in graph[node]:
                if neighbour not in path:
                    heapq.heappush(queue, (steps - 1, neighbour, path + [neighbour]))
    return max_steps, max_path

def visualise(path, grid):
    for node in path:
        grid[node[0]][node[1]] = 'O'
    for line in grid:
        print(''.join(line))

def part1(lines):
    grid = parse(lines)
    max_steps, path = dfs(grid, (0,0), (len(grid) - 1, len(grid[0]) - 1))
    return max_steps


def part2(lines):
    graph = parse_2(lines)
    max_steps, path = dfs_graph(graph, (0,0), (len(lines) - 1, len(lines[0]) - 2))
    return max_steps - 1

lines = open("./inputs/day23-input.txt", "r").readlines()
print("Q1:", part1(lines))
print("Q2:", part2(lines))