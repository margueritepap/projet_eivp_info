## Importation des données du csv sur Python
#Importer les données
import pandas as pd #biblio pandas: pour lire les données et pouvoir les traiter
import requests # permet de faire des requetes html en python
import io #permet de gérer les str


url = "https://raw.githubusercontent.com/margueritepap/projet_eivp_info/main/donnees.csv" # prend le fichier csv depuis git
download = requests.get(url).content #le télécharge

df = pd.read_csv(io.StringIO(download.decode('utf-8'))) #lis le contenu du fichier et le change en données exploitables par pandas (dataframe=df)


# print (df) #affiche toutes les données du fichier
#Séparer et convertir les données en listes exploitables

donnees_lignes = df.values.tolist()
tete=df.columns.values.tolist()
print (donnees_lignes)
print(tete)

#On doit maintenant remplacer les ; par des ,
#obsolète
def virgule(D): #remplace les ; par des ,
    l=len(D)
    A=[]
    n=0
    for k in range (l):
        i=D[k][0]
        n=i.replace(';',',')
        A+=[[n]]
    return A

def preleve_colonne(D,n): #prélève la colonne n du tableau D et la renvoie sous forme d'une liste
    l=len(D)
    a=D[0][0] #on sépare les entètes du reste du tableau
    b=[a.split(';')]
    c=b[0][n]
    S=[c]
    for k in range (1,l):
        a=D[k][0]
        b=[a.split(';')] #change les ; en ,
        c=float(b[0][n]) #change le str en chiffre
        S+=[c]
    return S


## Evolution d’une variable en fonction du temps
#Convertir
## Calcul des valeurs statistiques
from math import * #pour le calcul de l'écart type

def min(L):
    m=L[0]
    for k in range (len(L)):
        t=L[k]
        if t<m:
            m=t
    return m

def max(L):
    m=L[0]
    for k in range (len(L)):
        t=L[k]
        if t>m:
            m=t
    return m

def moyenne(L):
    l=len(L)
    m=0
    for k in range (l):
        m+=L[k]
    return m/l

def mediane(L):
    l=len(L)
    m=int(l%2) #parité du nb d'éléments de la liste
    if l!=0:
        if m==0: #si nb pair d'éléments
            i=int(l/2)
            mo=(L[i-1]+L[i+1])/2
            return int(mo)
        else: #si nb impaire d'éléments
            i=int((l-1)/2)
            return L[i]
    return "La liste est vide"

def variance(L):
    moy=moyenne(L)
    V=0
    l=len(L)
    if l!=0:
        for k in range (l):
            V+=(L[k]-moy)**2
        return V/l
    else:
        return "La liste est vide"

def ecart_type(L):
    v=variance(L)
    return sqrt(v)

## Calcul de l'indice “humidex”
#Extraction des températures et des taux d'humidité


#Fonction de calcul de humidex
def indice_humidex (T,H):#prend en arguments la liste de Temp et de %Hum
    t=T[0]
    h=H[0]
    hum=[] #liste des indices humidex pour chaque paire temp/%humidité
    for k in range (len(T)):
        I=(log(t/100)+((17.27*t)/(237.3+t)))/17.27
        rosee=(237.3*I)/(1-I)
        hum+=t+0.5555*(6.11*exp(5417.753*(1/273.16-1/(273.15+rosee)))-10)
        t=T[k]
        h=H[k]
    return hum

## Calcul de l’indice de corrélation entre un couple de variables

#Calcul du coeff de corrélation linéaire de Bravais-Pearson
def covariance (A,B): #Cov(A,B)
    l=len(A)
    if l!=0:
        c=0
        ma=moyenne(A)
        mb=moyenne(B)
        for k in range (l):
            c+=(A[k]-ma)*(B[k]-mb)
        return c/l
    return "La liste est vide"

def indice_correlation_Barvais_Pearson(A,B): #pour les valeurs régulières, peut atteindre ses limites en cas d'irrégularité
    ea=ecart_type(A)
    eb=ecart_type(B)
    cov=covariance(A,B)
    return cov/(ea*eb)

#Calcul de l'indice de corrélation de Spearman:

#pour des valeurs qui présentent des irrégularités, permet de mettre en évidence une relation non lénaire
def tri_rapide(L):
    if L==[]:
        return L
    L_g=[]
    L_d=[]
    for i in range(1,len(L)):
        if L[i]<=L[0]:
            L_g.append(L[i])
        else:
            L_d.append(L[i])
    return tri_rapide(L_g)+[L[0]]+tri_rapide(L_d)

def rang(a,L): #donne le rang de la première apparaition l'élément a dans la liste L
    T=tri_rapide(L)
    for k in range (len(L)):
        if a==L[k]:
            return k+1
    return "Cet élément n'est pas dans la liste"


def liste_rang(L): #renvoie la liste des rangs des éléments de L
    T=tri_rapide(L)
    r=0
    l=len(L)
    LR=[]
    for k in range (l):
        LR+=[rang(L[k],T)]
    return LR

def indice_correlation_Spearman(A,B):
    LA=liste_rang(A)
    LB=liste_rang(B)
    ea=ecart_type(LA)
    eb=ecart_type(LB)
    cov=covariance(LA,LB)
    return cov/(ea*eb)













