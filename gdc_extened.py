def gcdExtended(a, b):
    # Base Case
    # a 是除數
    if a == 0:
        return b, 0, 1
    print(b%a , a)
    gcd, x1, y1 = gcdExtended(b % a, a)

    # Update x and y using results of recursive
    # call

    # b//a是商數 1是倍數 X是上一次的餘數
    x = y1 - (b // a) * x1
    y = x1
    print("x = ", x, "y = ", y)

    return gcd, x, y


# Driver code
a, b = 3, 6
g, x, y = gcdExtended(a, b)
print("gcd(", a, ",", b, ") = ", g)
print(x,y)
