# for은 sequence대로 처리할 때 쓰인다.
days = ("Mon", "Tue", "Wed", "Thur","Fri")
# 아이템을 따로 각각 진행시킬 수 있다.

#for var in sequence:
  #var는 변수 이름이다. 아무거나 적어도 된다.
  # sequence도 위에 적어둔 sequence 중에 하나로 적는다.

for d5 in days:
  print(d5)
for number in [1, 2, 3, 4, 5]:
  print(number)

# for loop을 중간에 멈출 수 있다.

for stops in days:
  if stops is "Wed":
    break
  else:
      print(stops)

for letter in "nicolas":
  print(letter)