import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r"C:\Users\gkush\Downloads\chromedriver.exe")
url="https://datahack.analyticsvidhya.com/contest/all/"
r = requests.get(url)
driver.get(url)

content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,"html.parser")
upcoming=driver.find_elements_by_id('upcoming')
active=driver.find_elements_by_id('active')
up=[]
liv=[]
print("\n==================== Upcoming CHALLENGE ===================\n ")

for i in upcoming:
	up.extend(i.text.split("\n"))

showmore=driver.find_element_by_id("showMoreBtnActive").click()
sleep(2)

ch=[up[i:i + 5] for i in range(0, len(up), 5)]
for k in ch:
	print("\n=======================\n")
	for l in k[:5]:
		print(l)

print("\n\n==================== Live CHALLENGE ====================\n ")

for j in active:
	liv.extend(j.text.split("\n"))	

chn=[liv[j:j + 6] for j in range(1, len(liv), 6)]
for m in chn:
	print("\n=======================\n")
	for n in m[:6]:
		print(n)
 