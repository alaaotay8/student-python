from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QDialog,QMainWindow
import sys

from GestionEtudiants import*
from GestionEtudiantsTXT import*
from GestionMatieres import*
from GestionMatieresTXT import*

from GestionNotes import*
from CalculEtAffichage import*

def is_float(element):
    try:
        float(element)
        return True
    except ValueError:
        return False


#--------------------------------Acceuil------------------------------------------

class EcranAcceuil(QMainWindow):
    def __init__(self):
        super(EcranAcceuil,self).__init__()
        loadUi("welcomescreen.ui",self)
        self.action.triggered.connect(self.GoToAjoutEtudiant)
        self.actionSupprimer_un_tudiant.triggered.connect(self.GoToSupprimerEtudiant)
        self.actionModifier_les_infos_d_un_tudiant.triggered.connect(self.GoToModifierEtudiant)
        self.actionModifier_une_mati_re.triggered.connect(self.GoToModifierMatiere)
        self.actionAjouter_une_mati_re.triggered.connect(self.GoToAjoutMatiere)
        self.actionSupprimer_une_mati_re.triggered.connect(self.GoToSupprimerMatiere)
        self.actionAjouter_une_note_2.triggered.connect(self.GoToAjoutNote)
        self.actionSupprimer_une_note.triggered.connect(self.GoToSupprimerNote)
        self.actionModifier.triggered.connect(self.GoToModifierNote)
        self.actionRecherche_et_affichage_2.triggered.connect(self.gotoAfficherEtudiants)
        self.actionRecherche_et_affichage_3.triggered.connect(self.gotoAfficherMatieres)
        self.actionRecherche_et_affichage_4.triggered.connect(self.gotoAfficherNotes)
        self.actionBulletin_de_note_d_un_tudiant.triggered.connect(self.gotoBulletin)

        
    def GoToAjoutEtudiant(self):
        ecran=Ecran_Ajout_Etudiant()
        ecran.exec_()
        
    def GoToSupprimerEtudiant(self):
        ecran=Ecran_Supprimer_Etudiant()
        ecran.exec_()
        
    def GoToModifierEtudiant(self):
        ecran=Ecran_Modifier_Etudiant()
        ecran.exec_()
    
    def GoToModifierMatiere(self):
        ecran=Ecran_Modifier_Matiere()
        ecran.exec_()

    def GoToAjoutMatiere(self):
        ecran=Ecran_Ajouter_Matiere()
        ecran.exec_()
    
    def GoToSupprimerMatiere(self):
        ecran=Ecran_Supprimer_Matiere()
        ecran.exec_()

    def GoToAjoutNote(self):
        ecran=Ecran_Ajouter_Note()
        ecran.exec_()
    
    def GoToSupprimerNote(self):
        ecran=Ecran_Sup_Note()
        ecran.exec_()
    
    def GoToModifierNote(self):
        ecran=Ecran_Modifier_Note()
        ecran.exec_()
    
    def gotoAfficherEtudiants(self):
        ecran=ecran_afficher_etudiants()
        ecran.exec_()
    
    def gotoAfficherMatieres(self):
        ecran=ecran_afficher_matieres()
        ecran.exec_()
    
    def gotoAfficherNotes(self):
        ecran=ecran_afficher_notes()
        ecran.exec_()
    
    def gotoBulletin(self):
        ecran=bulletin()
        ecran.exec_()

#------------------------------AJOUT ETUDIANT-----------------------------------

