import numpy as np
import pandas as pd

#Mude para seu path
path_pesos = "C:\projetos\IA-BOT\Pesos\chronic_kidney"
path_bias = "C:\projetos\IA-BOT\Biases\chronic_kidney"

entradas = pd.read_csv('../Dataset/chronic_kidney/chronic_kidney.csv')
entradas = entradas.iloc[:,0:13].values
entradas = (entradas-entradas.min())/(entradas.max()-entradas.min())

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#Lendo pesos e biases
w_layer1 = np.genfromtxt(path_pesos + '/pesos1.txt', delimiter= ', ')
w_layer2 = np.genfromtxt(path_pesos + '/pesos2.txt', delimiter= ', ')
w_layer3 = np.genfromtxt(path_pesos + '/pesos3.txt', delimiter= ', ')
w_layer4 = np.genfromtxt(path_pesos + '/pesos4.txt', delimiter= ', ')

b_layer1 = np.genfromtxt(path_bias + '/bias1.txt', delimiter= ', ')
b_layer2 = np.genfromtxt(path_bias + '/bias2.txt', delimiter= ', ')
b_layer3 = np.genfromtxt(path_bias + '/bias3.txt', delimiter= ', ')
b_layer4 = np.genfromtxt(path_bias + '/bias4.txt', delimiter= ', ')


#calculo das previsoes
camada_oculta1 = sigmoid(np.dot(entradas, w_layer1) + b_layer1)
camada_oculta2 = sigmoid(np.dot(camada_oculta1, w_layer2) + b_layer2)
camada_oculta3 = sigmoid(np.dot(camada_oculta2, w_layer3) + b_layer3)
camada_saida = sigmoid(np.dot(camada_oculta3, w_layer4) + b_layer4)

saidas = np.where(camada_saida >= 0.8,1,0)


    


    
    
