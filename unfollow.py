import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import os
import re

os.chdir('C:/Users/Kshitij Sinha/Desktop/BOTS')


webdriver = webdriver.Firefox()
time.sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/')
time.sleep(2)
username = webdriver.find_element_by_name('username')
username.send_keys(your_username_here)
password = webdriver.find_element_by_name('password')
password.send_keys(your_password_here)
submit = webdriver.find_element_by_tag_name('form')
submit.submit()

# By passing the turn-on notifications
time.sleep(5)
noti = webdriver.find_element_by_xpath('//button[text()="Not Now"]')
noti.click()
# Navigaating to accounts page
acc = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a/span')
acc.click()
time.sleep(5)
# taking screenshot
webdriver.save_screenshot("unfollowing.png")
text = extract('unfollowing.png')
num = re.findall('\d+', text )
ra = int(num[1])

# Un-following
time.sleep(2)
for i in range(ra):
    follow = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
    follow.click()
    time.sleep(3)
    webdriver.find_element_by_xpath("/html/body/div[3]/div/div[2]/ul/div/li[1]/div/div[3]/button").click()
    confirm = webdriver.find_element_by_xpath('//button[text()="Unfollow"]')
    confirm.click()
    time.sleep(2)
    webdriver.refresh()
    time.sleep(5)

print("Executed!!!")