class Ecran_Ajout_Etudiant(QDialog):
    def __init__(self):
        super(Ecran_Ajout_Etudiant,self).__init__()
        loadUi("ajoutEtudiant.ui",self)
        self.pushButton.clicked.connect(self.enregistrer)
    
    def enregistrer(self):
        num_inscri=self.lineEdit.text()
        nom=self.lineEdit_2.text()
        prenom=self.lineEdit_10.text()
        date_n=self.lineEdit_3.text()
        adresse=self.lineEdit_4.text()
        mail=self.lineEdit_5.text()
        tel=self.lineEdit_6.text()
        section=self.lineEdit_7.text()
        niveau=self.lineEdit_8.text()
        self.label_13.setText("")
        if verifDonnees(num_inscri,nom,prenom,date_n,adresse,mail,tel,section,niveau):
            self.label_13.setText("Enregistré avec succés")
            ajouter_etudiant(Etudiants,num_inscri,nom,prenom,date_n,adresse,mail,tel,section,niveau)
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_10.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.lineEdit_7.clear()
            self.lineEdit_8.clear()
            self.label_12.setText("")
        else:
            if not SaisieNum(num_inscri):
                self.label_12.setText("Veuillez saisir un numéro d'inscription valide (8 chiffres)")
            elif not SaisieNom(nom):
                self.label_12.setText("Veuillez saisir un nom valide")
            elif not SaisieNom(prenom):
                self.label_12.setText("Veuillez saisir un prénom valide")
            elif not SaisieDate(date_n):
                self.label_12.setText("Veuillez saisir une date valide (jj/mm/aaaa)")
            elif not SaisieEmail(mail):
                self.label_12.setText("Veuillez saisir un email valide")
            elif not SaisieTelephone(tel):
                self.label_12.setText("Veuillez saisir un numéro de téléphone valide (8 chiffres)")
            elif not SaisieNiveauEtude(niveau):
                self.label_12.setText("Veuillez saisir un niveau valide (des caracteres numériques seulement)")
            elif len(section)>3:
                self.label_12.setText("Veuillez saisir une section valide (utiliser une abbreviation)")

    
#------------------------------SUPPRESSION ETUDIANT-------------------------------

class Ecran_Supprimer_Etudiant(QDialog):
    def __init__(self):
        super(Ecran_Supprimer_Etudiant,self).__init__()
        loadUi("supressionEtudiant.ui",self)
        self.pushButton.clicked.connect(self.gotoSupEtudDonne)
        self.pushButton_2.clicked.connect(self.gotoSupEtudSection)
        self.pushButton_3.clicked.connect(self.gotoSupEtudNiveau)
        self.pushButton_4.clicked.connect(self.gotoSupEtudSectNiveau)
    
    def gotoSupEtudDonne(self):
        ecran=Ecran_Sup_Etud_Donne()
        ecran.exec_()

    def gotoSupEtudNiveau(self):
        ecran=Ecran_Sup_Etud_Niv()
        ecran.exec_()

    def gotoSupEtudSection(self):
        ecran=Ecran_Sup_Etud_Sect()
        ecran.exec_()

    def gotoSupEtudSectNiveau(self):
        ecran=Ecran_Sup_Etud_Niv_Sect()
        ecran.exec_()


class Ecran_Sup_Etud_Donne(QDialog):
    def __init__(self):
        super(Ecran_Sup_Etud_Donne,self).__init__()
        loadUi("SupressionEtudDonne.ui",self)
        self.supp2.clicked.connect(self.CliquerSupprimerEtudDonne)
    
    def CliquerSupprimerEtudDonne(self):
        num_inscri=self.lineEdit.text()
        self.label_13.setText("")
        if not SaisieNum(num_inscri):
            self.label_14.setText("Veuillez saisir un numéro d'inscription valide (8 chiffres)")
        elif not num_inscri in Etudiants.keys():
            self.label_14.setText("Numéro d'inscription inexistant")

        else:
            self.label_14.setText("")
            self.label_13.setText("Supprimé avec succés")
            Etudiants.pop(num_inscri)
            self.lineEdit.clear()


class Ecran_Sup_Etud_Niv(QDialog):
    def __init__(self):
        super(Ecran_Sup_Etud_Niv,self).__init__()
        loadUi("SupressionEtudNiveau.ui",self)
        self.pushButton_2.clicked.connect(self.CliquerSupprimerEtudNiveau)
    
    def CliquerSupprimerEtudNiveau(self):
        niveau=self.lineEdit.text()
        self.label_13.setText("")
        if not SaisieNiveauEtude(niveau):
            self.label_14.setText("Veuillez saisir un niveau valide")
        else:
            self.label_14.setText("")
            self.label_13.setText("Supprimé avec succés")
            supprimer_niveau_etudiant(Etudiants,niveau)
            self.lineEdit.clear()


class Ecran_Sup_Etud_Sect(QDialog):
    def __init__(self):
        super(Ecran_Sup_Etud_Sect,self).__init__()
        loadUi("SupressionEtudSection.ui",self)
        self.pushButton_2.clicked.connect(self.CliquerSupprimerEtudSect)

    def CliquerSupprimerEtudSect(self):
        Sect=self.lineEdit.text()
        self.label_13.setText("")
        if not SaisieSection(Sect):
                self.label_14.setText("Veuillez saisir une section valide")
        else:
            self.label_13.setText("Supprimé avec succés")
            supprimer_section_etudiant(Etudiants,Sect)
            self.lineEdit.clear()


