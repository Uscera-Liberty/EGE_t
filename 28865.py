# s = 500 * '5'
# count = 0
# while '555' in s or '333' in s:
#     if '333' in s:
#         s = s.replace('333' , '5' , 1)
#         print(s)
#     else:
#         s = s.replace('555' , '3' , 1)
#         print(s)
#         count += 3
#
# print(s ,count)

# x = 3**40 + 3**60 - 125
# s = ''
# while x > 0:
#   s += str(x % 3) # n6 = str(n10 % 6) + n6 число в прямом порядке(не обратном)
#   x //= 3
# s = s[::-1]
# print(s.count('2'))

temp = 0
for a in range(1 , 1000):
    f = 1
    for x in range(1 , 1000):
        for y in range(1 , 1000):
            f *= (5*y + 7*x != 129) or (3*x > a) or (4*y > a)
        if not(f):
            break
    if f: temp = a
print(temp)