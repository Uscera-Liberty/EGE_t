# c = 0
# for i in range(1,9000):
#     n = i
#     if n%3== 0:n = n//3
#     else:n = n-1
#     if n%7== 0:n = n//7
#     else:n = n-1
#     if n%11== 0:n = n//11
#     else:n = n-1
#     if n == 6:
#         c+=1
# print(c)

# s = 63*'1' + 61*'2'
# while '111' in s :
#   s = s.replace('111','22',1)
#   s = s.replace('2222','1',1)
# print(s)

# s = bin(8**415-2**543-25)[2:]
# print(s.count('1'))
# temp = 0
# for a in range(1,1000):
#     f = 1
#     for x in range(1,1000):
#         f *= (x&a!=0)<=((x&20==0)<=(x&5!=0))
#         if f == 0:
#             break
#     if f:
#         temp = a
# print(temp)

# def f(n):
#     if n<= 3:return n+3
#     if n > 3 and f(n-1)%2 == 0:return f(n-2) + n
#     if n > 3 and f(n - 1) % 2 == 1: return f(n - 2) + 2*n
# sumc = 0
# print(f(40))

# with open('17-4.txt','r') as f:
#     c = 0
#     m = 0
#     a = [int(i) for i in f]
#     for i in a:
#         if i % 16 == 11:
#             if i % 7 == 0 and i % 6 != 0 and i % 13 != 0 and i % 19 != 0:
#                 c += 1
#                 m += i
#     print(m, c)