import csv
# CSV? comma 

def save_to_file(jobs):
  file = open("jobs.csv", mode="w", encoding="utf-8") # 파일 열기
  # mode="w"의 쓰기

  #csv 작성
  writer = csv.writer(file)
  writer.writerow(["title", "company", "location","link"]) #무조건 한줄로
  for job in jobs:
    # print(job.values()) 
    # dictionary는 값만 불러올수있다
    # print(type(job.values()) # 한줄로넣으려면 우리는 list tyep이 필요한데 이거는 dict_values type임
    # print(list(job.values()))
    writer.writerow(list(job.values()))
  return 