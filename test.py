


premières_lignes=[[';id;noise;temp;humidity;lum;co2;sent_at'], ['0;1;35.5;25.8;55.0;282;448;2019-08-11 17:48:06+02:00'], ['1;1;44.5;25.5;55.0;288;429;2019-08-11 18:03:03+02:00'],['2;1;34.5;25.5;55.0;286;417;2019-08-11 18:18:03+02:00'],['3;1;37.5;25.5;54.5;282;433;2019-08-11 18:33:03+02:00'], ['4;1;36.0;25.3;55.0;274;403;2019-08-11 18:48:03+02:00']]





def lister(D): #remplace les ; par des ,
    l=len(D)
    A=[]
    n=0
    for k in range (l):
        i=D[k][0]
        n=i.replace(';',',')
        A+=[[n]]
    return A

def extraire_colonne(D,n): #extrait la colonne n du fichier D
    L=lister(D)
   # l=len(L)
    C=[]
    for k in range (l):
        C+=[L[k][n]]
        print (C)
    return C


T='id,noise,temp,humidity,lum,co2,sent_at'


def preleve_colonne(D,n): #prélève la colonne n du tableau D
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