class Ecran_Sup_Etud_Niv_Sect(QDialog):
    def __init__(self):
        super(Ecran_Sup_Etud_Niv_Sect,self).__init__()
        loadUi("SupressionEtudNiveauSection.ui",self)
        self.pushButton_2.clicked.connect(self.CliquerSupprimerEtudNiveauSection)
    
    def CliquerSupprimerEtudNiveauSection(self):
        section=self.lineEdit_2.text()
        niveau=self.lineEdit.text()
        self.label_13.setText("")
        if not SaisieSection(section):
            self.label_14.setText("Veuillez saisir une section valide")
        elif not SaisieNiveauEtude(niveau):
            self.label_14.setText("Veuillez saisir un niveau valide")
        else:
            self.label_14.setText("")
            self.label_13.setText("Supprimé avec succés")
            supprimer_niveau_section_etudiant(Etudiants,niveau,section)
            self.lineEdit.clear()
            self.lineEdit_2.clear()

#-----------------------------MODIFIER ETUDIANT------------------------------------

class Ecran_Modifier_Etudiant(QDialog):
    def __init__(self):
        super(Ecran_Modifier_Etudiant,self).__init__()
        loadUi("modificationEtudiant.ui",self)
        self.pushButton.clicked.connect(self.gotoModEtudTel)
        self.pushButton_2.clicked.connect(self.gotoModEtudMail)
        self.pushButton_3.clicked.connect(self.gotoModEtudAdresse)
    
    def gotoModEtudTel(self):
        ecran=Ecran_Modifier_Etudiant_Tel()
        ecran.exec_()
    
    def gotoModEtudMail(self):
        ecran=Ecran_Modifier_Etudiant_Mail()
        ecran.exec_()
    
    def gotoModEtudAdresse(self):
        ecran=Ecran_Modifier_Etudiant_Adresse()
        ecran.exec_()


class Ecran_Modifier_Etudiant_Tel(QDialog):
    def __init__(self):
        super(Ecran_Modifier_Etudiant_Tel,self).__init__()
        loadUi("ModificationEtudiantTel.ui",self)
        self.pushButton_2.clicked.connect(self.CliquerModEtudTel)
    
    def CliquerModEtudTel(self):
        num_inscri=self.lineEdit.text()
        tel=self.lineEdit_2.text()
        self.label_13.setText("")
        if not SaisieNum(num_inscri):
            self.label_14.setText("Veuillez saisir un numéro d'inscription valide")
        elif not num_inscri in Etudiants.keys():
            self.label_14.setText("Numéro d'inscription inexistant")
        elif not SaisieTelephone(tel):
            self.label_14.setText("Veuillez saisir un numéro de téléphone valide")
        else:
            self.label_14.setText("")
            self.label_13.setText("Modifié avec succés")
            Etudiants[num_inscri][5]=tel
            self.lineEdit.clear()
            self.lineEdit_2.clear()


class Ecran_Modifier_Etudiant_Mail(QDialog):
    def __init__(self):
        super(Ecran_Modifier_Etudiant_Mail,self).__init__()
        loadUi("modificationEtudiantMail.ui",self)
        self.pushButton_2.clicked.connect(self.CliquerModEtudMail)

    def CliquerModEtudMail(self):
        num_inscri=self.lineEdit.text()
        Mail=self.lineEdit_2.text()
        self.label_13.setText("")
        if not SaisieNum(num_inscri):
            self.label_14.setText("Veuillez saisir un numéro d'inscription valide")
        elif not num_inscri in Etudiants.keys():
            self.label_14.setText("Numéro d'inscription inexistant")
        elif not SaisieEmail(Mail):
            self.label_14.setText("Veuillez saisir un email valide")
        else:
            self.label_14.setText("")
            self.label_13.setText("Modifié avec succés")
            modifier_mail(Etudiants,num_inscri,Mail)
            self.lineEdit.clear()
            self.lineEdit_2.clear()


