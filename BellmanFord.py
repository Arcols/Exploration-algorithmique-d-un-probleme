import numpy as np
import json
import time
from tracer_graphe import graphe2

inf = float('inf')


def listBellManFordEquals(list1, list2):
    """
    Compare deux listes entre elles savoir si elles sont égales
    In : list*2
    Out : Boolean 
    """
    # Convertir chaque dictionnaire en une chaîne JSON triée pour comparaison
    sorted_list1 = sorted(json.dumps(item, sort_keys=True) for item in list1)
    sorted_list2 = sorted(json.dumps(item, sort_keys=True) for item in list2)
    
    return sorted_list1 == sorted_list2

def accesDistance(L,d): # renvoie la distance du sommet d dans la liste de dictionnaires L
    """
    In : L - Liste distance (expl dans algoBel)
        d - nom sommet
    """
    return L[d][nomSommet(d)]['dist']

def accesValeurFleche (M,t) :    # renvoie la valeur de l'arrête du tuple t dans la matrice M
    """
    In : Matrice
        Tuple (i,j) indices de l'arrete
    Out : Nombre à l'indice i,j dans M
    """
    return M[t[0]][t[1]]

def additionDistance(Ld,arrete, M) :        # additionne la distance du sommet de départ avec la valeur de l'arrête
    """
    In : Ld / Lp Ex dans les autres fonctions
        
    """
    return accesDistance(Ld,arrete[0]) + accesValeurFleche(M,arrete)

def nomSommet(x):       # renvoie le char du sommet (0 = A, 1 = B,...)
    return chr(x+65)

def copie(liste):
    """
    Fonction pour copier une liste afin d'éviter que la liste copiée ait un pointeur sur la liste d'origine
    IN : List[Dict{Dict}]
    OUT : Copied List
    """
    listeAux=[]
    for sommet in liste:
        dictSommet = {}
        for key, values in sommet.items():
            dictDistAnt = {}
            for keyDA, valDA in values.items():
                dictDistAnt[keyDA] = valDA
            dictSommet[key] = dictDistAnt
        listeAux.append(dictSommet)
    return listeAux

def initialisationBellman_Ford(M,d):    # initialisation de l'algorithme
    n = len(M)  # longueur de la matrice
    L = []
    for i in range(n) :     # pour chaque sommet
        dicoaux={nomSommet(i):{'dist':float('inf'),'ant':None}}     # autres sommets : distance = inf, pas d'antécédent
        L.append(dicoaux)
    L[d][nomSommet(d)]['dist']=0      # sommet de départ : distance = 0, pas d'antécédent
    return L

def parcoursProfondeur(M,s):
    n=len(M)       # taille du tableau = nombre de sommets
    couleur={}     # On colorie tous les sommets en blanc et s en vert
    for i  in range(n):
        couleur[i]='blanc'
    couleur[s]='vert'
    pile=[s]       # on initialise la pile à s
    Resultat=[s] # on initialise la liste des résultats à s
    
    while pile !=[]: # tant que la pile n'est pas vide,
        i=pile[-1]          # on prend le dernier sommet i de la pile
        Succ_blanc=[]       # on crée la liste de ses successeurs non déjà visités (blancs)
        for j in range(n):
            if (M[i][j]!=inf and couleur[j]=='blanc'):
                Succ_blanc.append(j)
        if Succ_blanc!=[]:  # s'il y en a,
            v= Succ_blanc[0]    # on prend le premier (si on veut l'ordre alphabétique)
            couleur[v]='vert'   # on le colorie en vert, 
            pile.append(v)      # on l'empile
            Resultat.append(v)  # on le met en liste rsultat
        else:               # sinon:
            pile.pop()          # on sort i de la pile
    return parcours(M,Resultat)

def parcoursLargeur(M,s):
    n=len(M)
    couleur={}     # On colorie tous les sommets en blanc et s (départ) en vert
    for i  in range(n):
        couleur[i]='blanc'
    couleur[s]='vert'
    file=[s]
    Parcours=[s]
    while file !=[]:
        i=file[0]           # on prend le premier terme de la file
        for j in range(n):  # On enfile les successeurs de i encore blancs:
            if (M[file[0]][j]!=inf and couleur[j]=='blanc'):
                
                file.append(j)
                couleur[j]='vert' # On les colorie en vert (sommets visités)
                Parcours.append(j) # On les place dans la liste Resultat
        file.pop(0) # on défile i (on retire le premier élément)
    return parcours(M,Parcours)

def parcoursAleatoire(M,s) :
    L=[]
    for i in range(len(M)) :
        L.append(i) # On construit notre Liste de sommet
    L.pop(s) # On supprime de notre liste le sommet de départ
    np.random.shuffle(L)
    
    return parcours(M,[s]+L)

def parcours(M, p):
    """
    Cette fonction va prendre en parametre une liste d'un parcours et va retourner les parcours avec les différentes fleches
    In : M : matrice
        p : list (Ex. [3, 0, 2, 1])
    Out : List(tuple) (Ex. [(3, 0), (3, 2), (0, 3), (0, 1), (2, 0), (1, 2)] )
    """
    fleches = []

    # Créer une liste de toutes les fleches
    for i in range(len(p)):
        for j in range(len(M[p[i]])):
            if M[p[i]][j] != inf:  
                fleches.append((p[i], j))

    # Trier les fleches selon l'ordre des sommets dans la liste p
    order_dict = {val: idx for idx, val in enumerate(p)}
    fleches.sort(key=lambda x: (order_dict[x[0]], order_dict.get(x[1], float('inf'))))
    return fleches


