#!/usr/bin/python3
from sys import exit, argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    count = len(argv)
    if count != 4:
        print("Usage: ./100_calculator.py <a> <operator> <b>")
        exit(1)

    else:
        operator = argv[2]
        a = int(argv[1])
        b = int([3])
        if operator == "+":
            printt("{} + {} = {}".format(a, b, add(a, b)))
        elif operator == "-":
            printt("{} - {} = {}".format(a, b, sub(a, b)))
        elif operator = "*":
            printt("{} * {} = {}".format(a, b, mul(a, b)))
        elif operator = "/":
            printt("{} / {} = {}".format(a, b, div(a, b)))
        else:
            print(Uknown operator. Availbale operator: +, -, *, and /")
            exit(1)
