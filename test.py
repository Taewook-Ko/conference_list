from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

browser = webdriver.Chrome('PATH') # path where chromedriver_win32\\chromedriver exist
url = 'https://cse.snu.ac.kr/node/29041'
browser.get(url)
html_source = browser.page_source
browser.quit()
soup = BeautifulSoup(html_source, 'html.parser')
tds = soup.find_all('td')

lists = []
for i in range(0,len(tds),2):
    lists.append(tds[i].text)

df = pd.DataFrame(lists)
df.to_csv(PATH+'\\test.csv')  # path where to store csv file
