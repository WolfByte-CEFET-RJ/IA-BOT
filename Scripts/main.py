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

def derivada_sigmoid(x):
    return sigmoid(x)*(1-sigmoid(x))

def relu(x):
    return np.maximun(0, x)

#classe para criar uma camada
class Layer_Dense():
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases
        

#test predict
def test_predict(teste,teste_saidas,pesos1,pesos2,pesos3,pesos4,bias1,bias2,bias3,bias4,prt_saida=False):
    inp1 = np.dot(teste,pesos1) + bias1
    camada_oculta1 = sigmoid(inp1)

    inp2 = np.dot(camada_oculta1,pesos2) + bias2
    camada_oculta2 = sigmoid(inp2)

    inp3 = np.dot(camada_oculta2,pesos3) + bias3
    camada_oculta3 = sigmoid(inp3)

    inp4 = np.dot(camada_oculta3,pesos4) + bias4
    camada_saida = sigmoid(inp4)
    
    custo = bce(teste_saidas,camada_saida,qtt_test,False)
    
    if prt_saida:
        print("erro: %.10f"%(custo))
        print(camada_saida)
    
    return custo


#importando dataset
entradas = pd.read_csv('../Dataset/entradas_breast.csv')
saidas = pd.read_csv('../Dataset/saidas_breast.csv')

#normalização
entradas = (entradas-entradas.min())/(entradas.max()-entradas.min())

#transformando em array do numpy
dataset = np.array(entradas)
dataset_saidas = np.array(saidas)

#separando entre treino e teste
train, test, train_saidas, test_saidas = train_test_split(dataset,dataset_saidas,test_size=1/5)


#parametros
qtt_treino = len(train)
qtt_test = len(test)
epochs = 5000
learning_rate = 0.1
erros = []
erros2 = []


#criando as camadas
inp1 = Layer_Dense(30, 16)
inp2 = Layer_Dense(16, 16)
inp3 = Layer_Dense(16,8)
inp4 = Layer_Dense(8, 1)

#feedforward
for epocas in range(epochs + 1):
    inp1.forward(train)
    camada_oculta1 = sigmoid(inp1.output)

    inp2.forward(camada_oculta1)
    camada_oculta2 = sigmoid(inp2.output)

    inp3.forward(camada_oculta2)
    camada_oculta3 = sigmoid(inp3.output)

    inp4.forward(camada_oculta3)
    camada_saida = sigmoid(inp4.output)

    custo = bce(train_saidas, camada_saida, qtt_treino, False)
    erros.append(custo)
    print(custo)