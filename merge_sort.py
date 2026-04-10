def merge_sort(given_list):
    if len(given_list) > 1:
        mid = len(given_list) // 2

        left_arr = given_list[:mid]
        right_arr = given_list[mid:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = 0
        j = 0
        k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                given_list[k] = left_arr[i]
                i += 1
            else:
                given_list[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            given_list[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            given_list[k] = right_arr[j]
            j += 1
            k += 1

    return given_list
