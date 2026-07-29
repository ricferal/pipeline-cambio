import requests
import time

URL = "https://servicodados.ibge.gov.br/api/v3/noticias"


def  coletar_noticias(paginas: int = 3, por_pagina: int = 10) -> list[dict]:
    """Percorre páginas da API de notícias e acumula os itens."""
    todas = []

    for page in range(1, paginas + 1):
        params = {"qtd": por_pagina, "page": page}
        resposta = requests.get(URL, params=params, timeout=10)
        resposta.raise_for_status()

        itens = resposta.json()["items"]
        todas.extend(itens)

        print(f"página {page}: +{len(itens)} (total {len(todas)})")
        time.sleep(1)  # educação com o servidor

    return todas


if __name__ == "__main__":
    noticias = coletar_noticias()
    print(f"\nTotal de notícias coletadas: {len(noticias)}")