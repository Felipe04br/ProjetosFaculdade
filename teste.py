import streamlit as st
import pandas as pd
import numpy as np
# Configuração da Página
st.set_page_config(page_title="Comparativo Multi-Unidades", layout="wide")
st.title("Comparativo de Rede: Múltiplas Unidades e Meses")
st.markdown("Visão consolidada de consumo entre diferentes unidades de saúde e meses (Abas).")
# Função para criar dados aleatórios de demonstração (Com Abas/Meses)
def gerar_dados_demo():
    unidades = ['Unidade Centro', 'Unidade Norte']
    meses = ['Janeiro', 'Fevereiro', 'Março']
    medicamentos = ['Dipirona', 'Paracetamol', 'Amoxicilina', 'Ibuprofeno', 'Losartana']
    dias = [str(i) for i in range(1, 32)] # Dias como strings para colunas
    lista_dfs = []
    for uni in unidades:
        for mes in meses:
            # Gera matriz aleatória
            dados = np.random.randint(0, 25, size=(len(medicamentos), len(dias)))
            df = pd.DataFrame(dados, columns=dias)
            df.insert(0, "Medicamento", medicamentos)
            # Transforma de Matriz para Lista (Melt)
            df_long = df.melt(id_vars=['Medicamento'], var_name='Dia', value_name='Quantidade')
            df_long['Unidade'] = uni
            df_long['Mes'] = mes # Adiciona o mês (simulando a aba)
            lista_dfs.append(df_long)
    return pd.concat(lista_dfs, ignore_index=True)
# Upload de Arquivos (Múltiplos na barra lateral)
with st.sidebar:
    st.header("Carregar Planilhas")
    st.markdown("Selecione arquivos Excel com **Abas separadas por Mês**.")
    arquivos = st.file_uploader(
        "Upload Excel (Abas = Meses)", 
        type=['xlsx'], # CSV não suporta abas, foco em XLSX
        accept_multiple_files=True
    )
    df_master = pd.DataFrame()
    if arquivos:
        lista_temp = []
        for arquivo in arquivos:
            try:
                # Nome da unidade = Nome do arquivo sem extensão
                nome_unidade = arquivo.name.rsplit('.', 1)[0]
                # Ler TODAS as abas (sheet_name=None retorna um dicionário de abas)
                dicionario_abas = pd.read_excel(arquivo, sheet_name=None)
                for nome_aba, df_aba in dicionario_abas.items():
                    if df_aba.empty: continue
                    # Transformação (Melt) - De Colunas de Dias para Linhas, transforma os dias em uma coluna com dados e salva e um df
                    col_med = df_aba.columns[0] # Assume 1ª coluna como nome do medicamento
                    cols_dias = df_aba.columns[1:] # Restante são dias
                    df_melted = df_aba.melt(
                        id_vars=[col_med], 
                        value_vars=cols_dias, 
                        var_name='Dia', 
                        value_name='Quantidade'
                    )
                    df_melted.columns = ['Medicamento', 'Dia', 'Quantidade']
                    df_melted['Unidade'] = nome_unidade
                    df_melted['Mes'] = nome_aba # Nome da aba vira o Mês
                    lista_temp.append(df_melted)
            except Exception as e:
                st.error(f"Erro ao processar {arquivo.name}: {e}")
        if lista_temp:
            df_master = pd.concat(lista_temp, ignore_index=True)
    else:
        st.info("Usando dados de demonstração.")
        df_master = gerar_dados_demo()
if df_master.empty: # Verifica se há dados no df
    st.info("Aguardando...")
    st.stop()
# Corrreção para numéricos
df_master["Quantidade"] = pd.to_numeric(df_master["Quantidade"], errors='coerce').fillna(0)
df_master["Dia_Num"] = pd.to_numeric(df_master["Dia"], errors='coerce')
df_master = df_master.dropna(subset=['Dia_Num'])
df_master["Dia_Num"] = df_master["Dia_Num"].astype(int)
# Filtros, dar opções e deixar pre-selecionad
st.markdown("---")
col_f1, col_f2, col_f3 = st.columns(3)
with col_f1:
    lista_unidades = df_master['Unidade'].unique()
    sel_unidades = st.multiselect("Filtrar Unidades:", lista_unidades, default=lista_unidades)
with col_f2:
    lista_meses = df_master['Mes'].unique()
    sel_meses = st.multiselect("Filtrar Meses:", lista_meses, default=lista_meses)
with col_f3:
    lista_meds = df_master['Medicamento'].unique()
    sel_meds = st.multiselect("Filtrar Medicamentos:", lista_meds, default=lista_meds[:5])
# Aplicar Filtros, criar df com a interceção selecionada pelo úsuario
df_final = df_master[
    (df_master['Unidade'].isin(sel_unidades)) & 
    (df_master['Mes'].isin(sel_meses)) &
    (df_master['Medicamento'].isin(sel_meds))
]
if df_final.empty: #se não houver seleção
    st.warning("Nenhum dado para exibir com os filtros atuais.")
    st.stop()
# Tabela Comparativa (Pivot)
st.subheader("Comparativo de Totais (Unidade vs Medicamento)")
# Cria tabela: Linhas=Remédios, Colunas=Unidades, Valores=Soma
pivot_tab = pd.pivot_table(
    df_final, 
    values='Quantidade', 
    index='Medicamento', 
    columns='Unidade', 
    aggfunc='sum',
    fill_value=0
)
# Adiciona Coluna Total
pivot_tab['TOTAL GERAL'] = pivot_tab.sum(axis=1)
pivot_tab = pivot_tab.astype(int)
# Mostra tabela com destaque nos maiores valores, coorige a saida float feia e amarela
st.dataframe(
    pivot_tab.style.format("{:.0f}").highlight_max(axis=1, color="#ffffff", subset=pivot_tab.columns[:-1]), 
    use_container_width=True
)
st.markdown("---")
col_g1, col_g2 = st.columns(2)
# Gráfico de Barras (Quem consumiu mais?)
with col_g1:
    st.subheader("Volume Total por Unidade")
    # Index: Medicamento, Colunas: Unidade
    chart_bar = pd.pivot_table(
        df_final, 
        values='Quantidade', 
        index='Medicamento', 
        columns='Unidade', 
        aggfunc='sum'
    )
    st.bar_chart(chart_bar)
# Gráfico de Linha (Evolução no tempo)
with col_g2:
    st.subheader("Evolução Diária (Comparativo)")
    # Index: Dia, Colunas: Unidade
    chart_line = pd.pivot_table(
        df_final, 
        values='Quantidade', 
        index='Dia_Num', 
        columns='Unidade', 
        aggfunc='sum'
    ).sort_index()
    st.line_chart(chart_line)