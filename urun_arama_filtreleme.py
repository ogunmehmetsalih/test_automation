import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class UAFiltreleme(object):
    def __init__(self):

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        try:
            self.driver.get("https://www.hepsiburada.com/")
            time.sleep(5)
            print("sayfa yüklendi")
        except:
            print("sayfa yok")
    def arama(self):
        search_box = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH,
                                                                                         "/html/body/div[1]/div/div/div[4]/div[5]/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div/div/div")))
        search_box.click()
        time.sleep(5)
        search_box=self.driver.find_element(By.XPATH,
                                  "/html/body/div[1]/div/div/div[4]/div[5]/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/input")
        search_box.send_keys("akıllı telefon")
        time.sleep(5)

        self.driver.find_element_by_name("Value").send_keys(Keys.ENTER)
        time.sleep(5)



o2=UAFiltreleme()
o2.arama()