from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
from tkinter import Tk

PATH = "C:\\Program Files (x86)\\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://skribbl.io/")

privateButton = driver.find_element_by_id("buttonLoginCreatePrivate")
privateButton.click()
time.sleep(5)
#rounds = driver.find_element_by_id("lobbySetRounds")
#rounds.click()
select = Select(driver.find_element_by_id('lobbySetRounds'))
select.select_by_visible_text('6')
time.sleep(5)
linkCopy = driver.find_element_by_id("inviteCopyButton")
linkCopy.click()
link = Tk().clipboard_get()
print(link)

#driver.quit()