class Ecran_Modifier_Etudiant_Adresse(QDialog):
    def __init__(self):
        super(Ecran_Modifier_Etudiant_Adresse,self).__init__()
        loadUi("modificationEtudiantAdresse.ui",self)
        self.pushButton_2.clicked.connect(self.CliquerModEtudAdresse)

    def CliquerModEtudAdresse(self):
        num_inscri=self.lineEdit.text()
        Adresse=self.lineEdit_2.text()
        self.label_13.setText("")
        if not SaisieNum(num_inscri):
            self.label_14.setText("Veuillez saisir un numéro d'inscription valide")
        elif not num_inscri in Etudiants.keys():
            self.label_14.setText("Numéro d'inscription inexistant")
        else:
            self.label_14.setText("")
            self.label_13.setText("Modifié avec succés")
            modifier_adresse(Etudiants,num_inscri,Adresse)
            self.lineEdit.clear()
            self.lineEdit_2.clear()

#--------------------------------AJOUT Matiere--------------------------------------

class Ecran_Ajouter_Matiere(QDialog):
    def __init__(self):
        super(Ecran_Ajouter_Matiere, self).__init__()
        loadUi("ajoutMatiere.ui", self)
        self.pushButton.clicked.connect(self.CliquerAjouterMatiere)

    def CliquerAjouterMatiere(self):
        code = self.lineEdit.text()
        nom = self.lineEdit_2.text()
        coef = self.lineEdit_3.text()
        semestre = self.lineEdit_5.text()
        section = self.lineEdit_10.text()
        self.label_13.setText("")
        if not code.isnumeric():
            self.label_14.setText("Veuiller saisir un code valide (Utiliser uniquement des chiffres)")
        elif not is_float(coef):
            self.label_14.setText("Veuiller saisir un coefficient valide")
        elif not (semestre == "1" or semestre == "2"):
            self.label_14.setText("Veuiller saisir \"1\" ou \"2\" dans le champ \"Semestre\"")
        else:
            Matieres[code] = [nom, section, coef, semestre]
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_5.clear()
            self.lineEdit_10.clear()
            self.label_14.setText("")
            self.label_13.setText("Enregistré avec succés")

#--------------------------------SUPPRESSION Matiere-------------------------------

class Ecran_Supprimer_Matiere(QDialog):
    def __init__(self):
        super(Ecran_Supprimer_Matiere,self).__init__()
        loadUi("SuppressionMatiere.ui",self)
        self.pushButton_2.clicked.connect(self.CliquerSupprimerMatiere)
    def CliquerSupprimerMatiere(self):
        code=self.lineEdit.text()
        self.label_13.setText("")
        if not code.isnumeric():
            self.label_14.setText("Veuiller saisir un code valide (Utiliser uniquement des chiffres)")
        elif not code in Matieres.keys():
            self.label_14.setText("Code non existant!")
        else:
            Matieres.pop(code)
            self.label_14.setText("")
            self.lineEdit.clear()
            self.label_13.setText("Supprimé avec succés")

#----------------------------MODIFIER MATIERE--------------------------------------

class Ecran_Modifier_Matiere(QDialog):
    def __init__(self):
        super(Ecran_Modifier_Matiere,self).__init__()
        loadUi("modificationMatiere.ui",self)
        self.pushButton.clicked.connect(self.gotoModMatiereNom)
        self.pushButton_2.clicked.connect(self.gotoModMatiereCoef)

    def gotoModMatiereNom(self):
        ecran=Ecran_Modifier_Matiere_Nom()
        ecran.exec_()
    
    def gotoModMatiereCoef(self):
        ecran=Ecran_Modifier_Matiere_Coef()
        ecran.exec_()


class Ecran_Modifier_Matiere_Nom(QDialog):
    def __init__(self):
        super(Ecran_Modifier_Matiere_Nom,self).__init__()
        loadUi("modificationMatiereNom.ui",self)
        self.pushButton_2.clicked.connect(self.CliquerModMatiereNom)
        
    def CliquerModMatiereNom(self):
        code=self.lineEdit.text()
        nom=self.lineEdit_2.text()
        self.label_13.setText("")
        if not code.isnumeric():
            self.label_14.setText("Veuillez saisir un code valide")
        elif not code in Matieres.keys():
            self.label_14.setText("Code inexistant")
        else:
            self.label_14.setText("")
            self.label_13.setText("Modifié avec succés")
            modifier_nom_matiere(Matieres,code,nom)
            self.lineEdit.clear()
            self.lineEdit_2.clear()


