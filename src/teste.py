import sys
from pathlib import Path

import pandas as pd

sys.path.append(str(Path(__file__).resolve().parent.parent))

RAW_DIR = Path("data/raw")

caminho = RAW_DIR / f"cotacoes_2026.json"

caminho2 = Path("teste") / f"cotacoes_2026.json"

print(caminho)

print(caminho2)

data = [
    {"id": 1, "name": {"first": "Coleen", "last": "Volk"}},
    {"name": {"given": "Mark", "family": "Regner"}},
    {"id": 2, "name": "Faye Raker"},
]
df = pd.json_normalize(data)

print(df.head())
print(df.info())