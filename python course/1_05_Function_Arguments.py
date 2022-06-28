# function에서 중요한 것은 def다. print는 그저 출력해주는 것일 뿐이다.
def say_hello(who):
  print("hello", who)

say_hello("kwanghoon")


def plus(a, b):
  print(a + b)

# 공백시에 0를 넣어라고 하면, 인수 1개만 넣어도 동작된다.
# b=0과 같은 것을 default value(기본값)라고 한다.
def minus(a, b=0):
  print(a - b)

plus(2, 5)
minus(2, 5)

# default value를 annoymous로 주고 say_hell0를 출력하면, hello annoymous로 출력된다.
def say_hell0(name="annoymous"):
  print("hello", name)
say_hell0()