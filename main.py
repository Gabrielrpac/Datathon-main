import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utilidades.const import TITULO_PRINCIPAL
from utilidades.layout import output_layout
import warnings


warnings.filterwarnings("ignore")
st.set_page_config(page_title=TITULO_PRINCIPAL, layout="wide")
output_layout()

st.header(f":green[{TITULO_PRINCIPAL}]")

st.subheader(
    ":green[PROPOSTA DO PROJETO]",
    divider="blue",
)
st.markdown(
    """
    O grande objetivo do Datathon foi de trazer e gerar uma análise e um modelo de previsão para demonstrar o impacto que a ONG “Passos Mágicos” tem realizado sobre a comunidade que atende. A associação busca instrumentalizar o uso da educação como ferramenta para realizar mudanças nas condições de vida das crianças e jovens em vulnerabilidade social.
    
    Com base no dataset de pesquisa extensiva do desenvolvimento educacional no período de 2020, 2021 e 2022, trouxemos uma análise dos dados e também o modelo de predição.
"""
)

st.subheader(":green[PROPÓSITO]", divider="blue")
st.markdown(
    """
    Analisar o histórico de dados e as informações de cada aluno para criar análises e insights relevantes, trazendo também um modelo de machine learning que auxilie na previsão de métricas futuras.
    
    Durante este projeto, também foi abordado o *deploy* de modelos num ambiente produtivo, no caso, esta aplicação Streamlit.
"""
)


st.subheader(":green[RECURSOS]", divider="blue")
st.markdown(
    """
    Primeiro, Realizamos a importação dos dados dos aluno de acordo com a nossa base de dados "PEDE". Em seguida, analisamos os dados para entender melhor como estão distribuidos.

    Com base na análise feita, criamos um modelo através do SKlearn para que seja possível prever se um aluno irá ou não atingir a métrica do "Ponto de virada".
"""
)