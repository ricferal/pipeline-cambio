import requests
url = "https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=26c24013a8d6c1a5e5eeb63f82dcb402"
resposta = requests.get(url, timeout=10)
print("Status:", resposta.status_code) # passo 1: rodar e ver 200
tempo = resposta.json() # passo 2: converter
print("Tipo:", type(tempo)) # <class 'dict'>
print(tempo) 
