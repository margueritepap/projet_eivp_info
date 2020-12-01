premières_lignes=[['0;1;35.5;25.8;55.0;282;448;2019-08-11 17:48:06+02:00'], ['1;1;44.5;25.5;55.0;288;429;2019-08-11 18:03:03+02:00'],['2;1;34.5;25.5;55.0;286;417;2019-08-11 18:18:03+02:00'],['3;1;37.5;25.5;54.5;282;433;2019-08-11 18:33:03+02:00'], ['4;1;36.0;25.3;55.0;274;403;2019-08-11 18:48:03+02:00']]


[';id;noise;temp;humidity;lum;co2;sent_at']


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


G='id,noise,temp,humidity,lum,co2,sent_at'

def preleve_colonne(D,n): #prélève la colonne n du tableau D et la renvoie sous forme d'une liste (sans entete)
    l=len(D)
    a=D[0][0] #on sépare les entètes du reste du tableau
    b=[a.split(';')]
    c=float(b[0][n])
    S=[c]
    for k in range (1,l):
        a=D[k][0]
        b=[a.split(';')] #change les ; en ,
        c=float(b[0][n]) #change le str en chiffre
        S+=[c]
    return S



def preleve_dates(D,n):
    l=len(D)
    a=D[0][0] #on sépare les entètes du reste du tableau
    b=[a.split(';')]
    c=[b[0][n]]
    S=c
    for k in range (1,l):
        a=D[k][0]
        b=[a.split(';')] #change les ; en ,
        c=[b[0][n]]#change le str en chiffre
        S+=c
    return S



def indice_humidex(T,H):
    l=len(T)
    humi=[]
    for k in range (l):
        t=T[k]
        h=H[k]
        a=10**(7.5*t/(237.7+t))
        i=t+((5/9)*((6.112*a*h/100)-10))
        hum=round(i)
        humi+=[hum]
    return humi


def virgule(D): #remplace les ; par des ,
    l=len(D)
    A=[]
    n=0
    for k in range (l):
        i=D[k][0]
        n=i.replace(';',',')
        A+=[[n]]
    return A

def recup_date(L): #récupere la colonne de dates de L
    D=virgule(L)
    l=len(E)
    I=[]
    for k in range (l):
        i=D[k][0]
        e=i.split(',')
        I+=[e[7]]
    return I

A=['2019-08-11 17:48:06+02:00','2019-08-11 18:03:03+02:00']
def divise_dh(L): #sépare l'heure de la date
    R=recup_date(L)
    l=len(R)
    D=[]
    for k in range (l):
        h=R[k]
        a=h.split()
        D+=[a]
    return D

def preleve_jours(L): #prélève toutes les dates sans les horaires
    l=len(L)
    D=divise_dh(L)
    J=[]
    for k in range (l):
        J+=[D[k][0]]
    return J

def preleve_horaires(L):  #renvoie la liste des horaires
    l=len(L)
    D=divise_dh(L)
    H=[]
    for k in range (l):
        h=D[k][1]
        print(h)
        # T=h.split('+')
        # t=T[0]
        # H+=[t]
    return

B=['17:48:06', '18:03:03','18:18:03','18:33:03']

def timming(L):  #renvoie la liste des instants de mesure
    D=recup_date(L)
    H=preleve_horaires(D)
    l=len(H)
    t=0
    a=H[0].split(':')
    h=float(a[0]) #heure de la 1ere mesure
    m=float(a[1]) #minute de la 1ere mesure
    s=float(a[2]) #seconde de la 1ere mesure
    T=[] #liste des timmings de mesure
    hh=0
    mm=0
    ss=0
    jj=0
    for k in range (l):
        b=H[k].split(':')
        ss=round(float(b[2])-s) #pour chaque mesure on calcule à quel t elle a été réalisée si la première a été réalisée à t=0
        if ss<0:
            ss=ss+60
            mm=mm-1
        mm+=round(float(b[1])-m)
        if mm<0:
            mm=mm+60
            hh=hh-1
        hh+=round(float(b[0])-h)
        if hh>23:
            hh=0
            jj+=1
        sss=str(ss)
        mmm=str(mm)
        hhh=str(hh)
        jjj=str(jj)
        U=[jjj,hhh,mmm,sss]
        t=':'.join(U)
        T+=[t]
    return T


TE=[['7184;6;27.0;26.0;44.0;0;412;2019-08-18 06:01:20+02:00'], ['7185;6;27.0;26.0;44.0;0;397;2019-08-18 06:16:16+02:00'], ['7186;6;27.0;25.8;44.0;0;410;2019-08-18 06:31:16+02:00'], ['7187;6;27.0;25.8;44.0;0;408;2019-08-18 06:46:16+02:00'], ['7188;6;27.0;25.8;44.0;0;401;2019-08-18 07:01:17+02:00'], ['7189;6;27.0;25.8;44.5;0;405;2019-08-18 07:16:19+02:00'], ['7190;6;27.0;25.8;44.5;0;404;2019-08-18 07:31:17+02:00'], ['7191;6;31.5;25.8;44.5;2;410;2019-08-18 07:46:17+02:00'], ['7192;6;31.5;25.8;44.5;18;408;2019-08-18 08:01:18+02:00'], ['7193;6;36.5;25.8;44.5;64;410;2019-08-18 08:16:18+02:00'], ['7194;6;42.0;25.8;44.5;100;410;2019-08-18 08:31:19+02:00'], ['7195;6;43.5;25.8;45.0;144;430;2019-08-18 08:46:20+02:00'], ['7196;6;48.0;25.8;45.0;176;447;2019-08-18 09:01:21+02:00'], ['7197;6;46.5;25.8;45.0;184;463;2019-08-18 09:16:21+02:00']]



[';id;noise;temp;humidity;lum;co2;sent_at']

E=[['0;1;35.5;25.8;55.0;282;448;2019-08-11 17:48:06+02:00'], ['1;1;44.5;25.5;55.0;288;429;2019-08-11 18:03:03+02:00'],['2;1;34.5;25.5;55.0;286;417;2019-08-11 18:18:03+02:00'],['3;1;37.5;25.5;54.5;282;433;2019-08-11 18:33:03+02:00'], ['4;1;36.0;25.3;55.0;274;403;2019-08-11 18:48:03+02:00']]


def converti(L): #convertis le format YYYY-MM-DD HH:MM:SS+00:00 en [DD/MM/YYYY]
    return







def liste_teps(L):
    return





















