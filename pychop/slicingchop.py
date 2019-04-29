
def chop(element, lst):
    return functional_chop(element, lst, 0)

def functional_chop(element, lst, base):
    middle_idx = int(len(lst)/2)
    if len(lst) == 0:
        return -1
    if lst[middle_idx] == element:
        return base + middle_idx
    if lst[middle_idx] < element:
        return functional_chop(element, lst[middle_idx+1:], base + middle_idx + 1)
    return functional_chop(element, lst[:middle_idx], base)
