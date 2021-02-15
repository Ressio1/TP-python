#Baptiste Salamolard

import random
import time

class Guerrier():
    "Définition du Guerrier"
    PDV = 120
    PA = 20
    def DegatsGuerrier (self):
        return self.PA * random.uniform(0.1, 1)


class Sorcier():
    "Définition du Sorcier"
    PDV = 100
    PA = 10 
    NbrPotion = 5
    def BoirePotion(self):
        self.PDV = self.PDV + 15
        self.NbrPotion = self.NbrPotion -1
    def DegatsSorcier (self):
        return self.PA * random.uniform(0.1, 1)


class Game():
    warrior = Guerrier()
    mage = Sorcier()
    scoremage = 0
    scoreguerrier = 0

    def launch(self):
        #Boucle du jeu
        while (Game.warrior.PDV > 0) and (Game.mage.PDV > 0):
            #Tour Guerrier
            print("Début du tour du guerrier")
            result = random.randint(1, 5)
            if (result == 1):
                Game.warrior.PDV = Game.warrior.PDV - Game.warrior.DegatsGuerrier()
                print("Le Guerrier est débile et se tape tout seul, il perd :", Game.warrior.DegatsGuerrier())
                print("Le Guerrier n'a plus que :",Game.warrior.PDV,"PV")
            else:
                Game.mage.PDV = Game.mage.PDV - Game.warrior.DegatsGuerrier()
                print("Le Guerrier attaque le Sorcier et inflige",Game.warrior.DegatsGuerrier())
                print("Le Sorcier n'a plus que :",Game.mage.PDV,"PV")
            time.sleep(1)
            print("\n")

            if (Game.warrior.PDV > 0) and (Game.mage.PDV > 0):
                #Tour Sorcier
                print("Début du tour du Sorcier")
                result1 = random.randint(1, 2)
                if (result1 == 1):
                    if (Game.mage.NbrPotion > 0):
                        Game.mage.BoirePotion()
                        print("Le sorcier boit une potion et gagne : 15 PV, il lui reste ",Game.mage.NbrPotion)
                        print("Le Sorcier à encore :",Game.mage.PDV,"PV")
                Game.warrior.PDV = Game.warrior.PDV - Game.mage.DegatsSorcier()
                print("Le Sorcier tape le guerrier et inflige",Game.mage.DegatsSorcier())
                print("Le Guerrier n'a plus que :",Game.warrior.PDV,"PV")
                time.sleep(1)
                print("\n")
              
        #Fin
        if (Game.warrior.PDV <= 0):
            Game.scoreguerrier = Game.scoreguerrier + 1
            print("Le Guerrier meurt de ses blessures")
            print("Le Sorcier gagne le combat.")  
            print("\n")
            print("Victoire guerrier : ",Game.scoreguerrier)
            print("Victoire Sorcier : ",Game.scoremage)
        elif (Game.mage.PDV <= 0):
            Game.scoremage = Game.scoremage + 1
            print("Le Sorcier meurt de ses blessures")
            print("Le Guerrier gagne le combat.") 
            print("\n")
            print("Victoire guerrier : ",Game.scoreguerrier)
            print("Victoire Sorcier : ",Game.scoremage)
        Game.warrior = Guerrier()
        Game.mage = Sorcier()