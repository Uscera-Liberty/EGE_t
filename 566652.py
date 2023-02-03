# def f(s1 , s2 , c , m):
#     if s1+s2 >= 30:
#         return c%2 == m%2
#     if c == m:
#         return 0
#     h = [f(s1+1 , s2 , c+1 , m) , f(s1*2 , s2 , c+1 , m) ,f(s1 , s2+1, c+1 , m) , f(s1 , s2*2 , c+1 , m)]
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
# for s1 in range(1 , 30):
#     for s2 in range(1 , 30):
#         if s1 + s2 >= 30: continue
#         for m in range(1, 5): # от 1
#             if f(s1 ,s2 , 0 , m):
#                 if m == 2:
#                     print(s1, s2)
#                 else:
#                     break
def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


for i in range(834567, 1143211):  # диапазон
    a = div(i)
    f = 1
    for j in range(len(a) - 1):
        if a[j + 1] - a[j] != 2:
            f = 0
            break

    if f == 1 and len(a) > 1:  # проверка
        print(i, max(a))