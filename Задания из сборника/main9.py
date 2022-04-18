n = int(input())
a = []
c = 1
if n % 3 == 0 or n % 2 == 0 or n % 5 == 0:
    print(n)

else:
    for i in range(1 , n):
        if i% 3 == 0 or i % 2 == 0  or i % 5 == 0:
            c += 1

    print(c)
