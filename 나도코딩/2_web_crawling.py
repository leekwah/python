import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = "https://kr.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
  result = requests.get(URL)
  soup=Beautifulsoup(result.text,"html.parser")
  next_button = soup.find("a", {"aria-label":"다음"})


#페이지가 5페이지까지만 있고 next버튼이 생겨버리면서 귀찮아짐>> next를 찾고 끝까지 가봄

  start = 0
  start_int_list = [0]
  count = 0

  while next_button:
    URL_last=f"https://kr.indeed.com/jobs?q=python&limit=50&start={str(start)}"
    result_last = requests.get(URL_last)
    soup_last = BeautifulSoup(result_last.text, "html.parser")
    next_button = soup_last.find("a",{"aria-label":"다음"})

    count = count + 1
    if next_button == None:
      break
#다음 버튼이 없을때까지 반복
    start = int(start) + 50
    start_int_list.append(int(start/50))

  print(count)


#마지막 count로 페이지 숫자 계산(과거에는 한 페이지에서 마지막페이지를 알 수 있었는데 지금은 '다음'을 눌러봐야 마지막페이지를 알 수 있음. 따라서 '다음'이 안나올 때까지 출력하여 확인 )



def extract_indeed_jobs(last_page):
  page = 0
  list = []

  while page < last_page:
    list.append(page)
  page = page + 1

for pages in list:
  result = requests.get(f"{URL}&start={pages*LIMIT}")
print(result.status_code)