# ==294===258
# for n in range(250 ,400):
#     s = '5' * n
#     while '55555' in s :
#         s = s.replace('55555' , '88' , 1)
#         s = s.replace('888' , '555' , 1)
#     if s.count('5') == 1:
#         print(n)
#         break

# ==290===311
# temp = 0
# max = 0
# for n in range(300 ,1000):
#     s = '5' * n
#     while '55555' in s :
#         s = s.replace('55555', '88', 1)
#         s = s.replace('888', '55', 1)
#     if s.count('5') > max:
#         max = s.count('5')
#         temp = n
#
# print(temp)

#===282===100
# for n in range(100 , 1000):
#     s = '8' * 100
#     while '555' in s or '888'in s:
#          s = s.replace('555' , '8' ,1)
#          s = s.replace('888' , '55' , 1)
#     print(s)
#     if s.count('5') == 0:
#         print(n)
#         break
# temp = 0
# for x in range(1,1000):
#     for y in range(1,1000):
#         s = '1' * x + '3' * y
#         while '12' in s or '13' in s:
#             s = s.replace('12', '21', 1)
#             s = s.replace('31', '23', 1)
#             s = s.replace('13', '23', 1)
#         a = [int(i) for i in s]
#         if sum(a) != 404 and len(a) < temp:
#             break
#         elif sum(a) == 404 and len(a) > temp:
#             temp = len(a)
#         else:
#             break
# print(temp)

#===270===17
# for x1 in range(0,200):
#     for x2 in range(0,200):
#         for x3 in range(0,200):
#             if (2*x2 + x3 == 31) and (x2+ x3 == 24) and (x1 + 2*x2 + x3 == 46):
#                 print(x3)
# max = 0
# temp = dict()
# for n in range(100 ,1000):
#     s = n * '1'
#     while '333' in s or '111' in s:
#         s = s.replace('333' , '11' , 1)
#         s = s.replace('111' , '3' , 1)
#     if int(s) > max:
#         max = int(s)
# print(max)
# for n in range(100 ,1000):
#     s = '1' * n
#     while '333' in s or '111' in s:
#         s = s.replace('333' , '11' , 1)
#         s = s.replace('111' , '3' , 1)
#     if s == '3311':
#         print(n)
#         break
#

# s = '>' + 20 *'1' + 40 * '3' + 15 * '2' + '<'
# while '><' not in s:
#     s = s.replace('>1', '3>')
#     s = s.replace('>2', '2>')
#     s = s.replace('>3', '1>')
#     s = s.replace('3<', '<1')
#     s = s.replace('2<', '<3')
#     s = s.replace('1<', '<2')
# a = [int(i) for i in s if i != '<' and i != '>']
# print(sum(a))

# max = 10000000000000
# temp = 0
# for n in range(100 ,1000):
#     s = n * '1'
#     while '111' in s:
#         s = s.replace('111' , '2' , 1)
#         s = s.replace('2222' , '333' , 1)
#         s = s.replace('33' , '1' , 1)
#     if s.count('1') < max:
#         max = s.count('1')
#         temp = n
# print(temp)

for n in range(80 ,200):
    s = n * '1'
    while '111' in s:
        s = s.replace('111' , '2' , 1)
        s = s.replace('222' , '1' , 1)
    if s == '21':
        print(n)
        break


