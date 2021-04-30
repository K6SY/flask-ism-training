class Phone:
    def __init__(self,marque,capacite,numero):
        self.marque=marque
        self.capacite=capacite
        self.numero=numero
        self.demarre=False
        self.batterie=100

    def allumer(self):
        self.demarre=True
        print(f"Démarrage du phone {self.marque} .....")


    def getEtat(self):
        if self.demarre:
            print(f"{self.marque} est démarré")
        else:
            print(f"{self.marque} est éteint")

    def getBatterieLevel(self):
        return self.batterie
    
    def game(self):
        if self.batterie >10:
            self.batterie-=10
            print("Happy gaming")
        else:
            print(f"Veuillez charger votre téléphone. Niveau de charge restant{self.batterie}")

    def eteindre(self):
        self.demarre=False
        print(f"Extinction du phone {self.marque} .....")




phone1=Phone("Samsung","64Go RAM", "776543221")
phone2=Phone("Iphone","32Go RAM", "779873221")
phone3=Phone("Itel","32Go RAM", "775438921")

print(phone1.getEtat())
input()
phone1.allumer()
input()
print(phone1.getEtat())
input()
print(phone1.getBatterieLevel())
input()
for i in range(4):
    phone1.game()
input()
print(phone1.getBatterieLevel())
phone1.eteindre()
