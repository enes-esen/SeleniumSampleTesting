from selenium import webdriver
import time
from PIL import Image
from Screenshot import Screenshot
from datetime import datetime

driver = webdriver.Chrome()
url = "https://www.google.com/"
driver.get(url)


now = datetime.now()
today = now.strftime("%y%m%d")
times = now.strftime("%H%M%S")

print("Gün: ", today) 
print("Zaman: ", times)

path1 = "C:/Users/EraDev/Desktop/SELENIUM/Screenshot/"
path2 = today +"_" + times + ".png"
path = path1 + path2

driver.save_screenshot(path)
time.sleep(5)

screenshot = Image.open(path)
screenshot.show()