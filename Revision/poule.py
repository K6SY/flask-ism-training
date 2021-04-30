from random import *
class Poule:

    def __init__(self,height,poids):
        self.height=height
        self.poids=poids
    
    def pondre(self):
        a = 10
        print(f"La poule a pondu {a} oeufs")
    
    def crier(self):
        print("Cocoricoooooooo!!!")

braman=Poule(5.5,10)

braman.pondre()

braman.crier()