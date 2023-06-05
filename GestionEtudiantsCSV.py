#----------------------------------------------ENREGISTREMENT---------------------------------------
def enregistrer_etudiants_CSV (Etudiants):
    f=open("Etudiants.csv","w")
    ch_entete="Numero d'inscri:,Nom:,Prenom:,Date de naissance:,Adresse:,Mail:,Telephone:,Section:,Niveau:"
    f.write(ch_entete)
    f.write("\n")
    for cle,val in Etudiants.items():
        ligne=cle
        for info in val:
            ligne=ligne+","+info
        f.write(ligne+"\n")
    f.close ()

#----------------------------------------------RECUPERATION-----------------------------------------
def recuperer_etudiants_CSV(Etudiants):
    f=open("Etudiants.csv","r")
    f.readline()      #premiere ligne est l'entete
    for ligne in f.readlines():
        L_etudiant=ligne.split(",")
        L_etudiant[8]=L_etudiant[8].replace("\n","")  #suppression du caractere \n dans le niveau
        Etudiants[L_etudiant[0]]=L_etudiant[1:]
    f.close()