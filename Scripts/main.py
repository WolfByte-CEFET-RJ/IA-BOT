import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


#funções de custo
def bce(y, y_pred, t, derivative=False):
    if derivative:
        return -(y - y_pred) / (y_pred * (1 - y_pred) * t)
    return -np.mean(y * np.log(abs(y - y_pred)) +
                    (1 - y) * np.log(abs(1 - y_pred)))


#funções de ativação
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximun(0, x)

#classe para criar uma camada
class Layer_Dense():
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases
        

#importando dataset
previsores = pd.read_csv('entradas_breast.csv')
classe = pd.read_csv('saidas_breast.csv')

#normalização
previsores = (previsores-previsores.min())/(previsores.max()-previsores.min()) 

#separando entre treino e teste
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores,classe, test_size=0.25)



