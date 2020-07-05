# Bot to send message in WhatasppWeb 
# Importing webdriver from selenium 
from selenium import webdriver
import time 

# Giving a path of chromedriver and website to direct
chrome_browser = webdriver.Chrome(
    executable_path = 'P:/chromedriver.exe'
)
chrome_browser.get('https://web.whatsapp.com/')

# Pausing time till QR code is scanned
time.sleep(15)

# Taking input and storing in variables 
user_name = input("group or person you want to send the message : ")
msg = input("enter the message you want to send : ")
count = int(input("enter the number of times you want to print the message"))
# Giving path to scan name that is given by user and then clicking on it
user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
user.click()

# # Clicking on button to send the printed message  
message_box = chrome_browser.find_element_by_xpath('//div[@class="_3uMse"]')

# Loop to print message multiple times
for index in range(count):
    message_box.send_keys(msg)

# Clicking on button to send the printed message  
    chrome_browser.find_element_by_xpath('//button[@class="_1U1xa"]').click()

print("success")    