def get_signal_strength_sum(lines):
    signal_strength_sum = 0
    cycle = 1
    x = 1
    for line in lines:
        instruction = line.replace("\n", "").split(" ")
        cycle += 1
        if instruction[0] == "addx":
            cycle += 1
            x += int(instruction[1])
        if cycle % 40 == 20:
            signal_strength_sum += x * cycle
        elif cycle % 40 == 21:
            signal_strength_sum += (x - int(instruction[1])) * (cycle - 1)
    return signal_strength_sum


def get_crt_image(lines):
    cycle = 1
    crt_position = 0
    x = 1
    string_image = "##"
    for line in lines:
        instruction = line.replace("\n", "").split(" ")
        cycle += 1
        crt_position += 1
        string_image, crt_position = handle_string_drawing(x, crt_position, string_image)
        if instruction[0] == "addx":
            cycle += 1
            crt_position += 1
            x += int(instruction[1])
            string_image, crt_position = handle_string_drawing(x, crt_position, string_image)
    return string_image


def handle_string_drawing(x, crt_position, string_image):
    if crt_position == 40:
        crt_position = 0
        string_image += "\n"
    if x - 1 <= crt_position <= x + 1:
        string_image += "#"
    else:
        string_image += "."
    return string_image, crt_position


lines = open("./inputs/day10-input.txt", "r").readlines()

print("Q1:", get_signal_strength_sum(lines))
print("Q2:")
print(get_crt_image(lines))
