import pandas as pd
from pathlib import Path
from typing import List

# Define os caminhos base para o projeto
# Isso torna o script executável de qualquer lugar, mantendo as referências corretas.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "movies.csv"
PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed" / "movie_metadata.csv"


def _clean_text_data(text: str) -> str:
    """
    Remove espaços de strings para criar tokens únicos.
    Ex: 'Science Fiction' -> 'ScienceFiction'
    """
    if isinstance(text, str):
        return text.replace(" ", "").lower()
    return ""


def _create_metadata_soup(df: pd.DataFrame, columns: List[str]) -> pd.Series:
    """
    Combina múltiplas colunas de texto em uma única string ("soup").

    Args:
        df (pd.DataFrame): O DataFrame contendo os dados.
        columns (List[str]): Uma lista de nomes de colunas para combinar.

    Returns:
        pd.Series: Uma série contendo a string de metadados combinada para cada filme.
    """
    soup = pd.Series([""] * len(df), index=df.index)
    for col in columns:
        soup += df[col].apply(_clean_text_data) + " "
    return soup


def load_and_process_data(input_path: Path, output_path: Path) -> None:
    """
    Carrega os dados brutos, limpa, cria a coluna de metadados ("soup")
    e salva o arquivo processado.

    Args:
        input_path (Path): Caminho para o arquivo CSV bruto.
        output_path (Path): Caminho para salvar o arquivo CSV processado.
    """
    print("Iniciando o carregamento e processamento de dados...")

    # Carrega o dataset
    df = pd.read_csv(input_path)

    # Colunas que serão usadas para a recomendação
    feature_columns = ["genres", "director", "actors", "keywords"]

    # Preenche valores nulos com strings vazias para evitar erros
    for col in feature_columns:
        df[col] = df[col].fillna("")

    # Cria a coluna "soup" combinando os metadados
    print("Criando a coluna de metadados ('soup')...")
    df["soup"] = _create_metadata_soup(df, feature_columns)

    # Seleciona as colunas relevantes e salva o arquivo processado
    processed_df = df[["title", "soup"]]

    # Garante que o diretório de saída exista
    output_path.parent.mkdir(parents=True, exist_ok=True)
    processed_df.to_csv(output_path, index=False)

    print(f"Dados processados e salvos com sucesso em: {output_path}")


if __name__ == "__main__":
    # Este bloco permite que o script seja executado diretamente para processar os dados
    load_and_process_data(
        input_path=RAW_DATA_PATH, output_path=PROCESSED_DATA_PATH
    )

