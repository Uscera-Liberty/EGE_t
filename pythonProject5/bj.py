# def F(n):
#
#    if n <= 18:
#
#        return n+3
#
#    elif n>18 and n%3!=0:
#
#        return F(n-1) + n*n + 5
#
#    else:
#
#        return (n//3)*F(n//3) + n - 12
#
# def help(numb):
#
#    for i in str(numb):
#
#        if int(i)%2==0:
#
#            pass
#
#        else:
#            return False
#    return True
#
# count=0
#
# for i in range(1,801):
#
#    if help(F(i)):
#
#        count+=1
# print(count)


# for i in range(1,1000):
#     x = i
#     a = 0; b = 1
#     while x > 0:
#       a = a + 1
#       b = b * (x % 10)
#       x = x // 10
#     if a == 3 and b == 36:
#         print(i)

# def f( a, b ):
#     if a == b:
#         return 1
#     if a > b :
#         return 0
#     return f(a+1,b) + f(a*2,b) + f(a*3,b)
# print(f(2,12) * f(12,28))

# for i in range(4645283000,464517347,-1):
#     x = i
#     n = 1635
#     while (x+n)//1000 < 465283:
#       x = x - 2
#       n = n + 5
#     if n//1000 == 956:
#         print(i)
# for i in range(464901254,464708746):
#     x = i
#     n = 1635
#     while (x+n) < 465283000:
#       x = x - 2
#       n = n + 5
#     if n//1000 == 956:
#       print(i)
#       break
count = 0
for i in range(263388118,263389218):
    x = i
    n = 357
    while (x + n) // 1000 < 263542:
        x = x - 2
        n = n + 7
    if n//1000 == 214:
        count += 1
print(count)
