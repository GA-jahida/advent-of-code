import math

def get_monkey_array(lines):
    monkey_array = [{
        "start": [],
        "operation": [],
        "test": []
    } for x in range(int((len(lines) + 1) / 7))]
    test_divisors = []
    for i in range(0, len(lines), 7):
        monkey_array[i//7]["start"] = [
            int(x)for x in lines[i+1].replace("Starting items:", "").split(",")
        ]
        monkey_array[i//7]["operation"] = lines[i + 2].replace("Operation:", "").strip().split(" ")
        monkey_array[i//7]["test"] = [
            int(lines[i+3].replace("Test:", "").strip().split(" ")[2]),
            int(lines[i+4].replace("If true:", "").strip().split(" ")[3]),
            int(lines[i+5].replace("If false:", "").strip().split(" ")[3]),
        ]
        test_divisors.append(monkey_array[i//7]["test"][0])
    return monkey_array, math.lcm(*test_divisors)


def get_monkey_business_level(monkey_array, rounds, post_operation):
    monkey_levels = [0 for x in range(len(monkey_array))]
    for _ in range(rounds):
        for index, monkey in enumerate(monkey_array):
            for item in monkey["start"]:
                monkey_levels[index] += 1
                operand = monkey["operation"][4]
                if operand == "old":
                    operand = item
                new = post_operation(perform_operation(item, monkey["operation"][3], int(operand)))
                if new % monkey["test"][0] == 0:
                    monkey_array[monkey["test"][1]]["start"].append(new)
                else:
                    monkey_array[monkey["test"][2]]["start"].append(new)
            monkey["start"] = []
    monkey_levels.sort()
    return monkey_levels[-1] * monkey_levels[-2]


def perform_operation(old, operation, operand):
    match operation:
        case "*":
            return old * operand
        case "+":
            return old + operand


lines = open("./inputs/day11-input.txt", "r").readlines()

monkey_array, lcm = get_monkey_array(lines)
print("Q1:", get_monkey_business_level(monkey_array, 20, lambda x: x // 3))
monkey_array, lcm = get_monkey_array(lines)
print("Q2:", get_monkey_business_level(monkey_array, 10000, lambda x: x % lcm))

