import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

local_path = f'file:///{os.path.dirname(os.path.realpath(__file__))}/'
chrome = webdriver.Chrome()
chrome.implicitly_wait(5)

chrome.get(f'{local_path}exercicio01.html')
time.sleep(2)

titulo = chrome.title
print(f'a) Título da página: {titulo}')
time.sleep(2)

paragrafo_tag = chrome.find_element(By.TAG_NAME, 'p')
print(f'b) Conteúdo via TAG_NAME: {paragrafo_tag.text}')
time.sleep(2)

paragrafo_css = chrome.find_element(By.CSS_SELECTOR, 'p.content')
print(f'c) Conteúdo via CSS_SELECTOR: {paragrafo_css.text}')
time.sleep(3)

chrome.quit()