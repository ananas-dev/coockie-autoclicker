from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

class Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(0, 0)
    def login(self):
        self.driver.get('http://orteil.dashnet.org/cookieclicker/')
    def click(self):
        cookie = self.driver.find_element_by_xpath('//*[@id="bigCookie"]')
        cookie.click()

def main():
    os.system('clear')
    bot = Bot()
    bot.login()
    time.sleep(5)
    c = 0
    while True:
        bot.click()
        c = c+1
        print(c)
main()