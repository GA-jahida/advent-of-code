def get_directory_structure(lines):
    path_array = []
    structure_dict = {}
    separator = "/"
    for line in lines:
        cmd = line.replace("\n", "").split(" ")
        match cmd[0]:
            case "$":
                match cmd[1]:
                    case "cd":
                        match cmd[2]:
                            case "/":
                                path_array = []
                            case "..":
                                path_array.pop()
                            case _:
                                path_array.append(cmd[2])
                        if separator.join(path_array) not in structure_dict:
                            structure_dict[separator.join(path_array)] = {
                                "dir": [], "size": 0}
            case "dir":
                structure_dict[separator.join(
                    path_array)]['dir'].append(cmd[1])
            case _:
                if cmd[0].isdigit():
                    structure_dict[separator.join(
                        path_array)]['size'] += int(cmd[0])
    return structure_dict


def get_directory_size(structure_dict, parent_path, dir_list):
    total_directory_size = 0
    separator = "" if parent_path == "" else "/"
    for directory in dir_list:
        total_directory_size += (structure_dict[parent_path + separator + directory]['size'] +
                            get_directory_size(structure_dict, parent_path + separator + directory,
                            structure_dict[parent_path + separator + directory]["dir"]))
    return total_directory_size


def get_total_size_max_100000(structure_dict):
    total_size = 0
    for key in structure_dict:
        current_size = structure_dict[key]["size"] + get_directory_size(
            structure_dict, key, structure_dict[key]["dir"])
        if current_size <= 100000:
            total_size += current_size
    return total_size


def get_directory_min_30000000(structure_dict):
    size = 70000000
    free_space = 70000000 - structure_dict[""]["size"] - get_directory_size(
        structure_dict, "", structure_dict[""]["dir"])
    for key in structure_dict:
        current_size = structure_dict[key]["size"] + get_directory_size(
            structure_dict, key, structure_dict[key]["dir"])
        if 30000000 - free_space <= current_size < size:
            size = current_size
    return size


lines = open("./inputs/day7-input.txt", "r").readlines()

print("Q1:", get_total_size_max_100000(get_directory_structure(lines)))
print("Q2:", get_directory_min_30000000(get_directory_structure(lines)))
