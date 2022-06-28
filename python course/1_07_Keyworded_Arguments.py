# positional arguments
def plus(a, b):
  return a - b

result = plus(b=30, a=1)
print(result)

# 인자의 순서는 상관이 없다.

# f를 적고 난 뒤에 {}로 감싸주면 된다. f는 format을 나타낸다. {}는 변수를 가려내기 좋은 방법이다.
def say_hello1(name, age):
  return f"hello {name} you are {age} years old"
def say_hello2(name, age):
  return "hello " + name + " you are " + age + " years old"

hello1 = say_hello1("kwah","29")
hello2 = say_hello2(name="kwah",age="29")
print(hello1)
print(hello2)

def say_hello3(name, age, are_from, fav_food):
  return f"hello {name} you are {age} you {are_from} you like {fav_food}"

hello3 = say_hello3(name="kwah", age="29", are_from="are from Korean", fav_food="Kimchi")
print(hello3)