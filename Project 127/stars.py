from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("chromedriver copy")
browser.get(START_URL)

time.sleep(10)

scrapped_data = []

def scrape(): 
    soup = BeautifulSoup(browser.page_source, "html.parser")
    startable=soup.find("table", attrs={"class", "wikitable"})
    starbody=soup.find("tbody")
    startr=soup.find_all("tr")
    for row in startr:
        startd=soup.find_all("td")
        templist=[]
        for tdtag in startd:
            data = tdtag.text.strip()
            print(data)
            templist.append(data)
        scrapped_data.append(templist)

stars_data=[]

for i in range(0,len(scrapped_data)):
    star_names= scrapped_data[i][1]
    distance= scrapped_data[i][3]
    mass= scrapped_data[i][5]
    radius= scrapped_data[i][6]
    lum= scrapped_data[i][7]

    required_data=[star_names,distance,mass,radius,lum]
    stars_data.append(required_data)

headers=['Star_names','Distance','Mass','Radius','Luminosity']
star_df_1=pd.DataFrame(stars_data, columns=headers)
star_df_1.to_csv('scrapped_data.csv', index=True, index_label="id")


