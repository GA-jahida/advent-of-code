import heapq


def parse(lines):
    brick_bottom_dict = {}
    brick_top_dict = {}
    keys = [chr(x) for x in range(ord('A'), ord('A') + 10000)]
    for index, line in enumerate(lines):
        lines[index] = line.replace('\n', '')
    for index, line in enumerate(lines):
        x1,y1,z1 = [int(x) for x in line.split('~')[0].split(',')]
        x2,y2,z2 = [int(x) for x in line.split('~')[1].split(',')]
        add_brick(brick_bottom_dict, brick_top_dict, x1, x2, y1, y2, z1, z2, index)
    return brick_bottom_dict, brick_top_dict


def add_brick(brick_bottom_dict, brick_top_dict, x1, x2, y1, y2, z1, z2, key):
        if z1 in brick_bottom_dict:
            brick_bottom_dict[z1].append({
                'bottom' : (x1, y1, z1),
                'top' : (x2, y2, z2),
                'label': key
            })
        else:
            brick_bottom_dict[z1]= [{
                'bottom' : (x1, y1, z1),
                'top' : (x2, y2, z2),
                'label': key
            }]

        if z2 in brick_top_dict:
            brick_top_dict[z2].append({
                'bottom' : (x1, y1, z1),
                'top' : (x2, y2, z2),
                'label': key
            })
        else:
            brick_top_dict[z2]= [{
                'bottom' : (x1, y1, z1),
                'top' : (x2, y2, z2),
                'label': key
            }]


def check_overlap(x1, y1, x2, y2, x3, y3, x4, y4):
    return  (x1 <= x3 <= x2 or x1 <= x4 <= x2 or (x3 <= x1 and x4 >= x2) or (x3 >= x1 and x4 <= x2)) and (y1 <= y3 <= y2 or y1 <= y4 <= y2 or (y3 <= y1 and y4 >= y2) or (y3 >= y1 and y4 <= y2))


def get_brick_in_air(brick_bottom_dict, brick_top_dict):
    for brick_list in brick_bottom_dict.values():
        for brick in brick_list:
            x1, y1, z1 = brick['bottom']
            x2, y2, z2 = brick['top']
            if z1 == 1:
                continue
            if z1 - 1 in brick_top_dict:
                supported = False
                for brick_below in brick_top_dict[z1 - 1]:
                    x3, y3, z3 = brick_below['bottom']
                    x4, y4, z4 = brick_below['top']
                    if check_overlap(x1, y1, x2, y2, x3, y3, x4, y4):
                        supported = True
                        break
                if supported:
                    continue
            return brick
    return None


def drop_bricks(brick_bottom_dict, brick_top_dict):
    next_brick_in_air = get_brick_in_air(brick_bottom_dict, brick_top_dict) 
    while next_brick_in_air is not None:
        x1, y1, z1 = next_brick_in_air['bottom']
        x2, y2, z2 = next_brick_in_air['top']

        for i, brick in enumerate(brick_bottom_dict[z1]):
            if brick['label'] == next_brick_in_air['label']:
                brick_bottom_dict[z1].pop(i)

        for i, brick in enumerate(brick_top_dict[z2]):
            if brick['label'] == next_brick_in_air['label']:
                brick_top_dict[z2].pop(i)
        
        z1 -= 1
        z2 -= 1
        add_brick(brick_bottom_dict, brick_top_dict, x1, x2, y1, y2, z1, z2, next_brick_in_air['label'])
        next_brick_in_air = get_brick_in_air(brick_bottom_dict, brick_top_dict)
    return brick_bottom_dict, brick_top_dict


def get_support_dict(brick_bottom_dict, brick_top_dict):
    support_dict = {}

    for brick_list in brick_bottom_dict.values():
        for brick in brick_list:
            support_dict[brick['label']] = set()

    for brick_list in brick_bottom_dict.values():
        for brick in brick_list:
            x1, y1, z1 = brick['bottom']
            x2, y2, z2 = brick['top']
            if z1 == 1:
                continue
            if z1 - 1 in brick_top_dict:
                for brick_below in brick_top_dict[z1 - 1]:
                    x3, y3, z3 = brick_below['bottom']
                    x4, y4, z4 = brick_below['top']
                    if check_overlap(x1, y1, x2, y2, x3, y3, x4, y4):
                        support_dict[brick['label']].add(brick_below['label'])
    return support_dict


