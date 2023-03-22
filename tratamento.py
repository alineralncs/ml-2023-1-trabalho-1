import math
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

# --------------------------------- #
# dataset

data = pd.read_excel('dataset.xlsx')

# --------------------------------- #
# Ele isola os valores discrepantes selecionando 
# aleatoriamente uma característica do conjunto de características 
# fornecido e, em seguida, selecionando aleatoriamente um valor de 
# divisão entre o valor máximo e mínimo dessa característica. 
# Essa divisão aleatória de características produzirá caminhos 
# mais curtos nas árvores para os pontos de dados anômalos, 
# distinguindo-os do resto dos dados.

model = IsolationForest(n_estimators=100, max_samples='auto', contamination=float(0.05), random_state=42)


# erro could not convert string to float
# dividir as colunas em dojunto de colunas booleanas
fit = pd.get_dummies(data)

# fit.drop_duplicates()
# meu drop na apaga todas as 
fit =fit.dropna()

print(fit)

model.fit(fit)

outliers = model.predict(data)


sns.heatmap(outliers.reshape(-1, 1), cmap='coolwarm', cbar=False, yticklabels=False)


# print('d', dt)
# data = data.dropna()

# print('data', data)

# columns_to_get_hemoglobin = ['Hemoglobin']


# hemoglobin = data[columns_to_get_hemoglobin]


# # print(selected_columns)

# print('a', hemoglobin)

# # --------------------------------- #
# # encontrar a media do dataset
# def media_dt(dataset):
#     # sm = 0
#     # tamanho_dt = len(dataset)
#     # for i in range(tamanho_dt):
#     #     sm+=dataset[i]
#     #     media = sm/tamanho_dt
#     media = np.mean(dataset, axis=0)
#     return media


# def desvio_padrao(dataset):
#     return np.std(dataset)

# def coeficiente_variacao(media, desvio):
#     coef_var = desvio/media
#     print('coeficiente de variacao', coef_var)
#     return coef_var

# media_hemoglobin = media_dt(hemoglobin)

# desvio_hemoglobin = desvio_padrao(hemoglobin)


# coeficiente_variacao(media_hemoglobin, desvio_hemoglobin)




