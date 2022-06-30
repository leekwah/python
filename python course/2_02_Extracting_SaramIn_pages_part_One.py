import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://kr.indeed.com/jobs?q=python&limit=50&vjk=c36d1ebeab7c7987")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class":"pagination"})
#pages는 list라고 생각하면 된다.
pages = pagination.find_all('a')

spans = []
for page in pages:
  spans.append(page.find("span"))

print(spans)