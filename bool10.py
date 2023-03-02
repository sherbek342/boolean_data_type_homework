import math
def main(a):
    """
    Check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """  
    v = math.sqrt(a)
    f = round(v)

    return f*f==a
print(main(a))