import re
import string
from collections import Counter
def mostCommonWord(paragraph,banned) -> str:
  dic = {}
  paragraph = paragraph.lower()

  res=  re.findall(r'\w+', paragraph) 
  print(res)
  for r in res:
    if r not in banned:
      if r in dic:
        dic[r] += 1
      else:
        dic[r] = 1
  print(dic)
  return max(dic,key=dic.get)

para = "a, a, a, a, b, b, b, c, c"

banned =["a"]
print(mostCommonWord(para,banned))
