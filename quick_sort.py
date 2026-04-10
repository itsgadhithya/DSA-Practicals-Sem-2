def quick_sort(sequence):
    if len(sequence) < 1:
        return sequence
    pivot_element = sequence.pop()

    values_higher = []
    values_lower = []

    for element in sequence:
        if pivot_element > element:
            values_lower.append(element)
        else:
            values_higher.append(element)

    return quick_sort(values_lower) + [pivot_element] + quick_sort(values_higher)
