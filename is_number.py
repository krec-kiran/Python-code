def isDigit(string):
    try:
        if int(float(string)) == 0:
            return True
        val = float(string) or int(string)
    except ValueError:
        return False
    return True
