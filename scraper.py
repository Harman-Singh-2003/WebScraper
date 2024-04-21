from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import csv

options = Options()
# options.headless = True
options.arguments.append("--disable-web-security")
 
driver = webdriver.Chrome(options=options, executable_path='chromedriver location')
# driver = webdriver.Chrome(executable_path='C:\\Users\\Harman Singh\\Downloads\\chromedriver_win32')
driver.get("filepath to html")
sleep(5)

# while (driver.find_elements(By.ID, 'moreresultbutton')):
#     driver.find_elements(By.ID, 'moreresultbutton')[0].click()
#     sleep(5)

# a= driver.execute_script('showmore();')
# sleep(5)
# a=driver.execute_script('showmore();')
# sleep(5)

articles = driver.find_elements(By.TAG_NAME, "article")
links = []
print(len(articles))

for article in articles:
    links.append(article.find_element(By.TAG_NAME, 'a').get_attribute('href'))

job_info = []

# Open a new window
# driver.execute_script("window.open('');")
# # Switch to the new window
# driver.switch_to.window(driver.window_handles[1])
# driver.get("https://www.jobbank.gc.ca/jobsearch/jobsearch?searchstring=cook&locationstring=&sort=M")
# sleep(3)
# driver.switch_to.window(driver.window_handles[0])

# driver.close()
# driver = webdriver.Chrome(options=options, executable_path='C:\\Users\\Harman Singh\\Downloads\\chromedriver_win32')

links = links[0:len(links)]

for link in links:
    driver.get(link)
    sleep(3)
    job_dict = {}
    job_dict['job title'] = driver.find_element(By.XPATH, '//*[@id="wb-cont"]/span').text
    job_dict['company'] = driver.find_element(By.XPATH, '//*[@id="wb-auto-2"]/div[1]/div[1]/p/span[3]/span[2]/span/strong').text
    
    driver.find_element(By.ID, 'applynowbutton').click()    
    sleep(2)
    
    job_dict['email'] = driver.find_element(By.XPATH, '//*[@id="howtoapply"]/p[1]/a').text
    job_info.append(job_dict)

keys = job_info[0].keys()
with open('Developer Jobs2.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writerows(job_info)

driver.quit()

# Developer
# https://www.jobbank.gc.ca/jobsearch/jobsearch?fcid=4824&fcid=6906&fcid=6932&fcid=12083&fcid=20942&fcid=20944&fcid=296140&fn=2174&fn=2175&term=developer&sort=M&fprov=ON&fsrc=21

# Engineer
# https://www.jobbank.gc.ca/jobsearch/jobsearch?fn=2132&fn=2133&fn=2146&fn=2147&fn=2173&term=engineer&sort=M&fprov=ON&fsrc=21