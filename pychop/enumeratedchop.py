
def chop(element, lst):
    return enumerated_chop(element, list(enumerate(lst)))

def enumerated_chop(element, enumed_lst):
    idx = lambda e: e[0]
    val = lambda e: e[1]
    if len(enumed_lst) == 0:
        return -1
    else:
        mid_idx = int(len(enumed_lst) / 2)
        mid_elem = enumed_lst[mid_idx]
        if element == val(mid_elem):
            return idx(mid_elem)
        if element < val(enumed_lst[mid_idx]):
            return enumerated_chop(element, enumed_lst[:mid_idx])
        return enumerated_chop(element, enumed_lst[mid_idx+1:])

    
    
