#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      cagibi
# programme lisant un csv de fxdata, , filtre la premiere colonne qui contient la date et heure qu'on ne va pas decoder, et ensuite applique une moyenne mobile sur les open
# avant de l'afficher
#
# Created:     27/07/2014
# Copyright:   (c) cagibi 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


from numpy import genfromtxt
import numpy as np


# ============== on lit le csv ========================
def fxreadcsv(filename):
    stockFile=[]

    with open(filename) as f:
        for eachLine in f:
            splitLine = eachLine.split(';')
    #        if len(splitLine)==6:    # test si la ligne a le bon nb de valeurs
    #             if 'values' not in eachLine:
            stockFile.append(';'.join(splitLine[1:])) #regenere la liste ssans le premier champ
    del f

    # un print pour voir
    print stockFile[:10]

    opennp, highp,lowp, closep,volume = np.loadtxt(stockFile,delimiter=';', unpack=True)
    del stockFile

    return opennp, highp,lowp, closep,volume
# un print pour voir
#print closep[:10]



# ===================  generateur de window  ===================================
from collections import deque

def window(seq, n=5):
    it = iter(seq)
    win = deque((next(it, None) for _ in xrange(n)), maxlen=n) # cree la deque
    yield win    #yield
    append = win.append
    for e in it:
        append(e) #a chaque iteration on append le suivant (la limite est fixee par maxlen)
        yield win

# ==================== fonctions sur les fenetres ============================
calcul d'average sur 5 pts avec avec une convolution avec un vesteur 1/5
def average(values):
    weigths = np.repeat(1.0, 5)/5
    smas = np.convolve(values, weigths, 'valid')
    return smas[0] # renvoie a numpy array -> pour avoir la valeur on lit le 0

def tabmax(values):
    smas = np.max(values)
    return smas # renvoie a numpy array -> pour avoir la valeur on lit le 0

def tabmin(values):
    #smas = values.min() ne marche pas ca c'est pas un tableau
    smas = np.min(values)
    return smas # renvoie a numpy array -> pour avoir la valeur on lit le 0




#===========================
# main programme
#===========================

opennp, highp,lowp, closep,volume = fxreadcsv("G:\\stockage\\fxdata\\data\\DAT_ASCII_AUDUSD_M1_201401.csv")



#===================== on genere les tableaux de resultats =====================================
# sur closep

resuavg=[] #on init une liste -> on aura une liste a la fin
resumax=[]
resumin=[]

for lawin in window(closep,5):
    resuavg.append(average(lawin)) #  si on est avec des arrays : il faut faire append
    resumax.append(tabmax(lawin))
    resumin.append(tabmin(lawin))

# un print pour debug
#print resuavg[:10]
#print resumax[:10]
#print resumin[:10]


# on affiche tout ca

x=0
y=100 # len(closep) # longueur des donnees a visualiser

print "longueur", y

newAr=[] #nouveau tableau
while x<y :
  appendLine = x,opennp[x], closep[x], highp[x],lowp[x], volume[x]
  newAr.append(appendLine)
  print newAr
  x += 1


from matplotlib.finance import candlestick
import matplotlib.pyplot as plt

lafig = plt.figure()
ax1 = plt.subplot(2,1,1)

candlestick(ax1,newAr, width=.75, colorup='g', colordown='y')




plt.show()










