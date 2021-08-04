import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score
from keras.models import Sequential
from keras.layers import Dense

base = pd.read_csv("../../Dataset/cardiovascular_disease/cardiovascular.txt")

#normalizando os dados
base = (base-base.min())/(base.max()-base.min())

#separando o database em entrada e saida
entradas = base.iloc[:1000,1:12].values
saidas = base.iloc[:1000, 12:13].values

#separando entre treino e teste
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(entradas,saidas,test_size=1/4)

classificador = Sequential()
classificador.add(Dense(units=32, activation= 'relu', kernel_initializer= 'glorot_uniform', input_dim=11))
classificador.add(Dense(units=64, activation= 'relu', kernel_initializer= 'glorot_uniform'))
classificador.add(Dense(units=64, activation= 'relu', kernel_initializer= 'glorot_uniform'))
classificador.add(Dense(units=1, activation= 'sigmoid'))

classificador.compile(optimizer= 'adam', loss= 'binary_crossentropy', metrics=['accuracy'])

classificador.fit(previsores_treinamento,classe_treinamento,batch_size = 16, epochs=100)

previsoes = classificador.predict(previsores_teste)
previsoes = (previsoes > 0.5)
precisao = accuracy_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes)