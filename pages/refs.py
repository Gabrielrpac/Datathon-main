import streamlit as st
from utilidades.const import TITULO_PRINCIPAL, TITULO_REFERENCIAS
from utilidades.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_REFERENCIAS} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f":green[{TITULO_REFERENCIAS}]")
    
    st.markdown(
        """ 
        01. https://scikit-learn.org/stable/user_guide.html Acesso em  10/09/2024
        02. https://docs.streamlit.io/ Acesso em  10/09/2024
        03. https://passosmagicos.org.br Acesso em  10/09/2024
        04. https://numpy.org/doc/ Acesso em  10/09/2024
        05. https://drive.google.com/drive/folders/1Z1j6uzzCOgjB2a6i3Ym1pmJRsasfm7cD Acesso em  10/09/2024        
        06. https://pandas.pydata.org/docs/index.html Acesso em  02/09/2024
        07. https://matplotlib.org/stable/index.html Acesso em  10/09/2024
        08. https://docs.streamlit.io Acesso em  06/09/2024        
        
        """)
