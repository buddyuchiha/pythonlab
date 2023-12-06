from bs4 import BeautifulSoup
import requests 
import csv
from time import sleep
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.686 YaBrowser/23.9.5.686 Yowser/2.5 Safari/537.36"
  }

url = "https://www.gismeteo.ru/diary/4618/2023/11/"
response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.text, "lxml")
table = soup.find("table", align = "center")
lines = table.find_all("tr", align = "center") 
with open('dataset.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Day', 'Temperature Day', 'Wind Day', 'Night', 'Temperature Night', 'Wind Night'])
    for line in lines:
        information = line.find_all("td")
        values = [i.text for i in information]
        row = [values[1], values[2], values[5], values[6], values[7], values[10]]
        writer.writerow(row)
