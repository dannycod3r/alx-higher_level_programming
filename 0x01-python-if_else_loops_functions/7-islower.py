def islower(c):
    """islower - check if a number is lowercase
    @c: character
    Return: True if affirmative else False
    """
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False
