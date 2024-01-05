import heapq
import copy

def parse(lines):
    for i, line in enumerate(lines):
        lines[i] = line.replace("\n", "").strip()
    grid = [[x for x in line[1:len(line)-1]] for line in lines]
    return grid


def parse_2(lines):
    for i, line in enumerate(lines):
        lines[i] = line.replace('>', '.').replace('<', '.').replace('^', '.').replace('v', '.').replace("\n", "").strip()
    grid = [[x for x in line[1:len(line)-1]]for line in lines]
    return grid


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
    grid = parse_2(lines)
    max_steps, path = dfs(grid, (0,0), (len(grid) - 1, len(grid[0]) - 1))
    return max_steps

lines = open("./inputs/day23-input.txt", "r").readlines()
print("Q1:", part1(lines))
print("Q2:", part2(lines))