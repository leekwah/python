def age_check(age):
  print(f"you are {age}")
  if age < 18:
    print("you can't drink")
  # else if와 같은 것이다.
  elif age == 18:
    print("you are new to this!")
  # and 는 두 조건 중 하나만 False가 되어도 성립되지 않는다.
  # (둘 다 True여야 한다.)
  elif age > 20 and age < 25:
    print("you are still kind of young")
  else:
    print("enjoy your drink")





age_check(18)
age_check(23)