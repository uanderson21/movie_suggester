# 🎥 Guidelines de Projeto: Movie Suggester

## I. Definição do Projeto

- **Título:** Sistema de Recomendação de Filmes (Baseado em Conteúdo)
- **Objetivo:** Implementar um sistema que sugere filmes a partir de um título de referência, calculando a similaridade com base nos metadados (gênero, diretores, atores, tags).
- **Tecnologia Principal:** Python, Pandas, Scikit-learn (TfIdf, Similaridade de Cosseno).
- **Resultado Esperado:** Uma função ou API que recebe o nome de um filme e retorna uma lista ordenada dos Top 10 filmes mais similares.

## II. Estrutura de Pastas e Arquivos (Padrão Data Science/Python)

Esta estrutura ajuda a separar dados brutos, código, notebooks e o modelo treinado, seguindo as melhores práticas do mercado:

```
movie_suggester/
|__ docs/
│   └── 01_guidelines
|   │   └── GUIDELINES_MOVIE_SUGGESTER.md
|   |   |__ MODEL_STANDARDS.md
|   |   |__ ENVIROMENT_SETUP.md
|   |
├── data/
│   ├── raw/
│   │   └── movies.csv         # Dados brutos do MovieLens (não alterados)
│   └── processed/
│       └── movie_metadata.csv # Dados limpos e pré-processados
├── notebooks/
│   ├── 1.0-EDA_Data_Cleaning.ipynb # Análise Exploratória e limpeza inicial.
│   └── 2.0-Model_Training_Validation.ipynb # Desenvolvimento e testes do modelo.
├── src/
│   ├── __init__.py            # Torna o diretório 'src' um pacote Python
|   |
|   |__ settings.py            # Configurações do projeto
|   | 
│   ├── data/
│   │   └── data_loader.py     # Funções para carregar e limpar dados (Etapa 1)
│   ├── features/
│   │   └── feature_processor.py # Funções de vetorização (TfIdf) (Etapa 2)
│   └── models/
│       └── recommender.py     # Classe principal do modelo e cálculo de similaridade (Etapa 3 & 4)
├── main.py                    # Script principal para rodar o sistema/API de demonstração
├── requirements.txt           # Lista de dependências (pandas, scikit-learn, numpy, flask/fastapi)
├── README.md                  # Documentação do projeto no GitHub
└── .gitignore                 # Arquivos a serem ignorados (modelos treinados, virtual env, etc.)
```

## III. Melhores Práticas de Programação (Clean Code)

Aplicações de Machine Learning frequentemente pecam na Engenharia de Software. Seguir estas regras demonstra profissionalismo:

### 1. Nomenclatura (PEP 8)

- **Variáveis e Funções:** Utilize `snake_case` (ex: `calcula_similaridade`, `df_filmes_limpo`).
- **Classes:** Utilize `CamelCase` (ex: `RecommenderModel`, `DataLoader`).
- **Clareza é Prioridade:** Prefira nomes longos e descritivos a abreviações ambíguas (ex: use `indice_filme_referencia` em vez de `i` ou `idx`).

### 2. Modularização e Responsabilidade Única (SRP)

- **Separe as Etapas:** Cada arquivo em `src/` deve ter uma única responsabilidade.
    - `data_loader.py` deve apenas carregar e limpar dados.
    - `feature_processor.py` deve apenas vetorizar os dados e gerar a matriz de features.
    - `recommender.py` deve apenas calcular a similaridade e gerar as sugestões.
- **Funções Curtas:** Cada função deve fazer uma única coisa e fazê-la bem. Se uma função precisar de comentários para explicar o que faz, ela provavelmente está fazendo mais de uma coisa e precisa ser dividida.

### 3. Tipagem e Documentação

- **Type Hinting:** Use Type Hinting no Python para especificar os tipos de entrada e saída das funções. Isso torna o código mais seguro e legível.

  ```python
  # Exemplo de Type Hinting
  def carregar_dados(caminho_arquivo: str) -> pd.DataFrame:
      """Carrega e retorna o DataFrame de filmes."""
      # ... lógica de carregamento
      return df
  ```

- **Docstrings:** Use docstrings (preferencialmente no formato Google ou reStructuredText) para descrever o que cada função, classe e método faz, incluindo parâmetros e o que é retornado.

### 4. Gestão de Dependências e Ambiente

- **Ambiente Virtual:** Sempre use um ambiente virtual (como `venv` ou `conda`) para isolar as dependências do projeto.
- **requirements.txt:** Mantenha este arquivo atualizado para garantir que qualquer pessoa possa replicar o seu ambiente de forma idêntica (`pip freeze > requirements.txt`).
- **settings.py:** Utilize este arquivo para constantes de configurações caso necessário e mantenha atualizado.