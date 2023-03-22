import math
import numpy as np
import pandas as pd
data = pd.read_excel('dataset.xlsx')

data.replace('negative', 0, inplace=True)
data.replace('positive', 1, inplace=True)

# column1_get = ['Patient age quantile']
# column2_get = ['SARS-Cov-2 exam result']

# column3_get = ['Patient addmited to regular ward (1=yes, 0=no)']
# column4_get = ['Patient addmited to semi-intensive unit (1=yes, 0=no)']
# column5_get = ['Patient addmited to intensive care unit (1=yes, 0=no)']
# column6_get = ['Hematocrit']

columns2 = ['Patient age quantile','SARS-Cov-2 exam result', 'Patient addmited to regular ward (1=yes, 0=no)', 'Patient addmited to semi-intensive unit (1=yes, 0=no)', 'Patient addmited to intensive care unit (1=yes, 0=no)', 'Hematocrit']
columns = ['Hemoglobin', 'Hematocrit', 'Hematocrit']
for i in columns: 
    colunas = data[i]

print('colunas', colunas)
# print('a', hemoglobin)

# --------------------------------- #
# encontrar a media do dataset
def media_dt(dataset):
    # sm = 0
    # tamanho_dt = len(dataset)
    # for i in range(tamanho_dt):
    #     sm+=dataset[i]
    #     media = sm/tamanho_dt
    media = np.mean(dataset, axis=0)
    return media


def desvio_padrao(dataset):
    return np.std(dataset)

# O coeficiente de variação (CV) é uma medida estatística que indica a variabilidade
#  relativa de uma distribuição em relação à sua média. É calculado como o desvio padrão 
#  dividido pela média, expresso em porcentagem.

def coeficiente_variacao(media, desvio):
    coef_var = desvio/media 
    print('coeficiente de variacao', coef_var)

    return coef_var

# regra geral acima de 30% 
for i in columns:
        media = media_dt(data[i])
        desvio = desvio_padrao(data[i])
        coeficiente_variacao(media, desvio)
        cv_outlier = (np.max(data[i]) - np.median(data[i])) / np.std(data[i])
        if cv_outlier > 1:
            print('-- alta probabilidade de outlier -- ')
        else: 
            print('-- baixa probabilidade -- ')
        print('outlier', cv_outlier)
# media1 = media_dt(column1)
# media2 = media_dt(column2)
# media3 = media_dt(column3)
# media4 = media_dt(column4)
# media5 = media_dt(column5)
# media6 = media_dt(column6)

# desvio_1= desvio_padrao(column1)
# desvio_2= desvio_padrao(column2)
# desvio_3= desvio_padrao(column3)
# desvio_4= desvio_padrao(column4)
# desvio_5= desvio_padrao(column5)
# desvio_5= desvio_padrao(column6)

# a = coeficiente_variacao(media_hemoglobin, desvio_hemoglobin)
# a = coeficiente_variacao(media_hemoglobin, desvio_hemoglobin)
# a = coeficiente_variacao(media_hemoglobin, desvio_hemoglobin)
# a = coeficiente_variacao(media_hemoglobin, desvio_hemoglobin)