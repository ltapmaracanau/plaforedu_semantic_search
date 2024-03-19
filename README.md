# Busca Semântica PlaforEDU

Este projeto implementa uma API de busca semântica utilizando Python, PyTorch, Sentence Transformers e FAISS para o processamento de linguagem natural e a busca de semelhança de sentenças.

## Estrutura do Projeto

O projeto é composto por três arquivos principais:

- `search.py`: Contém a implementação do motor de busca semântica, utilizando embeddings de sentenças para realizar buscas por semelhança.
- `api.py`: Define uma API REST usando Flask que permite interagir com o motor de busca semântica.
- `Makefile`: Facilita a construção, execução e gestão do projeto Docker associado.

## Como Utilizar

### Pré-requisitos

Antes de começar, você precisará ter o seguinte instalado em sua máquina:
- Docker
- Python 3.6 ou superior

### Instalação e Execução

Para rodar o projeto, siga os passos abaixo:

1. Clone o repositório para sua máquina local.
2. Construa a imagem Docker utilizando o comando:
   ```
   make build
   ```
3. Inicie o serviço usando:
   ```
   make run
   ```
   Isso iniciará a API em um container Docker.

### Uso da API

Após iniciar o serviço, a API estará disponível no endereço `http://localhost:5000`. Você pode realizar buscas semânticas enviando requisições GET para o endpoint `/search` com os parâmetros:

- `query_text`: O texto que você deseja buscar.
- `top_k`: O número de resultados mais relevantes que você deseja obter (padrão é 5).

Exemplo de requisição:
```
GET http://localhost:5000/search?query_text=sua_consulta_aqui&top_k=3
```

### Comandos Adicionais

O `Makefile` inclui comandos adicionais para gestão do container Docker:

- `make stop`: Para interromper o container Docker em execução.
- `make clean`: Para remover o container Docker.
- `make logs`: Para visualizar os logs do container Docker.
