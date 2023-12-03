def parse_input(lines):
    for line in lines:
        line = line.replace("\n", "")
        packet = []
        print(line, '----------------------------------------------')
        a = parse_line(line[1::], packet)
        print(a)

def parse_line(line, packet, depth=-1):
    for index, char in enumerate(line):
        match char:
            case "[":
                packet.append([])
                packet.append(parse_line(line[index + 1::], packet[depth + 1]))
                print(packet)
            case ",":
                continue
            case "]":
                continue
            case _:
                packet.append(char)
    return packet


def part1(lines):
    parse_input(lines)


def part2():
    print("")

lines = open("./inputs/day13-input.txt", "r").readlines()
print("Q1:", part1(lines))
print("Q2:", part2())