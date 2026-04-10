# Linear search
def linear_search(given_list, target):
    for i in range(len(given_list)):
        if given_list[i] == target:
            return i


def binary_search(given_list, target):
    starting_index = 0
    ending_index = len(given_list) - 1

    mid_point = (starting_index + ending_index) // 2
    mid_point_value = given_list[mid_point]

    while starting_index <= ending_index:
        if mid_point_value == target:
            return mid_point
        elif mid_point_value > target:
            starting_index = mid_point + 1
        else:
            ending_index = mid_point - 1

    return None
