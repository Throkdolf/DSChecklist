import json
import helperfuncts
from enums import SpellType
from classes import Spell
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

extensions = ['sorceries', 'pyromancies', 'miracles'] #define type based on extensions
url = "http://darksouls3.wikidot.com/sorceries"
driver.get(url)
wait = WebDriverWait(driver, 10)

# Hierarchy of search elements
# id - guaranteed to be unique
# name - no necessarily unique
# class - no necessarily unique and is typically duplicated
# selenium uses the first occurance of the search element

table = wait.until(EC.visibility_of_element_located((By.XPATH, "//table[@class='wiki-content-table']")))
rows = table.find_elements(By.XPATH, "./tbody/tr")

sorceries = []
hrefs = []

for row in rows[1:]: # first row is the header
    a = row.find_element(By.XPATH, './/a')
    hrefs.append(a.get_attribute("href"))

for link in hrefs:
    driver.get(link) #hrefs[0] = link
    name, image, desc, fp, attunement = None, None, None, None, None

    name = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@id, 'page-title')]"))).text
    print(name)

    desc_bq = driver.find_elements(By.XPATH, "//blockquote/p/em")
    desc = []
    for em in desc_bq:
        desc.append(em.text)
        print(em.text + "\n")
    desc = "".join(desc)


    table = driver.find_element(By.XPATH, "//table[@class='wiki-content-table infobox']")
    rows = table.find_elements(By.XPATH, "./tbody/tr")
    for row in rows:
        data, header = None, None

        if helperfuncts.elementExists("./td", row):
            data = row.find_element(By.XPATH, "./td")
            # print("data set")

        if helperfuncts.elementExists("./th", row):
            header = row.find_element(By.XPATH, "./th")
            # print("header set")

        if data is not None and helperfuncts.elementExists(".//img[@class='main-image']", data):
            image = data.find_element(By.XPATH, ".//img[@class='main-image']").get_attribute("src")
            print(image)

        if header is not None and helperfuncts.elementExists(".//span[@class='header-text']", header):
            row_title = header.find_element(By.XPATH, ".//span[@class='header-text']").text
            match row_title:
                case "FP Cost":
                    fp = data.text
                    print("FP Cost: ", fp)
                case "Slots Used":
                    attunement = data.text
                    print("Slots Used: ", attunement)
                case _:
                    pass

        if data is not None and helperfuncts.elementExists(".//table", data):
            req_table = data.find_element(By.XPATH, ".//table")
            req_data = req_table.find_elements(By.XPATH, ".//td")

            int_req = req_data[0].text
            print("int: ", int_req)
            faith_req = req_data[1].text
            print("faith: ", faith_req)

    sorceries.append(Spell(name, desc, image, int_req, faith_req, attunement, "sorcery", fp).__dict__)
    driver.back()

with open("sorceries.json", "w") as file:
    json.dump(sorceries, file, indent=4)

driver.quit()

# driver.close() # closes tab
# driver.quit() # closes whole browser