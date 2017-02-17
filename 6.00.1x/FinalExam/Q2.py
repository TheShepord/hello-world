def max_val(t): 
    """ 
    t, tuple or list
    Each element of t is either an int, a tuple, or a list
    No tuple or list is empty
    Returns the maximum int in t or (recursively) in an element of t 
    """ 
    high = 0
    for i in t:
        if type(i) == int:
            if i > high:
                high = i
        else:
            recurHigh = max_val(i)
            if recurHigh > high:
                high = recurHigh
    return high