def algoBellman_Ford (M,Ld,Lp) :       # modifie la liste de dictionnaires ListeDistance en actualisant la distance la plus courte
    """
    IN : M - Matrice
        Ld - Liste Distance Ex. Ld=[{'A': {'dist': inf, 'ant': None}},
                                    {'B': {'dist': inf, 'ant': None}},
                                    {'C': {'dist': 0, 'ant': None}},
                                    {'D': {'dist': inf, 'ant': None}},
                                    {'E': {'dist': inf, 'ant': None}},
                                    {'F': {'dist': inf, 'ant': None}}] 
        Lp - Liste Parcours Ex. Lp=[(0, 1), (0, 4), (1, 0), (1, 2), (1, 3), (2, 1), (2, 5), (3, 1), (3, 4), (4, 0), (4, 3), (4, 5), (5, 2), (5, 4)] 
                                    tuples qui représente les arrêtes
    """
    for arrete in Lp :
        if additionDistance(Ld,arrete,M) < accesDistance(Ld,arrete[1]) : # on vérifie que la somme du sommet de départ et de l'arrête soit inférieure au sommet d'arrivée
            nomSommetArrivee=nomSommet(arrete[1])
            indiceSommetArrivee=arrete[1]
            Ld[indiceSommetArrivee][nomSommetArrivee]['dist'] = additionDistance(Ld,arrete,M)   # actualisation de la distance
            Ld[indiceSommetArrivee][nomSommetArrivee]['ant'] = nomSommet(arrete[0])     # actualisation de l'antécédent 

def itinéraireBellman_Ford(Ld,sommet,d,mat) : 
    """
    Renvoie l'itinéraire le plus court d'un sommet donné
    IN : Ld Liste distance, int (indice du sommet d'arrivé voulu), int (indice du sommet de départ de l'algorithme)
    OUT : STR
    """ 
    chemin=nomSommet(d)+" --> "
    Ant = Ld[sommet][nomSommet(sommet)]['ant'] # on récupère l'antécédent du sommet
    taille=0
    while Ant != nomSommet(d) and taille<=len(mat):     # on cherche l'antécédent à chaque fois jusqu'à arriver au sommet de départ
        indiceLettre=ord(Ant)-65
        chemin+=Ant+" --> "       # ajout du sommet dans la liste
        Ant = Ld[indiceLettre][Ant]['ant']   # on prend l'antécédent de l'antécédent
        taille+=1
    chemin+=nomSommet(sommet)
    if taille>=len(mat) :
        return []
    else :
        return chemin



def Bellman_Ford(M,d,listeParcours,affichage) :
    """
    In : M - Matrice
        d - nom sommet (0 = A , 1 = B , ...)
        p - parcours à emprunter ([(3, 0), (3, 2), (0, 3), (0, 1), (1, 2), (2, 0)])
        affichage - Boolean (true si on veut l'afficher false sinon)
    """
    listeDistance=initialisationBellman_Ford(M,d)   # liste des dictionnaires des sommets
    listePre=[]      # on utilise listePre pour comparer la liste actuelle de la liste précédente
    compteur=0
    for _ in range(len(M)) :     # on fait l'algorithme au maximum n-1 fois (n = taille de la matrice)
        algoBellman_Ford(M,listeDistance,listeParcours)
        compteur+=1
        if listBellManFordEquals(listePre,listeDistance) :
            break       # on arrète la boucle si la liste des dictionnaires ne change pas
        listePre=copie(listeDistance)  # on passe au suivant
        
    if affichage : 
        affichageBellman_Ford(M,d,listeDistance,listeParcours)
    return compteur+1 # On rajoute 1 car dans l'affichage on refait une fois l'algorithme

def affichageBellman_Ford(M,d,Ld,Lp) :
    listeAux=copie(Ld)
    print("Le plus court chemin en partant du sommet ",nomSommet(d)," pour chaque sommet est : \n")
    algoBellman_Ford(M,listeAux,Lp)
    for i in range(len(Ld)) :
        if i!=d :
            if Ld[i][nomSommet(i)]['dist']==inf :
                print("Le sommet ", nomSommet(i)," est injoignable")
            elif Ld[i][nomSommet(i)]['dist'] != listeAux[i][nomSommet(i)]['dist'] :
                print("Le sommet ", nomSommet(i)," est joignable depuis d par un chemin , mais pas de plus court chemin")
            else :
                if itinéraireBellman_Ford(Ld,i,d,M)==[] :
                    print("Le sommet ", nomSommet(i)," est joignable depuis d par un chemin , mais pas de plus court chemin")
                else :
                    print("Pour le sommet ",nomSommet(i)," on parcourt ",Ld[i][nomSommet(i)]['dist']," par cet itinéraire : ", itinéraireBellman_Ford(Ld,i,d,M))

def testItérations(s,nbSommet,a,b,p):
    totalAleatoire=0
    totalLargeur=0
    totalProfondeur=0
    for i in range(10) :
        M=graphe2(nbSommet,a,b,p)

        cA=Bellman_Ford(M,s,parcoursAleatoire(M,s),False)

        totalAleatoire+=cA

        cL=Bellman_Ford(M,s,parcoursLargeur(M,s),False)

        totalLargeur+=cL

        cP=Bellman_Ford(M,s,parcoursProfondeur(M,s),False)

        totalProfondeur+=cP

    print("\n \n \n")
    print("Pour 10 graphes distincts de taille "+str(nbSommet)+", le nombre d'itérations de l'algorithme de BellmanFord sur les différents parcours sont : \n Parcours aléatoire : " + str(totalAleatoire)+"\n Parcours Largeur : "+ str(totalLargeur)+"\n Prcours Profondeur : "+str(totalProfondeur))

