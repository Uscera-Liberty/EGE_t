#print("280-nomer+++6080818")
# for n in range(6000000,7000000):
#     sum_nech = 0
#     sum_chet = 0
#     a = [int(i) for i in str(n)]
#     for i in range(len(a)):
#         if a[i]%2 == 1:
#             sum_nech+=a[i]
#         if i%2==0:
#             sum_chet+=a[i]
#     if abs(sum_chet-sum_nech) == 29:
#         print(n)

#print("274-nomer+++6000086")
# for n in range(6000000,7000000):
#     sum_nech = 0
#     sum_chet = 0
#     a = [int(i) for i in str(n)]
#     for i in range(len(a)):
#         if a[i]%2 == 0:
#             sum_chet+=a[i]
#         if i%2==1:
#             sum_chet+=a[i]
#     if abs(sum_chet-sum_nech) == 28:
#         print(n)

#print("272-nomer+++15")
# for n in range(1,2000):
#     n = n//2
#     n1 = hex(n)[2:]
#     if n%4 != 0:
#         n2 =  'F' + str(n1) + 'A0'
#     else:
#         n2 = '15' + str(n1) + 'C'
#     res = int(n2,16)
#     if res < 65536:
#         print(n)
#
#print("270-nomer+++1287")
# for n in range(1,1000):
#     n1= bin(n)[2:]
#     if n%2==1:
#         n2 = '10' + str(n1) + '11'
#     else:
#         n2 = '1' + str(n1) + '00'
#     if int(n2,2) > 1023:
#         print(int(n2,2))
#         break

#print("268-nomer+++55")
# def f(n):
#     c1 = n.count('1')
#     c0 = n.count('0')
#     if c1 > c0:
#         return str(n) + '1'
#     else:
#         return str(n) + '0'
#
#
# for n in range(1,1000):
#     n = bin(n)[2:]
#     n1 = f(n)
#     n2 = f(n1)
#     if int(n2,2) < 57:
#         print(int(n2,2))

# print("266-nomer+++3")
# for n in range(1,1000):
#     if n%3 == 0:
#         n1 = n//3
#     else:
#         n1 = n-1
#
#     if n1 % 5 == 0:
#         n2 = n1 // 5
#     else:
#         n2 = n1- 1
#
#     if n2%11 == 0:
#         n3 = n2//11
#     else:
#         n3 = n2-1
#     if n3 ==8:
#         print(n)

# print("264-nomer+++3")
# for n in range(1,1000):
#     if n%2 == 0:
#         n1 = n//2
#     else:
#         n1 = n-1
#
#     if n1 % 5 == 0:
#         n2 = n1 // 5
#     else:
#         n2 = n1- 1
#
#     if n2%7 == 0:
#         n3 = n2//7
#     else:
#         n3 = n2-1
#     if n3 ==6:
#         print(n)

# print("261-nomer+++61")
# k = 0
# for n in range(1, 600):
#     a = n
#     x = ''
#     while a > 0:
#         x = str(a % 2) + x
#         a = a // 2
#     p = x.rfind('0')
#     if x.count('0') != 0:
#         s = x[:p] + x[0:2] + x[(p + 1):]
#         x = s[::-1]
#         b = int(x, 2)
#         if b == 127:
#             print(n)


# print("255-nomer+++225")
# def f(n):
#     c1 = n.count('1')
#     c0 = n.count('0')
#     if c1 == c0:
#         return str(n) + str(n[-1])
#     elif c1 > c0:
#         return str(n) + '0'
#     elif c1 < c0:
#         return str(n) + '1'
#
#
# for i in range(1,500):
#     n = bin(i)[2:]
#     n1 = f(n)
#     n2 = f(n1)
#     n3 = f(n2)
#     if int(n3,2)%4 == 0 and int(n3,2)%8 != 0:
#         print(i)

# def f(n):
#     c1 = n.count('1')
#     c0 = n.count('0')
#     if c1 == c0:
#         return str(n) + str(n[-1])
#     elif c1 > c0:
#         return str(n) + '0'
#     elif c1 < c0:
#         return str(n) + '1'
#
#
# for i in range(65,500):
#     n = bin(i)[2:]
#     n1 = f(n)
#     n2 = f(n1)
#     n3 = f(n2)
#     if int(n3,2)%4 == 0:
#         print(i)
#         break


# print("238-nomer+++21")
# for n in range(1,1000):
#     n1 = str(n) + str(n)[-1]
#     n2 = bin(int(n1))[2:]
#     c1 = n2.count('1')
#     if c1%2==0:
#         n3 = str(n2) + '0'
#     else:
#         n3 = str(n2) + '1'
#     if int(n3,2) > 413:
#         print(n)
#         break



