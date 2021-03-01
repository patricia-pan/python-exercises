# Write a method to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1
#
# Example method call
#
# factorial(5)
#
# > 120
#

def factorial(num):
    prod = 1
    while num > 1:
        prod *= num
        num -=1
    print prod
    return prod
    # Dave's solution used: for num in range(1, num+1)

factorial(5)
