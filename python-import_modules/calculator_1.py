#!/usr/bin/python3
import sys
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer
        The return value. a + b
    """
    return (a + b)

def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)
def sub(a, b):
    
    return (a - b)

def div(a, b):
    
    return int(a / b)
if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(add(a, b))

    print(mul(a, b))
    
    print(sub(a, b))
    print(div(a, b))
    
