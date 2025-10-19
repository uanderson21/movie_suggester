# 🎥 Movie Suggester

Bem-vindo ao Movie Suggester! Este é um sistema de recomendação de filmes que utiliza uma abordagem de **filtragem baseada em conteúdo** (*Content-Based Filtering*). A partir de um filme que você gosta, o sistema sugere outros 10 títulos com características similares.

## 💡 Como Funciona?

A lógica por trás do projeto é encontrar a "semelhança" entre os filmes com base em seus metadados. O processo é dividido nas seguintes etapas:

1.  **Preparação dos Dados:** Os dados de cada filme (gênero, diretor, atores e palavras-chave) são limpos e combinados em um único campo de texto, chamado de "soup". Essa "sopa de metadados" representa a essência de cada filme.

2.  **Vetorização:** O texto da "soup" é transformado em vetores numéricos usando a técnica **TF-IDF** (Term Frequency-Inverse Document Frequency). Isso permite que o computador entenda e compare as características de cada filme matematicamente.

3.  **Cálculo de Similaridade:** Com os filmes representados como vetores, a **Similaridade de Cosseno** é calculada entre todos os pares de filmes. Esse cálculo nos dá uma pontuação de quão "parecido" um filme é do outro.

4.  **Geração da Recomendação:** Ao receber um título de filme como entrada, o sistema encontra os 10 filmes com a maior pontuação de similaridade e os retorna como sugestão.

## 🎯 Metodologia e Propósito do Projeto

Além de ser um sistema de recomendação funcional, este repositório serve como um caso de estudo prático sobre a aplicação de boas práticas de engenharia de software em um projeto de Machine Learning.

1.  **Desenvolvimento Guiado por Diretrizes:** O projeto segue um conjunto de [diretrizes (`guidelines`)](./docs/01_guidelines/GUIDELINES_MOVIE_SUGGESTER.md) que definem a estrutura, os padrões de código (`Clean Code`) e os critérios para versionamento e documentação de modelos (`Model Cards`). O objetivo é garantir um desenvolvimento organizado, reprodutível e de fácil manutenção.

2.  **Desenvolvimento Assistido por IA:** Este projeto foi construído em colaboração com o **Gemini Code Assist**. Ele demonstra um fluxo de trabalho moderno onde a IA atua como uma assistente de programação para gerar código, criar documentação, seguir padrões e acelerar o ciclo de desenvolvimento, permitindo que o desenvolvedor foque mais na lógica de negócio e na estratégia do modelo.

## 📂 Estrutura do Projeto

O projeto segue uma estrutura padrão para aplicações de ciência de dados, separando dados, código-fonte, notebooks de exploração e documentação.

```
movie_suggester/
|__ data/
│   ├── raw/
│   └── processed/
|__ docs/
│   └── 01_guidelines/
├── notebooks/
├── src/
│   ├── data/
│   ├── features/
│   └── models/
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## 🚀 Como Executar

Para rodar o projeto em sua máquina local, siga os passos abaixo.

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/movie_suggester.git
    cd movie_suggester
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o pipeline de processamento de dados:**
    ```bash
    python src/data/data_loader.py
    ```

5.  **Execute a aplicação principal:**
    ```bash
    python main.py
    ```

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Pandas:** Para manipulação e análise de dados.
- **Scikit-learn:** Para a implementação do TF-IDF e da Similaridade de Cosseno.
- **NumPy:** Para operações numéricas eficientes.
