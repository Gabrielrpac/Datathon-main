import streamlit as st
from tabs.intro.pede_tab import IntroPEDE
from tabs.intro.sklearn_tab import IntroSKlearn
from tabs.intro.pm_tab import IntroPM
from utilidades.const import TITULO_INTRODUCAO, TITULO_PRINCIPAL
from utilidades.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_INTRODUCAO} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f":green[{TITULO_INTRODUCAO}]")

    st.markdown(
        """
        Nesta introdução, vamos apresentar algumas informações importantes para entendimento do contexto geral do projeto e como ele foi pensado para atender a necessidade proposta.\n\n
    """
    )

    tab0, tab1, tab2 = st.tabs(
        tabs=[
            "Sobre a Passos Mágicos",
            "Metodologia PEDE",
            "SKlearn"
        ]
    )

    IntroPM(tab0)
    IntroPEDE(tab1)
    IntroSKlearn(tab2)