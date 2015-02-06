#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      maison
#
# Created:     12/08/2014
# Copyright:   (c) maison 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import numpy as np


#lecture mois et paires
Process = False
while Process == False:
    Encore = True
    valeur = ""
    while Encore==True :
        annee = raw_input("annee")
        iannee = int(annee)
        mois = raw_input(" mois")
        imois  = int(mois)

        surv = raw_input("surveillance")


        paires = raw_input("paires")
        listepaires = np.array(paires.split(" "))

        if len(annee) !=0 :
            Encore = False

    Process = True

#test que le fichier existe
import os.path
listfic=[]
for paire in  listepaires:
    nomfich = "E:\\stockage\\fxdata\\HISTDATA_COM_ASCII_"+surv+paire+"_M1"+"%4d%02d"%(iannee,imois)+".zip"
    if (os.path.isfile(nomfich)):
        listfic.append([nomfich,0])
    nomfich = "E:\\stockage\\fxdata\\HISTDATA_COM_ASCII_"+paire+surv+"_M1"+"%4d%02d"%(iannee,imois)+".zip"
    if (os.path.isfile(nomfich)):
        listfic.append([nomfich,1])


for f in listfic:
   print f
