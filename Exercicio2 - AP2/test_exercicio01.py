import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

LOCAL_PATH = f'file:///{os.path.dirname(os.path.realpath(__file__))}/'

@pytest.fixture
def driver():
    chrome = webdriver.Chrome()
    chrome.implicitly_wait(5)
    chrome.get(f'{LOCAL_PATH}exercicio01.html')
    time.sleep(2)
    yield chrome
    time.sleep(2)
    chrome.quit()

def test_titulo_da_pagina(driver):
    assert driver.title == 'Exercício 01'

def test_conteudo_por_tag_name(driver):
    paragrafo = driver.find_element(By.TAG_NAME, 'p')
    assert paragrafo.text == 'O conteúdo do site vem aqui'

def test_conteudo_por_css_selector(driver):
    paragrafo = driver.find_element(By.CSS_SELECTOR, 'p.content')
    assert paragrafo.text == 'O conteúdo do site vem aqui'