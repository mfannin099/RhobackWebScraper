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

# ORIGINAL (JUST PULLING NAME/PRICE FROM LINE 12 LINK)
# ## Extract Putter Information (Name/Price)
putter_list = driver.find_element(By.CSS_SELECTOR, "ul#Slider-template--16677983912180__86207359-2a79-492b-b434-6794b1dff016")
putters = putter_list.find_elements(By.CSS_SELECTOR, "li.grid__item")
print(f"Found {len(putters)} products\n")

# for putter in putters:
#     try:
#         card_info = putter.find_element(By.CSS_SELECTOR, "div.card__information")

#         name_element = card_info.find_element(By.CSS_SELECTOR, "h3 a.full-unstyled-link")
#         name = name_element.get_attribute('textContent').strip()
        

#         price_element = putter.find_element(By.CSS_SELECTOR, "span.price-item--regular")
#         price = price_element.get_attribute('textContent').strip()

#         print(name)
#         print(price)

#     except Exception as e:
#         print(f"Error extracting putter: {e}")
#         continue


putter_name = []
putter_price = []
putter_link = []

for index in range(len(putters)):
    try:
        print(f"Processing putter {index + 1}/{len(putters)}...")
        
        # Get basic info from listing page
        putter_list = driver.find_element(By.CSS_SELECTOR, "ul#Slider-template--16677983912180__86207359-2a79-492b-b434-6794b1dff016")
        putters = putter_list.find_elements(By.CSS_SELECTOR, "li.grid__item")
        putter = putters[index]
        
        card_info = putter.find_element(By.CSS_SELECTOR, "div.card__information")

        # Name information
        name_element = card_info.find_element(By.CSS_SELECTOR, "h3 a.full-unstyled-link")
        name = name_element.get_attribute('textContent').strip()
        putter_name.append(name)

        
        price_element = putter.find_element(By.CSS_SELECTOR, "span.price-item--regular")
        price = price_element.get_attribute('textContent').strip()
        putter_price.append(price)
        
        # Get the product link
        product_link = name_element.get_attribute('href')
        putter_link.append(product_link)

        print(f"Name: {name}")
        print(f"Price: {price}")
        print(f"Link: {product_link}")
        print(f"Clicking into product page...")
        
        # Click into the product page
        driver.get(product_link)
        time.sleep(2)  # Wait for page to load
        
        # NOW WE'RE ON THE PRODUCT PAGE - scrape detailed info
        print(f"Current URL: {driver.current_url}")



        ## Returnig to the listing page
        print("Going back to listing page...")
        driver.get("https://detroitputterco.com/collections/our-putters")
        time.sleep(2)


    except Exception as e:
        driver.get("https://detroitputterco.com/collections/our-putters")
        time.sleep(2)
        print(f"Error extracting putter: {e}")
        continue





driver.close()


