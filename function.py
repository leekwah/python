 #def -> definition
def chat():
    print("철수: 안녕? 넌 몇 살이니?")
    print("영희: 나? 나는 20살")

# 쉽게 여러번 나오게 하는 방법
chat()
#만약 철수 영희 대신에 알렉스 대신에 윤하로 바꾸고 싶을 때는?
def chat(name1, name2):
    print("%s: 안녕? 넌 몇 살이니?" % name1)
    print("%s: 나? 나는 30살" % name2)
#name1과 name2에 각각 이름을 입력하면, 원하는 결과를 출력할 수 있다.
chat("알렉스", "윤하")

# 나이를 추가하고 싶으면?
def chat(name1, name2, age): #def -> definition
    print("%s: 안녕? 넌 몇 살이니?" % name1)
    # %d는 숫자를 추가하는 것이다.
    print("%s: 나? 나는 %d살" % (name2, age))
chat("명수", "준하", 40)