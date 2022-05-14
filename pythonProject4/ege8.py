from itertools import *
c = 0
# for x in product('onics' , repeat = 6):
#     w = ''.join(x)
#     if w.count('s') == 3 and w.count('o') == 1:
#         c+=1
# print(c)
# def prost(n):
#     if n%2 == 0:
#         return n == 2
#     d = 3
#     while d**2 <= n and n % d != 0:
#         d+=2
#     return d**2 > n

def kolpr( a, b ):
    if a == b:
        return 1
    if a > b :
        return 0
    return kolpr(a+1,b)+ kolpr(a*2,b)
print(kolpr(1,30))