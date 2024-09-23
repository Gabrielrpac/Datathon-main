import streamlit as st
from utilidades.const import TITULO_MODELO, TITULO_PRINCIPAL
from utilidades.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_MODELO} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f":green[{TITULO_MODELO}]")

    st.markdown(
        """
        Prever o preço do barril de petróleo Brent é um desafio crucial devido à sua importância na economia global. O petróleo Brent é usado como referência internacional para determinar os preços de compra e venda em todo o mundo. A ferramenta Prophet é valiosa porque simplifica o processo de previsão de preços, ajudando a entender tendências passadas e sazonalidades que influenciam os preços do petróleo. Isso é vital para empresas, governos e investidores que dependem de previsões precisas para tomar decisões estratégicas, como planejar investimentos, gerenciar riscos financeiros e ajustar políticas econômicas.
    """
    )

    tab0 = st.tabs(tabs=["Modelo de previsão SKlearn"])


import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

st.title("Previsão de Alunos para Atingir o Ponto de Virada em 2023")

df = pd.read_csv('assets/csv/PEDE_PASSOS_DATASET_FIAP.csv', sep = ';')

df.dropna(subset=['IPV_2020', 'IPV_2021', 'IPV_2022'], inplace=True)

df['IPV_2020'] = pd.to_numeric(df['IPV_2020'], errors='coerce')
df['IPV_2021'] = pd.to_numeric(df['IPV_2021'], errors='coerce')
df['IPV_2022'] = pd.to_numeric(df['IPV_2022'], errors='coerce')

# 1. Preparar os dados
features = df[['IPV_2020', 'IPV_2021', 'IPV_2022']]
target = df['IPV_2022']  # Usando IPV_2022 como alvo

# Dividir os dados em conjunto de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# 2. Treinamento do modelo
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 3. Prever o IPV para 2023
ipvs_previstos_2023 = model.predict(features)  # Prever baseado nas mesmas features

# 4. Calcular as notas de corte
media_2020 = df['IPV_2020'].mean()
media_2021 = df['IPV_2021'].mean()
media_2022 = df['IPV_2022'].mean()
media_2023 = ipvs_previstos_2023.mean()

desvio_2020 = df['IPV_2020'].std()
desvio_2021 = df['IPV_2021'].std()
desvio_2022 = df['IPV_2022'].std()
desvio_2023 = ipvs_previstos_2023.std()

nota_corte_2020 = media_2020 + desvio_2020
nota_corte_2021 = media_2021 + desvio_2021
nota_corte_2022 = media_2022 + desvio_2022
nota_corte_2023 = media_2023 + desvio_2023

# 5. Determinar se os alunos atingirão o ponto de virada
resultados = ["Sim" if ipv > nota_corte_2023 else "Não" for ipv in ipvs_previstos_2023]

# Criar um DataFrame com os resultados
resultado_df = pd.DataFrame({
    'Aluno': [f'Aluno {i + 1}' for i in range(len(resultados))],
    'IPV Previsto': ipvs_previstos_2023,
    'Atingirá o ponto de virada': resultados
})

# Exibir os resultados
st.subheader("Resultados dos Alunos")
st.write(resultado_df)

# Exibir notas de corte
st.subheader("Notas de Corte")
st.write(f"Nota de corte para 2020: {nota_corte_2020:.2f}")
st.write(f"Nota de corte para 2021: {nota_corte_2021:.2f}")
st.write(f"Nota de corte para 2022: {nota_corte_2022:.2f}")
st.write(f"Nota de corte para 2023: {nota_corte_2023:.2f}")
