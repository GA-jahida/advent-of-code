def get_max(lines):
    max = 0
    current = 0
    for line in lines:
        if line != "\n":
            current += int(line)
        else:
            if current > max:
                max = current
            current = 0
    return max


def get_sums(lines):
    sums = []
    current = 0
    for line in lines:
        if line != "\n":
            current += int(line)
        else:
            sums.append(current)
            current = 0
    return sums


lines = open("./inputs/day1-input.txt", "r").readlines()
print('Q1:', get_max(lines))
print('Q2:', sum(sorted(get_sums(lines))[-3:]))
