def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    a=s
    d=int(a[0])+int(a[1])+int(a[2])+int(a[3])+int(a[4])
    return d
print(main('12332'))
