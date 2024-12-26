from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Settle:

    def __init__(self,driver):
         self.driver=driver
         self.settle_button="(//button[@title='Settle Order'])[1]"
         self.settle_button2="(//button[@title='Settle Order'])[2]"
         self.All="(//button[@class='fk-settle-cal-btn t-text-white t-bg-ac text-capitalize'])[1]"
         self.running_settle_button="//button[@class='fk-settle-cal-btn bg-primary t-text-white t-bg-r text-capitalize']"
         self.cash="//button[text()='Cash']"

    def settle_button_click(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.settle_button)
                                             ))
        element.click()
        # self.driver.find_element(By.XPATH, self.settle_button).click()

    def settle_button_click2(self):
        self.driver.find_element(By.XPATH, self.settle_button2).click()

    def click_all_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.All)
                                             ))
        element.click()
        # self.driver.find_element(By.XPATH, self.All).click()

    def click_running_settle(self):
        self.driver.find_element(By.XPATH, self.running_settle_button).click()

    def click_cash(self):
        self.driver.find_element(By.XPATH, self.cash).click()