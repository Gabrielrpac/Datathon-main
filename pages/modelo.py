import streamlit as st
import pandas as pd
from PIL import Image
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
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
        Este projeto tem como objetivo prever o :green[Índicador do Ponto de Virada (IPV)] dos alunos para o :green[ano de 2023], utilizando técnicas de machine learning com a biblioteca :green[Scikit-learn (SKlearn)]. O modelo de previsão foi desenvolvido com a técnica de Random Forest, um método robusto e amplamente utilizado para análise preditiva, capaz de lidar bem com pequenas variações nos dados.

Além da previsão do IPV, o projeto também calcula a :green[nota de corte para o ano de 2023] e se o aluno em questão :green[atingiria o resultado ou não]. A nota de corte é determinada :green[somando] a :green[média do IPV do ano analisado ao desvio padrão], estabelecendo um parâmetro para avaliar quais alunos superam ou atingem o desempenho esperado.

Embora a base de dados seja limitada, contendo informações de apenas três anos (2020, 2021 e 2022), a técnica de Random Forest foi escolhida por sua capacidade de explorar relações complexas entre variáveis e gerar previsões confiáveis, mesmo com um conjunto de dados reduzido. Através desse modelo, esperamos capturar padrões históricos no IPV e prever os resultados futuros com a maior precisão possível.
    """
    )

tab0, tab1 = st.tabs(
    tabs=[
        "Modelo de previsão SKlearn",
        "Validando o modelo",
    ]
)

with tab0:

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

    # Exibir notas de corte
    st.subheader("Notas de Corte")
    st.markdown("Vamos iniciar realizando uma :green[previsão da nota de corte] utilizando os dados dos anos anteriores para cálcular a nota para o :green[ano de 2023]. A combinação dessas informações enriquece a análise do Ponto de Virada, permitindo avaliar a relação entre os resultados obtidos no desenvolvimento escolar dos alunos da associação e a avaliação específica do IPV. A junção desses dois conjuntos de dados pode servir como :green[ferramentas valiosas] para a Associação Passos Mágicos na avaliação dos alunos em relação aos programas de bolsas de estudo, cursos e treinamentos, e intercâmbios.")
    st.write(f"Nota de corte para 2020: {nota_corte_2020:.2f}")
    st.write(f"Nota de corte para 2021: {nota_corte_2021:.2f}")
    st.write(f"Nota de corte para 2022: {nota_corte_2022:.2f}")
    st.write(f"Nota de corte para 2023: {nota_corte_2023:.2f}")
    st.markdown("</div>", unsafe_allow_html=True)

    # Exibir os resultados
    st.subheader("Resultados dos Alunos")
    st.markdown("Agora com base no Ponto de virada calculado para o ano de 2023 realizamos a :green[predição da nota IPV] alcançada pelos alunos com base no valor dos anos anteriores e validamos se a métrica seria atingida ou não.")
    st.write(resultado_df)
    
with tab1:
    st.subheader("Distribuição dos alunos por fase")
    st.markdown("A Instituição Passos Mágicos organiza seus alunos em fases que correspondem aos níveis do sistema de ensino brasileiro. Essa estrutura não apenas facilita o acompanhamento do progresso educacional, mas também permite à instituição desenvolver atividades e intervenções específicas para cada grupo etário e nível de aprendizado. A fase 1, que abrange os alunos do 3º e 4º ano do ensino fundamental, apresenta o maior número de alunos, totalizando 172. Isso sugere que a instituição possui uma forte capacidade de atrair e manter alunos nessa faixa inicial do ensino fundamental, possivelmente refletindo um maior número de crianças nessa idade em situação de vulnerabilidade. Em contrapartida, as fases mais avançadas, especialmente as do ensino médio e da universidade, apresentam um número significativamente menor de alunos. Isso pode indicar desafios na retenção de jovens conforme avançam na educação, seja devido a fatores sociais, econômicos ou à falta de apoio contínuo. A fase 4, com apenas 55 alunos, e a fase 8, com 24, ressaltam a necessidade de estratégias específicas para apoiar a transição dos alunos para os anos finais do ensino fundamental e a continuidade no ensino superior. Em resumo, a análise da distribuição de alunos por fases do programa da Instituição Passos Mágicos revela um padrão que pode orientar ações futuras. Ao entender onde estão concentrados os alunos e quais fases apresentam maiores desafios, a instituição pode desenvolver programas mais eficazes e direcionados, garantindo que cada aluno receba o suporte necessário para alcançar seu pleno potencial educacional. Essa abordagem não só melhora a experiência dos alunos, mas também fortalece o impacto positivo da instituição em suas vidas.")
    image_path = 'assets/imgs/quantidade_de_alunos_por_fase.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos por fase', use_column_width=False, width=600)
    st.markdown("</div>", unsafe_allow_html=True)