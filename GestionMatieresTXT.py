def enregistrer_Matiere_txt(Matiere):
    f=open("Matieres.txt","w")
    ch_entete="12345678 |mohammed ali |la9ab twil |12/12/2002 |1 "
    entete=ch_entete.split("|")

    for cle,val in Matiere.items():
        ligne_etudiant= cle + " "*(len(entete[0])-len(cle))    
        k=1
        for info in val:
            ligne_etudiant= ligne_etudiant + "|" + info +" "*(len(entete[k])-len(info))
            k+=1
        f.write(ligne_etudiant+"\n")

    f.close()

#---------------------------------------RECUPERATION-----------------------------------------
def recuperer_Matiere_txt(Matiere):
    f=open("Matieres.txt","r")

    while True:
        infos_etudiant=f.readline().split("|") 

        if infos_etudiant==['']:    #derniere ligne = [''] 
            break

        for i in range(len(infos_etudiant)):              #suppression des espaces
            infos_etudiant[i]=infos_etudiant[i].strip()

        Matiere[ infos_etudiant[0] ] = infos_etudiant[1:]
    
    f.close()