import streamlit as st
import pandas as pd
import streamlit as st
from PIL import Image
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
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
    st.write(f"Nota de corte para 2020: :green[{nota_corte_2020:.2f}]")
    st.write(f"Nota de corte para 2021: :green[{nota_corte_2021:.2f}]")
    st.write(f"Nota de corte para 2022: :green[{nota_corte_2022:.2f}]")
    st.write(f"Nota de corte para 2023: :green[{nota_corte_2023:.2f}]")
    st.markdown("</div>", unsafe_allow_html=True)

    st.divider()

    # Exibir os resultados
    st.subheader("Resultados dos Alunos")
    st.markdown("Agora com base no Ponto de virada calculado para o ano de 2023 realizamos a :green[predição da nota IPV] alcançada pelos alunos com base no valor dos anos anteriores e validamos se a métrica seria atingida ou não.")
    st.write(resultado_df)
    
with tab1:
    st.subheader("Métricas utilizadas para avaliar os resultados do Modelo de Previsão")
    st.markdown(
        """
O MSE mede a :green[média dos quadrados dos erros], isto é, a média das diferenças ao quadrado entre os valores previstos e os reais. Quanto :green[menor o MSE], melhor o modelo está se ajustando ao seu dataset. :green[Um MSE de 0.01 é bastante baixo], indicando que o modelo está fazendo previsões muito próximas aos valores reais.

O RMSE é simplesmente a :green[raiz quadrada do MSE] e oferece a vantagem de estar nas mesmas unidades que a variável de resposta. Um :green[RMSE de 0.08], sendo uma magnitude pequena, sugere que o modelo está com um bom ajuste.

O MAE fornece a :green[média dos erros absolutos], isto é, as diferenças médias entre valores previstos e observados, sem considerar a direção do erro (positivo ou negativo). Um :green[MAE de 0.03] indica que, em média, as previsões do modelo desviam-se muito pouco dos valores reais.

O R² é uma medida de :green[quão bem as variáveis independentes estão prevendo a variável dependente]. Um R² de :green[1.00] é excepcional, indicando que o modelo explica 100% da variabilidade da resposta prevista pelos dados.
        """
    )
    
    st.divider()
    
    # Métricas MSE RMSE MAE R²
    mse = mean_squared_error(y_test, model.predict(X_test))
    st.write(f"Erro Quadrático Médio (MSE): :green[{mse:.2f}]")

    rmse = mse ** 0.5
    st.write(f"Raiz do Erro Quadrático Médio (RMSE): :green[{rmse:.2f}]")

    mae = mean_absolute_error(y_test, model.predict(X_test))
    st.write (f"Erro Absoluto Médio (MAE): :green[{mae:.2f}]")

    r2 = r2_score(y_test, model.predict(X_test))
    st.write(f"Coeficiente de Determinação (R²): :green[{r2:.2f}]")
    
    st.divider()

    st.subheader("Gráfico de Dispersão - IPV Previsto vs Nota de Corte")
    st.markdown(
        """
Este gráfico compara os :green[valores de IPV previstos para 2023] com a :green[nota de corte calculada]. A linha vermelha mostra a :green[nota de corte], que serve como um limite para determinar quais alunos atingem o ponto de virada.

Este gráfico ajuda a visualizar a distribuição das previsões em relação ao limite, permitindo avaliar se o modelo está prevendo corretamente as classificações.
        """)
    image_path = 'assets/imgs/dispersao_ipv.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos por fase', use_column_width=False, width=600)
    st.markdown("</div>", unsafe_allow_html=True)

    st.subheader("Histograma - Distribuição do IPV Previsto")
    st.markdown(
        """
O histograma mostra a :green[distribuição dos valores de IPV previstos]. A linha vermelha novamente marca a nota de corte de 2023.

Este gráfico permite avaliar como os valores de IPV estão distribuídos. Se a maioria dos valores previstos estiver próxima ou abaixo da nota de corte, isso sugere que poucos alunos atingirão o ponto de virada.
        """)
    image_path = 'assets/imgs/histograma_ipv.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos por fase', use_column_width=False, width=600)
    st.markdown("</div>", unsafe_allow_html=True)

    st.subheader("Gráfico de Resíduos")
    st.markdown(
        """
O gráfico de resíduos mostra a diferença entre as previsões e os valores reais de IPV, permitindo analisar o erro do modelo.

Os resíduos devem estar distribuídos de forma :green[aleatória] em torno de zero, o que indicaria que o modelo está fazendo boas previsões :green[sem padrões de erro evidentes]. Se houver uma tendência ou padrão nos resíduos (por exemplo, uma curva), isso pode sugerir que o modelo está sub ou superestimando as previsões em determinadas faixas de IPV, o que indicaria a necessidade de ajustes no modelo.

        """)
    image_path = 'assets/imgs/residuos.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos por fase', use_column_width=False, width=600)
    st.markdown("</div>", unsafe_allow_html=True)

    st.divider()