import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class odev2(object):
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        try:
            self.driver.get("https://www.pazarama.com/")
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            print("Sayfa yüklendi")
        except Exception as e:
            print(f"Sayfa yüklenirken hata oluştu: {e}")



    def sign_up(self):
        try:
            sign_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div[2]/div/header/div[1]/div[2]/div/div/div/div[2]/a/span[2]")))  # XPath'i daha genel hale getirdim.
            sign_button.click()
            print("Giriş yap butonuna tıklandı.")
            time.sleep(5)

            sign_up_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/ul/li[2]/button"))
            )
            self.driver.execute_script("arguments[0].click();", sign_up_button)
            sign_up_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/ul/li[2]/button"))
            )
            self.driver.execute_script("arguments[0].click();", sign_up_button)
            print("Kayıt ol butonuna tıklandı.")
        except Exception as e:
            print(f"Sign up işlemi hatalı: {e}")

        try:
            self.driver.execute_script("document.querySelector('div[class*=\"cookie\"]').style.display='none';")
            print("Çerez pop-up'ı gizlendi.")
            time.sleep(3)
            name_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.ID,"FirstName")))
            name_input.send_keys("mehmet salih")
            print("Ad girildi.")
            time.sleep(2)
            last_name_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.ID, "LastName")))
            last_name_input.click()
            last_name_input.send_keys("ogun")
            print("Soyad girildi.")
            time.sleep(2)

            mail_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.ID, "SignupUserName")))
            mail_input.click()
            mail_input.send_keys("dolet37153@gianes.com")
            time.sleep(2)
            print("E-posta girildi.")
            passw_input=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.ID, "registerPassword")))
            passw_input.click()
            passw_input.send_keys("asd123cn")
            time.sleep(2)
        except Exception as e:
            print(f"Üye ol bilgilerinde hata meydana geldi : {e}")
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            accept_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/div/div/form/label[1]/div/input")))
            accept_button.click()
            print("KVKK onayı verildi.")

            kvkk_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/div/div/form/label[2]/div[1]/input")))
            kvkk_button.click()
            print("KVKK kutusu işaretlendi.")

            agreement_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/div/div/form/label[3]/div/input")))
            agreement_button.click()
            print("Gizlilik sözleşmesi onayı verildi.")
            time.sleep(1)
        except Exception as e:
            print(f"sözleşme kısmında hata meydana gekdi {e}")
        try:
            devam = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "register-submit-button"))
            )
            devam.click()
            print("Devam et butonuna tıklandı.")
            time.sleep(2)
        except Exception as e:
            print(f"Bir hata oluştu: {e}")

    def cerez(self):
        try:
            kabul_et_butonu = WebDriverWait(self, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Kabul Et')]"))
            )
            kabul_et_butonu.click()
            print("Çerez kabul et butonuna tıklandı.")
        except:
            print("Çerez kabul et butonu bulunamadı veya başka bir hata oluştu.")

    def sign_in(self):
        try:
            self.driver.get("https://www.pazarama.com/")
            sign_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH,
                 "/html/body/div[1]/div[2]/div/header/div[1]/div[2]/div/div/div/div[2]/a/span[2]")))  # XPath'i daha genel hale getirdim.
            sign_button.click()
            login_mail = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.ID, "Username")))
            login_mail.send_keys("dolet37153@gianes.com")
            print("E-posta girildi.")
        except Exception as e:
            print(f"E-posta girilemedi: {e}")

        try:
            login_passw = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.ID, "Password")))
            login_passw.send_keys("asd123cn")
            print("Şifre girildi.")

            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "submit-button")))
            login_button.click()
            print("Giriş butonuna tıklandı.")
            time.sleep(10)
        except Exception as e:
            print(f"Şifre girilemedi veya giriş yapılamadı: {e}")


o1 = odev2()
o1.sign_up()
o1.sign_in()
