# import copy
# s = []
# for i in input().split():
#     if i.count("#") == 1 and i[0] == "#":
#         s.append(i)
# s = sorted(s)
# s2 = sorted(set(s))
# print(len(s2))
# for i in s2:
#     print(i,s.count(i))

divs = int(input())
if divs % 2 :
    n = 1
    while True:
        if int(n**0.5) == n**0.5 :
            count_of_dividers = 1
            for i in range(1, int(n**0.5)):
                if n % i == 0:
                    count_of_dividers += 2
            if count_of_dividers == divs:
                print(n)
                break
        n += 1
else :
    n = divs
    while True:
        if int(n**0.5) != n**0.5 :
            count_of_dividers = 0
            for i in range(1, int(n**0.5) + 1) :
                if n % i == 0 :
                    count_of_dividers += 2
            if count_of_dividers == divs:
                print(n)
                break
        n += 2