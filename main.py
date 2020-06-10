import sys
from random import randint

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

class Fenetre(BoxLayout):
    def __init__(self,**kwargs):
        super(Fenetre,self).__init__(**kwargs)
        self.nombre = ""
        self.score = 0
        self.vie = 5
        self.creationCalcul()

    def creationCalcul(self):
        self.nb1 = randint(1,9)
        self.nb2 = randint(1,9)
        operant = randint(1,4)
        if operant == 1:
            self.operant = "+"
            self.addition()
        elif operant == 2:
            self.operant = "X"
            self.multiplication()
        elif operant == 3:
            self.operant = ":"
            self.division()
        elif operant == 4:
            self.operant = "-"
            self.soustraction()

    def addition(self):
        self.resultat = self.nb1 + self.nb2

    def multiplication(self):
        self.resultat = self.nb1 * self.nb2

    def division(self):
        self.multiplication()
        self.nb1,self.resultat = self.resultat,self.nb1

    def soustraction(self):
        self.addition()
        self.nb1,self.resultat = self.resultat,self.nb1
           

    def chiffreRentre(self,chiffre):
        bouton = str(chiffre)
        self.nombre += bouton
        self.affichage()
           
    def valider(self):
        self.verification()
        self.nombre = ""
        self.affichage()
        
    def corriger(self):
        self.nombre = ""
        self.affichage()

    def verification(self):
        if str(self.nombre) == str(self.resultat):
            self.gagne()
        else:
            self.perdu()

    def gagne(self):
        self.score += 1
        self.creationCalcul()
        
    def perdu(self):
        self.vie -= 1
        if self.vie > 0:
            self.creationCalcul()
        
    
    def affichage(self):
        if self.vie > 0:
            self.labelvie.text = "Vies : {}".format(self.vie)
            self.labelscore.text = "Score : {}".format(self.score)

            self.labelnb1.text = str(self.nb1)
            self.labeloperant.text = str(self.operant)
            self.labelnb2.text = str(self.nb2)
            self.labelnombre.text = str(self.nombre)
    
        else:
            self.vie = 0
            self.labelvie.text = "Vies : {}".format(self.vie)
            self.labelscore.text = "Score : {}".format(self.score)
            self.labelnb1.text = str("")
            self.labeloperant.text = str("Perdu")
            self.labelnb2.text = str("")
            self.labelnombre.text = str("Ton score\n{}".format(self.score))
        


    def quitter(self):
        sys.exit()   

class CalculMentalApp(App):
    def build(self):
        self.root = Builder.load_file('calculmental.kv')

if __name__ == "__main__":
    CalculMentalApp().run()