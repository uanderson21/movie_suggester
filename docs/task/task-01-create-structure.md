# 📜 Tarefa 01: Criar Estrutura do Projeto

**Objetivo:** Criar a estrutura inicial de pastas e arquivos para o projeto `movie_suggester`.

Esta tarefa envolve a configuração do esqueleto fundamental da aplicação, garantindo que todos os diretórios e arquivos necessários estejam no lugar antes do início do desenvolvimento. Nenhuma lógica de programação é necessária para esta tarefa.

A estrutura deve ser criada de acordo com as especificações descritas no documento de diretrizes oficial do projeto: `docs/01_guidelines/GUIDELINES_MOVIE_SUGGESTER.md`.

**Estrutura Esperada:**

```
movie_suggester/
|__ data/
│   ├── raw/
│   │   └── movies.csv
│   └── processed/
│       └── movie_metadata.csv
|__ docs/
│   └── 01_guidelines/
|       ├── ENVIROMENT_SETUP.md
|       ├── GUIDELINES_MOVIE_SUGGESTER.md
|       └── MODEL_STANDARDS.md
├── notebooks/
│   ├── 1.0-EDA_Data_Cleaning.ipynb
│   └── 2.0-Model_Training_Validation.ipynb
├── src/
│   ├── __init__.py
│   ├── settings.py
│   ├── data/
│   │   └── data_loader.py
│   ├── features/
│   │   └── feature_processor.py
│   └── models/
│       └── recommender.py
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

**Critérios de Aceitação:**
- Todos os diretórios e arquivos especificados são criados.
- Os nomes dos arquivos e pastas correspondem exatamente à estrutura definida acima.
- A raiz do projeto contém todos os arquivos e diretórios de nível superior.