import numpy as np
from math import copysign
from matplotlib import pyplot as plt
walls = []


field = np.zeros((1000, 1000))

def draw_line(point1, point2):
    if point1[0] == point2[0]:
        offset = np.array([0, copysign(1,  point2[1]-point1[1])], dtype=np.int32)
    else:
        offset = np.array([copysign(1,  point2[0]-point1[0]), 0], dtype=np.int32)

    current_point = np.array(point1)
    end = np.array(point2)
    while (current_point != end).any():
        field[*current_point] = 1
        current_point += offset

    field[*end] = 1

def make_grain_fall_1():
    position = np.array([500, 0], dtype=np.int32)

    down_offset = np.array([0, 1], dtype=np.int32)
    left_down_offset = np.array([-1, 1], dtype=np.int32)
    right_down_offset = np.array([1, 1], dtype=np.int32)

    while position[1] < field.shape[0] - 1:
        test_position = position + down_offset
        if field[*test_position] == 0:
            position = test_position
            continue

        test_position = position + left_down_offset
        if field[*test_position] == 0:
            position = test_position
            continue

        test_position = position + right_down_offset
        if field[*test_position] == 0:
            position = test_position
            continue

        field[*position] = 2
        return False

    return True

def make_grain_fall_2():
    start_position = np.array([500, 0], dtype=np.int32)
    position = start_position.copy()

    down_offset = np.array([0, 1], dtype=np.int32)
    left_down_offset = np.array([-1, 1], dtype=np.int32)
    right_down_offset = np.array([1, 1], dtype=np.int32)

    while position[1] < field.shape[1] - 1 :
        test_position = position + down_offset
        if field[*test_position] == 0:
            position = test_position
            continue

        test_position = position + left_down_offset
        if field[*test_position] == 0:
            position = test_position
            continue

        test_position = position + right_down_offset
        if field[*test_position] == 0:
            position = test_position
            continue

        field[*position] = 2
        return (position == start_position).all()
    field[*position] = 2
    return False

with open('./data/14') as data_file:
    max_y = 0
    for line in data_file:
        points_str = line.split(' -> ')
        current_wall = []
        for point_str in points_str:
            x, y = map(int, point_str.split(','))
            max_y = max(y, max_y)
            current_wall.append([x, y])

        walls.append(current_wall)

    field = np.zeros((max(600, max_y * 10 + 1), max_y + 2))

    for wall in walls:
        for i in range(len(wall) - 1):
            draw_line(wall[i], wall[i+1])

    count = 1
    while not make_grain_fall_2():
        count += 1

    print(count)




        