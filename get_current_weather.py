from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument('--headless')
options.add_argument('--log-level=3')


def get_current_weather() -> list:
    driver = webdriver.Chrome(options=options)

    driver.get('https://www.google.com')

    textarea = driver.find_element(By.TAG_NAME, 'textarea')

    textarea.send_keys('weather')
    textarea.send_keys(Keys.ENTER)

    temperature = driver.find_element(By.ID, 'wob_tm').text
    condition = driver.find_element(By.ID, 'wob_dc').text

    driver.close()
    return [condition, temperature]
