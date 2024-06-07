from tracer_graphe import graphe2,nomSommet
inf = float('inf')
import numpy as np

def dijkstraParSommet(matrice,sommetDepart):
    
    #Definition des variables et de la constante 'dimensionMatrice'
    dimensionMatrice = matrice.shape[0]
    
    ligneActuelle = 0
    colonneActuelle = 0
    
    
    distanceSommetDepart = matrice[sommetDepart]
    dernierSommet = list()
    chemins = list()
    
    ####################################################################################
    
    #Initialisation
    
    
    for i in range(dimensionMatrice):
        dernierSommet.append(sommetDepart)
        
        chemins.append(list())
        chemins[i].append(i)
        
    distanceSommetDepart[sommetDepart]=float('inf')
    
    ####################################################################################
  
    #Parcourt en ligne
    while ligneActuelle<dimensionMatrice:
        
        colonneActuelle=0
        
        #Parcourt en colonne
        while colonneActuelle<dimensionMatrice:
            
            if colonneActuelle!=sommetDepart:
                if distanceSommetDepart[ligneActuelle]+matrice[ligneActuelle][colonneActuelle]<distanceSommetDepart[colonneActuelle]:
                    distanceSommetDepart[colonneActuelle]= distanceSommetDepart[ligneActuelle]+matrice[ligneActuelle][colonneActuelle]
                    dernierSommet[colonneActuelle]=ligneActuelle
            
            colonneActuelle+=1

        ligneActuelle+=1
     
    for i in range(dimensionMatrice):
        if i != sommetDepart:
            if distanceSommetDepart[i]==float('inf'):
                dernierSommet[i]=None
    
    for i in range (dimensionMatrice):
        sommetPrecedent=dernierSommet[i]
        if chemins[i][-1]!=sommetDepart:
            if dernierSommet[i]==None:
                chemins[i]=list()
            else:  
                if dernierSommet[i]==sommetDepart:
                    chemins[i].append(dernierSommet[i])
                else:
                    while chemins[i][-1]!=sommetDepart:
                        sommetPrecedent=dernierSommet[sommetPrecedent]
                        chemins[i].append(sommetPrecedent)
                    
    
    return chemins,distanceSommetDepart

def dijkstra(matrice, sommetDepart,affichage):
    """
    In : List (matrice)
         int (indice sommetDepart)
         Boolean (true,affichage ok)
    """
    chemins,distance = dijkstraParSommet(matrice, sommetDepart)
    if affichage :
        for i in range(len(chemins)) :
            if i!=sommetDepart :
                if distance[i]!= inf :
                    string=""
                    for j in chemins[i] :
                            if j==sommetDepart :
                                string+=nomSommet(j)+" De poids : "+str(distance[i])
                            else :
                                string+=nomSommet(j)+" <-- "
                    print(string)
                else :
                    print("Sommet ",nomSommet(i)," non joignable")