class Ecran_Modifier_Matiere_Coef(QDialog):
    def __init__(self):
        super(Ecran_Modifier_Matiere_Coef,self).__init__()
        loadUi("modificationMatiereCoefficient.ui",self)
        self.pushButton_2.clicked.connect(self.CliquerModMatiereCoef)

    
    def CliquerModMatiereCoef(self):
        code=self.lineEdit.text()
        coef=self.lineEdit_2.text()
        self.label_13.setText("")

        if not coef.isfloat():
            self.label_14.setText("Veuillez saisir un code valide")
        elif not code in Matieres.keys():
            self.label_14.setText("Code inexistant")
        else:
            self.label_13.setText("Modifié avec succés")
            modifier_coefficient_matiere(Matieres,code,coef)
            self.lineEdit.clear()
            self.lineEdit_2.clear()

#------------------------------------Notes-----------------------------------------

class Ecran_Ajouter_Note(QDialog):
    def __init__(self):
        super(Ecran_Ajouter_Note,self).__init__()
        loadUi("ajoutNote.ui",self)
        self.pushButton.clicked.connect(self.CliquerAjouterNote)

    def CliquerAjouterNote(self):
        num=self.lineEdit.text()
        code=self.lineEdit_2.text()
        note_DS=self.lineEdit_3.text()
        note_EX=self.lineEdit_5.text()
        self.label_13.setText("")
        if not num.isnumeric() or len(num)!=8:
            self.label_14.setText("Veuiller saisir un numéro d'inscription valide (8 chiffres)")
        elif not num in Etudiants.keys():
            self.label_14.setText("Numéro d'inscription non existant!")
        elif not code.isnumeric():
            self.label_14.setText("Veuiller saisir un code valide (Utiliser uniquement des chiffres)")
        elif not code in Matieres.keys():
            self.label_14.setText("Code non existant!")
        elif (num,code) in Notes.keys():
            self.label_14.setText("Cette note existe déjà")
        elif not 0<=float(note_DS)<=20:
            self.label_14.setText("Veuiller saisir une note DS valide")
        elif not 0<=float(note_EX)<=20:
            self.label_14.setText("Veuiller saisir une note EX valide")
        else:
            ajouter_note(Notes,num,code,note_DS,note_EX)
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_5.clear()
            self.label_14.setText("")
            self.label_13.setText("Enregistré avec succés")


class Ecran_Sup_Note(QDialog):
    def __init__(self):
        super(Ecran_Sup_Note,self).__init__()
        loadUi("suppressionNote.ui",self)
        self.pushButton_2.clicked.connect(self.CliquerSupNote)
        
    def CliquerSupNote(self):
        code=self.lineEdit_2.text()
        num=self.lineEdit.text()
        self.label_13.setText("")
        if not code.isnumeric():
            self.label_14.setText("Veuiller saisir un code valide (Utiliser uniquement des chiffres)")
        elif len(num)!=8:
            self.label_14.setText("Veuiller saisir un numéro d'inscription valide (8 chiffres)")
        elif not (num,code) in Notes.keys():
            self.label_14.setText("Note non existante!")
        else:
            Notes.pop((num,code))
            self.label_14.setText("")
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.label_13.setText("Supprimé avec succés")

    
class Ecran_Modifier_Note(QDialog):
    def __init__(self):
        super(Ecran_Modifier_Note,self).__init__()
        loadUi("ModNote.ui")
        self.pushButton_2.clicked.connect(self.CliquerModNote)

    def CliquerModNote(self):
        num=self.lineEdit.text()
        code=self.lineEdit_2.text()
        note_DS=self.lineEdit_3.text()
        note_EX=self.lineEdit_5.text()
        self.label_13.setText("")
        if not num.isnumeric() or len(num)!=8:
            self.label_14.setText("Veuiller saisir un numéro d'inscription valide (8 chiffres)")
        elif not num in Etudiants.keys():
            self.label_14.setText("Numéro d'inscription non existant!")
        elif not code.isnumeric():
            self.label_14.setText("Veuiller saisir un code valide (Utiliser uniquement des chiffres)")
        elif not code in Matieres.keys():
            self.label_14.setText("Code non existant!")
        if not (num,code) in Notes.keys():
            self.label_14.setText("Cette note n'existe pas.")
        elif not 0<=float(note_DS)<=20:
            self.label_14.setText("Veuiller saisir une note DS valide.")
        elif not 0<=float(note_EX)<=20:
            self.label_14.setText("Veuiller saisir une note EX valide.")
        else:
            ajouter_note(Notes,num,code,note_DS,note_EX)
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_5.clear()
            self.label_14.setText("")
            self.label_13.setText("Modifié avec succés")


