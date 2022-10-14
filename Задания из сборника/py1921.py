print('++++19++++')
def f(x,p):
  if x >= 65 and p == 3:
    return True
  else:
    if x< 65 and p == 3:
      return False
  return f(x+1,p+1) or f(x*3,p+1)

for i in range(1,65):
  if f(i,1):
    print(i)
    break
print('++++20++++')

def f(x,p):
  if x >= 65 and p == 4:
    return True
  else:
    if x< 65 and p == 4:
      return False
    elif x >= 65:
        return False

  if p % 2 == 1:
    return f(x+1,p+1) or f(x*3,p+1)
  else:
    return f(x + 1,p + 1) and f(x * 3, p + 1)

for i in range(1,65):
  if f(i,1):
    print(i)

print('++++21++++')

def f(x,p):
  if x >= 65 and (p == 3 or p == 5):
    return True
  else:
    if x < 65 and p == 5:
      return False
    else:
      if x >= 65:
        return False
  if p % 2 == 0:
    return f(x+1,p+1) or f(x*3,p+1)
  else:
    return f(x + 1, p + 1) and f(x * 3, p + 1)

def f1(x,p):
  if x >= 65 and p == 3:
    return True
  else:
    if x < 65 and p == 3:
      return False
    else:
      if x >= 65:
        return False
  if p % 2 == 0:
    return f1(x+1,p+1) or f1(x*3,p+1)
  else:
    return f1(x + 1, p + 1) and f1(x * 3, p + 1)

for i in range(1,65):
  if f(i,1):
    print(i)
print("==========")
for i in range(1,65):
  if f1(i,1):
    print(i)