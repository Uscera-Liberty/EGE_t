temp = 0
for a in range(1 , 1000):
    f = 1
    for x in range(1 , 1000):
        f *= (((x%a != 0 and x%21 == 0)) <= (x%14 != 0))
    if f:
        temp = a
print(temp)

# def f(n):
#     if n <= 15: return n*n + 11
#     elif n > 15 and n%2 == 0:
#         return f(n//2) + n ** 3 - 5 *n
#     else:
#         return f(n-1) + 2*n + 3
# c = 0
# for n in range(1 , 1000):
#     x = str(f(n))
#     if x.count('6') >= 3:
#         c += 1
# print(c)
# c = 0
# f = open('17-4.txt')
# a = [int(i) for i in f]
# temp = 0
# for i in range(len(a)):
#     if a[i]%5 == 3 and a[i]%9 == 5 and a[i]%8 != 7:
#         c+= 1
#         if temp < a[i]: temp = a[i]
#         else: pass
# print(c ,temp)