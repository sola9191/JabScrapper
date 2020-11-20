import requests
from bs4 import BeautifulSoup

#순서
#1. page가져오기
#2. request만들기
#3. job 추출하기
URL = "https://stackoverflow.com/jobs?q=python&sort=i"


# 마지막 page number 구하기
def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div", {"class": "s-pagination"}).find_all('a')
  last_page = pages[-2].get_text(strip=True)  # 빈칸없애줌
  return int(last_page)


def extract_jobs(last_page):
  jobs = []

  for page in range(last_page):
    print(f"Scrapping S0: page: {page}")
    result = requests.get(f"{URL}&pg={page+1}")
    #print(result) #200
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "-job"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
    
  
  return jobs



#일자리 추출
def extract_job(html):
    title = html.find("div", { "class": "grid--cell fl1"}).find("h2").find("a")["title"]

    # list에 요소가 2개이상인지 알고있을때 따로불러올수있음
    # unpacking value
    company, location = html.find("div", {
        "class": "grid--cell fl1"
    }).find("h3").find_all(
        "span", recursive=False)  
        # 이걸 안쓰면 span안에 있는 span도 가져와서 이걸써줬음
        # ==> 첫번째 단계의 span만 가져옴
    company = company.get_text(strip=True)
    location = location.get_text(strip=True)
    
    job_id = html["data-jobid"]
   
    return {"title": title, "company": company, "location": location, "apply_links": f"https://stackoverflow.com/jobs/{job_id}" }




def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs