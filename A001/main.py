import requests
import pandas as pd
import collections

# Caminho que devemos acessar para puxar os dados da loteria
url = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados?modalidade=Lotofácil'

# Request simula um acesso ao site
r = requests.get(url, verify=False) # verify=False para não validar o SSL

# Uso o text para transformar o que extraí do site em texto
r_text = r.text # transformando a resposta do request em formato de string

r_text

# Removendo valores caracteres nao necessárias, se nao removidas os dados iram possuir as mesmas
r_text = r_text.replace('\r\n', '') # Trantando as linhas sujas
r_text = r_text.replace('"\r\n}', '')
r_text = r_text.replace('{\r\n} "html": "', '')

df = pd.read_html(r_text, encoding='utf-8')[0]

type(df)

new_columns = df.columns
new_columns = list(i.replace('\\r\\n', '') for i in new_columns) # Tratando as colunas que estavam sujas
new_columns

df.columns = new_columns # Inserindo no df as colunas ajustadas
df # O df ainda tem linhas em branco, o que me interessa é apenas a linha populada
df = df[df['Bola1'] == df['Bola1']] # Quando comparo valor nulo com valor nulo, ele nunca vai ser igual, dessa forma garanto retirar os valores nulos do df

# A Lotofácil tem 25 números e você precisa escolher 15 números entre eles

nr_pop = list(range(1, 26)) # Carrego a população dos meus números da Lotofácil 1 - 25

# Números que quero encontrar
nr_pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
nr_impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
nr_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23]

# Combinações possíveis considerando pares, ímpares e primos
comb = []

# Número de veses que foi sorteado o número (À ser agregado os valores com o loop)
v_01 = 0
v_02 = 0
v_03 = 0
v_04 = 0
v_05 = 0
v_06 = 0
v_07 = 0
v_08 = 0
v_09 = 0
v_10 = 0
v_11 = 0
v_12 = 0
v_13 = 0
v_14 = 0
v_15 = 0
v_16 = 0
v_17 = 0
v_18 = 0
v_19 = 0
v_20 = 0
v_21 = 0
v_22 = 0
v_23 = 0
v_24 = 0
v_25 = 0

# Colunas que vou querer dentro do meu loop para buscar os números sorteados
lst_campos = ['Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5',
              'Bola6', 'Bola7', 'Bola8', 'Bola9', 'Bola10', 'Bola11', 'Bola12',
              'Bola13', 'Bola14', 'Bola15']

# A função iterrows faz o loop percorrer linha a linha de um dataframe (index é o número da linha, o row é o valor da linha)
for index, row in df.iterrows():
    # Em cada linha eu zero os valores de pares, ímpares e primos para que possa contabilizar o número por concurso
    v_pares = 0
    v_impares = 0
    v_primos = 0
    for campo in lst_campos:
        if row[campo] in nr_pares:
            v_pares += 1
        if row[campo] in nr_impares:
            v_impares += 1
        if row[campo] in nr_primos:
            v_primos += 1
        if row[campo] == 1:
            v_01 += 1
        if row[campo] == 2:
            v_02 += 1
        if row[campo] == 3:
            v_03 += 1
        if row[campo] == 4:
            v_04 += 1
        if row[campo] == 5:
            v_05 += 1
        if row[campo] == 6:
            v_06 += 1
        if row[campo] == 7:
            v_07 += 1
        if row[campo] == 8:
            v_08 += 1
        if row[campo] == 9:
            v_09 += 1
        if row[campo] == 10:
            v_10 += 1
        if row[campo] == 11:
            v_11 += 1
        if row[campo] == 12:
            v_12 += 1
        if row[campo] == 13:
            v_13 += 1
        if row[campo] == 14:
            v_14 += 1
        if row[campo] == 15:
            v_15 += 1
        if row[campo] == 16:
            v_16 += 1
        if row[campo] == 17:
            v_17 += 1
        if row[campo] == 18:
            v_18 += 1
        if row[campo] == 19:
            v_19 += 1
        if row[campo] == 20:
            v_20 += 1
        if row[campo] == 21:
            v_21 += 1
        if row[campo] == 22:
            v_22 += 1
        if row[campo] == 23:
            v_23 += 1
        if row[campo] == 24:
            v_24 += 1
        if row[campo] == 25:
            v_25 += 1
    # Antes de zerar os valores eu dou o append na minha lista comb
    comb.append(str(v_pares) + 'p-' + str(v_impares) + 'i-'+str(v_primos)+'np')


freq_nr = [
    [1, v_01],
    [2, v_02],
    [3, v_03],
    [4, v_04],
    [5, v_05],
    [6, v_06],
    [7, v_07],
    [8, v_08],
    [9, v_09],
    [10, v_10],
    [11, v_11],
    [12, v_12],
    [13, v_13],
    [14, v_14],
    [15, v_15],
    [16, v_16],
    [17, v_17],
    [18, v_18],
    [19, v_19],
    [20, v_20],
    [21, v_21],
    [22, v_22],
    [23, v_23],
    [24, v_24],
    [25, v_25]
]

# Ordeno a minha lista pelo segundo valor dela (tup[1])
freq_nr.sort(key=lambda tup: tup[1])
freq_nr[0]  # primeiro
freq_nr[-1]  # ultimo

# Trago os dados da minha lista comb para uma collections e irá quase num dataframe
counter = collections.Counter(comb)

# Transformo minha collections num df
resultado = pd.DataFrame(counter.items(), columns=['Combinacao', 'Frequencia'])

# Adiciono uma coluna e insiro nela o valor da minha frequência em percentual 
resultado['p_freq'] = resultado['Frequencia']/resultado['Frequencia'].sum()

# Ordeno meu df de acordo com a minha frequência (p_freq)
resultado = resultado.sort_values(by='p_freq')

print('''
O número mais frequente é o:  {}
O número menos frequente é o:  {}
A combinação de Pares, Ímpares e Primos mais frequente é: {} com a frequencia de: {}%
'''.format(freq_nr[-1][0], freq_nr[0][0], resultado['Combinacao'].values[-1], int((resultado['p_freq'].values[-1]*100)*100)/100)
)