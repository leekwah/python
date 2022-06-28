#for, while 둘 다 반복문

#i라는 변수가 넣는 것 -> 10번 반복하는 것
for i in range(3):
    print(i)
    print("철수: 안녕 영희야 뭐해?")
    print("영희: 안녕 철수야, 그냥 있어.")

#i를 코딩했지만, 0부터 시작됨 -> index라서 그렇다.

#while은 for와 다르게 조건을 달 수 있다.
i = 0
while i < 3:
    print(i)
    print("철수: 안녕 영희야 뭐해?")
    print("영희: 안녕 철수야, 그냥 있어.")
    i = i + 1

# while이 for보다 쓰기 편한 것 -> 무한루프
while True:
    print(i)
    print("철수: 안녕 영희야 뭐해?")
    print("영희: 안녕 철수야, 그냥 있어.")
    i = i+1
# break와 continue
    if i>10:
        break

for i in range(3):
    print(i)
    print("철수: 안녕 영희야 뭐해?")
    print("영희: 안녕 철수야, 그냥 있어.")

    if i == 1:
        continue

    print("워니: 안녕 철수와 영희야!")
    #이럴 경우, 1일 경우에는 워니가 말을 하지 않는다. 0과 2일 때는 말을 한다.
