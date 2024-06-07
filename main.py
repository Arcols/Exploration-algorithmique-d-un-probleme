from tracer_graphe import *
from tempsComparaison import *
from connexiteGraphe import *
from BellmanFord import *
from Djikstra import *

def main() :
    numeroExo=float(input("Veuillez rentrer le numéro de l'exercice voulu. \n Exemple: 6.1 pour obtenir le résultat des deux fonctions \"temps calcul\" \n"))
    if numeroExo==2.1 :
        matrice=graphe(4,1,5)
        choisirGraphe(matrice)
        print("Voici la matrice correspondant au graphe :\n",matrice,"\n")
    elif numeroExo==2.2 :
        matrice=graphe(5,1,5)
        G,labels=choisirGraphe(matrice)
        chemin(G, ['A','B','C'])
        print("Voici la matrice correspondant au graphe : \n",matrice,"\n")
        print("Voici le chemin emprunté : A --> B --> C \n")
    elif numeroExo==3.1 :
        n,a,b=demandeGraphe()
        print("Voici la matrice générée : \n",graphe(n,a,b),"\n")
    elif numeroExo==3.2 :
        n,a,b,p=demandeGraphe2()
        print("Voici la matrice générée : \n",graphe2(n,a,b,p),"\n")
    elif numeroExo==4.1 :
        n,a,b,p=demandeGraphe2()
        matrice=graphe2(n,a,b,p)
        print("Voici la matrice sur laquelle l'algorithme de Dijkstra sera appliqué avec pour sommet de départ A : \n",matrice,"\n")
        dijkstra(matrice,0,True)
    elif numeroExo==4.2 :
        n,a,b,p=demandeGraphe2()
        matrice=graphe2(n,a,b,p)
        print("Voici la matrice sur laquelle l'algorithme de Bellman-Ford sera appliqué avec pour sommet de départ A : \n",matrice,"\n")
        Bellman_Ford(matrice,0,parcoursLargeur(matrice),True)
    elif numeroExo==5 :
        n,a,b,p=demandeGraphe2()
        testItérations(0,n,a,b,p)
    elif numeroExo==6.1 :
        n=int(input("Veuillez rentrer la taille du graphe voulu.\n"))
        p=float(input("Veuillez rentrer la proportion de flèches du graphe voulu.\n"))
        print("Djikstra a pris",TempsDij(n,p)/10**9,"secondes a trouver le plus courts chemin de tous les sommets avec un graphe de taille",n,"et de",p*100,"%"" de fleches \n")
        print("Bellman-Ford a pris",TempsBF(n,p)/10**9,"secondes a trouver le plus courts chemin de tous les sommets avec un graphe de taille",n,"et de",p*100,"%"" de fleches \n")
    elif numeroExo==6.2 :
        p=float(input("Veuillez rentrer la proportion de flèches du graphe voulu.\n Si vous désirez obtenir 1/n de probabilité de flèches, insérez -1\n"))
        complexite(p)
    elif numeroExo==7 :
        n=int(input("Veuillez rentrer la taille du graphe voulu.\n"))
        p=float(input("Veuillez rentrer la proportion de flèches du graphe voulu.\n"))
        matrice=graphe0(n,1,2,p)
        print("Voici la matrice de votre graphe : \n",matrice)
        if fc(matrice) :
            print("Votre graphe est fortement connexe\n")
        else :
            print("Votre graphe n'est pas fortement connexe\n")
    elif numeroExo==8 :
        n=int(input("Veuillez rentrer la taille du graphe voulu.\n"))
        forteConnexite=teststatfc(n)
        if forteConnexite>=0.99 :
            print("Votre graphe est fortement connexe avec une probabilité de 50""%"" de flèches, il a obtenu un taux de",forteConnexite*100,"%\n")
        else :
            print("Votre graphe n'est pas fortement connexe avec une probabilité de 50""%"" de flèches, il a obtenu un taux de",forteConnexite*100,"%\n")
    elif numeroExo==9 :
        n=int(input("Veuillez rentrer la taille du graphe voulu.\n"))
        p=float(input("Veuillez rentrer la proportion de flèches du graphe voulu.\n"))
        forteConnexite=teststatfc2(n,p)
        if forteConnexite>=0.99 :
            print("Votre graphe est fortement connexe avec une probabilité de",p*100,"%"" de flèches, il a obtenu un taux de",forteConnexite*100,"%\n")
        else :
            print("Votre graphe n'est pas fortement connexe avec une probabilité de",p*100,"%"" de flèches, il a obtenu un taux de",forteConnexite*100,"%\n")
        print("La prochaine opération peut prendre du temps, Veuillez patienter\n")
        s=seuil(n)
        print("Le seuil de forte connexité de votre graphe est de :",int(s*100),"\n")
    elif numeroExo==10.1 :
        a=int(input("Veuillez rentrer la borne inférieure (a) de l'intervalle du nombre de sommets de vos graphes.\n"))
        b=int(input("Veuillez rentrer la borne supérieure (exclue) (b) de l'intervalle du nombre de sommets de vos graphes.\n"))
        print("La prochaine opération peut prendre du temps, Veuillez patienter\n")
        print("Des messages de chaque seuils vont être afficher pour vous montrer votre progression au fil du temps")
        values = np.arange(a,b)
        representationGraphiqueSeuil(values)
    else :
        print("Exercice introuvable, veuillez insérer un numéro correct")

def demandeGraphe2() :
    n=int(input("Veuillez rentrer la taille du graphe voulu.\n"))
    a=int(input("Veuillez rentrer la borne inférieure (a) des poids de votre graphe.\n"))
    b=int(input("Veuillez rentrer la borne supérieure (exclue) (b) des poids de votre graphe.\n"))
    p=float(input("Veuillez rentrer la proportion (p) de fleches dans votre graphe.\n"))
    return n,a,b,p

def demandeGraphe() :
    n=int(input("Veuillez rentrer la taille du graphe voulu.\n"))
    a=int(input("Veuillez rentrer la borne inférieure (a) des poids de votre graphe.\n"))
    b=int(input("Veuillez rentrer la borne supérieure (exclue) (b) des poids de votre graphe.\n"))
    return n,a,b

main()