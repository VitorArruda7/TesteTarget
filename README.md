# 🚀 Desafio Lógico e Análise de Dados

Este repositório contém soluções para problemas de lógica de programação e análise de dados, organizados em arquivos individuais para facilitar a execução e manutenção.

## 📂 Estrutura do Projeto

```
/Teste
│── main.py                # Arquivo principal que executa todos os problemas
│── problema_1.py           # Cálculo da variável SOMA
│── problema_2.py           # Verifica se um número pertence à sequência de Fibonacci
│── problema_3.py           # Análise de faturamento diário a partir de JSON e XML
│── problema_4.py           # Cálculo do percentual de faturamento por estado
│── problema_5.py           # Inversão de string sem métodos prontos
│── dados.json              # Arquivo JSON com os dados de faturamento
│── dados.xml               # Arquivo XML com os dados de faturamento
```

## 🛠️ Como Rodar o Projeto

### 1️⃣ Pré-requisitos

- Ter o Python 3.11 ou superior instalado
- Ter os arquivos `dados.json` e `dados.xml` na mesma pasta que os scripts

### 2️⃣ Executando os Problemas Individualmente

Se deseja executar um problema específico, utilize o seguinte comando no terminal:
```bash
python problema_1.py
```
Substitua `problema_1.py` pelo nome do arquivo do problema que deseja rodar.

### 3️⃣ Executando Todos os Problemas de Uma Vez

Para rodar todas as soluções de uma vez, basta executar o `main.py`:
```bash
python main.py
```

Isso chamará automaticamente cada problema e exibirá os resultados no terminal.

## 📋 Descrição dos Problemas

### 🔹 Problema 1: Cálculo da variável SOMA
Executa uma soma incremental de 1 até 13 e exibe o resultado.

### 🔹 Problema 2: Sequência de Fibonacci
Verifica se um número informado pelo usuário pertence à sequência de Fibonacci.

### 🔹 Problema 3: Análise de Faturamento Diário
Lê dados de faturamento diário a partir dos arquivos `dados.json` e `dados.xml`, exibindo:
- O menor valor de faturamento
- O maior valor de faturamento
- O número de dias com faturamento acima da média mensal

### 🔹 Problema 4: Percentual de Faturamento por Estado
Calcula e exibe o percentual de representação de faturamento por estado.

### 🔹 Problema 5: Inversão de String
Inverte uma string fornecida pelo usuário sem usar funções prontas.

## 📝 Notas
- Certifique-se de que os arquivos de dados (`dados.json` e `dados.xml`) estejam corretamente formatados.
- O script `problema_3.py` contém um ajuste para ler corretamente o XML, caso ele tenha múltiplas linhas sem uma tag raiz.
