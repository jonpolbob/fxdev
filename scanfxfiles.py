__author__ = 'cagibi'

import glob
import zipfile
import datetime
import numpy as np

#ce programme lit les zip, les ouvre et genere des tableaux/dictionnaires avec l a date et un champ de fxdata
# le probleme en suspend est de rajouter les resultat s d'une nouvelle paire alors que tous les fichiers n'ont pas
#forcement les memes heures.
#pour l'instant ca ne marche pas

# decodage d'une ligne et on renvoie un id de ligne pour faire la clef et une data dans une liste
def decodeline(laline):
  #  print laline
    leschamps = laline.split(";")
   # print 'champ',leschamps

    yyyy = leschamps[0][0:4]
    mm = leschamps[0][4:6]
    dd = leschamps[0][6:8]
    h = leschamps[0][9:11]
    m = leschamps[0][11:13]

    dt64now = np.datetime64(datetime.date(int(yyyy),int(mm),int(dd)))
    dt64origin = np.datetime64(datetime.date(2000,1,1))

    dateindex = dt64now - dt64origin #les dt64 peuvent etre sousrtraits
    dateinint = dateindex.item().total_seconds()  #avec item on poeut convertir en minutes
    index = dateinint/60 +int(h)*60 + int(m)
    print yyyy,mm,dd,h,m , '->', index,':',leschamps[1] #on laisse index en float pour avoir des ndarrays

    return yyyy+mm+dd+h+m, [index , float(leschamps[1])]



def scanfiles():
    listfiles = glob.glob("H:\\stockage\\fxdata\\*.zip")
    dictionnairefinal = {}

    tabvalues={}

    for file in listfiles:
        print file
        if (file[-3:]=='zip'):
            if (file.find('_ASCII_') == -1):
                print file , 'rejected'
                continue

            zfile = zipfile.PyZipFile(file,'r')
            for filename in zfile.namelist():
                if filename[-3:] == "csv":
                    print filename
                    tabvalues.clear()
                    data = zfile.read(filename)
                    leslignes = data.split('\n')

                    for ligne in leslignes[0:100]:
                        date,resu = decodeline(ligne)

                  #      print date, resu
                        tabvalues.update({date: resu})  # c'est un dictionnaire
                   #     print tabvalues


        for tabkey in tabvalues.keys():
            newvalue = tabvalues[tabkey]
            dicvalue = dictionnairefinal[tabkey]
            if len(dicvalue)==0:
                newvalue = newvalue
            else:
                newvalue = newvalue[tabkey].append(newvalue)

             #ici il au rajouter cette ligne au dictionnaire mais c'est complique:
             #si al ligne, existe deja, pas de souci
             #sinon l'initaliser  et la copleter
                # pour l'instant ca ne march epas.

                
            dictionnairefinal[tabkey] = newvalue
        for makey in dictionnairefinal.keys():
            print "val %s" % makey,dictionnairefinal[makey]



scanfiles()
