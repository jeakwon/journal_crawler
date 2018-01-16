
# coding: utf-8

# In[188]:


#!/usr/bin/python
# -*- coding:utf-8 -*-
# parser.py
import csv
import requests
import bs4
import datetime
from setdate import upcoming_weekday # 내가 만든 초간단 라이브러리

# 시간 설정
datenow = datetime.datetime.now()
upcoming_friday = upcoming_weekday(datenow, 5).date() #금요일 설정
last_friday = upcoming_thursday - datetime.timedelta(7) #범위 시작 설정
upcoming_thursday = upcoming_weekday(datenow, 4).date() #범위 끝 설정

# HTTP GET Request
req = requests.get('http://www.nature.com/neuro/research')

# HTML 소스 가져오기
html = req.text
# HTTP Header 가져오기
header = req.headers
# HTTP Status 가져오기 (200: 정상)
status = req.status_code
print(status)
# HTTP가 정상적으로 되었는지 (True/False)
is_ok = req.ok
print(is_ok)

# 파싱 시작
soup = bs4.BeautifulSoup(html,'html.parser')

# Article 항목 불러오기
articles = soup.select('article')

# CSV 파일로 만들기
f = open(upcoming_friday.strftime('%Y%m%d')+'_Nat_Neuro.csv', 'w', encoding='utf-8')
wr = csv.writer(f)
for article in articles:

    # 크롤링 범위에 있는지 검토 (최근 1주일만 크롤링)
    PubDateNum = article.find("time")['datetime'],
    DATE = datetime.datetime.strptime(PubDateNum[0], '%Y-%m-%d').date()
    if not last_friday<DATE<upcoming_thursday:
        continue

    # 아티클 타입 추출 및 검토 (Correction type 제외)
    Type = article.find("span", attrs={"data-test": "article.type"}).text,
    if Type[0].find('Correction') != -1:
        continue
    
    # 아티클 출판일
    PubDateStr = article.find("time").text,
    
    # 아티클 제목
    Title = article.find("a").text.replace('\n','').replace('  ',''),
    
    # 아티클 설명
    Description = article.find("div", attrs={"itemprop":"description"}).text.replace('\n',''),


    wr.writerow([Type[0], PubDateStr[0],Title[0],Description[0]])
f.close()  
    