#------------------------------------AFFICHAGE----------------------------------

class ecran_afficher_etudiants(QDialog):
    def __init__(self):
        super(ecran_afficher_etudiants,self).__init__()
        loadUi("affichageEtudiants.ui",self)
        self.pushButton.clicked.connect(self.valider)
        self.tableWidget.setColumnWidth(7,45)
        self.tableWidget.setColumnWidth(8,45)
        self.tableWidget.setColumnWidth(6,73)
        self.tableWidget.setColumnWidth(0,70)
        self.tableWidget.setColumnWidth(1,60)
        self.tableWidget.setColumnWidth(2,60)

    def recupererEtud(self,Etudiants):
        self.tableWidget.setRowCount(len(Etudiants.keys()))
        ligne=0
        for cle in Etudiants.keys():
            column=0
            self.tableWidget.setItem(ligne,column,QtWidgets.QTableWidgetItem(cle))
            for info in Etudiants[cle]:
                column+=1
                self.tableWidget.setItem(ligne,column,QtWidgets.QTableWidgetItem(info))
            ligne+=1

    def valider(self):
        num=self.lineEdit_10.text()
        niveau=self.lineEdit_11.text()
        section=self.lineEdit_12.text()
        if num!="" and num in Etudiants.keys():
            self.recupererEtud(recherche_par_num(Etudiants,num))
        elif niveau=="" and section=="":
            self.recupererEtud(Etudiants)
        elif section=="":
            self.recupererEtud(recherche_par_niveau_etudiant(Etudiants,niveau))
        elif niveau=="":
            self.recupererEtud(recherche_par_section_etudiant(Etudiants,section))
        else:
            self.recupererEtud(recherche_par_section_niveau_etudiant(Etudiants,section,niveau))


class ecran_afficher_matieres(QDialog):
    def __init__(self):
        super(ecran_afficher_matieres,self).__init__()
        loadUi("affichageMatieres.ui",self)
        self.pushButton.clicked.connect(self.valider)
    
    def recuperer(self,Matieres):
        self.tableWidget.setRowCount(len(Matieres.keys()))
        ligne=0
        for cle in Matieres.keys():
            column=0
            self.tableWidget.setItem(ligne,column,QtWidgets.QTableWidgetItem(cle))
            for info in Matieres[cle]:
                column+=1
                self.tableWidget.setItem(ligne,column,QtWidgets.QTableWidgetItem(info))
            ligne+=1
    
    def valider(self):
        code=self.lineEdit_10.text()
        section=self.lineEdit_11.text()
        semestre=self.lineEdit_12.text()

        if code!="":
            self.recuperer(recherche_matiere(Matieres,code))
        elif section=="" and semestre=="":
            self.recuperer(Matieres)
        elif section=="":
            self.recuperer(recherche_semestre_matiere(Matieres,semestre))
        else:
            self.recuperer(recherche_section_matiere(Matieres,section))


class ecran_afficher_notes(QDialog):
    def __init__(self):
        super(ecran_afficher_notes,self).__init__()
        loadUi("affichageNotes.ui",self)
        self.pushButton.clicked.connect(self.valider)
        self.tableWidget.setColumnWidth(0,120)
        self.tableWidget.setColumnWidth(3,90)

    def recuperer(self,notes):
        self.tableWidget.setRowCount(len(Notes.keys()))
        ligne=0
        for cle,val in notes.items():
            self.tableWidget.setItem(ligne,0,QtWidgets.QTableWidgetItem(cle[0]))
            self.tableWidget.setItem(ligne,1,QtWidgets.QTableWidgetItem(cle[1]))
            self.tableWidget.setItem(ligne,2,QtWidgets.QTableWidgetItem(val[0]))
            self.tableWidget.setItem(ligne,3,QtWidgets.QTableWidgetItem(val[1]))
            ligne+=1

    def valider(self,notes):
        code=self.lineEdit_10.text()
        section=self.lineEdit_11.text()
        semestre=self.lineEdit_12.text()
        num=self.lineEdit_13.text()
        niveau=self.lineEdit_14.text()
        if (not SaisieNum(num) or num not in Etudiants.keys()) and num!="":
            self.label_12.setText("Num. Insc. non valide")
        elif not SaisieNiveauEtude(niveau) and niveau!="":
            self.label_12.setText("Niveau non valide")
        elif (not code.isnumeric() or code not in Matieres.keys()) and code!="":
            self.label_12.setText("Code non valide")
        elif not SaisieSection(section) and section!="":
            self.label_12.setText("Section non valide")
        elif not (semestre in ["1","2",""]):
            self.label_12.setText("Semestre non valide")
        else:
            self.label_12.setText("")
            notes=Notes.copy()
            if niveau!="":
                notes=recherche_niveau_notes(Notes,Etudiants,niveau)
            if code!="":
                notes=recherche_code_notes(Notes,code)
            if section!="":
                notes=recherche_section_notes(Notes,Etudiants,section)
            if semestre!="":
                notes=recherche_semestre_notes(Notes,Matieres,semestre)
            if num!="":
                notes=recherche_num_inscri_notes(Notes,num)
            self.recuperer(notes)


