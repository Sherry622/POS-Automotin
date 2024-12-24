from selenium.webdriver.common.by import By
class DashboardB:

    def __init__(self,driver):
         self.driver=driver
         self.POS_button="(//div[@class='product-card__add'])[2]"
         self.Takeaway="(//button[@class='dropdwn--btn btn bg2-success text-white '])[3]"
         self.test_order="//figcaption[@class='item-name text-center px-2 mt-2']"
         self.fast_food="//div[text()='Fast Food Deals']"
         self.crispy_crunch="(//figcaption[@class='item-name text-center px-2 mt-2'])[1]"
         self.crunch_feast="(//figcaption[@class='item-name text-center px-2 mt-2'])[2]"
         self.fastfood_deal_1="(//figcaption[@class='item-name text-center px-2 mt-2'])[3]"
         self.fastfood_deal_2="(//figcaption[@class='item-name text-center px-2 mt-2'])[4]"
         self.Submit_dashboard="//button[text()='submit']"
         self.db_running_order = "//a[text()='Running Odr.']"
         self.work_period="//a[@class='t-heading-font btn btn-success btn-sm text-uppercase sm-text']"



    def POS_click(self):
        self.driver.find_element(By.XPATH,self.POS_button).click()


    def takeaway_click(self):
        self.driver.find_element(By.XPATH, self.Takeaway).click()

    def Testorder_click(self):
        self.driver.find_element(By.XPATH, self.test_order).click()

    def Fastfood_click(self):
        self.driver.find_element(By.XPATH, self.fast_food).click()

    def crispy_click(self):
        self.driver.find_element(By.XPATH, self.crispy_crunch).click()

    def crunch_click(self):
        self.driver.find_element(By.XPATH, self.crunch_feast).click()

    def deal_click(self):
        self.driver.find_element(By.XPATH, self.fastfood_deal_1).click()

    def deal2_click(self):
        self.driver.find_element(By.XPATH, self.fastfood_deal_2).click()

    def Submit_dash_click(self):
        self.driver.find_element(By.XPATH,self.Submit_dashboard).click()

    def dashboard_running_button(self):
        self.driver.find_element(By.XPATH, self.db_running_order).click()

    def click_work_period(self):
        self.driver.find_element(By.XPATH, self.work_period).click()

