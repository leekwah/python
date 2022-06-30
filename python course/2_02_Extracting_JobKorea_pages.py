import requests
from bs4 import BeautifulSoup

incruit_result = requests.get("https://job.incruit.com/jobdb_list/searchjob.asp?rgn2=11&kw=java")

incruit_soup = BeautifulSoup(incruit_result.text, "html.parser")

tplPagination = incruit_soup.find("p", {"class":"sqr_paging"})
#pages는 list라고 생각하면 된다.
pages = tplPagination.find_all('a')

# empty list를 제작할 것이다.
spans = []
for page in pages:
    # spans.append(page.find("strong")) #여기까진 아무일도 안일어남
    spans.append(page.find("span")) #여기까진 아무일도 안일어남
# print(spans) #리스트를 제작해서, 출력된다.
print(spans[0:9])
