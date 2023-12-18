from bs4 import BeautifulSoup
import requests 
import csv
from time import sleep

def get_url(year, month): #запрос URL
    url = "https://www.gismeteo.ru/diary/4618/{}/{}/".format(year, month)
    return url

def get_data(url, headers): #полчаем soup
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    return soup

def get_parse_table(soup): #находим таблицу и строки, начало парсинга
    table = soup.find("table", align="center")
    lines = table.find_all("tr", align="center")
    return lines

def parse_line(line): #парсинг строки
    information = line.find_all("td")
    values = [i.text for i in information]
    return values

def write_row(writer, date, values): #запись данных в csv
    row = [date, values[1], values[2], values[5], values[6], values[7], values[10]]
    writer.writerow(row)

def main ():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.686 YaBrowser/23.9.5.686 Yowser/2.5 Safari/537.36"
    }
    year = 2008
    month = 1
    day = 1
    flag = 0
    with open('dataset.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Day', 'Temperature Day', 'Pressure Day','Wind Day', 'Temperature Night','Pressure Night', 'Wind Night'])
        while month <= 12:
            while flag < 1:
                day = 10
                url = get_url(year, month)
                soup = get_data(url, headers)
                lines = get_parse_table(soup)
                for line in lines:
                    values = parse_line(line)
                    date = "{}-{:02d}-{:02d}".format(year, month, day)
                    write_row(writer, date, values)
                    day+=1
                month+=1
                if month == 2:
                    flag +=1
            day = 1
            url = get_url(year, month)
            soup = get_data(url, headers)
            lines = get_parse_table(soup)
            for line in lines:
                values = parse_line(line)
                date = "{}-{:02d}-{:02d}".format(year, month, day)
                write_row(writer, date, values)
                day += 1
            month += 1
            if month > 12:
                month = 1
                year += 1
                
