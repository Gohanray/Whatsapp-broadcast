from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=user-data")
driver = webdriver.Chrome(options=chrome_options, executable_path="C:/Users/user/Desktop/chromedriver")
driver.get('https://web.whatsapp.com')

members=int(input("Enter the number of members"))
for j in range(members):
    name = input('Enter the user name')
    text = input('Enter the text')
    count = int(input("Enter the count " ))

    input('Enter anything after scanning ')

    user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
    user.click()

    text_box = driver.find_element_by_class_name('DuUXI')

    for i in range(count):
        text_box.send_keys(text)
        driver.find_element_by_class_name('_2Ujuu').click()
