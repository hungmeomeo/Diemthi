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

s = Service("C:\webdriver\chromedriver.exe")
browser = webdriver.Chrome(service=s)
a = []
b = []
c = []
d = []
e = []
f = []
x = []

# for i in range(52012712, 52012714):
#     url = "https://thanhnien.vn/giao-duc/tuyen-sinh/2022/tra-cuu-diem-thi-thpt-quoc-gia.html"
#     browser.get(url)
#     end = browser.find_element("xpath", "/html/body/div[1]/div/div[1]/div[5]/div[2]/div/div/div[1]/div/input")
#     end.send_keys(str(i))
#
#     btn = browser.find_element("xpath", "/html/body/div[1]/div/div[1]/div[5]/div[2]/div/div/div[3]/div[2]/a")
#     btn.click()
#
#     toan = browser.find_elements("xpath", "/html/body/div[1]/div/div[1]/div[5]/div[3]/table/tbody/tr/td[7]")
#     van = browser.find_elements("xpath", "/html/body/div[1]/div/div[1]/div[5]/div[3]/table/tbody/tr/td[8]")
#     anh = browser.find_elements("xpath", "/html/body/div[1]/div/div[1]/div[5]/div[3]/table/tbody/tr/td[17]")
#     ly = browser.find_elements("xpath", "/html/body/div[1]/div/div[1]/div[5]/div[3]/table/tbody/tr/td[9]")
#     hoa = browser.find_elements("xpath", "/html/body/div[1]/div/div[1]/div[5]/div[3]/table/tbody/tr/td[10]")
#     sinh = browser.find_elements("xpath", "/html/body/div[1]/div/div[1]/div[5]/div[3]/table/tbody/tr/td[11]")
#     for toan1 in toan:
#         a.append(toan1.text)
#     for van1 in van:
#         b.append(van1.text)
#     for anh1 in anh:
#         c.append(anh1.text)
#     for ly1 in ly:
#         d.append(ly1.text)
#     for hoa1 in van:
#         e.append(hoa1.text)
#     for sinh1 in sinh:
#         f.append(sinh1.text)
#
# data = {
#     "Toan": a,
#     "Van": b,
#     "Anh": c,
#     "Ly": d,
#     "Hoa": e,
#     "Sinh": f,
# }
#
# df = pd.DataFrame(data)
# df.to_csv("diemthi.csv", index=False)

# s = Service("C:\webdriver\chromedriver.exe")
# driver = webdriver.Chrome(service=s)
# url = 'https://dantri.com.vn/giao-duc-huong-nghiep/tuyen-sinh/tra-cuu-diem.htm?fbclid=IwAR2K0_jfVavtRjL7frQjWrrkXAfcbN44JsEiUGaVzRb08wPAGcxrm3DWyWk'
# driver.get(url)
# diemthi = []

# Loop through all students
# for sbd in range(52000001, 52000014):
#     # Enter ID
#     description = driver.find_element("xpath", '/html/body/main/div[2]/div/div[1]/div/div/div[1]/input')
#     description.clear()
#     btn = browser.find_element("xpath", "/html/body/main/div[2]/div/div[1]/div/div/div[1]/input")
#     btn.click()
#
#     # Page source
#     html = driver.page_source
#     page = BeautifulSoup(html, 'lxml')
#
#     # Extract grades
#     rows = page.find('tbody', {'id': 'resultcontainer'}).findAll('tr')
#     for row in rows:
#         monthi = row.findAll('td')
#         diem = {}
#         if (len(monthi) == 18):
#             diem['SBD'] = monthi[3].text
#             diem['Toan'] = monthi[6].text
#             diem['Van'] = monthi[7].text
#             diem['Ly'] = monthi[8].text
#             diem['Hoa'] = monthi[9].text
#             diem['Sinh'] = monthi[10].text
#             diem['Anh'] = monthi[16].text
#             diemthi.append(diem.copy())
#
# # End session
# driver.quit()
#
# # Export as csv
# keys = diemthi[0].keys()
# a_file = open("diemthi.csv", "w")
# dict_writer = csv.DictWriter(a_file, keys)
# dict_writer.writeheader()
# dict_writer.writerows(diemthi)
# a_file.close()

import requests

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