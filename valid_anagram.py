from collections import Counter
def anagram(s,t):
  hashmap = Counter(s)
  for elem in t:
    if elem not in hashmap:
      return False
  return True
    
