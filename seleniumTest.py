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

time.sleep(3)
#Sayfa boyutunu max'da açıyor
browser.maximize_window()

browser.get("https://pypi.org/project/selenium/")

time.sleep(2)
browser.set_window_size(800,600)

browser.back()
time.sleep(5)




