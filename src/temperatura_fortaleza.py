import requests

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import requests
from config import OPENWEATHER_API_KEY


def obter_parametros_clima() -> dict:
    """Retorna os parâmetros para a requisição da API de clima."""
    return {
        "q": "Fortaleza,BR",
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
        "lang": "pt_br"
    }


def obter_temperatura_fortaleza() -> None:
    """Obtém e exibe a temperatura atual de Fortaleza."""
    url = "https://api.openweathermap.org/data/2.5/weather"

    parametros = obter_parametros_clima()

    try:
        resposta = requests.get(
            url,
            params=parametros,
            timeout=10
        )

        resposta.raise_for_status()

        dados = resposta.json()

        cidade = dados["name"]
        temperatura = dados["main"]["temp"]
        sensacao_termica = dados["main"]["feels_like"]
        temperatura_minima = dados["main"]["temp_min"]
        temperatura_maxima = dados["main"]["temp_max"]
        umidade = dados["main"]["humidity"]
        descricao = dados["weather"][0]["description"]

        print(f"Cidade: {cidade}")
        print(f"Temperatura atual: {temperatura:.1f} °C")
        print(f"Sensação térmica: {sensacao_termica:.1f} °C")
        print(f"Temperatura mínima: {temperatura_minima:.1f} °C")
        print(f"Temperatura máxima: {temperatura_maxima:.1f} °C")
        print(f"Umidade: {umidade}%")
        print(f"Condição: {descricao.capitalize()}")

    except requests.exceptions.Timeout:
        print("A requisição demorou muito para responder.")

    except requests.exceptions.ConnectionError:
        print("Não foi possível conectar à API.")

    except requests.exceptions.HTTPError:
        if resposta.status_code == 401:
            print("API key inválida ou ainda não ativada.")

        elif resposta.status_code == 404:
            print("Cidade não encontrada.")

        else:
            print(f"Erro HTTP: {resposta.status_code}")
            print(resposta.text)

    except KeyError:
        print("A resposta da API não possui os dados esperados.")

    except requests.exceptions.RequestException as erro:
        print(f"Erro durante a requisição: {erro}")


if __name__ == "__main__":
    obter_temperatura_fortaleza()