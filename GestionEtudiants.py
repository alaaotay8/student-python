import re
from datetime import date
Etudiants={}
    
def ajouter_etudiant(Etudiants,num_inscri,nom,prenom,datenais,adresse,mail,tel,section,niv):
    Etudiants[num_inscri]=[nom,prenom,datenais,adresse,mail,tel,section,niv]

def ajouter_plusieurs_etudiants(Etudiants):
    ajouter_etudiant(Etudiants)
    while True:
        rep=input("Voulez vous ajouter un autre etudiant? Tapez 'Oui' ou 'Non' : ")
        if (rep.upper()=="OUI" or rep.upper()=="NON"):
            break
    if(rep.upper()=="OUI"):
        ajouter_plusieurs_etudiants(Etudiants)

def supprimer_etudiant_donnée(Etudiants):
    num_inscri=input("Donner le numero d'inscription: ")
    Etudiants.pop(num_inscri)

def supprimer_section_etudiant(Etudiants,section):
    return ({cle:val for cle, val in Etudiants.items() if val[6]!=section})

def supprimer_niveau_etudiant(Etudiants,niv):
    return ({cle:val for cle, val in Etudiants.items() if val[7]!=niv})

def supprimer_niveau_section_etudiant(Etudiants,niveau,section):
    return(supprimer_section_etudiant(supprimer_niveau_etudiant(Etudiants,niveau),section))

def modifier_telephone(Etudiants,cle,tel):
    Etudiants[cle][5]=tel

def modifier_mail(Etudiants,cle,mail):
    Etudiants[cle][4]=mail

def modifier_adresse(Etudiants,cle,adresse):
    Etudiants[cle][3]=adresse

def recherche_par_num(Etudiants,num):
    return({num:Etudiants[num]})

def recherche_par_section_etudiant(Etudiants,section):
    return({cle:val for cle, val in Etudiants.items() if val[6]==section})

def recherche_par_niveau_etudiant(Etudiants,niv):
    return ({cle:val for cle, val in Etudiants.items() if val[7]==niv})

def recherche_par_section_niveau_etudiant(Etudiants,section,niv):
    return(recherche_par_niveau_etudiant(recherche_par_section_etudiant(Etudiants,section),niv))



def SaisieNom(Nom):
    if Nom.isalpha():
        return True
    else:
        return False

def SaisieNum(num):
    return(len(num)==8 and num.isnumeric())

def SaisieDate(date_n):
    if len(date_n)!=10:
        return False
    if date_n[2]!="/" and date_n[5]!="/":
        return False
    liste=date_n.split("/")
    if int(liste[0])>31 or len(liste[0])!=2:
        return False
    if int(liste[1])>12 or len(liste[1])!=2:
        return False
    if int(liste[2])>int(date.today().year):
        return False
    return True

def SaisieEmail (Email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, Email)):
        return True
    else:
        return False

def SaisieTelephone(Telephone):
    if (Telephone.isnumeric() and len(Telephone)==8):
        return True
    else:
        return False

def SaisieSection(Section):
    if Section.isalpha():
        return True
    else:
        return False

def SaisieNiveauEtude(NiveauEtude):
    if (NiveauEtude.isnumeric()):
        return True
    else:
        return False

def verifDonnees(num_inscri,nom,prenom,datenais,adresse,mail,tel,section,niv):
    return(SaisieNum(num_inscri) and SaisieNiveauEtude(niv) and SaisieDate(datenais) and SaisieSection(section) and SaisieEmail(mail) and SaisieNom(nom)and SaisieTelephone(tel)and SaisieNom(prenom))


