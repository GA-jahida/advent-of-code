def get_sum_possible_games(lines, max_cubes_dict):
    possible_game_sum = 0
    for index, line in enumerate(lines):
        games = line.split(':')[1].split(';')
        possible_game = True
        for game in games:
            cubes = game.split(',')
            for cube in cubes:
                cube_colour = cube.strip().split(" ")
                if max_cubes_dict[cube_colour[1]] < int(cube_colour[0]):
                    possible_game = False
        if possible_game:
            possible_game_sum += index + 1
    return possible_game_sum

def part1(lines):
    max_cubes_dict = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    return get_sum_possible_games(lines, max_cubes_dict)

def get_power_sets_sum(lines):
    power_sets_sum = 0
    for index, line in enumerate(lines):
        games = line.split(':')[1].split(';')
        red_max, blue_max, green_max = 0, 0, 0
        for game in games:
            cubes = game.split(',')
            for cube in cubes:
                cube_colour = cube.strip().split(" ")
                match cube_colour[1]:
                    case "blue":
                        if int(cube_colour[0]) > blue_max:
                            blue_max = int(cube_colour[0])
                    case "red":
                        if int(cube_colour[0]) > red_max:
                            red_max = int(cube_colour[0])
                    case "green":
                        if int(cube_colour[0]) > green_max:
                            green_max = int(cube_colour[0])
        print(red_max, green_max, blue_max, blue_max * green_max * red_max)
        power_sets_sum += blue_max * green_max * red_max
    return power_sets_sum

def part2(lines):
    return get_power_sets_sum(lines)

lines = open("./inputs/day2-input.txt", "r").readlines()
print("Q1:", part1(lines))
print("Q2:", part2(lines))