#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import sys

#%%
# Passo o cep como parâmetro na execução do arquivo
cep = sys.argv[1]

if cep:
    # Passo o relative path do meu chromedriver
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)    
    #%%
    # ### SITE DA HOW ###

    # # Entra no site repassado como parâmetro
    # driver.get('https://howedu.com.br/')
    # # Clica no elemento da tela inspecionando e copiando seu xpath
    # driver.find_element("xpath", '//*[@id="adopt-accept-all-button"]').click()
    # driver.find_element("xpath", '//*[@id="bootcamps"]/div/div/div/div[4]/div/div/div/form/div[2]/label/div/span').click()

    # %%
    # Acessando o site de BuscaCEP dos Correios
    driver.get('https://buscacepinter.correios.com.br/app/endereco/index.php?t')
    # Inspeciono e coleto o nome da busca do endereço
    elem_cep = driver.find_element(By.NAME, 'endereco')

    # %%
    # Boa prática para limpar a página de pesquisa
    elem_cep.clear()

    #%%
    # Passa uma sequência de caracteres
    elem_cep.send_keys('58074152')

    # %%
    # Usando o botão do tipo CEP
    elem_cmb = driver.find_element(By.NAME, 'tipoCEP')
    elem_cmb.click()
    # Selecionando logradouro
    driver.find_element(By.XPATH, '//*[@id="tipoCEP"]/optgroup/option[1]').click()

    # %%
    # Clicando no botão pesquisar
    driver.find_element(By.ID, 'btn_pesquisar').click()

    #%%
    # Retorno o texto que está dentro do elemento repassado
    logradouro = driver.find_element(By.XPATH, '/html/body/main/form/div[1]/div[2]/div/div[4]/table/tbody/tr/td[1]').text
    bairro = driver.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]').text
    localidade = driver.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]').text

    # Fecha o navegador no final
    driver.close()
    # %%
    print("""
    Para o CEP {}, temos:

    Endereço: {}
    Bairro: {}
    Localidade: {}
    """.format(
    cep,
    logradouro,
    bairro,
    localidade
    ))
