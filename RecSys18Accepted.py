from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

PATH = 'C:\\Users\\JihyunP\\Downloads\\chromedriver_win32\\chromedriver'
browser = webdriver.Chrome(PATH) # path where chromedriver_win32\\chromedriver exist
url ='https://recsys.acm.org/recsys18/accepted-contributions/'
browser.get(url)
html_source = browser.page_source
browser.quit()
soup = BeautifulSoup(html_source, 'html.parser')

spans = soup.find_all('span')
acceptedPapers = []
for i in range(1, len(spans), 2):
    acceptedPapers.append(spans[i].text)
acceptedPapers = acceptedPapers[:31]
