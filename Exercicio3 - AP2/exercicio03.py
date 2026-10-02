import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Abre o arquivo HTML local
local_path = f'file:///{os.path.dirname(os.path.realpath(__file__))}/'
chrome = webdriver.Chrome()
chrome.implicitly_wait(5)
chrome.maximize_window()
chrome.get(f'{local_path}exercicio03.html')
time.sleep(1)

# Nome
campo_nome = chrome.find_element(By.ID, 'nome')
campo_nome.send_keys('Maycon Ribeiro')
time.sleep(0.8)

# RA
campo_ra = chrome.find_element(By.ID, 'ra')
campo_ra.send_keys('123456')
time.sleep(0.8)

# Data de nascimento - Dia
Select(chrome.find_element(By.ID, 'dia')).select_by_visible_text('15')
time.sleep(0.8)

# Data de nascimento - Mês
Select(chrome.find_element(By.ID, 'mes')).select_by_visible_text('Outubro')
time.sleep(0.8)

# Data de nascimento - Ano
Select(chrome.find_element(By.ID, 'ano')).select_by_visible_text('2000')
time.sleep(0.8)

# Curso
Select(chrome.find_element(By.ID, 'curso')).select_by_visible_text('Análise e Desenvolvimento de Sistemas')
time.sleep(0.8)

# Aproveitamento do conteúdo
Select(chrome.find_element(By.ID, 'aproveitamento')).select_by_visible_text('9')
time.sleep(0.8)

# Sugestões
campo_sugestoes = chrome.find_element(By.ID, 'sugestoes')
campo_sugestoes.send_keys('Mais exercícios práticos com Selenium e integração com projetos reais.')
time.sleep(0.8)

# Observações (opcional)
campo_obs = chrome.find_element(By.ID, 'observacoes')
campo_obs.send_keys('Disciplina muito relevante para o mercado de trabalho.')
time.sleep(0.8)

# Clica no botão Enviar Feedback
chrome.find_element(By.ID, 'btn-enviar').click()
time.sleep(2)

print('Formulário preenchido com sucesso!')

# Aguarda para visualizar antes de fechar
time.sleep(5)
chrome.quit()
