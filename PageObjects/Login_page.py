from selenium.webdriver.common.by import By
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
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.user_name)
                                             ))
        element.send_keys(username)
         # self.driver.find_element(By.XPATH, self.user_name).send_keys(username)

    def password_click(self,password):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.password)
                                             ))
        element.send_keys(password)
         # self.driver.find_element(By.XPATH, self.password).send_keys(password)

    def Signup_click(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.signup_button)
                                             ))
        element.click()
         # self.driver.find_element(By.XPATH, self.signup_button).click()

#
    def dashboard_text(self):
         return self.driver.find_element(By.XPATH, self.dashboard).text
#
#




