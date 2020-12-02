# Web Scraping
from selenium import webdriver
from selenium.common.exceptions import *
# Data manipulation
import pandas as pd
# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
from selenium.webdriver.common.keys import Keys

webdriver_path = '/usr/local/bin/chromedriver'  # Enter the file directory of the Chromedriver
Lazada_url = 'https://www.lazada.com.my'
search_item = 'stand fan' # Chose this because I often search for coffee!

# Select custom Chrome options
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
# Open the Chrome browser
browser = webdriver.Chrome(webdriver_path, options=options)
browser.get(Lazada_url)

search_bar = browser.find_element_by_id('q')
search_bar.send_keys(search_item, Keys.ENTER)

item_titles = browser.find_elements_by_class_name('c16H9d')
item_prices = browser.find_elements_by_class_name('c13VH6')
item_reviews = browser.find_elements_by_class_name('c3XbGJ')
# Initialize empty lists
titles_list = []
prices_list = []
reviews_list = []
# Loop over the item_titles and item_prices
for title in item_titles:
    titles_list.append(title.text)
for price in item_prices:
    prices_list.append(price.text)
for review in item_reviews:
    reviews_list.append(review.text)

print(titles_list)
print(prices_list)
print(reviews_list)

try:
    browser.find_element_by_xpath('//*[@class="ant-pagination-next" and not(@aria-disabled)]').click()
    print('found next page button')
except NoSuchElementException:
    print('next page button not found')
    browser.quit()

dfL = pd.DataFrame(zip(titles_list, prices_list, reviews_list), columns=['ItemName', 'Price', 'Review'])

dfL['Price'] = dfL['Price'].str.replace('RM', '').astype(float)
# dfL = dfL[dfL['ItemName'].str.contains('170g') == True]



print(dfL)

