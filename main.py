#""People analytics""
#En el siguiente proyecto tratamos de analizar la brecha salarial que existe en diferentes países, así como la personalidad asociada a mujeres y hombres en el entorno laboral.

import requests
from bs4 import BeautifulSoup
import pandas as pd
import src.funciones_maria as fm
#visualizar con https://nbviewer.org/

#FASE 1: web scraping -> Brecha salarial

url = "https://www.businessinsider.es/10-paises-menos-brecha-genero-salarios-336157"
html = requests.get(url)
soup = BeautifulSoup(html.content,"html.parser")

idea = soup.findAll("h3",{"class":"title"})

dic={} #en este paso queremos quedarnos con el país y el porcentaje en un diccionario, omitiendo el número del ranking
for pais in idea:
    a = pais.getText().split()
    a[1].replace('#3-_',"")
    if len(a)>3:
        my_key = ['_'.join(a[1:-1])]
        dic.update({my_key[0][:-1]: (a[-1])})
    else:
        
        dic.update({a[-2][:-1]: (a[-1])})
dic


new_key = 'Cabo_Verde' #No entendemos porqué nos da fallito "Cabo verde" todo el rato, por lo que necesitamos hacerlo aparte
old_key = '#3–_Cabo_Verde' 
dic[new_key] = dic.pop(old_key)

seriedata = pd.Series(dic) #convertimos el diccionario en una serie y luego en un data frame

frame = pd.DataFrame(seriedata)

frame

puntito = frame[0].apply(fm.convertirdecimal)

puntito2 = pd.DataFrame(puntito) #volvemos a querer que sea un data frame

puntito2.reset_index(inplace=True) #necesitamos que los paises sean una columna

columnas = list(puntito2.columns)
print(columnas)

diccio_nuevas = {'index': 'paises', 0: '% brecha salarial'} #le ponemos nombres nuevos para trabajar mejor 

puntito2.rename(columns = diccio_nuevas, inplace=True)

# FASE 2: dataset de Kagle de HR¶

turnover = pd.read_csv('data/turnover.csv',encoding = "ISO-8859-1") #abrimos el csv)

#FASE 3: empezamos a trabajar con gráficos para establecer nuestras hipótesis

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go



# Configuración para setear y que todas las fig de Seaborn salgan por defecto con este tamaño
# Se puede especificar el tamaño de cada figura
sns.set_context("poster")
sns.set(rc={"figure.figsize": (12.,6.)})
sns.set_style("whitegrid")

puntito2.paises.unique()

#GRÁFICO 1: Con este gráfico tratamos de entender cómo se comporta la brecha salarial alrededor del mundo. vemos que la mayor parte de los países tienen una brecha de entre 5 al 35%. Sin embargo, hay algunos países en el que la brecha asciende a más de un 60%

sns.boxplot(x="% brecha salarial", data=puntito2);

#GRÁFICO 2: Con este gráfico buscamos entender si existen diferencias en los rasgos de personalidad entre hombres y mujeres. Tratando de aislar esta variable, (sin tener en cuenta toooooodo el enorme contexto cultural) podríamos decir que parece los rasgos más carácterísticos de los hombres se pagan más, vamos a ver cuáles son esos rasgos

etiquetas = ['extraversion', 'independ',
       'selfcontrol', 'anxiety', 'novator']

male = []
female = []

for etiqueta in etiquetas:
    group= turnover.groupby("gender")[f"{etiqueta}"].mean()
    male.append(group.values[1])
    female.append(group.values[0])

fig = go.Figure(data=[
    go.Bar(name='Male', x=etiquetas, y=male),
    go.Bar(name='Female', x=etiquetas, y=female)
])

fig.show()

#GRÁFICO 3: además, esta brecha salarial se incrementa dependiendo de la cultura del país donde (haciendo un salto lógico, se podrían incentivar algunos rasgos de personalidad

g = sns.barplot(x= 'paises', y ='% brecha salarial', data=puntito2)
g.set_xticklabels(
    labels=['Rusia', 'Sudáfrica', 'Malawi', 'Armenia', 'Reino_Unido',
       'Corea_del_Sur', 'Suiza', 'Países_Bajos', 'Nepal', 'Pakistán',
       'Bangladesh', 'Ecuador', 'Filipinas', 'Bulgaria', 'Rumanía',
       'Tailandia', 'Sierra_Leona', 'Panamá', 'Jordania', 'Cabo_Verde'], rotation=80);

