#%%
# Imports
import requests
import json

# %%

x = [
    12,
    13,
    42,
    51
]


# %%
print(x)
# %%
url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'

ret = requests.get(url) # get coleta dado de um lugar

# %%

# print(ret)
# O retorno 200, significa que o código teve sucesso

# ret.text traz um retrato de como está o código da respectiva página (normalmente em html)
print(ret.text)

# Para tratar os dados é necessário fazer um parse (fatiar os dados)
# %%

# Identifica se o retorno for positivo (200), ele printa
if ret:
    print(ret)
else:
    print('Falhou')
# %%

# Conseguimos visualizar o arquivo em json
json.loads(ret.text)
# %%

# Carregando apenas a cotação
dolar = json.loads(ret.text)['USDBRL']
# %%

# Retorno apenas a cotação do dólar
dolar['bid']

# %%

# Posso converter para usar o valor, exemplo:
print(f"15 dólares hoje equivale a {float(dolar['bid'])*15} reais.")


# %%

def cotacao(valor, moeda):
    url = f'https://economia.awesomeapi.com.br/json/last/{moeda}'
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-', '')]
    print(f"{valor} {moeda[:3]} hoje equivale a {float(dolar['bid']) * valor} {moeda[4:]}.")
# %%

cotacao(35, 'JPY-BRL')


# %%

# Tratando o erro
try:
    cotacao(20, 'Amadeus')
except:
    pass
else:
    print('ok')
# %%
try:
    cotacao(20, 'Amadeus')
except Exception as e:
    print(e)
else:
    print('ok')
# %%
try:
    10/0
except Exception as e:
    print(e)
else:
    print('ok')
# %%

def multi_moedas(valor, moeda):
    url = f'https://economia.awesomeapi.com.br/json/last/{moeda}'
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-', '')]
    print(f"{valor} {moeda[:3]} hoje equivale a {float(dolar['bid']) * valor} {moeda[4:]}.")

# %%
multi_moedas(20, 'USD-BRL')
# %%

# Busca uma função e valida se a função que passei e seus parâmetros
def error_check(func):
    def inner_func(*args, **kargs):
        try:
            func(*args, **kargs)
        except:
            print(f"{func.__name__} falhou")
    return inner_func

@error_check # Decorador da função
# Para função abaixo executar, ele vai precisar passar pelo @erro_check
def multi_moedas(valor, moeda):
    url = f'https://economia.awesomeapi.com.br/json/last/{moeda}'
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-', '')]
    print(f"{valor} {moeda[:3]} hoje equivale a {float(dolar['bid']) * valor} {moeda[4:]}.")

#%%
multi_moedas(20, 'USD-BRL')
multi_moedas(20, 'EUR-BRL')
multi_moedas(20, 'RPL-BRL')
multi_moedas(20, 'BTC-BRL')
multi_moedas(20, 'JPY-BRL')

#%%
import backoff
import random


# Trago o decorador backoff e listo as exceptions
# O expo expõe as falhas que podem acontecer
# Trago os tipos de exceção
# Numa API não podemos só tratar o erro, mas temos de tentar solucionar
# O max_tries limita a quantidade máxima de vezes que ele vai tentar rodar a API até funcionar
@backoff.on_exception(backoff.expo, (ConnectionAbortedError, ConnectionRefusedError, TimeoutError), max_tries=10)
def test_func(*args, **kargs):
    rnd = random.random()
    print(f"""
            RND = {rnd}
            args = {args if args else 'sem args'}
            kargs = {kargs if kargs else 'sem kargs'}
    """)
    if rnd < .2:
        raise ConnectionAbortedError('Conexão foi finalizada')
    elif rnd < .4:
        raise ConnectionRefusedError('Conexão foi recusada')
    elif rnd < .6:
        raise TimeoutError('Tempo de espera excedido')
    else:
        return "OK!"


# %%

# Testando com args
test_func(55)

# %%

# Testando com kargs
test_func(nome='Amadeus')

#%%
# Pacote para logs
import logging

#%%

log = logging.getLogger()  # Pego o log
log.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
) # Dia da info, nome do usuário, nível da minha info e mensagem
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)

# %%

# Uma ótima maneira de usar o backoff e o tratamento de erros é na ingestão de dados

@backoff.on_exception(backoff.expo, (ConnectionAbortedError, ConnectionRefusedError, TimeoutError), max_tries=10)
def test_func(*args, **kargs):
    rnd = random.random()
    log.debug(f"RND = {rnd}")     
    log.debug(f"args = {args if args else 'sem args'}")
    log.debug(f"kargs = {kargs if kargs else 'sem kargs'}")
    if rnd < .2:
        log.error('Conexão foi finalizada')
        raise ConnectionAbortedError('Conexão foi finalizada')
    elif rnd < .4:
        log.error('Conexão foi recusada')
        raise ConnectionRefusedError('Conexão foi recusada')
    elif rnd < .6:
        log.error('Tempo de espera excedido')
        raise TimeoutError('Tempo de espera excedido')
    else:
        return "OK!"