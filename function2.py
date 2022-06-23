def dsum(a, b):
    result = a + b
    #print 대신에 return을 시킨다.
    return result

d = dsum(4, 5)
print(d)

#결과값이 return이 아닌, print를 function을 실행시키면, 나오게 하는 것
#function 안에 값이 필요한 function은 return statement로 끝내야한다.
#그냥 print로 끝내면, None이 뜬다.