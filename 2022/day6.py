def get_start_of_packet_marker(line, marker_length):
    char_array = []
    for count, char in enumerate(line):
        if len(char_array) == marker_length:
            return count
        if char in char_array:
            char_array = char_array[char_array.index(char)+1:]
        char_array.append(char)


def get_start_of_packet_marker_set(line, marker_length):
    for i in range(marker_length, len(line) + 1):
        if len(set(line[i - marker_length: i])) == marker_length:
            return i


line = open("./inputs/day6-input.txt", "r").readline().strip()

print("Q1:", get_start_of_packet_marker_set(line, 4))
print("Q2:", get_start_of_packet_marker_set(line, 14))
