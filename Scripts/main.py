import pandas as pd
from sklearn.model_selection import train_test_split

#importando dataset
previsores = pd.read_csv('entradas_breast.csv')
classe = pd.read_csv('saidas_breast.csv')

#normalização
previsores = (previsores-previsores.min())/(previsores.max()-previsores.min()) 

#separando entre treino e teste
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores,classe, test_size=0.25)

