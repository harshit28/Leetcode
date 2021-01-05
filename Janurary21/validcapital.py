def cap(string):
  if string.isupper():
    return True

  if string.islower():
    return True

  if not string[0].isupper():
    return False

  else:
    for char in string[1:]:
      if char.isupper():
        return False
  return True
