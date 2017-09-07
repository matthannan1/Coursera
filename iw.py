def inhospitable_weather(temp):
    ''' (number) -> bool
    Return True if and only if the given temperature in degrees Celsius is unpleasant (too hot or too cold).
    >>> inhospitable_weather(20)
    False
    '''
##    if temp > 28:
##        return True
##    elif temp < 12:
##        return True
##    else:
##        return False

    return (temp > 28) or (temp < 12)
