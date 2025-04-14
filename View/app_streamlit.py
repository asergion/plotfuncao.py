# View/app_streamlit.py

# View/app_streamlit.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def main():
    st.set_page_config(page_title="Plot Função", layout="wide")
    st.title("📈 Visualização de Funções")

    # Sidebar
    st.sidebar.header("Configuração da Função")
    tipo_funcao = st.sidebar.selectbox("Escolha o tipo de função", ["Linear", "Quadrática"])

    st.sidebar.markdown("---")

    # Parâmetros da função com slider e input
    st.sidebar.subheader("Parâmetros da Função")

    if tipo_funcao == "Linear":
        col1, col2 = st.sidebar.columns([2, 3])
        a = col1.number_input("Coeficiente A (inclinação)", value=1.0)
        a_slider = col2.slider("A", -10.0, 10.0, a, step=0.1)
        a = a_slider  # priorizar slider

        col3, col4 = st.sidebar.columns([2, 3])
        b = col3.number_input("Coeficiente B (intercepto)", value=0.0)
        b_slider = col4.slider("B", -20.0, 20.0, b, step=0.5)
        b = b_slider

    elif tipo_funcao == "Quadrática":
        col1, col2 = st.sidebar.columns([2, 3])
        a = col1.number_input("Coeficiente A (quadrático)", value=1.0)
        a_slider = col2.slider("A", -10.0, 10.0, a, step=0.1)
        a = a_slider

        col3, col4 = st.sidebar.columns([2, 3])
        b = col3.number_input("Coeficiente B (linear)", value=0.0)
        b_slider = col4.slider("B", -10.0, 10.0, b, step=0.1)
        b = b_slider

        col5, col6 = st.sidebar.columns([2, 3])
        c = col5.number_input("Coeficiente C (constante)", value=0.0)
        c_slider = col6.slider("C", -20.0, 20.0, c, step=0.5)
        c = c_slider

    # Gerar pontos e plotar
    x = np.linspace(-10, 10, 400)

    if tipo_funcao == "Linear":
        y = a * x + b
    else:
        y = a * x**2 + b * x + c

    # Plot
    fig, ax = plt.subplots()
    ax.plot(x, y, label=f"Função {tipo_funcao}")
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

if __name__ == "__main__":
    main()
