from math import ceil, floor
#math.ceil(x) Return the ceiling of x as a float, the smallest integer value greater than or equal to x.
#math.floor(x) Return the floor of x as a float, the largest integer value less than or equal to x.

def karatsuba(x,y):
    #base case
    if x < 10 and y < 10: # in other words, if x and y are single digits
        return x*y

    n = max(len(str(x)), len(str(y)))
    m = ceil(n/2)   #Cast n into a float because n might lie outside the representable range of integers.

    x_H  = floor(x / 10**m)
    x_L = x % (10**m)

    y_H = floor(y / 10**m)
    y_L = y % (10**m)

    #recursive steps
    a = karatsuba(x_H,y_H)
    print('karatsuba({0},{1})={2}'.format(x_H,y_H,a))
    d = karatsuba(x_L,y_L)
    print('karatsuba({0},{1})={2}'.format(x_L,y_L,d))
    e = karatsuba(x_H + x_L, y_H + y_L) - a - d
    print('karatsuba({0}+{1},{2}+{3}) - {4} - {5}={6}'.format(x_H,x_L,y_H,y_L,a,d,e))

    return int(a*(10**(m*2)) + e*(10**m) + d)

print(karatsuba(3,11))