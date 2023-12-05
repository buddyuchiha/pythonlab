from bs4 import BeautifulSoup
import requests 
import csv
from time import sleep

url = "https://www.gismeteo.ru/diary/4618/2022/1/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
table = soup.find("table", allign = "center")
string = soup.find("tr", allign = "center")
temperature = soup.find("td", class_ = "first_in_group")
pressure = soup.find("td")
wind = soup.find("span")