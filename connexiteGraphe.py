from matplotlib import pyplot as plt
import numpy as np
inf = float('inf')

def graphe0(n, a, b, p):
    """
    Créer la matrice avec des 0 ou 1
    In :    n (int / taille matrice)
            a (int / premier poid matrice)
            b (int / deuxieme poid matrice)
            p (float / proportion de fleche matrice)
            
    Out : List (Matrice du graphe)
    """
    taille = n * n
    nb_zeros = int(taille*(1-p))
    nb_autres = taille - nb_zeros
    poids = [0] * nb_zeros + np.random.randint(a, b, nb_autres).tolist() # poids aléatoires des indices la matrice
    np.random.shuffle(poids)
    matrice = np.array(poids).reshape(n, n)
    return matrice 

def Red(M):  # Fonction Réduction qui met les coefficients non nuls de M à 1
    N = np.copy(M)
    N[N != 0] = 1
    return N

def Trans(M):
    k = np.shape(M)[0]  # Nombre de lignes du tableau M
    N = np.copy(M)      # Initialisation de la fermeture transitive avec la matrice d'adjacence
    P = np.copy(M)      # Initialisation des puissances de M
    for i in range(k-1):
        P = Red(np.dot(P, M))  # P = M^(i+1)
        N = Red(N + P)         # Fermeture transitive avec réduction
    return N

def fc(M) :
    N=Trans(M)
    boolean=True
    for i in range(len(N)):
        for j in range(len(N)):
            if N[i][j]==0 :
                boolean=False
    return boolean   

def teststatfc(n) :
    compteur=0
    for i in range(1000) : #On va tester la connexité d'un graphe à n sommet sur 1000 graphes distincts
        M=graphe0(n, 1, 2, 0.5)
        if fc(M) :
            compteur+=1
    return compteur/1000

def teststatfc2(n,p):
    compteur=0
    for i in range(1000) : #On va tester la connexité d'un graphe à n sommet sur 1000 graphes distincts
        M=graphe0(n, 1, 2, p)
        if fc(M) :
            compteur+=1
    return compteur/1000

def seuil(n):
    p_values = np.arange(0.1, 1.0, 0.01)[::-1]
    for p in p_values:
        if teststatfc2(n, p) < 0.99:
            return p+0.01
    return -1

def representationGraphiqueSeuil(values):
    listeSeuil=[]
    for n in values :
        x=seuil(n)
        listeSeuil.append(x)
        print("seuil pour ",n,": ",x)
    plt.figure(figsize=(10, 6))
    plt.plot(values, listeSeuil, label='Seuil de connexité du graphe en fonction du nombre de sommet', color='blue')
    plt.xlabel('Taille n du graphe')
    plt.ylabel('Seuil de forte connexité')
    plt.title('Seuil de forte connexité d\'un graphe à n sommet')
    plt.legend()
    plt.grid(True)
    plt.show()