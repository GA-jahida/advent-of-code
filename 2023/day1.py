number_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def part1(lines):
    sum_calibration = 0
    for line in lines:
        line = line.replace("\n", "")
        sum_calibration += find_int(line)
    return sum_calibration


def find_int_simple(line):
    '''
    sum_calibration += int(find_int_simple(line) + find_int_simple(line[::-1]))
    '''
    for char in line:
        if char.isdigit():
            return char
    return None


def find_int(line):
    values = [None, None]
    i = 0
    while values[0] is None or values[1] is None:
        if values[0] is None:
            if (line[i].isdigit()):
                values[0] = line[i]
        if values[1] is None:
            if line[len(line) - 1 - i].isdigit():
                values[1] = line[len(line) - 1 - i]
        i += 1
    return int(values[0] + values[1])


def part2(lines):
    sum_calibration = 0
    for line in lines:
        line = line.replace("\n", "")
        sum_calibration += find_number(line)
    return sum_calibration


def find_number_simple(line, is_reversed):
    '''
    sum_calibration += int(find_number_simple(line, False) + find_number_simple(line[::-1], True))
    '''
    searched = ""
    for char in line:
        if char.isdigit():
            return char
        if is_reversed:
            searched = char + searched
        else:
            searched += char
        for key, number in number_dict.items():
            if key in searched:
                return number
    return None


def find_number(line):
    values = [None, None]
    searched = ""
    searched_reverse = ""
    i = 0
    while values[0] is None or values[1] is None:
        if values[0] is None:
            if line[i].isdigit():
                values[0] = line[i]
            searched += line[i]
            for key, number in number_dict.items():
                if key in ''.join(searched):
                    values[0] = number

        if values[1] is None:
            if line[len(line) - 1 - i].isdigit():
                values[1] = line[len(line) - 1 - i]
            searched_reverse =  line[len(line) - 1 - i] + searched_reverse
            for key, number in number_dict.items():
                if key in ''.join(searched_reverse):
                    values[1] = number
        i += 1
    return int(values[0] + values[1])


lines = open("./inputs/day1-input.txt", "r").readlines()
print('Q1:', part1(lines))
print('Q2:', part2(lines))
