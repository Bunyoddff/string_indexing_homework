def main(a):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    x1=a[0]
    s=0
    if x1>='0' and x1<='9':
        s+=1
        return s 
print(main('7'))
