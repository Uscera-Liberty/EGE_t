# def f(x):
#     if x <= 10: return x
#     elif 10 <= x <= 36: return x//4 + f(x-10)
#     else: return 2*f(x-5)
# print(f(100))
# from math import factorial
# print((factorial(3303)+3303)/(factorial(3300)+3300))
# print(2022*2023*2021


def f(s1 , s2 , c , m):
    if s1+s2>= 40: return c%2 == m%2
    if c==m: return 0

    h = [f(s1+1 , s2 ,c+1 , m) , f(s1*2 , s2 ,c+1 , m) , f(s1 , s2+1 ,c+1 , m) , f(s1 , s2*2 ,c+1 , m)]
    return any(h) if (c+1)%2 == m%2 else all(h)

for s1 in range(1 , 25):
    for m in range(1 , 5):
        if f(s1,14,0, m) == 1:
            print(s1 , m)
            break



# res = 0
# with open("24-s1.txt") as file:
#     for line in file:
#         res += line.count("K") > line.count("U")
# print(res)
a = []
for m in range(0 , 30, 2):
    for n in range(1 , 30 , 2):
        if 100_000_000 <= 2**m*5**n <= 300_000_000:
            a.append([2**m*5**n , m+n])
print(*sorted(a))

