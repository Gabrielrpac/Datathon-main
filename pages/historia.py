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
        A Instituição Passos Mágicos desempenha um papel crucial no apoio a crianças e adolescentes em situação de vulnerabilidade social, buscando promover seu desenvolvimento integral por meio de educação, cultura e suporte emocional. Para entender melhor o impacto de suas atividades e identificar áreas de melhoria, a análise exploratória de dados se torna uma ferramenta fundamental.

        Este projeto visa explorar os dados coletados pela instituição, buscando padrões e insights que possam informar estratégias de atuação e aprimorar a eficácia dos programas oferecidos. A análise será realizada em diversas dimensões, incluindo o perfil dos atendidos, a fase em que o aluno se encontra no programa e o tipo de atividades participadas, além dos resultados alcançados em termos de desenvolvimento pessoal e acadêmico.

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
    st.markdown("A análise dos dados coletados revela insights sobre a faixa etária predominante, o que pode influenciar as estratégias de intervenção e o planejamento das atividades.Ao examinar as idades dos alunos, observamos uma variação significativa, com a presença de jovens desde os 7 até os 20 anos. A maioria dos alunos se concentra nas idades entre 10 e 17 anos, o que é comum em instituições que atendem crianças e adolescentes em desenvolvimento. Essa concentração pode sugerir a necessidade de programas direcionados a essas faixas etárias específicas, abordando questões pertinentes a essa fase da vida, como transição escolar, desenvolvimento social e emocional, e preparação para a vida adulta. Ao examinar as idades dos alunos, observamos uma variação significativa, com a presença de jovens desde os 7 até os 20 anos. A maioria dos alunos se concentra nas idades entre 10 e 17 anos, o que é comum em instituições que atendem crianças e adolescentes em desenvolvimento. Essa concentração pode sugerir a necessidade de programas direcionados a essas faixas etárias específicas, abordando questões pertinentes a essa fase da vida.")
    image_path = 'assets/imgs/quantidade_de_alunos_por_idade.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos por idade', use_column_width=False, width=600)
    st.markdown("</div>", unsafe_allow_html=True)

with tab1:
    st.subheader("Distribuição dos alunos por fase")
    st.markdown("A Instituição Passos Mágicos organiza seus alunos em fases que correspondem aos níveis do sistema de ensino brasileiro. Essa estrutura não apenas facilita o acompanhamento do progresso educacional, mas também permite à instituição desenvolver atividades e intervenções específicas para cada grupo etário e nível de aprendizado. A fase 1, que abrange os alunos do 3º e 4º ano do ensino fundamental, apresenta o maior número de alunos, totalizando 172. Isso sugere que a instituição possui uma forte capacidade de atrair e manter alunos nessa faixa inicial do ensino fundamental, possivelmente refletindo um maior número de crianças nessa idade em situação de vulnerabilidade. Em contrapartida, as fases mais avançadas, especialmente as do ensino médio e da universidade, apresentam um número significativamente menor de alunos. Isso pode indicar desafios na retenção de jovens conforme avançam na educação, seja devido a fatores sociais, econômicos ou à falta de apoio contínuo. A fase 4, com apenas 55 alunos, e a fase 8, com 24, ressaltam a necessidade de estratégias específicas para apoiar a transição dos alunos para os anos finais do ensino fundamental e a continuidade no ensino superior. Em resumo, a análise da distribuição de alunos por fases do programa da Instituição Passos Mágicos revela um padrão que pode orientar ações futuras. Ao entender onde estão concentrados os alunos e quais fases apresentam maiores desafios, a instituição pode desenvolver programas mais eficazes e direcionados, garantindo que cada aluno receba o suporte necessário para alcançar seu pleno potencial educacional. Essa abordagem não só melhora a experiência dos alunos, mas também fortalece o impacto positivo da instituição em suas vidas.")
    image_path = 'assets/imgs/quantidade_de_alunos_por_fase.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos por fase', use_column_width=False, width=600)
    st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.subheader("Distribuição dos alunos por tipo de instituição")
    st.markdown("Aqui você pode adicionar uma breve descrição ou contexto sobre a distribuição dos alunos por tipo de instituição.")
    image_path = 'assets/imgs/tipo_instituicao.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos por tipo de instituição', use_column_width=False, width=600)
    st.markdown("</div>", unsafe_allow_html=True)

with tab3:
    st.subheader("Distribuição dos alunos entre as instituições privadas")
    st.markdown("Aqui você pode adicionar uma breve descrição ou contexto sobre a distribuição dos alunos entre as instituições privadas.")
    image_path = 'assets/imgs/distribuicao_instituicao_privada.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos entre as instituições privadas', use_column_width=False, width=600)
    st.markdown("</div>", unsafe_allow_html=True)



st.divider()