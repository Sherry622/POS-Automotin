from selenium.webdriver.common.by import By
class Work_Period:
    def __init__(self,driver):
        self.driver=driver
        self.work_period="//button[@class='w-100 btn btn-secondary sm-text text-uppercase rounded']"
        self.add_button="(//button[@class='btn btn-success w-100 xsm-text text-uppercase t-width-max'])[2]"

    def start_work_click(self):
        self.driver.find_element(By.XPATH, self.work_period).click()


    def click_add(self):
        return self.driver.find_element(By.XPATH, self.click_add).click()