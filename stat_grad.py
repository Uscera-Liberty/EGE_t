# for n in range(2,1111):
#     s=bin(n)[2:]
#     s1=s[::2]
#     s0=s[1::2]
#     if abs(s1.count('0')-s0.count('1'))==5:
#         print(n)
#         break

# for i in range(1,1000):
#     s = i
#     s = s // 7
#     n = 1
#     while s < 255:
#         if (s + n) % 2 == 0:
#             s = s + 11
#         n = n + 5
#     if n == 96:
#         print(i)

# from itertools import permutations
# c = 0
# a = set()
# for x in permutations('12325474',8):
#     w = ''.join(x)
#     for i in range(len(w) - 1):
#         if (int(w[i])+int(w[i+1]))%2 != 0:
#             a.add(w)
# print(len(a))
#
# for x1 in range(1,200):
#     for x2 in range(1,200):
#         for x3 in range(1,200):
#             if (x1 + x2*2 + x3*3) == 70 and (x1 + x2 + 3*x3) == 56 and (x2 + x3) == 23:
#                 print(x1+x2+x3)


# x = 5 * 343**8 + 4 * 49**12 + 7**14 - 98
# s = ''
# while x:
#      s= str(x%7) + str(s)
#      x//=7
# print(s)

# def f(n):
#      if n == 0 :
#           return 0
#      elif n%2==1 :
#           return f(n-1) + 1
#      elif n%2 == 0 and n > 0 :
#           return f(n/2)
# c = 0
# for n in range(0,1000000):
#      if f(n) == 2:
#           c+=1
# print(c)

# f=open('17-68.txt')
# a = [int(i) for i in f]
# a_chet = [int(i) for i in a if i%2 == 0]
# sr_zn = sum(a_chet)/len(a_chet)
# c = 0
# s = []
# for i in range (len(a)-1):
#      if (a[i]%3 == 0 and a[i+1]<sr_zn) or (a[i+1]%3 == 0 and a[i]<sr_zn):
#           c+=1
#           s = [a[i] + a[i+1]]
# print(c)
# print(max(s))