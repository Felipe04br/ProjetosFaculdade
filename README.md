# 🎓 Projetos — Faculdade

Repositório com os projetos práticos desenvolvidos durante o curso, combinando lógica de programação, análise de dados e desenvolvimento de aplicações.

---

## 🗂️ Projetos

### 📊 Dashboard Comparativo de Medicamentos
> `Python` · `Streamlit` · `Pandas`

Aplicação web interativa para análise e comparação do consumo de medicamentos entre múltiplas unidades de saúde. Suporta upload de planilhas `.xlsx` com abas separadas por mês e gera visualizações automáticas.

| Arquivo | Descrição |
|---|---|
| `app.py` | Versão básica — múltiplas unidades, um mês por arquivo |
| `teste.py` | Versão completa — múltiplas unidades e meses via abas Excel |
| `Unidade_1.xlsx` | Planilha de exemplo — Unidade 1 (aba: Novembro) |
| `Unidade_2.xlsx` | Planilha de exemplo — Unidade 2 (abas: Novembro, Dezembro) |
| `Unidade_3.xlsx` | Planilha de exemplo — Unidade 3 (aba: Novembro) |

```bash
pip install streamlit pandas openpyxl
streamlit run app.py       # versão básica
streamlit run teste.py     # versão completa
```

---

### 🖩 Calculadora de Terminal
> `Python`

Calculadora interativa que roda no terminal com interface visual em ASCII. Suporta as operações básicas, módulo e raiz quadrada, além de um sistema de memória que permite encadear cálculos sequenciais.

**Operações suportadas:** `+` `-` `*` `/` `%` `√`

```bash
python Calculadora.py
```

---

### 📥 Extrator e Analisador de Microdados PNAD Contínua
> `Python` · `Pandas`

Pipeline para download automático via FTP do IBGE, extração e análise estatística dos microdados da PNAD Contínua, com filtragem por UF e geração de relatório Excel segmentado. O banco de dados atual cobre a Bahia (UF 29) de 2023 a 2025 — 274.541 registros e 77 variáveis.

| Arquivo | Descrição |
|---|---|
| `App.py` | Download, extração e filtragem dos microdados via FTP |
| `Media_Moda_Mediana.py` | Média, moda e mediana segmentadas por trimestre, ano e total |
| `Banco_de_dados.csv` | Base gerada — 274.541 registros (Bahia, 2023–2025) |

```bash
pip install pandas openpyxl
python App.py                  # gera o Banco_de_dados.csv
python Media_Moda_Mediana.py   # gera o Relatorio_PNAD_Segmentado.xlsx
```

---

### 🏗️ Sistema de Gestão de Construtora (POO)
> `Java`

Sistema de gestão desenvolvido em Java com foco em **Programação Orientada a Objetos**. Organizado em módulos com menus interativos, repositories e herança de classes.

**Módulos:**

| Módulo | Classes principais |
|---|---|
| `Cliente` | `Cliente`, `RepositoryCliente`, `MenuCliente` |
| `Funcionario` | `Funcionario`, `Gestao`, `Operacional`, `FuncionarioRepository`, `MenuFuncionario` |
| `Projeto` | `Projeto`, `ProjetoResidencial`, `ProjetoPredio`, `ProjetoReforma`, `Planta`, `TipoProjeto`, `StatusProjeto`, `MenuProjeto` |
| `Construtora` | `Construtora`, `RepositoryConstrutora`, `MenuConstrutora` |

**Conceitos aplicados:** herança, encapsulamento, polimorfismo, enums (`TipoProjeto`, `StatusProjeto`) e padrão Repository.

```bash
java -jar POO.jar
```

> Requer [Java](https://www.java.com/) instalado.

---

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Java](https://img.shields.io/badge/Java-E34A34?style=for-the-badge&logo=openjdk&logoColor=white)

---

## 📈 Em andamento

Novos projetos serão adicionados conforme o avanço no curso.