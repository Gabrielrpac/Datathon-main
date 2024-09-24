import streamlit as st
from st_pages import show_pages, Page
import locale

from utilidades.const import TITULO_ANALISE_EXPLORATORIA, TITULO_HISTORIA, TITULO_INTRODUCAO, TITULO_MODELO, TITULO_REFERENCIAS

def format_number(number, format='%0.0f'):
    return locale.format_string(format, number, grouping=True)

def output_layout():
    show_pages(
        [
            Page("./main.py","DATATHON",":books:", use_relative_hash=True),
            Page("./pages/intro.py", TITULO_INTRODUCAO, ":open_book:", use_relative_hash=True),
            Page("./pages/historia.py", TITULO_HISTORIA, ":blue_book:", use_relative_hash=True),
            Page("./pages/analise.py",TITULO_ANALISE_EXPLORATORIA, ":pencil:",use_relative_hash=True,),
            Page("./pages/modelo.py", TITULO_MODELO, ":dart:", use_relative_hash=True),
            Page("./pages/refs.py",TITULO_REFERENCIAS, ":globe_with_meridians:", use_relative_hash=True),
        ]
    )

    with st.sidebar:
        st.subheader("Aluno")
        st.text("Gabriel Ribeiro Da Silva")
        st.text("RM 353106 | 3DTAT")

        st.divider()