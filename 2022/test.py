def parse_line(line, index=0):
    packet = []
    current_list = packet  # Keep track of the current list being processed

    while index < len(line):
        char = line[index]

        if char == "[":
            inner_list, index = parse_line(line, index + 1)
            current_list.append(inner_list)
        elif char == "]":
            return packet, index + 1
        elif char == ",":
            index += 1
        else:
            # Assuming numbers or other characters
            # Add your logic here if needed
            current_list.append(int(char))

        index += 1

    return packet, index

# Your string representation of the nested list
nested_list_string = "[[1],[2,3,4]]"

# Call the function to parse the string
result, _ = parse_line(nested_list_string)

# Print the resulting list
print(result)
