n = int(input('Enter n (0 to quit): '))
while n != 0:
    prod = 1
    i = 2
    while i <= n:
        prod += i
        i += 1
    print('The triangle number is:', prod)
    if prod == n * (n + 1) /2:
        print('Triangle Number thorem holds')
    else:
        print('You fucked up')
    n= int(input('Enter n (0 to quit): '))
print('Bye now!')