import requests
import matplotlib.pyplot as plt

# Puxando a API de Cotações
cotacoes_all = requests.get('https://economia.awesomeapi.com.br/json/all')
cotacoes_dic_all = cotacoes_all.json()

# Pegando cotação atual do Dólar, Euro e Bitcoin
print('Dolar: {}'.format(cotacoes_dic_all['USD']['bid']))
print('Euro: {}'.format(cotacoes_dic_all['EUR']['bid']))
print('Bitcoin: {}'.format(cotacoes_dic_all['BTC']['bid']))


# Puxando API da cotação do Dólar em dias limitados
cotacoes_dollar = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/30')
cotacoes_dic_dollar = cotacoes_dollar.json()

# Pegando cotação dos últimos 30 dias do Dólar
lista_cotacoes_dollar = [float(item['bid']) for item in cotacoes_dic_dollar]
print(lista_cotacoes_dollar)

# Puxando API da cotação do Bitcoin de um período específico
cotacoes_bitcoin = requests.get('https://economia.awesomeapi.com.br/json/daily/BTC-BRL/200?start_date=20220101&end_date=2022090017')
cotacoes_dic_bitcoin = cotacoes_bitcoin.json()

# Pegando cotações do Bitcoin de Jan/21 a Out/21
lista_cotacoes_bitcoin = [float(item['bid']) for item in cotacoes_dic_bitcoin]
lista_cotacoes_bitcoin.reverse()

# Gráficos com as cotações do Bitcoin
plt.figure(figsize=(15, 5))
plt.plot(lista_cotacoes_bitcoin)
plt.show()