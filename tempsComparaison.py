import os
import time
import matplotlib.pyplot as plt
from tracer_graphe import graphe2
from Djikstra import dijkstra
from BellmanFord import *
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def TempsBF(n,p):
    M=graphe2(n,0,50,p)
    parcours=parcoursLargeur(M,0)
    debut = time.perf_counter_ns()
    Bellman_Ford(M,0,parcours,False)
    fin = time.perf_counter_ns()
    duree = fin - debut
    return duree

def TempsDij(n,p):
    M=graphe2(n,0,50,p)
    debut = time.perf_counter_ns()
    dijkstra(M,0,False)
    fin = time.perf_counter_ns()
    duree = fin - debut
    return duree

# Calculer les moyennes des durées pour chaque valeur de n
def average_duration(func, n,p, num_tests=100):
    durations = []
    for _ in range(num_tests):
        start_time = time.perf_counter_ns()
        func(n,p)
        end_time = time.perf_counter_ns()
        durations.append(end_time - start_time)
    return sum(durations)/num_tests 

def complexite(p) : 
     # Générer les valeurs de n
    n_values = range(2, 201) 
    if p==-1 :
        temps_dij = [average_duration(TempsDij, n,1/n) for n in n_values]
        temps_bm = [average_duration(TempsBF, n,1/n) for n in n_values]
    else :
        temps_dij = [average_duration(TempsDij, n,p) for n in n_values]
        temps_bm = [average_duration(TempsBF, n,p) for n in n_values]
    # Tracer les courbes
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, temps_dij, label='TempsDij(n)', color='blue')
    plt.plot(n_values, temps_bm, label='TempsBM(n)', color='red')
    plt.xlabel('n')
    plt.ylabel('Durée (nano secondes)')
    plt.title('Représentations des fonctions TempsDij(n) et TempsBM(n) avec moyennes sur 100 essais')
    plt.legend()
    plt.grid(True)
    plt.show()

