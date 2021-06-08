from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(ChromeDriverManager().install())
sleep(1)
driver.maximize_window()
print("Driver has been installed...")
sleep(1)
print("Opening selected website...")
driver.get('https://docs.google.com/forms/d/e/1FAIpQLScVX1N_BgNl9P373MzJMEqW9ipQxrW3GkgECnoQVZKHahfEmQ/viewform?fbclid=IwAR0anl4LBr5BnEIcReBS-vGAMVt5NcM8yWuNOFAUFBXtP4c3BYxxRBPMDB4')
print('Entering to website...')

email_box = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
email_box.send_keys('14256@srm.ac.th')
sleep(1)
email_box.send_keys(Keys.TAB)


name_box = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
name_box.send_keys('นายสรนันท์ รุ่งธานี')
sleep(1)

name_box.send_keys(Keys.TAB)

button_box = driver.find_element_by_xpath('//*[@id="i13"]/div[3]/div')
button_box.click()
sleep(1)



number_box = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
number_box.send_keys('8')
sleep(1)


next_box = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span')
next_box.click()
sleep(1)

one_box = driver.find_element_by_xpath('//*[@id="i12"]/div[3]/div')
one_box.click()

sleep(1)
one_next_box = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div[2]/span')
one_next_box.click()
sleep(1)

text_box = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
text_box.send_keys('Test')
sleep(1)
text_box_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span')
text_box.click()
