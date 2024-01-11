direction_map = {
    ((0,1), '|'): [(1,0), (-1,0)],
    ((0,-1), '|'): [(1,0), (-1,0)],
    ((1,0), '|'): [(1,0)],
    ((-1,0), '|'): [(-1,0)],
    ((0,1), '-'): [(0,1)],
    ((0,-1), '-'): [(0,-1)],
    ((1,0), '-'): [(0,1), (0,-1)],
    ((-1,0), '-'): [(0,1), (0,-1)],
    ((0,1), '\\'): [(1,0)],
    ((0,-1), '\\'): [(-1,0)],
    ((1,0), '\\'): [(0,1)],
    ((-1,0), '\\'): [(0,-1)],
    ((0,1), '/'): [(-1,0)],
    ((0,-1), '/'): [(1,0)],
    ((1,0), '/'): [(0,-1)],
    ((-1,0), '/'): [(0,1)],
}


def parse(lines):
    grid = [[x for x in line.replace("\n", "").strip()] for line in lines]
    return grid


def traverse(grid, start_node, start_direction):
    queue = [(start_node, start_direction)]
    visited = set()
    visited.add((start_node, start_direction))

    while queue:
        node, direction = queue.pop(0)
        x, y = node
        dx, dy = direction

        if not 0 <= x + dx < len(grid) or not 0 <= y + dy < len(grid[0]):
            continue

        while grid[x][y] == '.':
            visited.add(((x,y), direction))
            x += dx
            y += dy
            if not 0 <= x < len(grid) or not 0 <= y < len(grid[0]):
                break

        if not 0 <= x < len(grid) or not 0 <= y < len(grid[0]):
            continue

        new_directions = direction_map[direction, grid[x][y]]
        visited.add(((x, y), direction))

        for new_direction in new_directions:
            dx, dy = new_direction
            if ((x + dx, y + dy), new_direction) not in visited:
                visited.add(((x + dx, y + dy), new_direction))
                queue.append(((x + dx, y + dy), new_direction))

    return set([x for x,y in visited if 0 <= x[0] < len(grid) and 0 <= x[1] < len(grid[0])])


def visualise(grid, visited):
    for node in visited:
        x, y = node
        grid[x][y] = '#'
    for line in grid:
        print(''.join(line))


def part1(lines):
    grid = parse(lines)
    visited = traverse(grid, (0, 0), (0, 1))
    # visualise(grid, visited)
    return len(visited)


def part2(lines):
    grid = parse(lines)
    max_energy = 0
    for i in range(0, len(grid)):
        visited = traverse(grid, (i, 0), (0, 1))
        if len(visited) > max_energy:
            max_energy = len(visited)
    for i in range(0, len(grid)):
        visited = traverse(grid, (i, len(grid[0]) - 1), (0, -1))
        if len(visited) > max_energy:
            max_energy = len(visited)
    for i in range(0, len(grid[0])):
        visited = traverse(grid, (0, i), (1, 0))
        if len(visited) > max_energy:
            max_energy = len(visited)
    for i in range(0, len(grid[0])):
        visited = traverse(grid, (len(grid) - 1, i), (-1, 0))
        if len(visited) > max_energy:
            max_energy = len(visited)
    return max_energy


lines = open("./inputs/day16-input.txt", "r").readlines()
print("Q1:", part1(lines))
print("Q2:", part2(lines))