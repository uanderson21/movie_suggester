# 📜 Padrões para Modelos de Machine Learning

## I. Introdução

Este documento estabelece os padrões para o desenvolvimento, avaliação, versionamento e documentação dos modelos de Machine Learning no projeto **Movie Suggester**. O objetivo é garantir que os modelos sejam robustos, reprodutíveis, transparentes e fáceis de manter.

---

## II. Versionamento de Modelos

Manter um histórico claro das versões dos modelos é crucial para a reprodutibilidade e para gerenciar o ciclo de vida em produção.

- **Nomenclatura:** Os artefatos de modelo (arquivos serializados como `.pkl`, `.joblib` ou `.h5`) devem seguir o padrão `[nome_do_modelo]_v[MAJOR].[MINOR].[PATCH].ext`.
  - **Exemplo:** `content_recommender_v1.0.0.pkl`
- **Armazenamento:** Modelos são arquivos binários e não devem ser commitados diretamente no Git. Utilize o **Git LFS (Large File Storage)** para rastrear os arquivos de modelo.
- **Associação com Código:** Cada versão do modelo deve estar associada a um commit específico do código-fonte que o gerou. Use tags do Git para marcar a versão do código que treinou um modelo específico.
  - **Exemplo de Tag:** `git tag -a v1.0.0-model -m "Modelo inicial de recomendação com TF-IDF e similaridade de cosseno"`

---

## III. Avaliação e Métricas

A avaliação de um modelo de recomendação vai além da simples acurácia. Devemos medir a qualidade e a relevância das sugestões.

### Métricas Offline Principais

Para um sistema de recomendação "Top-N" como o nosso, as seguintes métricas são essenciais:

1.  **Precision@k:** Das `k` recomendações feitas, quantas são relevantes?
    - **Foco:** Acurácia das `k` primeiras sugestões.
2.  **Recall@k:** Dos itens relevantes que o usuário gostaria, quantos nós conseguimos recomendar entre os `k` primeiros?
    - **Foco:** Cobertura de itens relevantes.
3.  **Mean Average Precision (MAP):** Uma média da precisão para cada recomendação relevante, considerando a ordem das sugestões. Penaliza modelos que colocam itens relevantes no final da lista.
4.  **Normalized Discounted Cumulative Gain (NDCG@k):** A métrica mais completa, que valoriza a posição dos itens relevantes. Recomendações corretas no topo da lista valem mais do que as que aparecem no final.

### Avaliação Qualitativa

- **Análise de Casos de Uso:** Teste o modelo com filmes conhecidos e analise a coerência das recomendações.
  - *Exemplo:* Para o filme "The Matrix", o modelo sugere outros filmes de ficção científica com temas semelhantes, como "Blade Runner" ou "Ghost in the Shell"?
- **Diversidade e Serendipidade:** Avalie se o modelo não está apenas recomendando filmes óbvios ou populares (diversidade) e se ele é capaz de fazer sugestões surpreendentes, mas relevantes (serendipidade).

---

## IV. Documentação (Model Card)

Todo modelo treinado e candidato a produção deve ser acompanhado por um "Model Card". Este é um documento curto que fornece informações essenciais sobre o modelo. Crie um arquivo `MODEL_CARD_recommender_v1.md` para cada versão principal.

### Template do Model Card

```markdown
### Model Card: Content Recommender v1.0

**1. Detalhes do Modelo**
- **Versão:** 1.0.0
- **Tipo:** Recomendação baseada em conteúdo (Content-Based Filtering).
- **Algoritmo:** TF-IDF para vetorização de metadados + Similaridade de Cosseno.
- **Data de Treinamento:** YYYY-MM-DD

**2. Uso Pretendido**
- **Cenário:** Sugerir 10 filmes similares a um filme de referência fornecido pelo usuário.
- **Usuário-alvo:** Usuários da plataforma de streaming buscando novas descobertas de filmes.

**3. Fora do Escopo de Uso**
- O modelo não faz recomendações personalizadas para um *usuário* (não é Collaborative Filtering).
- Não deve ser usado para descobrir tendências de popularidade.

**4. Dados de Treinamento**
- **Fonte:** MovieLens Dataset (movies.csv).
- **Features Utilizadas:** `genres`, `director`, `actors`, `keywords`.
- **Pré-processamento:** Limpeza de texto, combinação de metadados em um único "caldo de cultura" por filme.

**5. Dados de Avaliação**
- **Estratégia:** Hold-out de 20% dos dados para teste.
- **Métricas:**
  - **NDCG@10:** [Valor]
  - **Precision@10:** [Valor]

**6. Considerações Éticas e vieses (Bias)**
- **Viés de Popularidade:** O modelo pode tender a favorecer filmes de gêneros mais representados no dataset.
- **Viés de Seleção:** Os dados do MovieLens não representam a totalidade dos filmes existentes, podendo haver sub-representação de certas cinematografias.
- **Mitigação:** N/A para esta versão. Futuras versões podem explorar técnicas de re-ranking para aumentar a diversidade.
```

---

## V. Testes do Modelo

O código do modelo deve ser testável para garantir sua robustez.

- **Testes Unitários:** Funções de pré-processamento e auxiliares devem ter testes unitários para validar sua lógica.
- **Testes de Integração:** Crie um teste que valide o pipeline completo: `dado de entrada -> pré-processamento -> predição -> formato de saída`.
- **Teste de Regressão (Golden Test):** Tenha um pequeno conjunto de dados de entrada e suas saídas esperadas (golden dataset). Rode o modelo contra esses dados e compare o resultado. Qualquer alteração no código que mude essa saída deve ser intencional.
