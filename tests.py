entete="Numéros d'inscris:  |Noms:       |Prenoms:    |Dates de naissances: |Adresses:      |Mails:       |Telephones:   |Sections:   |Niveaux:"
L_entetes=entete.split("|")
i=0
for info in L_entetes:
    L_entetes[i]=info.strip()
    i+=1
print(L_entetes)