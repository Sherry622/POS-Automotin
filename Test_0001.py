import time
import pytest
from PageObjects.Login_page import Login
from  PageObjects.Dashboard import DashboardB
from utilitise.loggers import Logs
from PageObjects.settle_page import Settle
from PageObjects.work_period_page import Work_Period
import configparser
conig = configparser.ConfigParser()
conig.read("utilitise/input.ini")
@pytest.mark.usefixtures("setup")
class Test(Logs):
    @pytest.mark.skip
    def test_001(self):
        lgs=self.getlogs()
        lg=Login(self.driver)
        lgs.info("Test Case 01")
        lgs.info("Test Case Starting")
        lg.user_name_click(conig.get("credentials","user_name"))
        lgs.info("Enter username")
        lg.password_click(conig.get("credentials","passord"))
        lgs.info("Enter password")
        lg.Signup_click()
        lgs.info("Click signup button")
        lg.dashboard_text()

        if 'Sherry' in lg.dashboard_text():
            assert True
            lgs.info("Test Case Pass ")
        else:
            lgs.critical("Test Case Fail")
            assert False

    @pytest.mark.skip
    def test_002(self):
        lgs = self.getlogs()
        lg = Login(self.driver)
        lgs.info("Test Case 01")
        lgs.info("Test Case Starting")
        lg.user_name_click(conig.get("credentials", "user_name"))
        lgs.info("Enter username")
        lg.password_click(conig.get("credentials", "invelid_password"))
        lgs.info("Enter password")
        lg.Signup_click()
        lgs.info("Click signup button")
        # time.sleep(5)
        lg.error_mess()


        if 'Email or password is wrong!' in lg.error_mess():
            assert True
            lgs.info("Test Case Pass ")
        else:
            lgs.critical("Test Case Fail")
            assert False

    # @pytest.mark.skip
    def test_003(self):
        lgs = self.getlogs()
        lg = Login(self.driver)
        db=DashboardB(self.driver)
        wp=Work_Period(self.driver)
        lgs.info("Test Case 01")
        lgs.info("Test Case Starting")
        lg.user_name_click(conig.get("credentials", "user_name"))
        lgs.info("Enter username")
        lg.password_click(conig.get("credentials", "passord"))
        lgs.info("Enter password")
        lg.Signup_click()
        lgs.info("Click signup button")
        time.sleep(4)
        db.pos_click()
        lgs.info("Click pos button")
        db.click_work_period()
        lgs.info("click work period")
        wp.click_start_workperiod()
        lgs.info("click start work period")
        wp.click_add()
        lgs.info("add cash")
        wp.click_header_pos()
        lgs.info("click header pos")
        db.takeaway_click()
        lgs.info("Click takeaway button")
        db.Fastfood_click()
        lgs.info("Click fastfood button")
        db.deal2_click()
        lgs.info("Click deal2 button")
        db.crispy_click()
        lgs.info("Click crispy button")
        db.crunch_click()
        lgs.info("Click crunch button")
        db.deal_click()
        lgs.info("Click fastfood deal1")
        db.Submit_dash_click()
        lgs.info("Click submit button")
        time.sleep(1)


    # @pytest.mark.skip
    def test_004(self):

                lgs = self.getlogs()
                lg = Login(self.driver)
                db=DashboardB(self.driver)
                sp=Settle(self.driver)
                wp = Work_Period(self.driver)
                lgs.info("Test Case 03")
                lgs.info("Test Case Starting")
                lg.user_name_click(conig.get("credentials", "user_name"))
                lgs.info("Enter username")
                lg.password_click(conig.get("credentials", "passord"))
                lgs.info("Enter password")
                lg.Signup_click()
                lgs.info("Click signup button")
                time.sleep(4)
                db.pos_click()
                lgs.info("Click pos button")
                db.dashboard_running_button()
                lgs.info("click running_order button")
                sp.settle_button_click()
                lgs.info("click settle button")
                sp.click_all_button()
                lgs.info("click all button")
                sp.click_cash()
                lgs.info("click cash button")
                sp.click_running_settle()
                lgs.info("order settle successfull")
                wp.click_header_home()
                lgs.info("click header home")
                db.click_time_work()
                lgs.info("click work period main")
                wp.click_end_wp()
                lgs.info("click end work period button")
                wp.click_end_popup()
                lgs.info("day end")






