def insertion_sort(given_list):
    for i in range(1, len(given_list)):
        value_to_sort = given_list[i]

        while given_list[i - 1] > value_to_sort and i > 0:
            given_list[i], given_list[i - 1] = given_list[i - 1], given_list[i]
            i -= 1

    return given_list
