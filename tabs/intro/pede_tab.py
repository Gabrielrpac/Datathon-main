import streamlit as st
from tabs.tab import TabInterface
from PIL import Image

class IntroPEDE(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":green[Metodologia PEDE]", divider="blue")
            st.markdown(
                """
                A Pesquisa Extensiva do Desenvolvimento Educacional, PEDE, constitui mais um esforço, dentro do programa de Governança Institucional da Associação Passos Mágicos, de sistematizar as suas ações sociais e registrar de forma rigorosa os seus resultados.

                A abordagem multidimensional adotada nesta pesquisa possibilitou a produção de um Indice sintético, que aglutina um extensivo conjunto de avaliações sobre o desenvolvimento educacional de cada um dos alunos da Associação Passos Mágicos. Esse índice, por sua vez, é composto por indicadores que guardam forte identidade com os princípios que norteiam as ações educacionais e culturais desenvolvidas pela associação.

                Identidades essas que, asseguram ao processo de avaliação um caráter empírico, que buscam medir as atividades desenvolvidas no seu caráter mais prático. Daí a nossa proposta de avaliação da própria Associação Passos Mágicos, se dar, portanto, pela interpretação dos resultados individuais de cada um dos indicadores, enquanto referências objetivas dos resultados das ações desenvolvidas. Os resultados que são efetivamente relevantes da Associação Passos Mágicos, são aqueles alcançados pelas suas ações, que se podem observar e medir pelo seu objetivo maior, o de atendimento as suas crianças e jovens.
                """
            )

            # caminho da imagem
            image_path = 'assets/imgs/inde_formacao.jpg'

            # Carregar e exibir a imagem
            image = Image.open(image_path)
            st.image(image, caption='Fonte: Silva, Dario da. Pesquisa extensiva do Desenvolvimento Educacional - PEDE 2020, pg. 4', use_column_width=True)

            st.divider()