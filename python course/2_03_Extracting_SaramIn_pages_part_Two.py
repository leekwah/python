import requests
from bs4 import BeautifulSoup

saramin_result = requests.get("https://www.saramin.co.kr/zf_user/search/recruit?searchType=search&searchword=JAVA%2FJSP&loc_cd=101010&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&panel_type=&search_optional_item=y&search_done=y&panel_count=y&recruitPage=1&recruitSort=relation&recruitPageCount=40&inner_com_type=&show_applied=&quick_apply=&except_read=&ai_head_hunting=&mainSearch=n")

saramin_soup = BeautifulSoup(saramin_result.text, "html.parser")

pagination = saramin_soup.find("div", {"class":"pagination"})
#pages는 list라고 생각하면 된다.
links = pagination.find_all('a')

pages = []
for link in links:
  # pages.append(link.find("span").string) #안에 있는 string만 가져오는 방법
  #pages.append(link.string) # 위에 있는 것과 같은 결과가 나온다.
  pages.append(int(link.string))

max_page = pages[-1]
print(pages[-1]) # 페이지에서 제일 큰 넘버를 찾는 법
