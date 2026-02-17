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

product_list = driver.find_element(By.CSS_SELECTOR, "ul#Slider-template--16677983912180__86207359-2a79-492b-b434-6794b1dff016")
products = product_list.find_elements(By.CSS_SELECTOR, "li.grid__item")
print(f"Found {len(products)} products\n")

# for product in products:
#     try:
#         # The div you're looking for is the second child div inside each product
#         # li > div > div > div:nth-child(2)
#         target_div = product.find_element(By.CSS_SELECTOR, "div > div > div:nth-child(2)")
        
#         # Get all the text from that div
#         product_info = target_div.text
        
#         print(product_info)
#         print("-" * 50)
        
#     except Exception as e:
#         print(f"Error extracting product: {e}")
#         continue

driver.close()


