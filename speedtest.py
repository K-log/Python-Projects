import json
import io
import sys
import os
import time
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def startup_check(file_path):
    if os.path.isfile(file_path) and os.access(file_path, os.W_OK) and os.access(file_path, os.R_OK):
        # Check if file exists and if we have read/write access
        print("Storage file accessable.")
    else:
        print("File is missing and/or not read/writable, creating a new file...")
        # Seed data for the empty file
        start_data = {
            "speedtest": {
                "date": str(datetime.now()),
                "speed": -1
            }
        }
        with io.open(os.path.join(file_path, 'speed_tests.json'), 'a') as db_file:
            json.dump(start_data, db_file)

    print("Startup checks successful!")
    return True


def render_page(url):
    options = Options()
    options.set_headless(headless=True)
    driver = webdriver.Chrome(chrome_options=options)
    print("Connecting to URL...")
    driver.get(url)
    print("Waiting for page contents to load...\n(Should take about 10 seconds)")
    time.sleep(10)
    print("Web page content retrieval successful!")
    ret = driver.page_source
    print('Closing browser...')
    driver.close()
    return ret 

def find_elements(page_source):
    try:
        print('Parsing webpage source...')
        soup = BeautifulSoup(page_source, "html.parser")
        speed_value = soup.find('div', attrs={'class': 'speed-results-container'})
    except:
        print('Failed to parse webpage source...')
        speed_value = -1
    return speed_value

def store_data(data, file_path):
    pass 
    """
     with io.open(file_path, 'w') as db_file:
         entry = {
             "speedtest"
         } 
        json.dump( db_file)
    """
if __name__ == "__main__":
    path = sys.argv[0]
    try:
        startup_check(path)
    except:
        print("Failed to complete startup check.")
    target_url = "http://fast.com"
    page = render_page(target_url)
    contents = find_elements(page)
    print("Your current download speed is: " + contents.string + "Mbps!")
    store_data(contents.string, path)