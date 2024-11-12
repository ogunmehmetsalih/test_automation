import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Odev(object):
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        try:
            self.driver.get("https://www.hepsiburada.com/")
            time.sleep(5)
            print("sayfa yüklendi")
        except:
            print("sayfa yok")
    def logo(self):
        try:
            WebDriverWait(self.driver,2).until(EC.presence_of_element_located((By.CSS_SELECTOR,"a[title='Hepsiburada'] svg")))
            print("logo var")
        except:
            print("logo yok")
    def search_box_control(self):
        try:
            search_box=WebDriverWait(self.driver,2).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div[4]/div[5]/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div/div/div")))
            search_box.click()
            time.sleep(2)
            self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[4]/div[5]/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/input")
            print("arama butonu bulundu")
            time.sleep(2)
        except:
            print("arama butonu bulunmadı")
    def login_menu(self):

        self.driver.get("https://www.hepsiburada.com/")
        try:
            login_menu = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div/div[4]/div[5]/div/div/div/div[1]/div[2]/div[3]/div[2]")))
            action = ActionChains(self.driver)
            action.move_to_element(login_menu).perform()
            time.sleep(2)
            login_button = self.driver.find_element(By.XPATH,
                                               "/html/body/div[1]/div/div/div[4]/div[5]/div/div/div/div[1]/div[2]/div[3]/div[2]/div/div/ul/li[1]/a")
            login_button.click()
            time.sleep(2)
            print("Giriş Yap Butonuna Tıklandı")

        except:
            print("Giriş Yap Butonuna Tıklanmadı")



o1=Odev()
o1.__init__()