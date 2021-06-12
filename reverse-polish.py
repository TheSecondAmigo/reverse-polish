#!/usr/bin/env python3

"""

Good morning! Here's your coding interview problem for today.

This problem was asked by Jane Street.

Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.

The expression is given as a list of numbers and operands.
For example:
[5, 3, '+'] should return 5 + 3 = 8.

For example:
[15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5,
since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

You can assume the given expression is always valid.

"""

import operator

def rev_polish(exprlist):

    opmap = { '+': operator.add,
              '-': operator.sub,
              '*': operator.mul,
              '/': operator.ifloordiv,
            }

    operand = list()

    for item in exprlist:
        if isinstance(item, int):
            operand.append(item)
        elif isinstance(item, str):
            op2 = operand.pop()
            op1 = operand.pop()
            operand.append(opmap[item](op1, op2))

    # print(operand)
    return operand[0]


if __name__ == "__main__":

    tests = [([5, 3, '+'], 8),
             ([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'], 5),
            ]

    for exprlist, exp in tests:
        rc = rev_polish(exprlist)
        print(f"exprlist = {exprlist}, exp = {exp}, rc = {rc}, {exp == rc}")

