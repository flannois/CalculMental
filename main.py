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
        print("creation calcul")
        self.nb1 = randint(1,12)
        self.nb2 = randint(1,12)
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
        print("addition")
        self.resultat = self.nb1 + self.nb2

    def multiplication(self):
        print("multiplication")
        self.resultat = self.nb1 * self.nb2

    def division(self):
        print("division")
        self.multiplication()
        self.nb1,self.resultat = self.resultat,self.nb1

    def soustraction(self):
        print("soustraction")
        self.addition()
        self.nb1,self.resultat = self.resultat,self.nb1
           

    def chiffreRentre(self,chiffre):
        print("chiffreRentre")    
        bouton = str(chiffre)
        self.nombre += bouton
        self.affichage()
        print(self.nombre)
           
    def valider(self):
        print("valider")
        self.verification()
        self.nombre = ""
        self.affichage()
        
    def corriger(self):
        print("corriger")
        self.nombre = ""
        self.affichage()

    def verification(self):
        print("verification")
        print(self.nombre,self.resultat)
        if str(self.nombre) == str(self.resultat):
            self.gagne()
        else:
            self.perdu()

    def gagne(self):
        print("gagne")
        self.score += 1
        self.creationCalcul()
        
    def perdu(self):
        print("perdu")
        self.vie -= 1
        if self.vie > 0:
            self.creationCalcul()
        
    
    def affichage(self):
        if self.vie > 0:
            print("affichage")
            self.labelvie.text = "Vies : {}".format(self.vie)
            self.labelscore.text = "Score : {}".format(self.score)

            self.labelnb1.text = str(self.nb1)
            self.labeloperant.text = str(self.operant)
            self.labelnb2.text = str(self.nb2)
            self.labelnombre.text = str(self.nombre)
    
        else:
            self.vie = 0
            print("finDuJeu")
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