def get_tree_array(lines):
    tree_array = [0 for x in range(len(lines))]
    for index, line in enumerate(lines):
        tree_array[index] = list(line.strip())
    return tree_array


def get_sum_visible_trees(tree_array):
    sum_visible_trees = 0
    for array_index, array in enumerate(tree_array):
        for tree_index, height in enumerate(array):
            if (array_index == 0 or array_index == len(tree_array)-1 or tree_index == 0
                or tree_index == len(array)-1):
                sum_visible_trees += 1
            else:
                if is_tree_visible(tree_array, tree_index, array_index, height):
                    sum_visible_trees += 1
    return sum_visible_trees


def is_tree_visible(tree_array, tree_index, array_index, height):
    for i in range(0, tree_index + 1):
        if i == tree_index:
            return True
        if int(tree_array[array_index][i]) >= int(height):
            break
    for i in range(tree_index + 1, len(tree_array[array_index]) + 1):
        if i == len(tree_array[array_index]):
            return True
        if int(tree_array[array_index][i]) >= int(height):
            break
    for i in range(0, array_index + 1):
        if i == array_index:
            return True
        if int(tree_array[i][tree_index]) >= int(height):
            break
    for i in range(array_index + 1, len(tree_array) + 1):
        if i == len(tree_array):
            return True
        if int(tree_array[i][tree_index]) >= int(height):
            break
    return False


def get_max_scenic_score(tree_array):
    max_scenic_score = 0
    for array_index, array in enumerate(tree_array):
        for tree_index, height in enumerate(array):
            scenic_score = get_scenic_score(
                tree_array, tree_index, array_index, height)
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score
    return max_scenic_score


def get_scenic_score(tree_array, tree_index, array_index, height):
    scenic_score = 1
    for i in range(tree_index - 1, -1, -1):
        if i == 0:
            scenic_score = scenic_score * (tree_index - i)
        elif (int(tree_array[array_index][i]) >= int(height)):
            scenic_score = scenic_score * (tree_index - i)
            break
    for i in range(tree_index + 1, len(tree_array[array_index])):
        if i == len(tree_array[array_index]) - 1:
            scenic_score = scenic_score * (i - tree_index)
        elif int(tree_array[array_index][i]) >= int(height):
            scenic_score = scenic_score * (i - tree_index)
            break
    for i in range(array_index - 1, -1, -1):
        if i == 0:
            scenic_score = scenic_score * (array_index - i)
        elif int(tree_array[i][tree_index]) >= int(height):
            scenic_score = scenic_score * (array_index - i)
            break
    for i in range(array_index + 1, len(tree_array)):
        if i == len(tree_array) - 1:
            scenic_score = scenic_score * (i - array_index)
        elif (int(tree_array[i][tree_index]) >= int(height)):
            scenic_score = scenic_score * (i - array_index)
            break
    return scenic_score


lines = open("./inputs/day8-input.txt", "r").readlines()

print("Q1:", get_sum_visible_trees(get_tree_array(lines)))
print("Q2:", get_max_scenic_score(get_tree_array(lines)))
