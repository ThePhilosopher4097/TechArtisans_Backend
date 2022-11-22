from Scrapper.UserFunctions import user_func

url ='https://internshala.com/internships/'

user_func.get_url(url)
# get the beautified html file and extract job titles and job links
def get_soup(soup):
    
    job_title = [] #list to store job titles
    job_link = [] #list to store job links
    
    # Extracting links and job titles
    for div in divs:
        job_title.append(div.a.text)
        job_link.append(base+div.a.get('href'))
        
    return job_title, job_link


