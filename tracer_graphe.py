import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
inf = float('inf')

def choisirGraphe(matrice):
    labels = {}
    if(estGrapheNonOrienté(matrice)):
        G,labels=créerGrapheNonOrienté(matrice)
        afficherGraphe(G, labels)
    else :
        G,labels = créerGrapheOrienté(matrice)
        afficherGraphe(G, labels)
    return G,labels

def nomSommet(x):
    return chr(x+65)


def graphe2(n, a, b, p):
    """
    Créer la matrice
    In :    n (int / taille matrice)
            a (int / premier poid matrice)
            b (int / deuxieme poid matrice)
            p (float / proportion de fleche matrice)
            
    Out : List (Matrice du graphe)
    """
    taille = n * n
    nb_zeros = int(taille*(1-p))
    nb_autres = taille - nb_zeros
    poids = [inf] * nb_zeros + np.random.randint(a, b, nb_autres).tolist() # poids aléatoires des indices la matrice
    np.random.shuffle(poids)
    matrice = np.array(poids).reshape(n, n)
    matrice = matrice.astype('float64')  
    return matrice


def graphe(n, a, b):
    """
    Créer la matrice
    In :    n (int / taille matrice)
            a (int / premier poid matrice)
            b (int / deuxieme poid matrice)
            
    Out : List (Matrice du graphe)
    """
    taille = n * n
    nb_zeros = int(taille*(0.5))
    nb_autres = taille - nb_zeros
    poids = [inf] * nb_zeros + np.random.randint(a, b, nb_autres).tolist() # poids aléatoires des indices la matrice
    np.random.shuffle(poids)
    matrice = np.array(poids).reshape(n, n)
    matrice = matrice.astype('float64')  
    return matrice


def estGrapheNonOrienté(matrice):
    """
    Vérifie si un graphe est orienté ou non
    In : Matrice carrée , Expl : M = [[1,0,0],
                                      [0,0,0],
                                      [0,0,0]]
    Out : Boolean

    Expl : M = [[1,0,0],
                [0,0,0],
                [0,0,0]]
            Return False
    """
    for indiceSommet in range(len(matrice)) : 
        for indiceArrette in range(len(matrice)) :
            if matrice[indiceSommet][indiceArrette] != matrice[indiceArrette][indiceSommet]:
                return False
    return True

def créerGrapheNonOrienté(matrice):
    """
    Créer un graphe non orienté et l'affiche
    In : Matrice carrée , Expl : M = [[1,0,0],
                                      [0,0,0],
                                      [0,0,0]]
    Out : Graph (G) , List[Dict,Dict] (Labels)
    """
    # On crée un graphe vide
    G= nx.Graph()
    G.add_nodes_from([nomSommet(i) for i in range(len(matrice))]) # Ajout  des sommets
    labels={}
    indiceSommet=0
    for sommet in matrice : # Parcourt la matrice pour prendre chaque sommet
        indiceArrette=0     # Initialise la premire arrête de chaque sommet
        for indice in sommet : # Parcourt chaque sommet pour prendre chaque arrete et vérifier si il y bien une arrete 
            if indiceArrette >= indiceSommet :
                if not np.isinf(indice) : # Vérifie si une arrete doit etre tracée
                    G.add_edge(nomSommet(indiceSommet),nomSommet(indiceArrette)) # Trace l'arrête
                    labels[(nomSommet(indiceSommet),nomSommet(indiceArrette))]=str(indice) # Ajout du poids à l'arrete
            indiceArrette+=1
        indiceSommet+=1
    return G,labels


def créerGrapheOrienté(matrice):
    """
    Créer un graphe orienté et l'affiche
    In : Matrice carrée , Expl : M = [[1,0,0],
                                      [0,0,0],
                                      [0,0,0]]
    Out : Graph (G) , List[Dict,Dict] (Labels)
    """
    G= nx.DiGraph()
    G.add_nodes_from([nomSommet(i) for i in range(len(matrice))]) # Ajout  des sommets
    labels={}
    indiceSommet=0
    for sommet in matrice : # Parcourt la matrice pour prendre chaque sommet
        indiceArrette=0     # Initialise la premire arrête de chaque sommet
        for indice in sommet : # Parcourt chaque sommet pour prendre chaque arrete et vérifier si il y bien une arrete 
            if not np.isinf(indice) : # Vérifie si une arrete doit etre tracée
                G.add_edge(nomSommet(indiceSommet),nomSommet(indiceArrette)) # Trace l'arrête
                labels[(nomSommet(indiceSommet),nomSommet(indiceArrette))]=str(indice) # Ajout du poids à l'arrete
            indiceArrette+=1
        indiceSommet+=1
    return G,labels


def chemin(G,lst):
    """
    Affiche un chemin donné dans un graphe en rouge 
    In :    Graph (G)
            List[Str] (noms des sommets du chemin) 
    """
    pos = nx.spring_layout(G)
    H = nx.create_empty_copy(G)
    # Créer les chemins voulus
    for i in range(len(lst)-1):
        H.add_edge(lst[i],lst[i+1],color='red')
    # Superpose les deux graphes
    R = nx.compose(G,H)
    # Met toutes les arretes du chemin voulu en rouge les autres en noir
    edge_colors = ['red' if edge in H.edges() else 'black' for edge in R.edges()]
    nx.draw(R,
            edge_color=edge_colors,
            connectionstyle='arc3,rad=0.2',
            node_color= 'yellow',  
            node_size= 500,
            with_labels=True)
    
    plt.show()


def afficherGraphe(G,labels):
    """
    Affiche un graphe donné
    In :    Graph (G), 
            List[Dict,Dict] (poid des arretes)
    """
    pos = nx.spring_layout(G)
    nx.draw(G,pos, with_labels=True , 
            connectionstyle='arc3,rad=0.1',
            node_color= 'yellow',  
            node_size= 500,         
            edge_color= 'tab:blue')
    for edge, label in labels.items():
        x1, y1 = pos[edge[0]]
        x2, y2 = pos[edge[1]]
        x = (x1 + x2) / 2
        y = (y1 + y2) / 2
        # Calcule l'angle des arretes
        angle = np.arctan2(y2 - y1, x2 - x1)
        # Ajout d'un petit décalage entre les positions
        offset_x = 0.1 * np.cos(angle + np.pi/2)
        offset_y = 0.1 * np.sin(angle + np.pi/2)
        plt.text(x - offset_x, y - offset_y, label, fontsize=10, ha='center', va='center', bbox=dict(facecolor='white', alpha=0.8))
    plt.show()

