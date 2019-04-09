
def chop(element, lst):
    return BinarySearcher(lst).find(element)

class BinarySearcher(object):
    def __init__(self, lst, base=0):
        self._list = lst
        self._base = base
        self._init_finder()
    
    def _init_finder(self):
        if self._list:
            self._finder = self._find_by_binary_search
        else:
            self._finder = self._always_return_not_found
    
    def find(self, element):
        return self._finder(element)
    
    def _find_by_binary_search(self, element):
        lst = self._list
        mid_idx = int(len(lst)/2)
        mid_elem = lst[mid_idx]
        if mid_elem == element:
            return self._base + mid_idx
        if mid_elem > element:
            return BinarySearcher(lst[:mid_idx], self._base).find(element)
        return BinarySearcher(lst[mid_idx + 1:], self._base + mid_idx + 1).find(element)
    
    def _always_return_not_found(self, *args, **kwargs):
        return -1