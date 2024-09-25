import streamlit as st
from tabs.tab import TabInterface

class IntroPM(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()
    
    def render(self):
        with self.tab:
            st.subheader(':green[Associação Passos Mágicos]', divider='blue')
            st.markdown('''
            A Associação Passos Mágicos tem uma trajetória de 30 anos de atuação, trabalhando na transformação da vida de crianças e jovens de baixa renda os levando a melhores oportunidades de vida.
                        
            A transformação, idealizada por Michelle Flues e Dimetri Ivanoff, começou em 1992, atuando dentro de orfanatos, no município de Embu-Guaçu.
                        
            Em 2016, depois de anos de atuação, decidem ampliar o programa para que mais jovens tivessem acesso a essa fórmula mágica para transformação que inclui: educação de qualidade, auxílio psicológico/psicopedagógico, ampliação de sua visão de mundo e protagonismo. Passaram então a atuar como um projeto social e educacional, criando assim a Associação Passos Mágicos.

            ''')
            st.divider()