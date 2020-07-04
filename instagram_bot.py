from selenium import webdriver
from time import sleep


class InstaBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.username = self.username
        self.driver.get("https://instagram.com")
        sleep(2)
