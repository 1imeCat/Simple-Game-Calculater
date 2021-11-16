import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def xpath_text(xpath):
	xp = driver.find_element_by_xpath(xpath)
	return xp.text


def update():
	#setup chrome
	driver = webdriver.Chrome('./chromedriver') 
	driver.implicitly_wait(20)
	
	#open website
	driver.get('https://lostark.game.onstove.com/Market')
	time.sleep(20)	#wait user to login manualy (will be fixed later)
	
	#view all items
	src_button = driver.find_element_by_xpath('//*[@id="lostark-wrapper"]/div/main/div/div/div[2]/form/fieldset/div/div[4]/button[1]')
	src_button.click()
	time.sleep(1)
	
	#get all item datas
	error = 0
	items = {'none':0}
	item_trade []
	while error == 0 :
		try:
			for page in range(3,13) :
				try:
					time.sleep(2)
					for tr_index in range(1,11) :
						xpath_tr = '//*[@id="tbodyItemList"]/tr[{}]/'.format(tr_index)
						item_info = []
						for td_index in range(1,5) :
							item_info.append(xpath_text(xpath_tr + 'td[{}]'.format(td_index)
						item_trade.append(item_info)
				except:
					error += 1
					print("crawling finished")
				wait = WebDriverWait(driver,10)
				element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="marketList"]/div[2]/a[{}]'.format(page))))
		except :
			error += 1
			print("error occured")
	time.sleep(2)
	driver.quit
	
	# divide information into name and price
	data_df = pd.DataFrame(item_trade)
	for i in range(len(data_df)) :
		txt = data_df[0][i]
			name = txt.split('\n')[0]
			#change price per unit to price per piece
			if '100' in txt.split('\n')[1]:
				price = int(data_df[3][i])/100
			elif '10' in txt.split('\n')[1]:
				price = int(data_df[3][i])/10
			else:
				price = int(data_df[3][i])
			items[name] = price

	return items



# need to add automatic login
# current code is crawling useless data
