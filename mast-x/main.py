from selenium import webdriver
from time import sleep
from selenium.webdriver.common.utils import find_connectable_ip
from webdriver_manager import driver
from webdriver_manager import chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

user = input("Enter your username: ")
pw = input("Enter your password: ")


driver = webdriver.Chrome(ChromeDriverManager().install())
sleep(1)
driver.get('https://xhofficial.com/login')
username_box = driver.find_element_by_id('username')
username_box.send_keys(user)
password_box = driver.find_element_by_id('password')
password_box.send_keys(pw)
password_box.send_keys(u'\ue007')
print("Logged In........")
sleep(1)
print('Choose Your Favourite: pamela ')
print('-----------------------------------')
sleep(1)
print("Okay...")
sleep(1)
driver.get('https://xhamsterlive.com/PamelaWet')
