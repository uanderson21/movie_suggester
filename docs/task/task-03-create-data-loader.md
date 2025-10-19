# 📜 Tarefa 03: Criar o Script de Carregamento e Processamento de Dados

**Objetivo:** Implementar o script `src/data/data_loader.py`, responsável por carregar os dados brutos, realizar a limpeza e o pré-processamento, e salvar os dados tratados para a próxima fase.

## Descrição

Este script é o primeiro passo do pipeline de ML. Ele deve ser capaz de:
1.  Ler o arquivo `data/raw/movies.csv`.
2.  Tratar valores ausentes nas colunas de metadados (`genres`, `director`, `actors`, `keywords`).
3.  Limpar e padronizar os dados textuais, removendo espaços para criar tokens únicos (ex: "Science Fiction" -> "sciencefiction").
4.  Criar a coluna "soup", que é a concatenação de todos os metadados relevantes em uma única string para cada filme.
5.  Salvar um novo arquivo `data/processed/movie_metadata.csv` contendo apenas as colunas `title` e `soup`.

## Código de Implementação (`src/data/data_loader.py`)

O script a ser criado deve conter a seguinte lógica:

```python
import pandas as pd
from pathlib import Path
from typing import List

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "movies.csv"
PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed" / "movie_metadata.csv"

def load_and_process_data(input_path: Path, output_path: Path) -> None:
    """
    Carrega os dados brutos, limpa, cria a coluna de metadados ("soup")
    e salva o arquivo processado.
    """
    df = pd.read_csv(input_path)
    feature_columns = ["genres", "director", "actors", "keywords"]
    for col in feature_columns:
        df[col] = df[col].fillna("")
    df["soup"] = df[feature_columns].apply(lambda row: ' '.join(row.astype(str).str.replace(' ', '')), axis=1)
    processed_df = df[["title", "soup"]]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    processed_df.to_csv(output_path, index=False)
    print(f"Dados processados e salvos com sucesso em: {output_path}")
```

## Critérios de Aceitação
- O arquivo `src/data/data_loader.py` é criado com a lógica descrita.
- O script pode ser executado de forma independente via `python src/data/data_loader.py`.
- Após a execução, o arquivo `data/processed/movie_metadata.csv` é gerado corretamente.