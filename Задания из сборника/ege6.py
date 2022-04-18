
for i in range(377763879,377763679,-1):
  x=i
  n = 4321
  while (x+n)//1000 < 378128:
    x = x - 2
    n = n + 4
  if n//1000 == 724:
    print(i)
#724
