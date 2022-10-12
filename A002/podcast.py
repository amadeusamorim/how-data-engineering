#%%
import requests
from bs4 import BeautifulSoup as bs
import logging
import pandas as pd

#%%

url = 'https://portalcafebrasil.com.br/'

# %%

# Retorno
ret = requests.get(url)

# %%
ret.text
# %%
# pip install bs4 (importo o BeautifulSoup)

soup = bs(ret.text)

#%%

soup
# %%
soup.find('h5')

#%%
soup.find('h5').text

# %%
soup.find_all('h5')

# %%
lst_podcast = soup.find_all('h5')

#%%

for item in lst_podcast:
    print(f"EP: {item.text}")
# %%

# Extraio a informação do inspect
url = 'https://portalcafebrasil.com.br/todos/podcasts/page/{}/?ajax=true'
# %%

url.format(5)
# %%

def get_podcast(url):
    ret = requests.get(url)
    soup = bs(ret.text)
    return soup.find_all('h5')

# %%
get_podcast(url.format(5))

#%%

log = logging.getLogger()  
log.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)

# %%

i = 1
lst_podcast = []
lst_get = get_podcast(url.format(i)) # Lista intermediária
log.debug(f"Coletado {len(lst_get)} episódios do link: {url.format(i)}")

while len(lst_get) > 0:
    lst_podcast = lst_podcast + lst_get
    i += 1
    lst_get = get_podcast(url.format(i))
    log.debug(f"Coletado {len(lst_get)} episódios do link: {url.format(i)}")

#%%
len(lst_podcast) # Quantidade de podcasts

# %%
lst_podcast


# %%
df = pd.DataFrame(columns=['nome', 'link'])

# %%
for item in lst_podcast:
    df.loc[df.shape[0]] = [item.text, item.a['href']] # shape retorna as duas dimensões do df

# %%
df.shape


# %%
df

# %%
df.to_csv('banco_de_podcasts.csv', sep=';', index=False)

# %%
