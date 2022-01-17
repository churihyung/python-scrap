from indeed_max_page import max_page_finder, extra_indeed_jobs


max_page = max_page_finder()

indeed_jobs = extra_indeed_jobs(max_page)
print(indeed_jobs)
