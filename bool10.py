import math
def main(a):
    """
    Check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    kv = math.sqrt(a)   
    return kv 
print(main(121))