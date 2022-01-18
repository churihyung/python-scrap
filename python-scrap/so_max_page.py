from bs4 import BeautifulSoup
import requests

URL = f"https://stackoverflow.com/jobs?q=javascript"


def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div", {"class":"s-pagination"}).find_all("a")
  print(pages)

def get_so_job():
  last_page = get_last_page()
  print(last_page)
  return []