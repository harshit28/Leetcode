def checkpal(pal):
  n=len(pal)
  if n % 2 ==0:
    return pal == pal[::-1]
  else:
    mid = n // 2
    prev, nex = pal[:mid], pal[mid+1:]
    return prev == nex[::-1]

def validpal(string):
    for i in range(len(string)):
        prev, nex = string[:i] , string[i+1:]
        if checkpal(prev+nex):
          return True
    return False
