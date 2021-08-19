import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import rd;

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

chrome_options1 = webdriver.ChromeOptions()
prefs1 = {"profile.default_content_setting_values.notifications" : 2}
chrome_options1.add_experimental_option("prefs",prefs1)
driver1 = webdriver.Chrome(chrome_options=chrome_options1)

chrome_options2 = webdriver.ChromeOptions()
prefs2 = {"profile.default_content_setting_values.notifications" : 2}
chrome_options2.add_experimental_option("prefs",prefs2)
driver2 = webdriver.Chrome(chrome_options=chrome_options2)

for i in range(1):
    #brower = webdriver.Chrome('C:/Users/Hoang Nguyen/Desktop/auto/chromedriver.exe')
    brower = driver
    brower1 = driver1
    brower2 = driver2
    brower.get('https://www.facebook.com/signup')
    brower1.get('https://temp-mail.org/en/')
    brower.find_element_by_name('lastname').send_keys(rd.ho1())
    time.sleep(2)
    brower.find_element_by_name('firstname').send_keys(rd.ten1())
    time.sleep(5)
    brower2.get('https://raw.githubusercontent.com/hoangks5/auto_reg_clone_fb/main/pass/pass.txt')
    a = brower1.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/form/div[2]/button')
    a.send_keys(Keys.ENTER)
    brower.find_element_by_name('reg_email__').send_keys(Keys.ENTER)
    act = ActionChains(brower)
    act.key_down(Keys.CONTROL).send_keys("v").perform()
    time.sleep(5)
    brower.find_element_by_name('reg_email_confirmation__').click()
    act2 = ActionChains(brower)
    act2.key_down(Keys.CONTROL).send_keys("v").perform()

    act1 = ActionChains(brower2)
    act1.key_down(Keys.CONTROL).send_keys("a").perform()
    act1.key_down(Keys.CONTROL).send_keys("c").perform()
    time.sleep(5)
    brower.find_element_by_id('password_step_input').click()
    act3 = ActionChains(brower)
    act3.key_down(Keys.CONTROL).send_keys("v").perform()

    year = brower.find_element_by_name('birthday_day')
    year.click()
    time.sleep(2)
    for i in range(random.randint(1,20)):
        year.send_keys(Keys.DOWN)
        time.sleep(0.5)
    time.sleep(2)
    year.send_keys(Keys.ENTER)
    year = brower.find_element_by_name('birthday_month')
    year.click()
    time.sleep(2)
    for i in range(random.randint(1,12)):
        year.send_keys(Keys.DOWN)
        time.sleep(0.6)
    time.sleep(2)
    year.send_keys(Keys.ENTER)
    year = brower.find_element_by_name('birthday_year')
    year.click()
    time.sleep(3)
    for i in range(random.randint(20,30)):
        year.send_keys(Keys.DOWN)
        time.sleep(0.5)
    year.send_keys(Keys.ENTER)
    time.sleep(2)
    brower.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[1]/label').click()
    time.sleep(2)
    brower.find_element_by_name('websubmit').send_keys(Keys.ENTER)
