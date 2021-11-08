# Brecha salarial, personalidad y cultura
¿Qué? El presente proyecto tiene como objetivo tratar de profundizar y comprender la brecha salarial en función del país y la personalidad

¿Cómo? Dos documentos: (i) Csv de Kagle con información de profesionales de distintas empresas, con el detalle de su personalidad (ii) Web scraping de una web con información del porcentaje de brecha salarial en diferentes países   

¿Para qué? Para demostrar: (i) que existe brecha salarial oscilando entre un 5 y más de un 60%, (ii) que mujeres y hombres parece que no tienen los mismos rasgos de personalidad (iii) la cultura impacta de lleno en la brecha, generando una oscilación amplia en este indicador



### Librerías utilidazas
import requests

from bs4 import BeautifulSoup

import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

import plotly.express as px

import plotly.graph_objects as go
