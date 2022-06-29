def plus1(a, b):
  if type(b) is str: # user gave b a string / str = string
    return None #ERROR
  else:
    return a + b

  return a + b

plus1(12, "10")

def plus2(a, b):
  if type(b) is int or type(b) is float: # user gave b a string / str = string
    return a + b
  else:
    return None #ERROR


plus2(12, "10")
print(plus2(12, 1.2))