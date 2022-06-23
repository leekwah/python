students = ["egoing", "sori", "maru", "kwah", "eeaoo"]
grades = [2,1,4]
print("students[1]", students[1])

print("len(students)", len(students)) #students가 몇 개의 리스트로 이루어져있는 지 알고 싶을 때
print("min(grades)", min(grades)) #grades 값 중에 가장 작은 값을 알고 싶을 때
print("max(grades)", max(grades)) #grades 값 중에 가장 큰 값을 알고 싶을 때
print("sum(grades)", sum(grades)) #grades 총 합

#통계
import statistics
print("statistics.mean(grades)", statistics.mean(grades)) #평균
#이외에도 중앙값, 표준편차 등 쉽게 구할 수 있음

import random
print("random.choice(students)",random.choice(students)) #