# print("235-nomer+++32")
# def f(n1):
#     c1 = n1.count('1')
#     c0 = n1.count('0')
#     if c1 > c0: return str(n1) + '0'
#     else:
#         return '11' + str(n1)
#
# for n in range(1,1000):
#     n1 = bin(n)[2:]
#     n2 = f(n1)
#     n3 = f(n2)
#     if int(n3,2) > 500:
#         print(n)

# print("234-nomer+++13")
# def alg(x):
#     s = bin(x)[2:]
#     if s.count('1') > s.count('0'):
#         s += '0'
#     else:
#         s += '1'
#     m = len(s) // 2
#     if len(s) % 2 == 0:
#         s = s[:m - 1] + s[m + 1:]
#     else:
#         s = s[:m - 1] + s[m + 2:]
#     return s
#
#
# MAX = 100000
# d = {}
# for N in range(10, MAX):
#     R = int(alg(N), 2)
#     d[R] = 1
#
# count = 0
# for R in range(50, 100):
#     if R in d:
#         print(R)
#         count += 1
#
# print(count)
# print("230-nomer+++12")
# c = 0
# for n in range(10,100000):
#     n = bin(n)[2:]
#     n1 = str(n) + str(n)[-2]
#     n2 = str(n1) + str(n1)[1]
#     if int(n2,2) >= 150 and int(n2,2) <= 200:
#         c+=1
# print(c)
# print("221-nomer+++15")
# c = 0
# for n in range(900,1000):
#     a = [int(i) for i in str(n)]
#     a.sort()
#     if a[0]!= '0':
#         res = int(str(a[2])+str(a[1])) - int(str(a[0])+str(a[1]))
#     elif a[0] == '0':
#         res = int(str(a[2]) + str(a[1])) - int(str(a[1]) + str(a[0]))
#     else:
#         res = 0
#     if res == 70:
#         c+=1
# print(c)

# print("208-nomer+++30")
# a = set()
# for n in range(20,50):
#     n1 = bin(n)[2:]
#     sum1 = n1.count('1')
#     n2 = str(n1) + str(sum1%2)
#
#     sum1 = n2.count('1')
#     n3 = str(n2) + str(sum1 % 2)
#     a.add(int(n3,2))
# print(len(a))
# print("192-nomer+++40")
# for n in range(1,1000):
#     n = bin(n)[2:]
#     c1 = n.count('1')
#     c0 = n.count('0')
#     if c1 > c0 :
#         n1 = str(n) + '1'
#     else:
#         n1 = str(n) + '0'
#     if int(n1,2) < 43:
#         print(int(n1,2))

# print("187-nomer+++")
# n = 193
# x = bin(n)[2:]
#
# x = '0' * (8 - len(x)) + x
#
# z = x.rfind('1')
# x_2 = ''
# for i in x[:z]:
#     if i == '1':
#         x_2 += '0'
#     else:
#         x_2 += '1'
# x_2 = x_2 + x[z:]
#
# print(int(x_2, 2))

# print("183-nomer+++")
# n = 204
# n1 = bin(n-1)[2:]
# n2 = '0'*(8-len(n1)) + n1
# s = ''
# for i in n2:
#     if i == '1':
#         s += '0'
#     else:
#         s += '1'
# res = int(s,2)
# print(res)

# print("181-nomer+++35")
# for n in range(0,1000):
#     n1 = bin(n)[2:]
#     n2 = '0'*(8-len(n1)) + n1
#     s = ''
#     for i in n2:
#         if i == '1':
#             s += '0'
#         else:
#             s += '1'
#     res = int(s,2)
#     res+=1
#     if res == 221:
#         print(n)

# print("175-nomer+++146")
# s = set()
# for i in range(20, 601):
#     s.add(int(format(i, 'b')[:-2], 2))
# print(len(s))

# print("168-nomer+++960")
# a = list()
# for i in range(1,1000):
#     n = str(bin(i)[2:])
#     a = [str(i) for i in n]
#     a.reverse()
#     s = ''.join(a).lstrip('0')
#     if int(s,2) == 15:
#         print(i)

# print("160-nomer+++117")
# for n in range(0,1000):
#     n1 = bin(n)[2:]
#     n2 = '0'*(8-len(n1)) + n1
#     s = ''
#     for i in n2:
#         if i == '1':
#             s += '0'
#         else:
#             s += '1'
#     res = int(s,2)
#     res1 = res-n
#     if res1 == 21:
#         print(n)
# print("155-nomer+++25")
# for n in range(1,1000):
#     n1 = bin(n)[2:]
#     if n%2 == 0:
#         n2 = str(n1) + '01'
#     else:
#         n2 = str(n1) + '10'
#     if int(n2,2) > 97:
#         print(n)
