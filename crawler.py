from selenium import webdriver
form selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def xpath_text(xpath):
	xp = driver.find_element_by_xpath(xpath)
	return xp.text

def update():
	#crawling by selenium
	return item_price

driver = webdriver.Chrome('./chromedriver') #should downloaded
#driver.get('https://lostark.game.onstove.com/Market')
#and login process
#src = button = driver.find_element_by_xpath('//*[@id="lostark-wrapper"]/div/main/div/div/div[2]/form/fieldset/div/div[4]/button[1]
#//*[@id="tbodyItemList"]/tr[{}]/
#.format(tr_index) <using for roop
