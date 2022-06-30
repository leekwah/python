import requests


import requests
res = requests.get("http://google.com")
res.raise_for_status()
#응답 코드를 찍는 법
# print("응답코드 :", res.status_code) #200이면 정상

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
  f.write(res.text)