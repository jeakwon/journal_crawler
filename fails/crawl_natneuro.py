#!/usr/bin/python
# -*- coding:utf-8 -*-
# parser.py
import requests
import bs4

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

soup = bs4.BeautifulSoup(html,'html.parser')
print(soup)
# results = soup.select(
# 'p'
# )
# for result in results:
#     print(result.text)
