import csv
import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.chromium.webdriver import ChromiumDriver

url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("/chromedriver")

def main () :
  headers = ["Name","Distance","Mass","Radius"]
  starData = []
  soup = bs(browser.page_source, "html.parser")
  for i in soup.find_all("ul", attrs={"class","expoplanet"}) :
    liTag = i.find_all("li")
    templist = []
    for index, li in enumerate (liTag) :
      if index == 0 :
        templist.append(li.find_all("a")[0].contents[0])
      else :
        try :
          templist.append(li.contents[0])
        except :
          templist.append("")
    starData.append(templist)
  browser.find_element_by_xpath("//*[@id='primary_column']/footer/div/div/div/nav/span[2]/a").click()

main()