from math import prod
from itertools import combinations
import re

def parse(lines, multiplier):
    c = 0
    pattern = re.compile(r'\.+')
    for line in lines:
        spring_groups = line.replace('\n','').split(' ')[1].split(',')*multiplier
        conditions = line.replace('\n','').split(' ')[0]
        conditions = '?'.join([conditions] * multiplier)
        # conditions_list = list(filter(None, pattern.sub('.', conditions).replace('\n','').split('.')))
        # arranged_conditions = rearrange(conditions_list, spring_groups)
        # d = [0 for x in range(len(arranged_conditions))]
        # for index, arranged_condition in enumerate(arranged_conditions):
        #     combinations = replace_question_marks(arranged_condition[0], sum(map(int, arranged_condition[1])))
        #     print(combinations)
        #     for combination in combinations:
        #         if check_arrangement(combination, arranged_condition[1]):
        #             print('adding')
        #             d[index] += 1
        #     if len(combinations) == 0:
        #         d[index] = 1
        #     print(d)
        # c += prod(d)
        combinations = replace_question_marks(conditions, sum(map(int, spring_groups)))
        for combination in combinations:
            if check_arrangement(combination, spring_groups):
                c += 1
    return c


def rearrange(conditions_list, spring_groups):
    rearranged_conditions = []
    if len(spring_groups) == len(conditions_list):
        for index, condition_list in enumerate(conditions_list):
            rearranged_conditions.append([condition_list, spring_groups[index]])
    elif len(conditions_list) == 1:
        return [[conditions_list[0], spring_groups]]
    else:
        for condition_list in conditions_list:
            temp_spring_groups = [spring_groups[0]]
            index = 1
            while index < len(spring_groups) and len(condition_list) - sum(map(int, temp_spring_groups)) - int(spring_groups[index]) >= 1:
                temp_spring_groups.append(spring_groups[index])
                index += 1
            rearranged_conditions.append([condition_list, temp_spring_groups])
            spring_groups = spring_groups[index:]
    return rearranged_conditions


def replace_question_marks(string, hashtags_count):
    current_hashtag_count = string.count('#')
    indices = [index for index, char in enumerate(string) if char == '?']
    combinations_indices = list(combinations(indices, hashtags_count - current_hashtag_count))
    combinations_list = []
    for combination in combinations_indices:
        new_string = string
        for index in combination:
            new_string = new_string[:index] + '#' + new_string[index + 1:]
        for i, char in enumerate(new_string):
            if char == '?':
                new_string = new_string[:i] + '.' + new_string[i + 1:]
        combinations_list.append(new_string)
    return combinations_list


def check_arrangement(conditions, spring_groups):
    conditions = list(filter(None, conditions.split('.')))
    if len(conditions) != len(spring_groups):
        return False
    for index, spring_group in enumerate(spring_groups):
        if len(conditions[index]) != int(spring_group):
            return False
    return True


def part1(lines):
    return parse(lines, 1)


def part2(lines):
    return parse(lines, 5)


lines = open("./inputs/day12-input.txt", "r").readlines()
print("Q1:", part1(lines))
print("Q2:", part2(lines))