#! /usr/bin/env python3

# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#     1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the total of the even-valued terms.

total = 0


def fib(n, k):
    output = n + k
    global total

    if output % 2 == 0:
        print(output)
        total = total + output

    if output > 4000000:
        return

    fib(k, output)


fib(1, 2)

print()
print("total:", total)
