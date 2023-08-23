from selenium import webdriver
import time

#winDriverPath = "C:\Users\EraDev\Downloads\chromedriver_win32\chromedriver.exe"
#Chrom .Driver bir browser'ı açar/çalıştırır.

#Browser'ı açmak için
browser = webdriver.Chrome()
browser.get("https://www.udemy.com/course/learn-selenium-automation-in-easy-python-language/")


#time.sleep(5)

#Açılan browser'ı kapatmak için
#browser.quit()


print("Site Başlığı: ", browser.title)
browser.refresh()

time.sleep(1)
#Sayfa boyutunu max'da açıyor
browser.maximize_window()

browser.get("https://google.com/")
time.sleep(1)
browser.get("https://pypi.org/project/selenium/")

time.sleep(5)
browser.set_window_size(800,600)

#Sayfanın kaynağı alma
print(browser.page_source)

#Sayfanın screenshut'ını alma
from datetime import date

today = date.today()
today = today.strftime("%m/%d/%y")

#path = *"C:/Users/EraDev/Desktop/SELENIUM/Screenshot/",today,".png"
path = *today,".png"

browser.save_screenshot(path)
print(path)



#Başka metodlara bakmak için
#https://www.askpython.com/python-modules/important-python-selenium-functions sitesindede bakılabilir veya cmd'de browser.+TAB diyerekte görebiliriz.
#https://www.simplilearn.com/tutorials/python-tutorial/selenium-with-python

browser.back()
time.sleep(2)




