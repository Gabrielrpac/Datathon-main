import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

csv_file_path =("assets\csv\PEDE_PASSOS_DATASET_FIAP.csv")
df = pd.read_csv(csv_file_path)

df_idade = df.copy()
df_idade['IDADE_ALUNO_2020'] = pd.to_numeric(df_idade['IDADE_ALUNO_2020'], errors='coerce')
df_idade['IDADE_ALUNO_2020'] = df_idade['IDADE_ALUNO_2020'].fillna(0).astype(int)
df_idade = df_idade.dropna(subset=['IDADE_ALUNO_2020'])
df_idade = df_idade[df_idade['IDADE_ALUNO_2020'] > 0]

# Supondo que df_idade já esteja carregado no script
idade_counts = df_idade['IDADE_ALUNO_2020'].value_counts().sort_index()

# Título da página no Streamlit
st.title('Distribuição de Idade dos Alunos (2020)')

# Configuração do gráfico com Matplotlib
fig, ax = plt.subplots(figsize=(12, 6))
idade_counts.plot(kind='bar', color='skyblue', edgecolor='black', ax=ax)
ax.set_xlabel('Idade do Aluno')
ax.set_ylabel('Quantidade de Alunos')
ax.set_title('Quantidade de Alunos por Idade (2020)')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Exibir o gráfico no Streamlit
st.pyplot(fig)