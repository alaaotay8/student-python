#---------------------------------------ENREGISTREMENT-----------------------------------------
def enregistrer_etudiants_txt(Etudiants):
    f=open("Etudiants.txt","w")
    ch_entete="12345678 |mohammed ali |la9ab twil |12/12/2002 |4 rue med denguezli cité riad|pinkpotato2002@gmail.com|12345678 |CPI     |123"
    
    entete=ch_entete.split("|")

    for cle,val in Etudiants.items():
        ligne_etudiant= cle + " "*(len(entete[0])-len(cle))    
        k=1
        for info in val:
            ligne_etudiant= ligne_etudiant + "|" + info +" "*(len(entete[k])-len(info))
            k+=1
        f.write(ligne_etudiant+"\n")

    f.close()

#---------------------------------------RECUPERATION-----------------------------------------
def recuperer_etudiants_txt(Etudiants):
    f=open("Etudiants.txt","r")

    while True:
        infos_etudiant=f.readline().split("|") 

        if infos_etudiant==['']:    #derniere ligne = [''] 
            break

        for i in range(len(infos_etudiant)):              #suppression des espaces
            infos_etudiant[i]=infos_etudiant[i].strip()

        Etudiants[ infos_etudiant[0] ] = infos_etudiant[1:]
    
    f.close()