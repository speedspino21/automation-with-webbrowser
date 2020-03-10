import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import codecs
from openpyxl import load_workbook
st = 1
options = webdriver.ChromeOptions ()
# options.add_argument ('window-size=1920x1080')
options.add_argument ('--start-maximized')
options.add_argument('--log-level=3')
options.add_argument('--disable-extensions')
driver = webdriver.Chrome('chromedriver(2).exe', chrome_options=options)
# driver.get("http://lifeinsuranceusa.hindiform.com")
driver.get("http://lifeinsuranceusa.hindiform.com")
time.sleep(st)
driver.find_element_by_xpath("//div[@class='td-ss-main-sidebar']/aside/ul/li[1]/a").click()
time.sleep(3)
# driver.execute_script("window.scrollTo(0, 500)")
# driver.execute_script("window.scrollTo(501, 1000)")    
driver.execute_script("window.scrollTo(0, 500);")
time.sleep(5)
driver.execute_script("window.scrollTo(500, 1000);")
time.sleep(5)
driver.execute_script("window.scrollTo(1000, 1500);")
time.sleep(5)
driver.execute_script("window.scrollTo(1500, document.body.scrollHeight);")
time.sleep(5)
driver.execute_script("window.scrollTo(document.body.scrollHeight, 1500);")
time.sleep(5)
driver.execute_script("window.scrollTo(1500, 1000);")
time.sleep(5)
driver.execute_script("window.scrollTo(1000, 500);")
time.sleep(5)
driver.execute_script("window.scrollTo(500, 0);")
time.sleep(30)
driver.find_element_by_xpath("//div[@class='td-ss-main-sidebar']/aside/ul/li[2]/a").click()

time.sleep(10)
driver.find_element_by_xpath("//div[@class='td-ss-main-sidebar']/aside/ul/li[3]/a").click()
time.sleep(10)
driver.find_element_by_xpath("//div[@class='td-ss-main-sidebar']/aside/ul/li[4]/a").click()
time.sleep(10)
driver.find_element_by_xpath("//div[@class='td-ss-main-sidebar']/aside/ul/li[5]/a").click()
time.sleep(10)

