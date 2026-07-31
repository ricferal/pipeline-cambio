import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import pandas as pd
import requests
from sqlalchemy import create_engine
from config import POSTGRES_URL
URL = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
resposta = requests.get(URL, timeout=10)

resposta.raise_for_status()
df = pd.json_normalize(resposta.json(), sep="_")
engine = create_engine(POSTGRES_URL)
df.to_sql("estados", engine, if_exists="replace", index=False)
conferencia = pd.read_sql(
    "SELECT sigla, nome, regiao_nome FROM estados LIMIT 5", engine)
print(conferencia)