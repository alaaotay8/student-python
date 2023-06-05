    def CalculMoyenneMat(self, keys):
        return ((int(NT.Notes[keys][0])) * 0.25 + (int(NT.Notes[keys][1])) * 0.75)

    def CalculMoyenneGen(self, Numinscrits):
        Moy = 0
        Coefficinets = 0
        for keys in NT.Notes:
            if keys[0] == Numinscrits:
                Coefficinets += float(Mat.Matieres[keys[1]][2])
                Moy += self.CalculMoyenneMat(keys) * float(Mat.Matieres[keys[1]][2])
        Moy /= Coefficinets
        return (Moy)

    def CalculRang (self,Numinscrit):
        dict={}
        Section = self.Section.toPlainText()
        Tab = Keys(Section)

        for keys in Tab:
            if keys not in dict:
                dict.update({keys:self.CalculMoyenneGen(keys)})
        T = sorted(dict.items(), key=lambda x: x[1])
        return (T.index ((Numinscrit,self.CalculMoyenneGen(Numinscrit)))+1)
