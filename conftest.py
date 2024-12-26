import time

from selenium import webdriver
import pytest
import configparser
conig = configparser.ConfigParser()
conig.read("utilitise/input.ini")

@pytest.fixture()

def setup(request):
   request.cls.driver=webdriver.Chrome()
   request.cls.driver.get(conig.get("url","base_url"))
   request.cls.driver.maximize_window()
   # time.sleep(1)
   yield
   request.cls.driver.quit()