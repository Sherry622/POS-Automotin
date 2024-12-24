from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class Login:
    def __init__(self,driver):
         self.driver=driver

         self.user_name="//input[@name='email']"
         self.password="//input[@name='password']"
         self.signup_button="//button[@type='submit']"
         self.dashboard="//a[@class='font-weight-bold text-capitalize sm-text nav-link dropdown-toggle pl-2']"

    def user_name_click(self,username):
         self.driver.find_element(By.XPATH, self.user_name).send_keys(username)

    def password_click(self,password):
         self.driver.find_element(By.XPATH, self.password).send_keys(password)

    def Signup_click(self):
         self.driver.find_element(By.XPATH, self.signup_button).click()

#
    def dashboard_text(self):
         return self.driver.find_element(By.XPATH, self.dashboard).text
#
#




