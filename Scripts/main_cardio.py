import pandas as pd

base = pd.read_csv("cardio.txt")


base.describe()

previsores = base.iloc[:,1:12].values
classe = base.iloc[:, 12].values



from sklearn.model_selection import train_test_split
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.25, random_state=0)



