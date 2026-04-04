# 📊 Dashboard Comparativo de Consumo de Medicamentos

Dashboard interativo em **Streamlit** para análise e comparação do consumo de medicamentos entre múltiplas unidades de saúde, com suporte a múltiplos meses via abas de planilha Excel.

---

## 🗂️ Estrutura do Projeto

```
.
├── app.py          # Versão básica: múltiplas unidades, um mês por arquivo
├── teste.py        # Versão avançada: múltiplas unidades e meses (abas Excel)
├── Unidade_1.xlsx  # Exemplo de planilha — Unidade 1 (aba: Novembro)
├── Unidade_2.xlsx  # Exemplo de planilha — Unidade 2 (abas: Novembro, Dezembro)
├── Unidade_3.xlsx  # Exemplo de planilha — Unidade 3 (aba: Novembro)
└── README.md
```

---

## ✨ Funcionalidades

- Upload de múltiplas planilhas `.xlsx` simultaneamente
- Leitura automática de **todas as abas** (cada aba representa um mês)
- Filtros interativos por **Unidade**, **Mês** e **Medicamento**
- **Tabela comparativa** com totais por unidade e destaque no maior consumidor
- **Gráfico de barras** — volume total por medicamento/unidade
- **Gráfico de linha** — evolução do consumo ao longo dos dias do mês
- Modo de demonstração com dados gerados automaticamente (sem necessidade de upload)

---

## 📋 Formato Esperado das Planilhas

Cada arquivo `.xlsx` representa **uma unidade**. O nome do arquivo (sem extensão) é usado como nome da unidade.

Cada **aba** da planilha representa **um mês**.

| ITEM | 1 | 2 | 3 | ... | 31 |
|------|---|---|---|-----|----|
| Dipirona 500mg comp. | 0 | 12 | 5 | ... | 8 |
| Paracetamol 750mg comp. | 3 | 0 | 0 | ... | 2 |

- **Coluna 1**: Nome do medicamento
- **Demais colunas**: Dias do mês (1 a 31) com a quantidade dispensada

---

## 🚀 Como Executar

### 1. Instale as dependências

```bash
pip install streamlit pandas numpy openpyxl
```

### 2. Execute o app desejado

**Versão básica** (um mês por arquivo):
```bash
streamlit run app.py
```

**Versão avançada** (múltiplos meses por abas):
```bash
streamlit run teste.py
```

### 3. Acesse no navegador

O Streamlit abrirá automaticamente em `http://localhost:8501`

---

## 🔀 Diferença entre `app.py` e `teste.py`

| Característica | `app.py` | `teste.py` |
|---|---|---|
| Formatos aceitos | `.xlsx` e `.csv` | Somente `.xlsx` |
| Suporte a múltiplos meses | ❌ | ✅ (via abas) |
| Filtro por mês | ❌ | ✅ |
| Complexidade | Simples | Completa |

> **Recomendação**: Use `teste.py` para análises com histórico mensal. Use `app.py` para relatórios pontuais ou arquivos CSV.

---

## 🛠️ Tecnologias

- [Python 3.8+](https://www.python.org/)
- [Streamlit](https://streamlit.io/) — interface web interativa
- [Pandas](https://pandas.pydata.org/) — manipulação de dados
- [NumPy](https://numpy.org/) — geração de dados de demonstração
- [OpenPyXL](https://openpyxl.readthedocs.io/) — leitura de arquivos `.xlsx`
