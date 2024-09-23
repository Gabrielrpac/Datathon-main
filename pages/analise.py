import streamlit as st
import pandas as pd
from PIL import Image
from utilidades.const import TITULO_ANALISE_EXPLORATORIA, TITULO_PRINCIPAL
from utilidades.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_ANALISE_EXPLORATORIA} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    with open("assets/historia.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    st.header(f":green[{TITULO_ANALISE_EXPLORATORIA}]")
    st.markdown(
        """
        Ao longo dos anos, diversos eventos significativos, como guerras e revoluções, influenciaram profundamente o contexto geopolítico global de suas respectivas épocas. Esses acontecimentos desempenharam um papel crucial nas oscilações dos preços do petróleo, uma commodity fundamental na economia mundial.\n\n

        A seguir, serão apresentados alguns dos principais eventos que influenciaram diretamente

        * Guerra do Golfo (1990-1991)
        * Atentados terroristas nos EUA (2001)
        * Guerra do Iraque (2003-2011)
        * Crise financeira global (2007-2009)
        * Primavera Árabe (2010-2012)
        * OPEP - Grande ritmo de produção e baixa demanda (2014-2015)
        * Pandemia de COVID-19 (2020-2022)
        * Conflito Rússia-Ucrânia (2022~)

        Esses eventos não apenas alteraram o equilíbrio geopolítico global, mas também tiveram impactos diretos nos mercados de petróleo, influenciando seus preços e volatilidade ao longo dos anos.
    """
    )

tab0, tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, = st.tabs(
    tabs=[
        "Ponto de virada",
        "INDE",
        "Pedras",
        "Indicador de Aprendizagem",
        "Indicador de Engajamento",
        "Indicador de Adequação ao nível",
        "Indicador de Auto avaliação",
        "Indicador Psicossocial",
        "Indicador Psicopedagógico",
        "Indicador de Ponto de virada",
    ]
)

with tab0:
    st.subheader("Análise Ponto de virada")
    st.markdown("Aqui você pode adicionar uma breve descrição ou contexto sobre a distribuição dos alunos por idade.")
    image_path = 'assets/imgs/atingiram_pv.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos por idade', use_column_width=False, width=600)  # Ajuste o valor conforme necessário
    st.markdown("</div>", unsafe_allow_html=True)

with tab1:
    st.subheader("Análise Índice do Desenvolvimento Educacional")
    st.markdown("Aqui você pode adicionar uma breve descrição ou contexto sobre a distribuição dos alunos por fase.")
    image_path = 'assets/imgs/inde_var.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos por fase', use_column_width=False, width=600)  # Ajuste o valor conforme necessário
    st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.subheader("Análise Pedras")
    st.markdown("Aqui você pode adicionar uma breve descrição ou contexto sobre a distribuição dos alunos por tipo de instituição.")
    image_path = 'assets/imgs/pedra_var.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos por tipo de instituição', use_column_width=False, width=600)  # Ajuste o valor conforme necessário
    st.markdown("</div>", unsafe_allow_html=True)

with tab3:
    st.subheader("Análise IDA")
    st.markdown("Aqui você pode adicionar uma breve descrição ou contexto sobre a distribuição dos alunos entre as instituições privadas.")
    image_path = 'assets/imgs/ida_var.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos entre as instituições privadas', use_column_width=False, width=600)  # Ajuste o valor conforme necessário
    st.markdown("</div>", unsafe_allow_html=True)

with tab4:
    st.subheader("Análise IEG")
    st.markdown("Aqui você pode adicionar uma breve descrição ou contexto sobre a distribuição dos alunos entre as instituições privadas.")
    image_path = 'assets/imgs/ieg_var.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos entre as instituições privadas', use_column_width=False, width=600)  # Ajuste o valor conforme necessário
    st.markdown("</div>", unsafe_allow_html=True)

with tab5:
    st.subheader("Análise IAN")
    st.markdown("Aqui você pode adicionar uma breve descrição ou contexto sobre a distribuição dos alunos entre as instituições privadas.")
    image_path = 'assets/imgs/ian_var.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos entre as instituições privadas', use_column_width=False, width=600)  # Ajuste o valor conforme necessário
    st.markdown("</div>", unsafe_allow_html=True)

with tab6:
    st.subheader("Análise IAA")
    st.markdown("Aqui você pode adicionar uma breve descrição ou contexto sobre a distribuição dos alunos entre as instituições privadas.")
    image_path = 'assets/imgs/iaa_var.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos entre as instituições privadas', use_column_width=False, width=600)  # Ajuste o valor conforme necessário
    st.markdown("</div>", unsafe_allow_html=True)

with tab7:
    st.subheader("Análise IPS")
    st.markdown("Aqui você pode adicionar uma breve descrição ou contexto sobre a distribuição dos alunos entre as instituições privadas.")
    image_path = 'assets/imgs/ips_var.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos entre as instituições privadas', use_column_width=False, width=600)  # Ajuste o valor conforme necessário
    st.markdown("</div>", unsafe_allow_html=True)

with tab8:
    st.subheader("Análise IPP")
    st.markdown("Aqui você pode adicionar uma breve descrição ou contexto sobre a distribuição dos alunos entre as instituições privadas.")
    image_path = 'assets/imgs/ipp_var.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos entre as instituições privadas', use_column_width=False, width=600)  # Ajuste o valor conforme necessário
    st.markdown("</div>", unsafe_allow_html=True)

with tab9:
    st.subheader("Análise IPV")
    st.markdown("Aqui você pode adicionar uma breve descrição ou contexto sobre a distribuição dos alunos entre as instituições privadas.")
    image_path = 'assets/imgs/ipv_var.png'
    image = Image.open(image_path)
    st.markdown(f"<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='Distribuição dos alunos entre as instituições privadas', use_column_width=False, width=600)  # Ajuste o valor conforme necessário
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()