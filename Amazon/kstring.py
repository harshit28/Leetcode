#https://leetcode.com/discuss/interview-question/370112
def unique(s,k):
  ls= []
  ms= s
  for i in range(1,len(s)):
    ns= ms[i:i+k]
    if k == len(set(ns)) and ns not in ls:
          ls.append(ns)

  return ls

s = 'awaglknagawunagwkwagl'
print(unique(s,4))