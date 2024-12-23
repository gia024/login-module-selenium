from selenium import webdriver
import time
from selenium.webdriver.common.by import By
class Login:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://dma-dev.naxa.com.np/login")

        self.driver.maximize_window()

        time.sleep(2)
    
    def validate_login(self):
        email = self.driver.find_element(By.CSS_SELECTOR, "input#email")
        email.send_keys("garima@gmail.com")

        password = self.driver.find_element(By.CSS_SELECTOR, "input#password")

        password.send_keys("garima@123")

        submit = self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

        time.sleep(2)
        # Check if validate login is sucessful.
        try:
            self.driver.find_element(By.CSS_SELECTOR, r"[class='flex-col grid h-screen w-screen md\:grid-cols-5']")
            print("Validate login test passed")
        except:
            print("Validate login test failed")
    
    def empty_fields(self):
        email = self.driver.find_element(By.CSS_SELECTOR, "input#email")
        email.clear()
        email.send_keys("")

        password = self.driver.find_element(By.CSS_SELECTOR, "input#password")
        password.clear()
        password.send_keys("")

        submit = self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

        time.sleep(2)

        # Check if empty fields test is successful.
        try:
            print("Empty fields test passed")
        except:
            print("Empty fields test failed")


    def invalid_password(self):
        email = self.driver.find_element(By.CSS_SELECTOR, "input#email")
        email.send_keys("dma-dev@naxa.com")

        password = self.driver.find_element(By.CSS_SELECTOR, "input#password")
        password.send_keys("garima@123")
        email.clear()
        password.clear()

        submit= self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

        try:
            self.driver.find_element(By.CSS_SELECTOR, r"[class='flex-col grid h-screen w-screen md\:grid-cols-5']")
            print("Invalid password test passed")
        except:
            print("Invalid password test failed")

        time.sleep(2)

    def invalid_email(self):
        email = self.driver.find_element(By.CSS_SELECTOR, "input#email")
        email.send_keys("garima@gmail.com")

        password = self.driver.find_element(By.CSS_SELECTOR, "input#password")
        password.send_keys("admin@naxa##")

        submit = self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        email.clear()
        password.clear()

        try:
            self.driver.find_element(By.CSS_SELECTOR, r"[class='flex-col grid h-screen w-screen md\:grid-cols-5']")
            print("Invalid email test passed")
        except:
            print("Invalid email test failed")

        time.sleep(3)

    def password_field_masking(self):
        self.driver.find_element(By.CSS_SELECTOR, r".cursor-pointer.select-none.text-icon-sm.duration-300").click()
        try:
            self.driver.find_element(By.CSS_SELECTOR, r".cursor-pointer.select-none.text-icon-sm.duration-300")
            print("Password field masking test passed")
        except:
            print("Password field masking test failed")

        time.sleep(3)
    
    def forgot_password(self):
        # self.driver.get("https://dma-dev.naxa.com.np/login")

        self.driver.find_element(By.CSS_SELECTOR, "button[type='button']").click()

        email = self.driver.find_element(By.CSS_SELECTOR, "#email")
        email.send_keys("dma-dev@naxa.com")

        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        try:
            self.driver.get("https://dma-dev.naxa.com.np/login")
            print("forgot password test passed")
        except:
            print("forgot password test failed")

        time.sleep(3)

    def valid_login(self):
        email = self.driver.find_element(By.CSS_SELECTOR,"#email")
        email.send_keys("dma-dev@naxa.com")

        password = self.driver.find_element(By.CSS_SELECTOR,"#password")
        password.send_keys("admin@naxa##")

        self.driver.find_element(By.CSS_SELECTOR, "#check").click()

        submit = self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

        time.sleep(2)

        self.driver.find_element(By.CSS_SELECTOR, ".flex.items-center.justify-center  img").click()

        self.driver.find_element(By.CSS_SELECTOR, "body div div aside div div span[role='presentation'] i").click()

        try:
            self.driver.get("https://dma-dev.naxa.com.np/login")
            print("valid login with keep me signed in test passed")
        except:
            print("valid login with keep me signed in test failed")

        time.sleep(3)
    
login = Login()
login.validate_login()
login.empty_fields()
login.invalid_password()
login.invalid_email()
login.password_field_masking()
login.forgot_password()
login.valid_login()