def get_supported_by_dict(brick_bottom_dict, brick_top_dict):
    supported_by_dict = {}

    for brick_list in brick_bottom_dict.values():
        for brick in brick_list:
            supported_by_dict[brick['label']] = [] 

    for brick_list in brick_top_dict.values():
        for brick in brick_list:
            x1, y1, z1 = brick['bottom']
            x2, y2, z2 = brick['top']
            if z1 + 1 in brick_bottom_dict:
                for brick_above in brick_bottom_dict[z1 + 1]:
                    x3, y3, z3 = brick_above['bottom']
                    x4, y4, z4 = brick_above['top']
                    if check_overlap(x1, y1, x2, y2, x3, y3, x4, y4):
                        supported_by_dict[brick['label']].append(brick_above['label'])
    return supported_by_dict


def identify_supporting(brick_bottom_dict, brick_top_dict):
    support_dict = get_support_dict(brick_bottom_dict, brick_top_dict)
    bricks_to_disintegrate = set()

    for brick_list in brick_bottom_dict.values():
        for brick in brick_list:
            bricks_to_disintegrate.add(brick['label'])

    bricks_to_not_disintegrate = set()
    for bricks in support_dict.values():
        if len(bricks) == 1:
            [brick] = bricks
            bricks_to_not_disintegrate.add(brick)

    return len(bricks_to_disintegrate) - len(bricks_to_not_disintegrate)


def visualise(brick_bottom_dict, brick_top_dict):
    max_z = 0
    for brick_list in brick_top_dict.values():
        for brick in brick_list:
            if brick['top'][2] > max_z:
                max_z = brick['top'][2]
    x_perspective = ['..........' for x in range(max_z+1)]
    y_perspective = ['..........' for x in range(max_z+1)]
    
    for i in range(len(brick_bottom_dict), 0, -1):
        if i in brick_bottom_dict:
            for brick in brick_bottom_dict[i]:
                x1, y1, z1 = brick['bottom']
                x2, y2, z2 = brick['top']
                for z in range(z1, z2 + 1):
                    for x in range(x1, x2 + 1):
                        if x_perspective[z][x] == '.':
                            x_perspective[z] = x_perspective[z][:x] + brick['label'] + x_perspective[z][x+1:]
                        else:
                             x_perspective[z] = x_perspective[z][:x] + '?' + x_perspective[z][x+1:]
                    for y in range(y1, y2 + 1):
                        if y_perspective[z][y] == '.':
                            y_perspective[z] = y_perspective[z][:y] + brick['label'] + y_perspective[z][y+1:]
                        else:
                             y_perspective[z] = y_perspective[z][:y] + '?' + y_perspective[z][y+1:]
    print('-------------------------------------------------------')
    for i in range(len(x_perspective)-1, -1, -1):
        print(x_perspective[i], i)
    print('-------------------------------------------------------')
    for i in range(len(x_perspective)-1, -1, -1):
        print(y_perspective[i], i)
    print('-------------------------------------------------------')


def get_sum_other(support_dict):
    sum_other = 0
    queue = [{brick} for brick in support_dict.keys()]
    
    while queue:
        fallen = heapq.heappop(queue)
        brick_fell_len = len(fallen)
        for brick, support_bricks in support_dict.items():
            if not support_bricks - fallen and support_bricks:
                fallen.add(brick)
        if len(fallen) > brick_fell_len:
            heapq.heappush(queue, fallen)
        else:
            sum_other += len(fallen) - 1

    return sum_other


def part1(lines):
    brick_bottom_dict, brick_top_dict = parse(lines)
    brick_bottom_dict, brick_top_dict = drop_bricks(brick_bottom_dict, brick_top_dict)
    return identify_supporting(brick_bottom_dict, brick_top_dict)


def part2(lines):
    brick_bottom_dict, brick_top_dict = parse(lines)
    brick_bottom_dict, brick_top_dict = drop_bricks(brick_bottom_dict, brick_top_dict)
    support_dict = get_support_dict(brick_bottom_dict, brick_top_dict)
    return get_sum_other(support_dict)


lines = open("./inputs/day22-input.txt", "r").readlines()
print("Q1:", part1(lines))
print("Q2:", part2(lines))