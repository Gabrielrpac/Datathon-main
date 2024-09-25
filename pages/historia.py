import streamlit as st
import pandas as pd
from PIL import Image
from utilidades.const import TITULO_HISTORIA, TITULO_PRINCIPAL
from utilidades.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_HISTORIA} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    with open("assets/historia.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    st.header(f":green[{TITULO_HISTORIA}]")
    st.markdown(
    """
A Instituição Passos Mágicos desempenha um papel crucial no apoio a crianças e adolescentes em situação de vulnerabilidade social, buscando promover seu :green[desenvolvimento integral por meio de educação, cultura e suporte emocional]. Para entender melhor o impacto de suas atividades e identificar áreas de melhoria, a análise exploratória de dados se torna uma ferramenta fundamental.

Este projeto visa :green[explorar os dados coletados pela instituição, buscando padrões e insights que possam informar estratégias de atuação e aprimorar a eficácia dos programas oferecidos]. A análise será realizada em diversas dimensões, incluindo o perfil dos atendidos, a fase em que o aluno se encontra no programa e o tipo de atividades participadas, além dos resultados alcançados em termos de desenvolvimento pessoal e acadêmico.

Por meio dessa análise, esperamos mapear a distribuição dos alunos envolvidos e também identificar oportunidades para otimização do esforço e das ações da instituição, garantindo que cada criança e adolescente tenha acesso ao suporte necessário para alcançar seu potencial máximo.
    """
    )

tab0, tab1, tab2, tab3 = st.tabs(
    tabs=[
        "Distribuição dos alunos por idade",
        "Distribuição dos alunos por fase",
        "Distribuição dos alunos por tipo de instituição",
        "Distribuição dos alunos entre as instituições privadas",
    ]
)

with tab0:
    st.subheader("Distribuição dos alunos por idade")
    st.markdown(
        """
A análise dos dados coletados revela insights sobre a faixa etária predominante, o que pode influenciar as estratégias de intervenção e o planejamento das atividades. Ao examinar as idades dos alunos, observamos uma :green[variação significativa], com a presença de jovens desde os 7 até os 20 anos. 

A maioria dos alunos se concentra nas idades entre :green[10 e 17 anos], o que é comum em instituições que atendem crianças e adolescentes em desenvolvimento. Essa concentração pode sugerir a necessidade de programas direcionados a essas faixas etárias específicas, abordando questões pertinentes a essa fase da vida, como transição escolar, desenvolvimento social e emocional, e preparação para a vida adulta. 

Ao examinar as idades dos alunos, observamos uma variação significativa, com a presença de jovens desde os :green[7 até os 20 anos]. A maioria dos alunos se concentra nas idades entre :green[10 e 17 anos], o que é comum em instituições que atendem crianças e adolescentes em desenvolvimento. Essa concentração pode sugerir a necessidade de programas direcionados a essas faixas etárias específicas, abordando questões pertinentes a essa fase da vida.
        """)
    image_path = 'assets/imgs/quantidade_de_alunos_por_idade.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos por idade', use_column_width=False, width=600)
    st.markdown("</div>", unsafe_allow_html=True)

with tab1:
    st.subheader("Distribuição dos alunos por fase")
    st.markdown(
        """
A Instituição Passos Mágicos organiza seus alunos em :green[fases] que correspondem aos níveis do sistema de ensino brasileiro. Essa estrutura não apenas facilita o acompanhamento do progresso educacional, mas também permite à instituição desenvolver atividades e intervenções específicas para cada grupo etário e nível de aprendizado. 

A :green[fase 1], que abrange os alunos do 3º e 4º ano do ensino fundamental, apresenta o maior número de alunos, totalizando :green[172]. Isso sugere que a instituição possui uma forte capacidade de atrair e manter alunos nessa faixa inicial do ensino fundamental, possivelmente refletindo um maior número de crianças nessa idade em situação de vulnerabilidade. 

Em contrapartida, as fases mais avançadas, especialmente as do ensino médio e da universidade, apresentam um número significativamente menor de alunos. Isso pode indicar desafios na retenção de jovens conforme avançam na educação, seja devido a fatores sociais, econômicos ou à falta de apoio contínuo. A :green[fase 4], com apenas :green[55 alunos], e a :green[fase 8], com :green[24], ressaltam a necessidade de estratégias específicas para apoiar a transição dos alunos para os anos finais do ensino fundamental e a continuidade no ensino superior. 

Em resumo, a análise da distribuição de alunos por fases do programa da Instituição Passos Mágicos revela um padrão que pode orientar ações futuras. Ao entender onde estão concentrados os alunos e quais fases apresentam maiores desafios, a instituição pode desenvolver programas mais eficazes e direcionados, garantindo que cada aluno receba o suporte necessário para alcançar seu pleno potencial educacional. Essa abordagem não só melhora a experiência dos alunos, mas também fortalece o impacto positivo da instituição em suas vidas.
        """)
    image_path = 'assets/imgs/quantidade_de_alunos_por_fase.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos por fase', use_column_width=False, width=600)
    st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.subheader("Distribuição dos alunos por tipo de instituição")
    st.markdown(
        """
Ao analisarmos os dados sobre a distribuição dos alunos por tipo de instituição concluímos que a maioria significativa dos alunos da ONG está matriculada em :green[escolas públicas], representando cerca de :green[85% do total], enquanto os alunos de :green[Escolas Particulares] compõem cerca de :green[15%]. A concentração majoritária de alunos em escolas públicas indica que a ONG atende predominantemente alunos de baixa ou média renda, dado que o acesso à escola pública é mais comum em contextos de vulnerabilidade social. 

A atuação da ONG passa a ser essencial para fornecer :green[suporte acadêmico e social] a esses alunos, especialmente os das escolas públicas, onde os recursos podem ser mais limitados.
        """)
    image_path = 'assets/imgs/tipo_instituicao.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos por tipo de instituição', use_column_width=False, width=600)
    st.markdown("</div>", unsafe_allow_html=True)

with tab3:
    st.subheader("Distribuição dos alunos entre as instituições privadas")
    st.markdown(
        """
O gráfico de barras mostra a distribuição dos alunos da Passos Mágicos entre diferentes instituições privadas. Com base no gráfico, a Rede Decisão/União se destaca de forma significativa, atendendo mais de :green[100 alunos], o que representa a maior parcela dos estudantes matriculados em instituições privadas.
        
Isso indica uma forte concentração dos alunos em uma única rede de ensino, o que pode ser resultado de parcerias específicas ou do perfil socioeconômico da comunidade atendida. A predominância de uma instituição privada pode sugerir que a instituição já tem e deve explorar mais parcerias com a Rede Decisão/União, dada a representatividade dela entre os alunos. 

Fortalecer essa relação pode gerar melhores resultados para os estudantes. Também seria interessante a ONG buscar diversificar suas parcerias com outras instituições privadas que possam acolher mais alunos, equilibrando melhor a distribuição e potencialmente oferecendo oportunidades educacionais variadas.
        """)
    image_path = 'assets/imgs/distribuicao_instituicao_privada.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos entre as instituições privadas', use_column_width=False, width=600)
    st.markdown("</div>", unsafe_allow_html=True)



st.divider()