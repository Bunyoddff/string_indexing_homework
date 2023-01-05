def main(s):
    """
    The s string variable is given. Return three characters from the beginning.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    s=s[0]+s[1]+s[2]
    return s
print(main('number'))