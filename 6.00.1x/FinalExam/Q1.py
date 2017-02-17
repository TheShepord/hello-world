def sum_digits(s):
    """ 
    assumes s a string
    Returns an int that is the sum of all of the digits in s.
    If there are no digits in s it raises a ValueError exception. 
    """
    try:
        digits = ['0','1','2','3','4','5','6','7','8','9']
        result = 0

        s[0] in digits
        for i in s:
            if i in digits:
                result += int(i)
            
        return result
    
    except:
        raise ValueError("string of length 0")