# Model/model.py

import numpy as np

class Funcao:
    def __init__(self, tipo: str, coeficientes: dict):
        self.tipo = tipo  # "linear" ou "quadratica"
        self.coef = coeficientes

    def calcular(self, x):
        if self.tipo == "linear":
            a = self.coef.get("a", 1)
            b = self.coef.get("b", 0)
            return a * x + b
        elif self.tipo == "quadratica":
            a = self.coef.get("a", 1)
            b = self.coef.get("b", 0)
            c = self.coef.get("c", 0)
            return a * x**2 + b * x + c
        else:
            raise ValueError("Tipo de função inválido. Use 'linear' ou 'quadratica'.")
