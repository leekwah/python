# list를 이용해서, Sat를 추가하거나, Wed만 추출 할 수 있다.
# list의 기본 형태는 list = ["i","j","k","l"]식으로 구성된다.
days = ["Mon","Tue","Wed","Thur","Fri"]

# type은'list'가 된다.
print(type(days))
# Sun이 days에 없으므로, False가 나오게 된다.
print("Sun" in days)
# Mon은 days에 있으므로, True가 나오게 된다.
print("Mon" in days)
# days의 갯수가 궁금하면 len을 이용할 수 있다.
print(len(days))
# Index 때문에, 3을 적으면 4번째인 Thur이 추출된다.
print(days[3])
# Sat을 추가하려면 아래와 같이 적으면 된다.
# reverse를 적으면, 전환이 된다.
    # sequence.append(x)
print(days)
days.append("Sat")
days.reverse()
print(days)

# list는 수정가능하다 -> mutable