from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "http://jde.eracs.com.tr:9000/jde/E1Menu.maf?jdeLoginAction=LOGOUT&RENDER_MAFLET=E1Menu"
driver.get(url)


#Bu satırı yakalamak için id'yi kullanabiliriz.

#Bunun için bir "User" değişkeni oluşturabiliriz.
#Find_element yönteminin ihtiyaçlarını tamamlarken aradığımız ID'nin değerini bildirmeliyiz. 
#Bu durumda kimlik “id” şeklindedir.

time.sleep(3)
#<input size="20" class="textfield margin-top5" type="text" name="User" id="User" value="">
user = driver.find_element(By.ID, "User")

#<input autocomplete="OFF" size="20" maxlength="10" class="textfield margin-top5" type="password" name="Password" id="Password" value="">
password = driver.find_element(By.ID, "Password")

# Sonra Kullanıcının adını yazmamız gerekiyor.
# Bunun için send_keys fonksiyonunu kullanırız.
user.send_keys("EESEN")
password.send_keys("Gkc!esen72")
#time.sleep(5)

#Butona tıklama
#<input class="buttonstylenormal margin-top5" type="submit" value="Sign In" onclick="return isFirstClick()">
signin_Button = driver.find_element(By.XPATH, value="//input[@value='Sign In']")
#time.sleep(10)
signin_Button.click()


#Girişin doğru yapıldığını kontrol edebilmek için sayfa başlığını(title'nı) kontrol edebiliriz.
# Bunun için iki değeri karşılaştırabiliriz.
assert driver.title == "JD Edwards"

pageTitle = driver.title
print("Title: ", pageTitle)

#Aktivite ekranına giriş

#NAVIGATOR
#<div id="drop_mainmenu" class="e1MenuBarItemChild MenuBarFocusableDiv" tabindex="1"></div>
navigator = driver.find_element(By.ID, "drop_mainmenu")
navigator.click()
time.sleep(1)
#ERA
#<span id="fldnode10038088" title="Task Type:Task View, Fastpath Code: TV:100">ERA</span>
era = driver.find_element(By.XPATH, "//span[@id='fldnode10038088']")
era.click()
time.sleep(1)

#AKTİVİTE İŞLEMLERİ
#<span id="fldnode10038091" title="Task Type: Folder, Fastpath Code: JDE030506">Aktivite İşlemleri</span>
aktivite_islemleri = driver.find_element(By.XPATH, "//span[@id='fldnode10038091']")

#AKTİVİTE GİRİŞ
#<a 
#	id="fldnode10038093" 
#	"arrownav="yes" 
#	onkeydown="return doMenuKeyDown(this,event)" 
#	href="javascript:RunNewApp(&quot;launchForm&quot;,&quot;0&quot;,&quot;P58AF002&quot;,&quot;APP&quot;,&quot;W58AF002C&quot;,&quot;&quot;,&quot;1&quot;,&quot;&quot;,&quot;Aktivite%20Giri%C5%9Fi&quot;,&quot;&quot;,&quot;&quot;,&quot;&quot;,&quot;&quot;,&quot;node10038093&quot;,&quot;&quot;,&quot;ec061823150d9c17&quot;,&quot;6380A95C009502-002941F7E9FFFB40-OIJY_6380A92C028800-002941F7E9FFFB40-OIJY_10038093&quot;)" 
#	onclick="checkHrefKeyPress(this, event, null)" 
#	title="Application: P58AF002, Form: W58AF002C">
#	Aktivite Girişi
#</a>
aktivite_giris = driver.find_element(By.XPATH, "fldnode10038093")
aktivite_giris.click()


time.sleep(10)
#driver.quit()



#-------------Radio Butonunu seçebilmek için-------------
#<label class="custom-control-label" for="input-newsletter-yes" style="">Yes</label>
#//label[@for='input-newsletter-yes']
#newsletter = driver.find_element(By.XPATH, value="//label[@for='input-newsletter-yes']")
#newsletter.click()

#-------------Onay butonuna tıklayabilmek için-------------
#<label class="custom-control-label" for="input-agree">I have read and agree to the <a href="https://ecommerce-playground.lambdatest.io/index.php?route=information/information/agree&amp;information_id=3" class="agree"><b>Privacy Policy</b></a></label>
#terms = driver.find_element(By.XPATH, value="//label[@for='input-agree']")
#terms.click()

#-------------Butona tıklamak için-------------
#<input type="submit" value="Continue" class="btn btn-primary">
#continue_button = browser.find_element(By.XPATH, value="//input[@value='Continue']")
#continue_button.click()

#-------------İki Değeri karşılaştırma-------------
#assert browser.title == "Your Account Has Been Created!" 