# This file handle the part of collecting data ( scraaping from
# Amazon.fr webpage ) and saving it into a csv file

# Our imports
from src.common.settings import reviews_div_cls,rev_cols

# System Imports
import os
import sys
import unicodedata
import pickle as pk

# Web Scrapping
from bs4 import BeautifulSoup
from selenium import webdriver



# Data Imports
import pandas as pd

root_path = os.path.dirname(os.path.realpath(__file__))

# Scrapping Reviews Data
def reviews_scrapper(driver, prod, rev_url, ds):
    driver.get(rev_url)
    rev_soup = BeautifulSoup(driver.page_source, 'html.parser')
    reviews_div = rev_soup.find_all('div', {'class': reviews_div_cls})

    for review in reviews_div:
        try:
            review_title = review.find('a', {'data-hook': 'review-title'}).text
        except AttributeError:
            review_title = 'Null'

        try:
            review_rate = review.find('i', {'data-hook': 'review-star-rating'}).text
        except AttributeError:
            review_rate = '0'

        review_body = review.find('span', {'data-hook': 'review-body'}).text

        try:
            review_help = review.find('span', {'data-hook': 'helpful-vote-statement'}).text
        except AttributeError:
            review_help = '0'
        try:
            review_home = review.find('span', {'data-hook': 'review-date'}).text
        except AttributeError:
            review_home = '0'

        rev_result = tuple(map(lambda x: unicodedata.normalize("NFKD", x.strip()),
                               [review_title, review_rate, review_body, review_help, review_home]))
        ds.append(rev_result + (prod,))

    return ds

# Preparing Webdriver
def init_webdriver():
    sys.path.insert(0, '/usr/lib/chromium-browser/chromedriver')
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('chromedriver', options=options)
    return driver

# This function help us to generate the dataset of reviews
# and also the dataframe of several products
def build_dataset(prod_urls,driver):
    lst_rev = []
    for category, products in prod_urls.items():
        for prod in products:
            for i in range(1, prod['rev_pages'] + 1):
                lst_rev = reviews_scrapper(driver, prod['prod_id'], f'{prod["rev_url"]}&pageNumber={i}', lst_rev)

    df_rev = pd.DataFrame(lst_rev)
    df_rev.columns = rev_cols

    ds = df_rev[df_rev["Rev_Home"] == 'France']
    ds = ds[["Rev_Title", "Rev_Bdy"]]

    dataset_path = os.path.join(root_path, 'common', 'reviews.csv')
    ds.to_csv(dataset_path, index=False)



if __name__ == '__main__':
    settings_path = os.path.join(root_path, 'common', 'settings.pkl')
    settings_file = open(settings_path, "rb")
    prod_urls = pk.load(settings_file)
    print(prod_urls)
    driver = init_webdriver()
    build_dataset(prod_urls,driver)

    settings_file.close()
