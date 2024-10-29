import requests #importar biblioteca

response = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")

dados = response.json()

taxa_dolar = dados["USDBRL"]["bid"]
print(f"Taxa do dólar: {taxa_dolar}")