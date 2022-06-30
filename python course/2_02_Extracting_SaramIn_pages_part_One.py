import requests
from bs4 import BeautifulSoup

saramin_result = requests.get("https://www.saramin.co.kr/zf_user/search/recruit?searchType=search&searchword=JAVA%2FJSP&loc_cd=101010&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&panel_type=&search_optional_item=y&search_done=y&panel_count=y&recruitPage=1&recruitSort=relation&recruitPageCount=40&inner_com_type=&show_applied=&quick_apply=&except_read=&ai_head_hunting=&mainSearch=n")

saramin_soup = BeautifulSoup(saramin_result.text, "html.parser")

pagination = saramin_soup.find("div", {"class":"pagination"})
#pages는 list라고 생각하면 된다.
pages = pagination.find_all('a')

spans = []
for page in pages:
  spans.append(page.find("span"))

print(spans)