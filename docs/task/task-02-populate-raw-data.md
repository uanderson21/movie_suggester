# 📜 Tarefa 02: Popular Dados Brutos Iniciais

**Objetivo:** Criar e popular o arquivo `data/raw/movies.csv` com um conjunto de dados fictícios e reais (mock data) para permitir o desenvolvimento e teste do pipeline de dados.

## Descrição

Para que as tarefas de carregamento, processamento e modelagem possam começar, o arquivo `movies.csv` deve ser populado com mais de 50 exemplos de filmes.

Este arquivo deve ser colocado no diretório `data/raw/`.

## Conteúdo do Arquivo (`data/raw/movies.csv`)

Segue exemplo de conteúdo

```csv
title,genres,director,actors,keywords,overview
A Jornada Quântica,Science Fiction|Adventure|Action,Alex Rivera,"Zoe Saldana,Idris Elba,Oscar Isaac",time travel|parallel universe|quantum physics,"Uma física descobre uma forma de viajar entre realidades, mas fica presa em um universo onde a humanidade perdeu a guerra contra as máquinas."
Sombras de Neon,Thriller|Mystery|Crime,Sofia Coppola,"Anya Taylor-Joy,Daniel Kaluuya,Willem Dafoe",neo-noir|conspiracy|detective,"Em uma cidade chuvosa e iluminada por neon, um detetive particular investiga o desaparecimento de uma cantora, descobrindo uma conspiração corporativa."
O Último Alquimista,Fantasy|Adventure|Drama,Guillermo del Toro,"Eddie Redmayne,Eva Green,Tom Hiddleston",alchemy|magic|immortality,"Um alquimista secular busca o ingrediente final para a Pedra Filosofal, uma jornada que o força a confrontar os fantasmas de seu passado imortal."
```

## Critérios de Aceitação
- O arquivo `data/raw/movies.csv` é criado.
- O arquivo contém o cabeçalho `title,genres,director,actors,keywords,overview`.
- O arquivo contém pelo menos 50 linhas de dados de exemplo seguindo o formato CSV.