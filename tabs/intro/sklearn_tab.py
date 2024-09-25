import streamlit as st
from tabs.tab import TabInterface


class IntroSKlearn(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(
                ":green[O que é o SKlearn?]", divider="blue"
            )
            st.markdown(
                """
                O scikit-learn ou SKlearn é uma biblioteca de código aberto para aprendizado de máquina que oferece uma gama ampla de algoritmos e ferramentas para análise e modelagem de dados. É amplamente usado por cientistas de dados e engenheiros para construir e avaliar modelos preditivos.

                Dentre as principais funcionalidades podemos listar:
                
                - Algoritmos de Aprendizado de Máquina: Inclui algoritmos para classificação, regressão, clustering, e redução de dimensionalidade.

                - Pré-processamento: Ferramentas para normalização, padronização e transformação de dados.
                
                - Modelos de Seleção: Métodos para avaliação e seleção de modelos, como validação cruzada e busca em grade.
                
                - Pipeline: Facilita a construção de pipelines de pré-processamento e modelagem, garantindo um fluxo de trabalho eficiente e reproduzível.
            """,
                unsafe_allow_html=True,
            )

            st.divider()