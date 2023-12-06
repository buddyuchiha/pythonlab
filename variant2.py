from bs4 import BeautifulSoup
import requests 
import csv
from time import sleep
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.686 YaBrowser/23.9.5.686 Yowser/2.5 Safari/537.36"
}
year = 2008
month = 1
day = 1
with open('dataset.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Day', 'Temperature Day', 'Pressure Day','Wind Day', 'Temperature Night','Pressure Night', 'Wind Night'])
    
    while month <= 12:
        day = 1
        url = "https://www.gismeteo.ru/diary/4618/{}/{}/".format(year, month)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        table = soup.find("table", align="center")
        lines = table.find_all("tr", align="center") 
        
        for line in lines:
            information = line.find_all("td")
            values = [i.text for i in information]
            date = "{:02d}/{:02d}/{}".format(day, month, year)
            row = [date, values[1], values[2], values[5], values[6], values[7], values[10]]
            writer.writerow(row)
            day += 1
        
        month += 1
        if month > 12:
            month = 1
            year += 1
        print(url)
print("Ссылка: ", url)
