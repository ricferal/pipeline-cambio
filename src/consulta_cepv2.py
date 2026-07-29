import requests


def consultar_cep(cep: str) -> dict | None:
    """Consulta um CEP no ViaCEP. Devolve dict ou None se falhar."""
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()
        if dados.get("erro"):
            print(f"[aviso] CEP {cep} não existe")
            return None
        return dados
    except requests.exceptions.Timeout:
        print(f"[erro] ViaCEP demorou demais (CEP={cep})")
        return None
    except requests.exceptions.ConnectionError:
        print("[erro] Sem conexão ou servidor fora do ar")
        return None
    except requests.exceptions.HTTPError as erro:
        print(f"[erro] HTTP {resposta.status_code}: {erro}")
        return None
    except requests.exceptions.Timeout:
        print(f"[erro] ViaCEP demorou demais (CEP={cep})")
        return None
    except requests.exceptions.ConnectionError:
        print("[erro] Sem conexão ou servidor fora do ar")
        return None
    except requests.exceptions.HTTPError as erro:
        print(f"[erro] HTTP {resposta.status_code}: {erro}")
        return None

    if dados.get("erro"):
        print(f"[aviso] CEP {cep} não existe")
        return None

    return dados
    
if __name__ == "__main__":
    ceps = ["11111111", "abc", "52050480", "00000000", "01310100", "60356000"]
    for cep in ceps:
        endereco = consultar_cep(cep)
        if endereco:
            print(cep, endereco["logradouro"], endereco["bairro"],endereco["estado"])


