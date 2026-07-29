import requests

def consultar_cep(cep: str) -> dict | None:
    """Consulta um CEP no ViaCEP. Devolve dict, ou None se falhar."""
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url, timeout=10)  # cinto 1
        resposta.raise_for_status()  # cinto 2
        print(resposta.status_code)
    except requests.exceptions.Timeout:  # cinto 3...
        print(f"[erro] ViaCEP demorou demais (cep={cep})")
        return None
    except requests.exceptions.ConnectionError:
        print("[erro] Sem conexao ou servidor fora do ar")
        return None
    except requests.exceptions.HTTPError as erro:
        print(f"[erro] HTTP {resposta.status_code}: {erro}")
        return None

    return resposta.json()



#url = "https://viacep.com.br/ws/60356000/json/"
#url = "https://viacep.com.br/ws/00000000/json/"
url = "https://viacep.com.br/ws/abc/json/"
resposta = requests.get(url, timeout=10)
#print("Status", resposta.status_code) 
#print("Texto da resposta",resposta.json()) 
#print("Texto da resposta",resposta.text) 
#consultar_cep("60356000")
#consultar_cep("abc")
#consultar_cep("00000000")
consultar_cep("abc")

print("Texto da resposta",resposta.text) 
#print("Texto da resposta",resposta.json()) 


