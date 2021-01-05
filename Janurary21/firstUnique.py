def unique(string):
   
  char_array = [0] * 256

  for char in string:
    char_array[ord(char)] +=1
  
  for i in range(len(string)):
    if char_array[ord(string[i])] == 1:
      return i
  return -1
