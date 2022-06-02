#!/usr/bin/python3

if __name__ == "__main__":
    '''My Advance calculator'''
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        usage = "Usage: ./100-my_calculator.py <a> <operator> <b>"
        print(usage)
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(ops.keys()):
        unknown = "Unknown operator. Available operators: +, -, * and /"
        print(unknown)
        sys.exit(1)
