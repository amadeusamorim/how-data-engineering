import datetime 
from apis import DaySummaryApi

def test_get_endpoint_BTC():
    date = datetime.date(2022, 10, 29) # Data
    api = DaySummaryApi(coin="BTC") # Moeda
    actual = api._get_endpoint(date=date) # Valor em test é o actual
    expected = "https://www.mercadobitcoin.net/api/BTC/day-summary/2022/10/29" # Valor esperado no teste
    assert actual == expected # Retorna verdadeiro se os dois forem iguais e se for True, o teste passou

# É boa prática fazer testes em separado
def test_get_endpoint_ETH():
    date = datetime.date(2022, 10, 29) 
    api = DaySummaryApi(coin="ETH") 
    actual = api._get_endpoint(date=date) 
    expected = "https://www.mercadobitcoin.net/api/ETH/day-summary/2022/10/29" 
    assert actual == expected 