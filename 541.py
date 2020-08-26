def reverse(s,k):
  kd = 2*k
  st = ''
  while s:
    if len(s) >= kd:
      new_s = s[:kd]
      s = s[kd:]
    else:
      new_s = s
      s= ''
    if len(new_s) < k:
      st += new_s[::-1]
    else:
      print('1',new_s[:k][::-1],'+',new_s[k:len(new_s)])
      st += new_s[:k][::-1] + new_s[k:len(new_s)]
  return st
print(reverse('abcdefg',3))