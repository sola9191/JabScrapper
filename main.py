from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs
from save import save_to_file


##########################3function을 여러개로 쪼개서 indeed.py에 넣어놈
so_jobs = get_so_jobs()
indeed_jobs = get_indeed_jobs()
jobs = indeed_jobs+so_jobs
save_to_file(jobs)