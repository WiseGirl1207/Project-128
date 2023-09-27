from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import requests

START_URL2 = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"


page = requests.get(START_URL2)
soup = bs(page.text,'html.parser')
temp_list=[]

dwarf_table = soup.find('table')
table_rows = dwarf_table.find_all('tr')

for row in table_rows:
    dwarftd=soup.find_all("td")
    for tdtag in dwarftd:
        data = tdtag.text.strip()
        print(data)
        temp_list.append(data)


scrapped_data=[]

for i in range(0,len(temp_list)):
    star_names= temp_list[i][0]
    distance= temp_list[i][5]
    mass= temp_list[i][8]
    radius= temp_list[i][9]

    required_data=[star_names,distance,mass,radius]
    scrapped_data.append(required_data)

headers=['Star_names','Distance','Mass','Radius']
dwarf_df=pd.DataFrame(scrapped_data, columns=headers)
dwarf_df.to_csv('scrapped_data.csv', index=True, index_label="id")