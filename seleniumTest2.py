from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = 'C:/Users/EraDev/Downloads/chromedriver_win32/chromedriver.exe')
url = "https://www.google.com/"
driver.get(url)
driver.save_screenshot()
time.sleep(5)

from datetime import date
today = date.today()
today = today.strftime("%m/%d/%y")
print("Tarih: ", today)





#path = *"C:/Users/EraDev/Desktop/SELENIUM/Screenshot/",today,".png"
path = *today,".png"

browser.save_screenshot(path)
print(path)
