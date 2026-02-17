from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the driver
driver = webdriver.Chrome()

driver.get("https://detroitputterco.com/")

driver.get("https://detroitputterco.com/collections/our-putters")
time.sleep(1) 

putter_list = driver.find_element(By.CSS_SELECTOR, "ul#Slider-template--16677983912180__86207359-2a79-492b-b434-6794b1dff016")
putters = putter_list.find_elements(By.CSS_SELECTOR, "li.grid__item")
print(f"Found {len(putters)} products\n")

for putter in putters:
    try:
        card_info = putter.find_element(By.CSS_SELECTOR, "div.card__information")

        name_element = card_info.find_element(By.CSS_SELECTOR, "h3 a.full-unstyled-link")
        name = name_element.get_attribute('textContent').strip()
        

        price_element = putter.find_element(By.CSS_SELECTOR, "span.price-item--regular")
        price = price_element.get_attribute('textContent').strip()

        print(name)
        print(price)

    except Exception as e:
        print(f"Error extracting putter: {e}")
        continue

driver.close()


