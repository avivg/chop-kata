
def chop(element, lst):
    start = 0
    stop = len(lst) - 1
    while start <= stop:
        middle_idx = int((start + stop)/2)
        middle_element = lst[middle_idx]
        if middle_element == element:
            return middle_idx
        if middle_element < element:
            start = middle_idx + 1
        else:
            stop = middle_idx - 1
    return -1