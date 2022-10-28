#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

#%%
s = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=s)
driver.get('https://pt.wikipedia.org/wiki/Nicolas_Cage')
tabela = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]')
# driver.close()

# %%
print(tabela.get_attribute('innerHTML'))

# %%

# Preciso adicionar a referência de que ela é uma table
# Coloco a referência 0, pois ele criou uma lista
df = pd.read_html('<table> ' + tabela.get_attribute('innerHTML')+ '</table>')[0]

#%%

# O with garante que o arquivo esteja aberto somente enquanto o laço dele esteja rodando
with open('print.png', 'wb') as f:
    f.write(driver.find_element(By.XPATH, '/html/body/div[1]').screenshot_as_png) # Screenshot da página

# %%

# Retorno só os filmes do ano de 1984
df[df['Ano']==1984]
# %%

# Persistindo em csv
df.to_csv('filmes_Nicolas_cage.csv', sep=';', index=False)
# %%

# pip freeze -> Lista todos os pacotes que tenho instalado

# Ideal é salvarmos os pacotes em um txt, passando pip freeze > requirements.txt

# Para instalar os pacotes, uso o pip install -r arquivo.txt