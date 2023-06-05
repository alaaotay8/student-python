from GestionMatieres import*
from GestionEtudiants import*
from GestionNotes import*

def moyenne_matiere(num,code):
    return(float(Notes[(num,code)][0])*0.3 + float(Notes[(num,code)][1])*0.7) 

def moyenne(num):
    Moy=0
    Coefficinets=0
    for cle in Notes.keys():
        if cle[0]==num:
            Coefficinets += float(Matieres[cle[1]][2])
            Moy += moyenne_matiere(num,cle[1]) * float(Matieres[cle[1]][2])
    Moy /= Coefficinets
    return (Moy)
def moyenne_sem(num,sem):
    Moy=0
    Coefficinets=0
    for cle in Notes.keys():
        if cle[0]==num and Matieres[cle[1]][3]==sem:
            Coefficinets += float(Matieres[cle[1]][2])
            Moy += moyenne_matiere(num,cle[1]) * float(Matieres[cle[1]][2])
    Moy /= Coefficinets
    return (Moy)




