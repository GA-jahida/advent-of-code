def product_records(times, distances):
    total = 1
    for index, time in enumerate(times):
        speed = 0
        ways_to_win = 0
        while int(time) - speed > 0:
            if (int(time) - speed) * speed > int(distances[index]):
                ways_to_win += 1
            speed += 1
        total = total * ways_to_win
    return total

def part1(lines):
    times = lines[0].replace("Time:", "").strip().split()
    distances = lines[1].replace("Distance:", " ").strip().split()
    return product_records(times, distances)


def part2(lines):
    times = lines[0].replace("Time:", "").replace(" ", "")
    distances = lines[1].replace("Distance:", " ").replace(" ", "")
    return product_records([times], [distances])

lines = open("./inputs/day6-input.txt", "r").readlines()
print("Q1:", part1(lines))
print("Q2:", part2(lines))