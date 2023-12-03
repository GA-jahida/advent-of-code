def get_total_score(lines, score_dict):
    score = 0
    for line in lines:
        if not line.strip() in score_dict:
            print('Missing from dict:', line.strip())
        score += score_dict.get(line.strip())
    return score


# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 l, 3 d, 6 w
score_dict = {
    "A X": 1+3,
    "A Y": 2+6,
    "A Z": 3+0,
    "B X": 1+0,
    "B Y": 2+3,
    "B Z": 3+6,
    "C X": 1+6,
    "C Y": 2+0,
    "C Z": 3+3,
}

# Q2. X lose, Y draw, Z win
score_dict_q2 = {
    "A X": 3+0,
    "A Y": 1+3,
    "A Z": 2+6,
    "B X": 1+0,
    "B Y": 2+3,
    "B Z": 3+6,
    "C X": 2+0,
    "C Y": 3+3,
    "C Z": 1+6,
}

lines = open("./inputs/day2-input.txt", "r").readlines()
print('Q1:', get_total_score(lines, score_dict))
print('Q2:', get_total_score(lines, score_dict_q2))
