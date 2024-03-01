# Some numbers have funny properties. For example:

# 89 --> 8¹ + 9² = 89 * 1
# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
# Given two positive integers n and p, we want to find a positive integer k, if it exists, 
# such that the sum of the digits of n raised to consecutive powers starting from p is equal to k * n.

# If it is the case we will return k, if not return -1.

# Note: n and p will always be strictly positive integers.



# Didn't work for all test cases but worked for most...
# def dig_pow(n, p):
#     digits = [int(digit) for digit in str(n)]
#     count = 0
#     for digit in digits:
#         digits[count] = digit ** (p + count)
#         count += 1
#     total = sum(digits)/n
#     if total - round(total) <0.001:
#         return round(total)
#     else:
#         return -1

def dig_pow(n, p):
    digits = [int(digit) for digit in str(n)]
    count = 0
    for digit in digits:
        digits[count] = digit ** (p + count)
        count += 1
    total = sum(digits)/n
    if round(total) * n == sum(digits):
        return round(total)
    else:
        return -1
    
# given solution

# def dig_pow(n, p):
#     s = 0
#     for i,c in enumerate(str(n)):
#         s += pow(int(c),p+i)
#     return s/n if s%n==0 else -1