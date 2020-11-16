import requests #파이썬에서 http요청을 보내는 모듈
from bs4 import BeautifulSoup

LIMIT = 50
INDEED_URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={LIMIT}"

#예를들어 'JAVA'라고 JOB을 검색시에 몇페이지가 나오는지 알아내는 METHOD
def extract_indeed_page(): 
  result = requests.get(INDEED_URL)

  # print(result.text) # response [200] 이라고 왔는데 ok라는 뜻임
  ############## 여기까지는 url 을 통해 html 가져오기임
  ## beautifusoup html 정보 추출하는데 좋은 라이브러리
  ## 이걸 이용해서 페이지 갯수를 알아낼것임
  ## soup --> 데이터 추출

  soup = BeautifulSoup(result.text, "html.parser")
  # 주소 넣어주고 html.parser 쓸거라고 작성

  pagination = soup.find("div", {"class": "pagination"})
  #find() : 해당조건에 맞는 하나의 태그를 가져온다.
  links = pagination.find_all('a')
  #find_all() : 해당족너에 맞는 모든태그를 가져온다. 
  # print(type(pages)) #list type임

  pages = [] # 빈배열 생성
  for link in links[0:-1]:
    pages.append(int(link.find("span").string)) # <span>부터 list에넣어줌
    
  # pages.append(link.string)해도 똑같은 결과나옴
  # links[0:-1]의 의미: list의 첫번째부터 마지막에서 -1 뺀 length 까지 출력 ==> list배열의 마지막꺼는 출력안됨
  # page숫자를 list로 가져왔는데 type이 String라서 (int)로 형변환
  #print(pages) 
  #### 페이지중에서 가장큰 숫자 가져오는 작업
  max_page = pages[-1] #10
  #print(range(max_page)) # range(0, 10)로 출력됨

  return max_page

## 작성한 코드를 function으로 처리해서 main에서 이 function 쓰는 방식으로 처리함

# 마지막 페이지가 뭔지 확인하고 job list 뽑아내는 함수
def extract_indeed_jobs():
  jobs = [] # 잡을 넣을 빈 리스트만들기

  #for page in range(last_page):
  result = requests.get(f"{INDEED_URL}&start={0*LIMIT}")
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
 
  for result in results:
     # job title 가져오기
    title = result.find("h2", {"class": "title"}).find("a")["title"]
    # company name 가져오기
    # 어떤것은 링크가 걸려있고 어떤건 안걸려있음
    company = result.find("span", {"class":"company"})
    if company.find("a") is not None: # 링크가 있으면
      company = company.find("a").string #a태그안의 글자출력
    else: 
      company = company.string  #span태그안의 글자출력
    company = company.strip()
    # strip() 사용하면 빈칸을 지워준다
    
  return jobs