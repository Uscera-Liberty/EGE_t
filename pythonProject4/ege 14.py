# print("316")
# s = 8**20 + ((8**22 - 8**17)*(8**13 + 8**16))
# s1 = ''
# while s:
#     s1 = str(s%8) + s1
#     s//=8
# s2 = s1.replace('7' , '0')
# sums = 0
# print(s)
# for i in s2:
#     sums += int(i)
# print(sums)

from math import sqrt
divs = []
n = 100
print(sqrt(n))
for d in range(2,int(sqrt(n))+ 1):
    if n % d == 0:
        divs.append(d)
        divs.append(n / d)
print(divs)