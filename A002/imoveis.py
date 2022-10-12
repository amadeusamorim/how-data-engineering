#%%
from os import link
from wsgiref.validate import validator
from pyparsing import col
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from wcwidth import wcswidth
import json
import time

# %%

url = "https://glue-api.vivareal.com/v2/listings?addressCity=João Pessoa&addressLocationId=BR>Paraiba>NULL>Joao Pessoa&addressNeighborhood&addressState=Paraíba&addressCountry=Brasil&addressStreet&addressZone&addressPointLat=-7.118835&addressPointLon=-34.881434&business=SALE&facets=amenities&unitTypes=APARTMENT&unitSubTypes=UnitSubType_NONE,DUPLEX,LOFT,STUDIO,TRIPLEX&unitTypesV3=APARTMENT&usageTypes=RESIDENTIAL&listingType=USED&parentId=null&categoryPage=RESULT&includeFields=search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones),medias,accountLink,link)),totalCount),page,seasonalCampaigns,fullUriFragments,nearby(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones),medias,accountLink,link)),totalCount)),expansion(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones),medias,accountLink,link)),totalCount)),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones,phones),developments(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones),medias,accountLink,link)),totalCount)),owners(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,unitTypes,nonActivationReason,propertyType,unitSubTypes,id,portal,parkingSpaces,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,bedrooms,pricingInfos,showPrice,status,advertiserContact,videoTourLink,whatsappNumber,stamps),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,phones),medias,accountLink,link)),totalCount))&size=300&from={}&q&developmentsSize=5&levels=CITY,UNIT_TYPE&ref&pointRadius&isPOIQuery"


headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)",
 "x-domain": "www.vivareal.com.br" 
}

payload = ""

#%%

def get_json(url, i, headerList, payload):
    ret = requests.request("GET", url.format(i), data=payload, headers=headerList)
    soup = bs(ret.text, 'html.parser')
    return json.loads(soup.text)

#%%

df = pd.DataFrame(
    columns=[
        'descricao',
        'endereco',
        'area',
        'quartos',
        'wc',
        'vagas',
        'valor',
        'condominio',
        'wlink'
    ]
)


# %%

imovel_id = 0
json_data = get_json(url, imovel_id, headersList, payload)

while len(json_data['search']['result']['listings']) > 0:
    qtd = len(json_data['search']['result']['listings']) # Qtd de registros que recebi
    print(f'Qtd de imóveis: {qtd} | Total: {imovel_id}') # Qtd de imóveis e total
    for i in range(0, qtd):
        try:
            descricao = json_data['search']['result']['listings'][i]['listing']['title']
        except:
            descricao = '-'
        try:
            try:
                endereco = json_data['search']['result']['listings'][i]['listing']['address']['street'] + ", " + json_data['search']['result']['listings'][i]['listing']['address']['streetNumber']
            except:
                endereco = json_data['search']['result']['listings'][i]['listing']['address']['street']
        except:
            endereco = '-'
        try:
            area = json_data['search']['result']['listings'][i]['listing']['totalAreas']
        except:
            area = '-'
        try:
            quartos = json_data['search']['result']['listings'][i]['listing']['bedrooms']
        except:
            quartos = '-'
        try:
            wc = json_data['search']['result']['listings'][i]['listing']['bathrooms']
        except:
            wc = '-'
        try:
            vagas = json_data['search']['result']['listings'][i]['listing']['parkingSpaces']
        except:
            vagas = '-'
        try:
            valor = json_data['search']['result']['listings'][i]['listing']['pricingInfos'][0]['price']
        except:
            valor = '-'
        try:
            condominio = json_data['search']['result']['listings'][i]['listing']['pricingInfos'][0]['monthlyCondoFee']
        except:
            condominio = '-'
        try:
            wlink = 'https://www.vivareal.com.br' + json_data['search']['result']['listings'][i]['link']['href']
        except:
            wlink = '-'
        
        df.loc[df.shape[0]] = [
            descricao,
            endereco,
            area,
            quartos,
            wc,
            vagas,
            valor,
            condominio,
            wlink
        ]
    
    imovel_id = imovel_id + qtd
    if imovel_id > 9500: # Mais de 10.000 imóveis a API para, colocando 9500 por margem
        break
    time.sleep(2) # Evitando erro 429 (Timeout)
    json_data = get_json(url, imovel_id, headersList, payload)

#%%

df.to_csv('banco_de_imoveis.csv', sep=';', index=False)

#%%

# Código antigo

# i = 1
# ret = requests.get(url.format(i))
# soup = bs(ret.text)

#%%

# Código antigo sem API

# houses = soup.find_all('a', {'class': 'property-card__content-link js-card-title'}) # Pego só a classe que tem aquele meu link repassado
# qtd_imoveis = float(soup.find('strong', {'class': 'results-summary__count'}).text.replace('.', ''))

# %%

# len(houses) # Quantidade de casas por página
# qtd_imoveis # Quantidade total de imóveis

# tot_pag = qtd_imoveis / len(houses) # Total de páginas

#%%

# house = houses[0]

# %%

# house

# %%



#%%

# Código antigo

# for house in houses:
#     try:
#         descricao = house.find('span', {'class':'property-card__title'}).text.strip()
#     except:
#         descricao = None
#     try:
#         endereco = house.find('span', {'class':'property-card__address'}).text.strip()
#     except:
#         endereco = None
#     try:
#         area = house.find('span', {'class':'js-property-card-detail-area'}).text.strip()
#     except:
#         area = None
#     try:
#         quartos = house.find('li', {'class':'js-property-detail-rooms'}).span.text.strip()
#     except:
#         quartos = None
#     try:
#         wc = house.find('li', {'class':'js-property-detail-bathroom'}).span.text.strip()
#     except:
#         wc = None
#     try:
#         vagas = house.find('li', {'class':'js-property-detail-garages'}).span.text.strip()
#     except:
#         vagas = None
#     try:
#         valor = house.find('div', {'class':'js-property-card__price-small'}).p.text.strip()
#     except:
#         valor = None
#     try:
#         condominio = house.find('strong', {'class':'js-condo-price'}).text.strip()
#     except:
#         condominio = None
#     try:
#         wlink = 'https://www.vivareal.com.br' + house['href']
#     except:
#         wlink = None
    
#     df.loc[df.shape[0]] = [
#         descricao,
#         endereco,
#         area,
#         quartos,
#         wc,
#         vagas,
#         valor,
#         condominio,
#         wlink
#     ]

#%%
