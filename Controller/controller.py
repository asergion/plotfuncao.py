# Controller/controller.py

from Model.model import Funcao
import numpy as np

def gerar_dados_grafico(tipo: str, coeficientes: dict, x_range=(-10, 10), num_pontos=100):
    funcao = Funcao(tipo, coeficientes)
    x = np.linspace(x_range[0], x_range[1], num_pontos)
    y = funcao.calcular(x)
    return x, y
