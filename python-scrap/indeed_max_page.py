from bs4 import BeautifulSoup
import requests

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=javascript&limit={LIMIT}&filter=0"
def max_page_finder(start=0):
  indeed_url = f"{URL}&start={start * 50}"
  indeed_result = requests.get(indeed_url)

  indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
  pagination = indeed_soup.find("div", {"class": "pagination"})

  links = pagination.find_all("a")
  pages = []
  for link in links:
    if link.string:
      pages.append(int(link.string))
      max_page = pages[-1]

  next_button = pagination.find("a", {"aria-label": "다음"})
  if next_button:
    return max(max_page, max_page_finder(max_page + 1))
  else:
    return max_page


def extra_indeed_jobs(last_page):
#  for page in range(last_page):
  result = requests.get(f"{URL}&start={0*LIMIT}")
  soup = BeautifulSoup(result.text, "html.parser")
  result_div = soup.find_all("div",{"id":"mosaic-provider-jobcards"})
  
  for div in result_div:

    tables = div.find_all("table",{"class":"jobCard_mainContent"})
    for table in tables:
      test = table.find("div",{"class":"heading4"})
      find = test.find("span",title=True).string
      print(find)
    

      





