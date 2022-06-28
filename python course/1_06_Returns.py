def p_plus(a, b):
  print(a + b)

def r_plus (a, b):
  return a + b
  # return은 값을 return하고, function을 종료한다. 아래의 "something", "True"는 나오지 않는다.
  print("something", True)

p_result = p_plus(2, 3)
r_result = r_plus(2, 3)

# function이 return function값으로 치환되어 졌기 때문에, 먼저 r_result가 5로 나오고,
# p_result는 None으로 값이 나오지 않았다.
print(p_result, r_result)