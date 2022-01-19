# 1.회사 명, a의 url 가져오기 (link)
# 2.회사 for문 돌면서 url 접근
# 3.알바내용 스크랩
# 급히하는 과제라 함수 한방에 때려넣음


from bs4 import BeautifulSoup
import requests
import csv

URL = "http://www.alba.co.kr"

result = requests.get(URL)
soup = BeautifulSoup(result.text, "html.parser")
brand_box = soup.find("div", {"id":"MainSuperBrand"})
brand_a = brand_box.find_all("a",{"class":"goodsBox-info"})

alba = []


###########     1번 start    ###################
for a in brand_a:
  brands = a.find_all("span",{"class":"company"})
  
  
  for brand in brands:
    if brand.string is not None:
      brand_name = brand.string
      alba.append({"company":brand_name,"link":a["href"]})
    else:
      brand_name = brand.find("strong").string + "test"
      alba.append({"company":brand_name,"link":a["href"]})

# print(alba)
########    1번 end    #############

#####  2번 start #####
for link in alba:
  link_url = (link["link"])
  result = requests.get(link_url)
  # result = requests.get("http://paris.alba.co.kr/job/brand/")
  soup = BeautifulSoup(result.text, "html.parser")
  normal_info = soup.find("div", {"id":"NormalInfo"})
  
  local=''
  title=''
  alba_time=''
  pay =''
  alba_date=''

  alba_detail = []

  for tr in normal_info.find_all("tr"):
    print(tr)
    if tr.find("td",{"class":"local"}) is not None:
      local = tr.find("td",{"class":"local"}).get_text()
    else:
      local = 'what'

    if tr.find("span",{"class":"company"}) is not None:
      title = tr.find("span",{"class":"company"}).get_text()

    else:
      title = 'happen'
    
    if tr.find("span",{"class":"time"}) is not None:
      alba_time = tr.find("span",{"class":"time"}).get_text()

    else:
      alba_time = 'in'

    if tr.find("span",{"class":"payIcon"}) is not None:
      pay = tr.find("span",{"class":"payIcon"}).get_text() + tr.find("span",{"class":"number"}).get_text()

    else:
      pay = 'code'

    if tr.find("td",{"class":"regDate"}) is not None:
      alba_date = tr.find("td",{"class":"regDate"}).get_text() 
    else:
      alba_date = '?'

    alba_detail.append({"local":local,"title":title,"time":alba_time,"pay":pay,"date":alba_date})

#### 2번 end #####


#### 3번 start ######
  file = open((link["company"])+".csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["place","title","time","pay","date"])
  
  for detail in alba_detail:
    
    writer.writerow(detail.values())

#### 3번 end #################






