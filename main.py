import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# from loginInfo.myInfo import returnMyPassword

load_dotenv(verbose=True)
id = os.getenv('MY_ID')
pw = os.getenv('MY_PASSWORD')
driver = webdriver.Chrome('./chromedriver')
driver.get(f'https://plato.pusan.ac.kr/')
# import time
# time.sleep(5)

# url = driver.current_url
# driver.get(url)
inputId = driver.find_element_by_xpath('//*[@id="input-username"]')
inputPassword = driver.find_element_by_xpath('//*[@id="input-password"]')

inputId.send_keys(id)
inputPassword.send_keys(pw)
inputPassword.send_keys(Keys.ENTER)

driver.implicitly_wait(1)


courseLinkList = driver.find_element_by_xpath('//*[@id="page-content"]/div/div[1]/div[2]').find_elements_by_tag_name('a')
for courseLink in courseLinkList:
    driver.get(courseLink.get_attribute('href'))
    currentWeekVideosLinkList = driver.find_element_by_xpath('//*[@id="page-content"]/div/div[2]/div/div/div[2]').find_elements_by_tag_name('a')
    for videoLink in currentWeekVideosLinkList:
        print(currentWeekVideosLinkList)
        iconSrc = videoLink.find_element_by_tag_name('img').get_attribute('src')
        if iconSrc == 'https://plato.pusan.ac.kr/theme/image.php/coursemosv2/vod/1649769022/icon':
            videoLink.click()
            link = (videoLink.get_attribute('href'))
            print(link)
            driver.switch_to.window(driver.window_handles[1])
            driver.find_element_by_xpath('//*[@id="my-video"]/button').click()
            driver.switch_to.window(driver.window_handles[0])

