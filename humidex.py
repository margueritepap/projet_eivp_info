import pandas as pd
#import matplotlib.pyplot as plt
import csv
df=plt.reader_csv(r"C:\Users\mpapo\Downloads\EIVP_KM (1).csv",sep=';')
print(df)

#Humidex=Ta+5/9((6.112*10^(7.5*(Ta/(237.7+Ta)))*H/100)-10)
def indice_humidex (T,H):#prend en arguments la liste de Temp et de %Hum
    t=T[0]
    h=H[0]
    hum=[] #liste des indices humidex pour chaque paire temp/%humidité
    for k in range len(T):
        I=(log(t/100)+((17.27*t)/(237.3+t)))/17.27
        rosee=(237.3*I)/(1-I)
        hum+=t+0.5555*(6.11*exp(5417.753*(1/273.16-1/(273.15+rosee)))-10)
        t=T[k]
        h=H[k]
    return hum

