import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np


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
        self.weights = 2 * np.random.random((n_inputs, n_neurons)) -1
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases
        
#test predict
def test_predict(teste,teste_saidas,pesos1,pesos2,pesos3,pesos4,bias1,bias2,
                 bias3,bias4,prt_saida=False):
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

#importando Dataset
base = pd.read_csv("../../Dataset/chronic_kidney/chronic_kidney.csv")

#normalizando os dados
base = (base-base.min())/(base.max()-base.min())

base.describe()

#separando o database em entrada e saida
entradas = base.iloc[:,0:13].values
saidas = base.iloc[:, 13:14].values

#transformando em array do numpy
dataset = np.array(entradas)
dataset_saidas = np.array(saidas)

#separando entre treino e teste
train, test, train_saidas, test_saidas = train_test_split(dataset,dataset_saidas,test_size=1/5)

#parametros
qtt_treino = len(train)
qtt_test = len(test)
epochs = 7000
learning_rate = 2
erros = []
erros2 = []

#criando as camadas
inp1 = Layer_Dense(13, 7)
inp2 = Layer_Dense(7, 7)
inp3 = Layer_Dense(7, 4)
inp4 = Layer_Dense(4,1)

#calculo das previsoes
for epocas in range(epochs + 1):
    #feedforward
    inp1.forward(train)
    camada_oculta1 = sigmoid(inp1.output)

    inp2.forward(camada_oculta1)
    camada_oculta2 = sigmoid(inp2.output)

    inp3.forward(camada_oculta2)
    camada_oculta3 = sigmoid(inp3.output)

    inp4.forward(camada_oculta3)
    camada_saida = sigmoid(inp4.output)

    custo = bce(train_saidas, camada_saida, qtt_treino, False)
    result = test_predict(test,test_saidas,inp1.weights,inp2.weights,inp3.weights,inp4.weights,inp1.biases,inp2.biases,inp3.biases,inp4.biases)
    erros.append(custo)
    erros2.append(result)
    print("epoca: %d/%d erro_train: %f erro_test: %f"%(epocas,epochs,custo,result))
    
    #backpropagation
    derivada_saida = bce(train_saidas,camada_saida,qtt_treino,True)
    
    dinp4 = derivada_sigmoid(inp4.output) * derivada_saida # dy =  da(y) * df(y')
    derivada_oculta3 = np.dot(dinp4,inp4.weights.T) # dx = w.T * dy 
    d_pesos4 = np.dot(dinp4.T,camada_oculta3) # dw = x * dy.T
    d_pesos4 +=  (1.0/train_saidas.shape[0] * inp4.weights).T
    d_bias4 = 1.0 * dinp4.sum(axis=0,keepdims=True) # db = sum(dy) 
    
    dinp3 = derivada_sigmoid(inp3.output) * derivada_oculta3
    derivada_oculta2 = np.dot(dinp3,inp3.weights.T)
    d_pesos3 = np.dot(dinp3.T,camada_oculta2)
    d_pesos3 += (1.0/train_saidas.shape[0] * inp3.weights).T
    d_bias3 = 1.0 * dinp3.sum(axis=0,keepdims=True)
    
    dinp2 = derivada_sigmoid(inp2.output) * derivada_oculta2
    derivada_oculta1 = np.dot(dinp2,inp2.weights.T)
    d_pesos2 = np.dot(dinp2.T,camada_oculta1)
    d_pesos2 += (1.0/train_saidas.shape[0] * inp2.weights).T
    d_bias2 = 1.0 * dinp2.sum(axis=0,keepdims=True)
    
    dinp1 = derivada_sigmoid(inp1.output) * derivada_oculta1
    derivada_entrada = np.dot(dinp1,inp1.weights.T)
    d_pesos1 = np.dot(dinp1.T,train)
    d_pesos1 += (1.0/train_saidas.shape[0] * inp1.weights).T
    d_bias1 = 1.0 * dinp1.sum(axis=0,keepdims=True)
    
    inp4.weights = inp4.weights + (-learning_rate * d_pesos4.T)
    inp3.weights = inp3.weights + (-learning_rate * d_pesos3.T)
    inp2.weights = inp2.weights + (-learning_rate * d_pesos2.T)
    inp1.weights = inp1.weights + (-learning_rate * d_pesos1.T)
    
    inp4.biases = inp4.biases - learning_rate * d_bias4
    inp3.biases = inp3.biases - learning_rate * d_bias3
    inp2.biases = inp2.biases - learning_rate * d_bias2
    inp1.biases = inp1.biases - learning_rate * d_bias1

result = test_predict(test,test_saidas,inp1.weights,inp2.weights,inp3.weights,inp4.weights,inp1.biases,inp2.biases,inp3.biases,inp4.biases)

#calculando taxa de acerto
def predict (test,funcao_ativacao):
    
    if funcao_ativacao == "sigmoid":
        f = sigmoid
        
    camada_oculta1 = f(np.dot(test,w_layer1) + b_layer1)
    camada_oculta2 = f(np.dot(camada_oculta1,w_layer2) + b_layer2)
    camada_oculta3 = f(np.dot(camada_oculta2,w_layer3) + b_layer3)

    return f(np.dot(camada_oculta3,w_layer4) + b_layer4)


w_layer1, w_layer2, w_layer3, w_layer4, b_layer1, b_layer2, b_layer3, b_layer4 = inp1.weights,inp2.weights,inp3.weights,inp4.weights,inp1.biases,inp2.biases,inp3.biases,inp4.biases

saidas_real = dataset_saidas
saidas = predict(dataset,"sigmoid")
saidas = np.where(saidas >= 0.8,1,0)

acertos = 0
for y1,y2 in zip(saidas,saidas_real):
    if y1 == y2:
        acertos += 1

print("Taxa de acerto %.2f"%(acertos/len(saidas)*100) +"%")

resultado = (acertos/len(saidas)*100)

path = 'C:\projetos\IA-BOT/' #mudar para seu path
resposta = input("Deseja fazer um Dump dos pesos e bias? S/N: ")


if resposta == "S":
    np.savetxt(path + "Pesos\\chronic_kidney\\pesos1.txt", inp1.weights, delimiter=", ")
    np.savetxt(path + "Pesos\\chronic_kidney\\pesos2.txt", inp2.weights, delimiter=", ")
    np.savetxt(path + "Pesos\\chronic_kidney\\pesos3.txt", inp3.weights, delimiter=", ")
    np.savetxt(path + "Pesos\\chronic_kidney\\pesos4.txt", inp4.weights, delimiter=", ")
    
    np.savetxt(path + "Biases\\chronic_kidney\\bias1.txt", inp1.biases, delimiter=", ")
    np.savetxt(path + "Biases\\chronic_kidney\\bias2.txt", inp2.biases, delimiter=", ")
    np.savetxt(path + "Biases\\chronic_kidney\\bias3.txt", inp3.biases, delimiter=", ")
    np.savetxt(path + "Biases\\chronic_kidney\\bias4.txt", inp4.biases, delimiter=", ")
    print("Dump dos pesos e bias concluido")
    
else: 
    print("Pesos e Bias não foram salvos")




   