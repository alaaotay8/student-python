from GestionEtudiants import*
from GestionMatieres import*
Notes={}
def ajouter_note(Notes,num_insc,code,Note_DS,Note_EX):
    Notes[(num_insc,code)]=[Note_DS,Note_EX]
 
def ajouter_plusieurs_notes(Notes):
    ajouter_note(Notes)
    while True:
        rep=input("Voulez vous ajouter une autre note? Tapez 'Oui' ou 'Non': ")
        if (rep.upper()=="OUI" or rep.upper()=="NON"):
            break
    if(rep.upper()=="OUI"):
        ajouter_plusieurs_notes(Notes)

def supprimer_note(Notes,num,code):
    Notes.pop((num,code))


def recherche_niveau_notes(Notes,Etudiants,niv):
    return{cle:val for cle,val in Notes.items() if (Etudiants[cle[0]][7]==niv)}

def recherche_section_notes(Notes,Etudiants,section):
    return{cle:val for cle,val in Notes.items() if (Etudiants[cle[0]][6]==section)}

def recherche_num_inscri_notes(Notes,num_insc):
    return{cle:val for cle,val in Notes.items() if (cle[0]==num_insc )}

def recherche_code_notes(Notes,num_insc):
    return{cle:val for cle,val in Notes.items() if (cle[1]==num_insc )}

def recherche_semestre_notes(Notes,Matieres,semestre):
    return{cle:val for cle,val in Notes.items() if cle[1] in Matieres.keys() and (Matieres[cle[1]][3]==semestre)}


def enregistrer_Notes_txt(Notes):
    f=open("Notes.txt","w")

    for cle,val in Notes.items():
        ligne_note=cle[0]+" |"+ cle[1]+" |" +val[0]+" |"+val[1]
        f.write(ligne_note+"\n")

    f.close()

#---------------------------------------RECUPERATION-----------------------------------------
def recuperer_Notes_txt(Notes):
    f=open("Notes.txt","r")

    while True:
        infos_note=f.readline().split("|") 

        if infos_note==['']:    #derniere ligne = [''] 
            break

        for i in range(len(infos_note)):              #suppression des espaces
            infos_note[i]=infos_note[i].strip()

        Notes[ (infos_note[0],infos_note[1]) ] = infos_note[2:]
    
    f.close()