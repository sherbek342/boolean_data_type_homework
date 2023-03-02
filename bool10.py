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

    return v*v==a
print(main(9))