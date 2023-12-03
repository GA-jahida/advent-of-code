def get_contained_pairs_sum(lines):
    contained_pairs_sum = 0
    for line in lines:
        pair = line.strip().split(',')
        first_pair_sections = [
            int(pair[0].split('-')[0]), int(pair[0].split('-')[1])]
        second_pair_sections = [
            int(pair[1].split('-')[0]), int(pair[1].split('-')[1])]
        if (first_pair_sections[0] == second_pair_sections[0] 
        or first_pair_sections[1] == second_pair_sections[1]):
            contained_pairs_sum += 1
        elif first_pair_sections[0] > second_pair_sections[0]:
            if second_pair_sections[1] > first_pair_sections[1]:
                contained_pairs_sum += 1
        elif first_pair_sections[1] > second_pair_sections[1]:
            contained_pairs_sum += 1
    return contained_pairs_sum


def get_overlap_pairs_sum(lines):
    overlap_pairs_sum = 0
    for line in lines:
        pair = line.strip().split(',')
        first_pair_sections = [
            int(pair[0].split('-')[0]), int(pair[0].split('-')[1])]
        second_pair_sections = [
            int(pair[1].split('-')[0]), int(pair[1].split('-')[1])]
        if (first_pair_sections[0] <= second_pair_sections[1] 
        and second_pair_sections[0] <= first_pair_sections[1]):
            overlap_pairs_sum += 1
    return overlap_pairs_sum


lines = open("./inputs/day4-input.txt", "r").readlines()

print('Q1:', get_contained_pairs_sum(lines))
print('Q2:', get_overlap_pairs_sum(lines))
