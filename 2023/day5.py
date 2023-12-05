def get_min_location(lines, start_array, seeds):
    seed_to_soil = [[] for x in range(start_array[0], start_array[1]-2)]
    for i in range(start_array[0], start_array[1]-2):
        seed_to_soil[i - start_array[0]] = lines[i].strip().split(" ")

    soil_to_fertilizer = [[] for x in range(start_array[1], start_array[2]-2)]
    for i in range(start_array[1], start_array[2]-2):
        soil_to_fertilizer[i - start_array[1]] = lines[i].strip().split(" ")

    fertilizer_to_water = [[] for x in range(start_array[2], start_array[3]-2)]
    for i in range(start_array[2], start_array[3]-2):
        fertilizer_to_water[i - start_array[2]] = lines[i].strip().split(" ")

    water_to_light = [[] for x in range(start_array[3], start_array[4]-2)]
    for i in range(start_array[3], start_array[4]-2):
        water_to_light[i - start_array[3]] = lines[i].strip().split(" ")

    light_to_temp = [[] for x in range(start_array[4], start_array[5]-2)]
    for i in range(start_array[4], start_array[5]-2):
        light_to_temp[i - start_array[4]] = lines[i].strip().split(" ")        

    temp_to_humid = [[] for x in range(start_array[5], start_array[6]-2)]
    for i in range(start_array[5], start_array[6]-2):
        temp_to_humid[i - start_array[5]] = lines[i].strip().split(" ")

    humid_to_location = [[] for x in range(start_array[6], len(lines))]
    for i in range(start_array[6], len(lines)):
        humid_to_location[i - start_array[6]] = lines[i].strip().split(" ")

    min_location = None
    for seed in seeds:
        soil = map_number(seed_to_soil, int(seed))
        fertilizer = map_number(soil_to_fertilizer, soil)
        water = map_number(fertilizer_to_water, fertilizer)
        light = map_number(water_to_light, water)
        temp = map_number(light_to_temp, light)
        humid = map_number(temp_to_humid, temp)
        location = map_number(humid_to_location, humid)
        print(location)
        if min_location is None or location < min_location:
            min_location = location
    return min_location


def map_number(lists, number):
    for list in lists:
        if int(list[1]) + int(list[2]) > number >= int(list[1]):
            # print(number + int(list[0]) - int(list[1]))
            return number + int(list[0]) - int(list[1])
    # print(number)
    return number

def part1(lines):
    seeds = lines[0].replace("seeds: ", "").strip().split(" ")
    start_array = [3, 20, 35, 68, 92, 127, 173]
    # start_array = [3, 7, 12, 18, 22, 27, 31]
    return get_min_location(lines, start_array, seeds)


def part2(lines):
    start_array = [3, 7, 12, 18, 22, 27, 31]
    start_array = [3, 20, 35, 68, 92, 127, 173]
    seed_ranges = lines[0].replace("seeds: ", "").strip().split(" ")
    seeds = []
    for i in range(0, len(seed_ranges), 2):
        # seeds.append(int(seed_ranges[i]))
        # seeds.append(int(seed_ranges[i]) + int(seed_ranges[i+1]))
        # seeds.append(int(seed_ranges[i]) + int(seed_ranges[i+1]) - 1)
        # seeds.append((int(seed_ranges[i]) + int(seed_ranges[i+1]))//2)
        for j in range(int(seed_ranges[i]), int(seed_ranges[i]) + int(seed_ranges[i+1])):
            seeds.append(j)
    # print(seeds)
    return get_min_location(lines, start_array, seeds)

lines = open("./inputs/day5-input.txt", "r").readlines()
# print("Q1:", part1(lines))
print("Q2:", part2(lines))