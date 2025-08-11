# Projeto - Airline Passengers ETL & EDA

![Python](https://img.shields.io/badge/python-3.8+-blue) ![Pandas](https://img.shields.io/badge/pandas-1.3+-brightgreen) ![Matplotlib](https://img.shields.io/badge/matplotlib-3.3+-orange) ![SQLite](https://img.shields.io/badge/SQLite-lightgrey)

---

## Descrição do Projeto

Este projeto implementa um pipeline simples de Engenharia de Dados que realiza:

- Download automático de um dataset público sobre passageiros de voos mensais (1949-1960).
- Análise exploratória dos dados (visualização do conteúdo e estatísticas básicas).
- Visualização gráfica da evolução mensal do número de passageiros.
- Armazenamento dos dados processados em um banco de dados SQLite local.

Este projeto é ideal para quem está começando a aprender Engenharia de Dados e quer praticar um fluxo ETL (Extract, Transform, Load) completo usando Python.

---

## Dataset

O dataset utilizado é público e disponível no seguinte link:  
[Airline Passengers Dataset](https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv)  

O arquivo contém duas colunas:
- **Month**: data no formato AAAA-MM
- **Passengers**: número total de passageiros naquele mês

---

## Tecnologias Utilizadas

- Python 3.8 ou superior
- Pandas (manipulação de dados)
- Matplotlib (visualização)
- SQLite (banco de dados leve, local)

---

## Como Rodar o Projeto

### Pré-requisitos

- Python instalado na sua máquina (versão 3.8+)
- Git (opcional, para clonar o repositório)

### Passos

1. Clone o repositório:
   ```bash
   git clone https://github.com/lucasabreuzip/airline-passengers-etl.git
   cd airline-passengers-etl
