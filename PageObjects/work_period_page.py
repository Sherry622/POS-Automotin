from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Work_Period:
    def __init__(self,driver):
        self.driver=driver
        self.work_period="//button[@class='w-100 btn btn-secondary sm-text text-uppercase rounded']"
        self.add_button="//button[text()='Add']"
        self.start_work="//button[@class='w-100 btn btn-secondary sm-text text-uppercase']"
        self.header_pos="//i[@class='fa fa-cutlery text-primary']"

    def start_work_click(self):
        self.driver.find_element(By.XPATH, self.work_period).click()


    def click_add(self):
        element=WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH,self.add_button)
        ))
        element.click()
         # self.driver.find_element(By.XPATH, self.click_add).click()

    def click_start_workperiod(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.start_work)
            ))
        element.click()
         # self.driver.find_element(By.XPATH, self.start_work).click()

    def click_header_pos(self):
        element = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, self.header_pos)
        ))
        element.click()