Matieres={}
def ajout_matiere(Matieres,code,designation,section,coefficient,semestre):
    Matieres[code]=[designation,section,coefficient,semestre]

def supprimer_matiere(Matieres,code):
    Matieres.pop(code)

def modifier_nom_matiere(Matieres,code,nom):
    Matieres[code][0]=nom

def modifier_coefficient_matiere(Matieres,code,coef):
    Matieres[code][2]=coef

def recherche_matiere(Matieres,code):
    return({cle:val for cle,val in Matieres.items() if cle==code })
def recherche_section_matiere(Matieres,section):
    return({cle:val for cle,val in Matieres.items() if val[1]==section })

def recherche_semestre_matiere(Matieres,section):
    return({cle:val for cle,val in Matieres.items() if val[3]==section })

def recherche_section_semestre_matiere(Matieres,semestre):
    return({cle:val for cle,val in recherche_section_matiere(Matieres).items() if val[3]==semestre})

