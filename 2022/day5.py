def get_crate_dict(lines):
    crate_dict = {i: [] for i in range(1, NUMBER_OF_STACKS+1)}
    for i in range(CRATE_BOTTOM_LINE_NUMBER, -1, -1):
        for j in range(NUMBER_OF_STACKS, 0, -1):
            if lines[i][1+(j-1)*4].strip() != "":
                crate_dict[j].append(lines[i][1+(j-1)*4])
    return crate_dict


def get_crates_dict_rearranged(lines, crate_dict):
    for i in range(INSTRUCTIONS_START_LINE, len(lines), 1):
        instructions = lines[i].replace("\n", "").split(" ")
        crate_dict[int(instructions[5])].extend(
            reversed(crate_dict[int(instructions[3])][-int(instructions[1]):]))
        crate_dict[int(instructions[3])] = crate_dict[int(instructions[3])][:len(
            crate_dict[int(instructions[3])])-int(instructions[1])]
    return crate_dict


def get_crates_dict_rearranged_2(lines, crate_dict):
    for i in range(INSTRUCTIONS_START_LINE, len(lines), 1):
        instructions = lines[i].replace("\n", "").split(" ")
        crate_dict[int(instructions[5])].extend(
            crate_dict[int(instructions[3])][-int(instructions[1]):])
        crate_dict[int(instructions[3])] = crate_dict[int(instructions[3])][:len(
            crate_dict[int(instructions[3])])-int(instructions[1])]
    return crate_dict


def get_top_crates(crate_dict):
    top_crates_string = ""
    for i in range(1, len(crate_dict)+1):
        top_crates_string += crate_dict.get(i)[-1]
    return top_crates_string


lines = open("./inputs/day5-input.txt", "r").readlines()
NUMBER_OF_STACKS = 9
CRATE_BOTTOM_LINE_NUMBER = 7
INSTRUCTIONS_START_LINE = 10
print('Q1:', get_top_crates(get_crates_dict_rearranged(lines, get_crate_dict(lines))))
print('Q2:', get_top_crates(
    get_crates_dict_rearranged_2(lines, get_crate_dict(lines))))
