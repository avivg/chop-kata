
def chop(element, lst):
    start = 0
    stop = len(lst) - 1
    return rec_chop(element, lst, start, stop)

def rec_chop(element, lst, start, stop):
    if start > stop:
        return -1
    middle_idx = int((start + stop)/2)
    middle_elem = lst[middle_idx]
    if middle_elem == element:
        return middle_idx
    if middle_elem < element:
        return rec_chop(element, lst, middle_idx + 1, stop)
    return rec_chop(element, lst, start, middle_idx - 1)
    
    