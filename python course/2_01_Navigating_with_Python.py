# 처음에 pip로 install을 해준다.
# (repl.it에서는 안해도 됨. package로 검색)
# pip install requests
# pip install request2
# pip install beautifulsoup4

import requests

#sth.sth 이런식으로 쓰는 이유는 다음번에 가르쳐주겠다고 했음.
indeed_result = requests.get("https://www.jobkorea.co.kr/Search/?stext=java&local=I000%2CH000")

print(indeed_result)
# <Response [200]>
# 위의 뜻은 OK

# 모든 HTML을 가져온 것이다.
print(indeed_result.text)

# 가져올 것은, 
# beautifulsoup