class bulletin(QDialog):
    def __init__(self):
        super(bulletin,self).__init__()
        loadUi("bulletinEtud.ui",self)
        self.pushButton.clicked.connect(self.valider)

    
    def valider(self):
        semestre=self.lineEdit_12.text()
        num=self.lineEdit_13.text()
        if not num in Etudiants.keys():
            self.label_14.setText("Num. d'insc. non existant!")
        elif semestre!="1" and semestre!="2" and semestre!="":
            self.label_14.setText("Semestre non valide")
        else:
            self.label_14.setText("")
            self.label_7.setText(Etudiants[num][6])
            self.label_8.setText(Etudiants[num][0]+" "+Etudiants[num][1])
            if semestre=="":
                self.tableWidget.setRowCount(len(Matieres.keys()))
                self.label_13.setText("10")
                for cle,val in Notes.items():
                    ligne=0
                    if cle[0]==num and cle[1] in Matieres.keys():
                        self.tableWidget.setItem(ligne,0,QtWidgets.QTableWidgetItem(Matieres[cle[1]][0]))
                        self.tableWidget.setItem(ligne,1,QtWidgets.QTableWidgetItem(val[0]))
                        self.tableWidget.setItem(ligne,2,QtWidgets.QTableWidgetItem(val[1]))
                        self.tableWidget.setItem(ligne,3,QtWidgets.QTableWidgetItem(str(moyenne_matiere(num,cle[1]))))
                        ligne+=1
            elif semestre=="1":
                self.label_13.setText(str(moyenne_sem(num,"1")))
                for cle,val in Notes.items():
                    ligne=0
                    if cle[0]==num and cle[1] in Matieres.keys() and Matieres[cle[1]][3]==semestre:
                        self.tableWidget.setItem(ligne,0,QtWidgets.QTableWidgetItem(Matieres[cle[1]][0]))
                        self.tableWidget.setItem(ligne,1,QtWidgets.QTableWidgetItem(val[0]))
                        self.tableWidget.setItem(ligne,2,QtWidgets.QTableWidgetItem(val[1]))
                        self.tableWidget.setItem(ligne,3,QtWidgets.QTableWidgetItem(str(moyenne_matiere(num,cle[1]))))
                        ligne+=1
            elif semestre=="2":
                self.label_13.setText(str(moyenne_sem(num,"2")))
                for cle,val in Notes.items():
                    ligne=0
                    if cle[0]==num and cle[1] in Matieres.keys() and Matieres[cle[1]][3]==semestre:
                        self.tableWidget.setItem(ligne,0,QtWidgets.QTableWidgetItem(Matieres[cle[1]][0]))
                        self.tableWidget.setItem(ligne,1,QtWidgets.QTableWidgetItem(val[0]))
                        self.tableWidget.setItem(ligne,2,QtWidgets.QTableWidgetItem(val[1]))
                        self.tableWidget.setItem(ligne,3,QtWidgets.QTableWidgetItem(str(moyenne_matiere(num,cle[1]))))
                        ligne+=1


#------------------------------------main--------------------------------------

recuperer_etudiants_txt(Etudiants)
recuperer_Matiere_txt(Matieres)
recuperer_Notes_txt(Notes)

app = QApplication(sys.argv)
welcome = EcranAcceuil()
welcome.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")
    enregistrer_Matiere_txt(Matieres)
    enregistrer_etudiants_txt(Etudiants)
    enregistrer_Notes_txt(Notes)

