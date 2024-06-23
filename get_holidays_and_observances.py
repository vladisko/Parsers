from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import validators
import csv

options = Options()
options.add_argument('--headless')
options.add_argument('--log-level=3')


def get_holidays_and_observances(countries: list | str, year=2024) -> None:
    for country in countries:
        link = f"https://www.timeanddate.com/holidays/{country}/{year}"

        if not validators.url(link):
            print('Invalid link')
            return

        driver = webdriver.Chrome(options=options)
        driver.get(link)
        table_rows = driver.find_elements(By.TAG_NAME, 'tr')

        with open(f'HolidaysAndObservances\{country}.csv', 'w', encoding='utf-8', newline='') as file:
            for row in table_rows:

                row = row.text.split(' ', 3)
                if not '' in row:
                    csv.writer(file).writerow(row)

    driver.close()
