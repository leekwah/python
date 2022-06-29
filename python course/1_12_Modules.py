# python에서 제일 자주 쓰이는 것은 module이다.
#만약에 import를 해야한다고 하면, 그냥 위에 import math라고 적으면 된다.
import math
print(math.ceil(1.2)) #올림
print(math.fabs(-1.2)) #절대값이 나온다.

# 특정 함수만 추출하는 방법
from math import ceil, fsum as sexy_sum
print(ceil(1.2))
print(sexy_sum([1, 2, 3, 4, 5, 6, 7]))

#내가 작성한 calculator.py 에서 함수를 불러올 때
from calculator import plus1, minus1
print (plus1(1,2))
print (minus1(1,2))

#어떻게 print함수가 무한 매개변수를 가질 수 있는지?
#django를 쓰기 위해서는 알아야함