from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import time
import requests

s = Service("C:\webdriver\chromedriver.exe")
browser = webdriver.Chrome(service=s)
a = []
b = []
c = []
d = []
e = []
f = []
x = []

for i in range(52000001, 52012714):
    print(i)
    x.append(i)
    scraping_url = "https://dantri.com.vn/thpt/1/0/99/" + \
                   str(i) + "/2022/0.2/search-gradle.htm"
    payload = {}
    headers = {}
    response = requests.request(
        "GET", scraping_url, headers=headers, data=payload)
    info = response.json()['student']
    toan = info['toan']
    a.append(str(toan))
    ly = info['vatLy']
    d.append(str(ly))
    hoa = info['hoaHoc']
    e.append(str(hoa))
    sinh = info['sinhHoc']
    f.append(str(sinh))
    van = info['van']
    b.append(str(van))
    anh = info['ngoaiNgu']
    c.append(str(anh))


data = {
    "SBD":x,
    "Toan": a,
    "Van": b,
    "Anh": c,
    "Ly": d,
    "Hoa": e,
    "Sinh": f,
}

df = pd.DataFrame(data)
df.to_csv("diemthi.csv", index=False)
