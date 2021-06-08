from selenium import webdriver
from time import sleep
from selenium.webdriver.common.utils import find_connectable_ip
from webdriver_manager import driver
from webdriver_manager import chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains


# user = input("Enter your username: ")
# pw = input("Enter your password: ")

user = input('Enter your username: ')
pw = 'Enter your password'
print('Keep In Mind This is could not save your password, Until your edit at 14th and 15th line into Your password and username.')


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
sleep(1)
driver.get('https://xhofficial.com/login')
username_box = driver.find_element_by_id('username')
username_box.send_keys(user)
password_box = driver.find_element_by_id('password')
password_box.send_keys(pw)
password_box.send_keys(u'\ue007')
print("Logged In........")
sleep(1)
print("Okay...")
sleep(1)
driver.get('https://xhamsterlive.com/PamelaWet')
button_box = driver.find_elements_by_xpath('//*[@id="body"]/div[2]/div/div/div[2]/div[1]/button')
button_box[0].click()