import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import webbrowser
from selenium import webdriver
import urllib
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from tqdm import notebook
import time

df = pd.read_csv('countries.csv')


def element_presence(by, xpath, time):
    element_present = EC.presence_of_all_elements_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)


def send_message(url):
    driver.get(url)
    time.sleep(2)
    element_presence(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    msg_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    msg_box.send_keys('\n')
    time.sleep(1)

def prepare_msg(dataframe, name_col, phone_col):
    file = dataframe[[name_col, phone_col]]
    base_msg = """
    Hi {}
    Texting ! Texting Python !!!!
    """
    base_url = 'https://web.whatsapp.com/send?phone={}&text={}'
    for i, j in notebook.tqdm(file.iterrows()):
        phone_no = j[phone_col]
        name = i[name_col].title()
        msg = urllib.parse.quote(base_msg.format(name))
        url_msg = base_url.format(phone_no, msg)
        send_message(url_msg)

chrome_options = Options()
chrome_options.add_argument("--user-data-dir-Session")
chrome_options.add_argument("--profile-directory=Default")

PATH = "./chromedriver.exe"
driver = webdriver.Chrome(executable_path='C:/bin/chromedriver.exe', options=chrome_options)
prepare_msg(df, 'Name', 'Phone')