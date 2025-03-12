# 📘 Detalhes Técnicos do Projeto

## 📌 Visão Geral
Este projeto foi desenvolvido para análise de dados meteorológicos, utilizando bibliotecas poderosas para manipulação, análise e visualização de dados. A estrutura modular permite escalabilidade e fácil manutenção.

---

## 🛠 Tecnologias Utilizadas

✅ **Python 3.8+** → Linguagem principal do projeto  
✅ **Pandas** → Manipulação e análise de dados  
✅ **Matplotlib** → Geração de gráficos  
✅ **Seaborn** → Estilização avançada para gráficos  
✅ **Jupyter Notebook (opcional)** → Ambiente interativo para testes  

---

## 📂 Estrutura do Projeto

```
📂 projeto-analise-meteorologica
│-- 📂 data                # Diretório de arquivos de dados
│   ├── dates.csv
│
│-- 📂 src                 # Código-fonte principal
│   ├── data_loader.py     # Carregamento e tratamento de dados
│   ├── analysis.py        # Funções de análise estatística
│   ├── visualization.py   # Geração de gráficos e visualizações
│   ├── main.py            # Script principal para execução do projeto
│
│-- 📄 requirements.txt     # Dependências do projeto
│-- 📄 .gitignore           # Arquivos a serem ignorados pelo Git
```

---

## ⚙️ Funcionalidades Principais

### 🔹 Carregamento e Tratamento de Dados (**data_loader.py**)
- Carrega os dados a partir do arquivo CSV
- Converte a coluna de datas para o formato correto
- Remove registros inválidos, como precipitações negativas
- Gera colunas auxiliares, como "ano" e "mês"

### 🔹 Análises Estatísticas (**analysis.py**)
- Identifica o dia mais chuvoso do histórico
- Calcula o mês mais chuvoso ao longo dos anos
- Analisa a média da temperatura mínima para um mês específico

### 🔹 Visualização de Dados (**visualization.py**)
- Gera gráficos para visualizar padrões climáticos
- Utiliza Seaborn e Matplotlib para personalização

### 🔹 Script Principal (**main.py**)
- Integra todas as funcionalidades
- Solicita entrada do usuário para escolha de mês
- Exibe estatísticas no terminal e gráficos interativos

---

## 🚀 Instalação e Execução

### 1️⃣ **Instalar Dependências**
```bash
pip install -r requirements.txt
```

### 2️⃣ **Executar o Script Principal**
```bash
python src/main.py
```

### 3️⃣ **Executar via Jupyter Notebook (Opcional)**
```bash
jupyter notebook
```

---

## 📈 Exemplo de Saída

```bash
Data mais chuvosa: 15-06-2012 com 120.5 mm de precipitação
Ano/Mês mais chuvoso: 2017-02 com 350.7 mm de precipitação
Digite o número do mês (1-12): 6
Gerando gráfico da temperatura mínima para junho...
```

---

## 📄 Licença e Contato

Este projeto está sob a licença **MIT**. Para dúvidas ou sugestões, entre em contato!  
