from asyncio.proactor_events import _ProactorDuplexPipeTransport
from random import randint

class Armes:
    def __init__(self, degats = 0):
        self.__degat = degats

    def getDegat(self):
        return self.__degat

class Armures:
    def __init__(self, protection = 0):
        self.__protection = protection

    def getProtection(self):
        return self.__protection

class Potions:
    def __init__(self, potion_Mana = 0, potion_Force = 0, potion_Stamina = 0, potion_Soin = 0, potion_Def = 0, potion_Crit = 0, potion_Agi = 0):
        self.__potMana = potion_Mana
        self.__potForce = potion_Force
        self.__potStamina = potion_Stamina
        self.__potSoin = potion_Soin
        self.__potDef = potion_Def
        self.__potCrit = potion_Crit
        self.__potAgi = potion_Agi

    #region getter Potion
    def getPotMana(self):
        return self.__potMana

    def getPotForce(self):
        return self.__potForce

    def getPotStamina(self):
        return self.__potStamina

    def getPotSoin(self):
        return self.__potSoin

    def getPotDef(self):
        return self.__potDef

    def getPotCrit(self):
        return self.__potCrit

    def getPotAgi(self):
        return self.__potAgi
    #endregion

    #region setter Potion
    def setPotMana(self, potMana):
        self.__potMana = potMana

    def setPotForce(self, potForce):
        self.__potForce = potForce

    def setPotStamina(self, potStamina):
        self.__potStamina = potStamina

    def setPotSoin(self, potSoin):
        self.__potSoin = potSoin

    def setPotDef(self, potDef):
        self.__potDef = potDef

    def setPotCrit(self, potCrit):
        self.__potCrit = potCrit

    def setPotAgi(self, potAgi):
        self.__potAgi = potAgi
    #endregion


class Personnage :

    __niveauMax = 100

    def __init__(self, niveau = 1, force = 10.0, defense = 5.0, hp = 100.0, hpMax = 100.0, critique = 2, agilite = 2, defPen = 1.5, stamina = 100.0, staminaMax = 100.0) :
        self.__niveau = niveau
        self.__force = force
        self.__defense = defense
        self.__hp = hp
        self.__hpMax = hpMax
        self.__critique = critique
        self.__agilite = agilite
        self.__defPen = defPen
        self.__stamina = stamina
        self.____staminaMax = staminaMax
        self.__armeEquiper = Armes()
        self.__armureEquiper = Armures()

    def estVivant(self) : 
        return self.__hp > 0 

    def equiperArme(self, arme):
        self.__armeEquiper = arme

    def equiperArmure(self, armure):
        self.__armureEquiper = armure
    
    def attaquer(self, ennemi) :
        randomInt = randint(0,10)
        if (randomInt > ennemi.getAgi()):
            randomInt = randint(0,10)
            if (randomInt <= self.getCrit()) :
                ennemi.__hp -= (((self.getForce() + self.getDegatArme()))*2 - (ennemi.getDef() + ennemi.getProtectArmure()))
            else :
                ennemi.__hp -= ((self.getForce() + self.getDegatArme()) - (ennemi.getDef() + ennemi.getProtectArmure()))
        else:
            print ("L'attaque à échouée")
    
    #region getter Personnage
    def getHp(self):
        return self.__hp
    
    def getForce(self):
        return self.__force

    def getDef(self):
        return self.__defense

    def getCrit(self):
        return self.__critique
    
    def getAgi(self):
        return self.__agilite

    def getDefPen(self):
        return self.__defPen

    def getStamina(self):
        return self.__Stamina

    def getNiveau(self):
        return self.__niveau
    
    def getNivMax():
        return Personnage.__niveauMax

    def getStamina(self):
        return self.__stamina

    def getStaminaMax():
        return Personnage.__staminaMax

    def getDegatArme(self):
        return self.__armeEquiper.getDegat()

    def getProtectArmure(self):
        return self.__armureEquiper.getProtection()
    #endregion

    #region setter Personnage
    def setHp(self, hp):
        if (hp < self.__hpMax):
            self.__hp = hp  
        elif (hp < self.__hpMax):  
            self.__hp = hp  
        else :
            self.__hp = self.__hpMax

    def setHpMax(self, hpMax):
        self.__hpMax = hpMax
    
    def setForce(self, force):
        self.__force = force

    def setDef(self, defense):
        self.__defense = defense

    def setAgi(self, agilite):
        self.__agilite = agilite

    def setCrit(self, critique):
        self.__critique = critique

    def setPenArmure(self, defPen):
        self.__defPen = defPen

    def setStamina(self,stamina):
        if (stamina < self.____staminaMax):
            self.__stamina = stamina
        else :
            self.__stamina = self.__staminaMax

    def setStaminaMax(self, staminaMax):
        self.____staminaMax = staminaMax

    def setNiveau(self, niveau):
        self.__niveau = niveau
    #endregion


class Elements :

    def __init__(self) :
        self.__cryo = 3
        self.__pyro = 3
        self.__hydro = 3
        self.__death = 3
        self.__life = 3

    
    #region getter Elements
    def getPyro(self):
        return self.__pyro

    def getCryo(self):
        return self.__cryo

    def getElectro(self):
        return self.__electro

    def getAnemo(self):
        return self.__anemo

    def getHydro(self):
        return self.__hydro

    def getDeath(self):
        return self.__death
    
    def getLife(self):
        return self.__life
    #endregion



class Epee(Armes):

    def __init__(self, degats = 5):
        super().__init__(degats)

class Arc(Armes):
    
    def __init__(self, degats = 3):
        super().__init__(degats)
        self.__nbFleches = 50
        self.__nbFlechesMax = 50

    #region getter fleches
    def getNbFleches(self):
        return self.__nbFleches

    def getNbFlechesMax(self):
        return self.__nbFlechesMax
    #endregion

class Dague(Armes):
    
    def __init__(self, degats = 2):
        super().__init__(degats)

class Baton(Armes):

    def __init__(self, degats = 2):
        super().__init__(degats)

class Lance(Armes):

    def __init__(self, degats = 5):
        super().__init__(degats)

class BouclierLance(Armes):

    def __init__(self, degats = 5):
        super().__init__(degats)


class ArmureLourde(Armures):
    def __init__(self, protection=6):
        super().__init__(self)

class ArmureLégère(Armures):
    def __init__(self, protection=3):
        super().__init__(self)


class Mage(Personnage, Elements) : 
    
    def __init__(self, magie = 100.0, magieMax = 100.0):
        Personnage.__init__(self)
        Elements.__init__(self)
        self.__magie = magie
        self.__magieMax = magieMax
        self.setCrit(3)

    def equiperWeapon(self, arme):
        if (isinstance(arme, Baton.__class__)):
            self.equiperArme(arme)
        else:
            print("Cette arme ne me sied guère ")
    
    def equiperArmor(self, armure):
        if (isinstance(armure, ArmureLégère.__class__)):
            self.equiperArme(armure)
            self.setDef(self.getDef()+self.getProtectArmure())
        else:
                print("Cette armure ne me convient pas")

    #region sort
    def lancerSortFeu(self, ennemi) :
        randomInt = randint(0,10)
        if (randomInt > ennemi.getAgi()):
            randomInt = randint(0,10)
            if (randomInt <= self.getCrit()) :
                ennemi.setHp(ennemi.getHp() - ((self.getForce() + self.getDegatArme() + self.getPyro())*2 - (ennemi.getDef() + ennemi.getProtectArmure())))
                self.setMagie(self.getMagie()-10)
            else :
                ennemi.setHp(ennemi.getHp() - ((self.getForce() + self.getDegatArme() + self.getPyro()) - (ennemi.getDef() + ennemi.getProtectArmure())))
                self.setMagie(self.getMagie()-10)

    def lancerSortCryo(self, ennemi) :
        randomInt = randint(0,10)
        if (randomInt > ennemi.getAgi()):
            randomInt = randint(0,10)
            if (randomInt <= self.getCrit()) :
                ennemi.setHp(ennemi.getHp() - ((self.getForce() + self.getDegatArme() + self.getCryo())*2 - (ennemi.getDef() + ennemi.getProtectArmure())))
                self.setMagie(self.getMagie()-10)
            else :
                ennemi.setHp(ennemi.getHp() - ((self.getForce() + self.getDegatArme() + self.getCryo()) - (ennemi.getDef() + ennemi.getProtectArmure())))
                self.setMagie(self.getMagie()-10)


    def lancerSortHydro(self, ennemi) :
        randomInt = randint(0,10)
        if (randomInt > ennemi.getAgi()):
            randomInt = randint(0,10)
            if (randomInt <= self.getCrit()) :
                ennemi.setHp(ennemi.getHp() - ((self.getForce() + self.getDegatArme() + self.getDeath()) - (ennemi.getDef() + ennemi.getProtectArmure())))
                self.setMagie(self.getMagie()-10)
            else :
                ennemi.setHp(ennemi.getHp() - ((self.getForce() + self.getDegatArme() + self.getLife()) - (ennemi.getDef() + ennemi.getProtectArmure())))
                self.setMagie(self.getMagie()-10)


    def lancerSortDeath(self, ennemi) :
        randomInt = randint(0,10)
        if (randomInt > ennemi.getAgi()):
            randomInt = randint(0,10)
            if (randomInt <= self.getCrit()) :
                ennemi.setHp(ennemi.getHp() - ((self.getForce() + self.getDegatArme() + self.getDeath())*2 - (ennemi.getDef() + ennemi.getProtectArmure())))
                self.setMagie(self.getMagie()-10)
            else :
                ennemi.setHp(ennemi.getHp() - ((self.getForce() + self.getDegatArme() + self.getDeath()) - (ennemi.getDef() + ennemi.getProtectArmure())))
                self.setMagie(self.getMagie()-10)


    def lancerSortLife(self, ennemi) :
        randomInt = randint(0,10)
        if (randomInt > ennemi.getAgi()):
            randomInt = randint(0,10)
            if (randomInt <= self.getCrit()) :
                ennemi.setHp(ennemi.getHp() - ((self.getForce() + self.getDegatArme() + self.getLife())*2 - (ennemi.getDef() + ennemi.getProtectArmure())))
                self.setMagie(self.getMagie()-10)
            else :
                ennemi.setHp(ennemi.getHp() - ((self.getForce() + self.getDegatArme() + self.getLife()) - (ennemi.getDef() + ennemi.getProtectArmure())))
                self.setMagie(self.getMagie()-10)

    #endregion

    #region getter Mage
    def getMagie(self):
        return self.__magie

    def getMagieMax(self):
        return self.__magieMax
    #endregion

    #region setter Mage
    def setMagie(self, magie):
        self.__magie = magie
    #endregion

class Pretre(Personnage) :
    
    def __init__(self, magie = 100.0, magieMax = 100.0):
        super().__init__()
        self.setCrit(3)
        self.__magie = magie
        self.__magieMax = magieMax
    
    def equiperWeapon(self, arme):
        if (isinstance(arme, Baton.__class__)):
            self.equiperArme(arme)
        else:
            print("Cette arme ne me sied guère ")

    def equiperArmor(self, armure):
        if (isinstance(armure, ArmureLégère.__class__)):
            self.equiperArme(armure)
            self.setDef(self.getDef()+armure.getProtection())
        else:
                print("Cette armure ne me convient pas")
    
    #region sort Pretre
    def sortSoin(self, allier) :
        randomInt = randint(0,10)
        if (randomInt > allier.getAgi()):
            randomInt = randint(0,10)
            if (randomInt <= self.getCrit()) :
                allier.setHp(allier.getHp()+5*2)
                self.setMagie(self.getMagie()-10)
            else:
                allier.setHp(allier.getHp()+5)
                self.setMagie(self.getMagie()-10)
            
    def sortDef(self, allier) :
        randomInt = randint(0,10)
        if (randomInt > allier.getAgi()):
            randomInt = randint(0,10)
            if (randomInt <= self.getCrit()) :
                allier.setDef(allier.getDef()+3*2)
                self.setMagie(self.getMagie()-10)
            else:
                allier.setDef(allier.getDef()+3)
                self.setMagie(self.getMagie()-10)

    def sortAgi(self, allier) :
        randomInt = randint(0,10)
        if (randomInt > allier.getAgi()):
            randomInt = randint(0,10)
            if (randomInt <= self.getCrit()) :
                allier.setAgi(allier.getAgi()+2*2)
                self.setMagie(self.getMagie()-10)
            else:
                allier.setAgi(allier.getAgi()+2)
                self.setMagie(self.getMagie()-10)
    #endregion

    #region getter Pretre
    def getMagie(self):
        return self.__magie

    def getMagieMax(self):
        return self.__magieMax
    #endregion

    #region setter Pretre
    def setMagie(self, magie):
        self.__magie = magie
    #endregion

class Voleur(Personnage):

    def __init__(self):
        super().__init__()
        self.setCrit(4)
        self.setPenArmure(1.3)

    def equiperWeapon(self, arme):
        if (isinstance(arme, Dague.__class__)):
            self.equiperArme(arme)
        else:
            print("Cette arme ne me sied guère ")

    def equiperArmor(self, armure):
        if (isinstance(armure, ArmureLégère.__class__)):
            self.equiperArme(armure)
            self.setDef(self.getDef()+armure.getProtection())
        else:
            print("Cette armure ne me convient pas")

    #uniquement pour le fun
    def backstab(self, ennemi):
        ennemi.setHp(ennemi.getHp() - ennemi.getHp())

    def attaqueRapide(self, ennemi):
            randomInt = randint(0,10)
            if (randomInt > ennemi.getAgi()):
                randomInt = randint(0,10)
                if (randomInt <= self.getCrit()) :
                    ennemi.setHp(ennemi.getHp() - ((self.getForce() + self.getDegatArme())*2 - (ennemi.getDef() + ennemi.getProtectArmure())/self.getDefPen()))
                    self.setStamina(self.getStamina()-10)
                else :
                    ennemi.setHp(ennemi.getHp() - ((self.getForce() + self.getDegatArme()) - (ennemi.getDef() + ennemi.getProtectArmure())/self.getDefPen()))
                    self.setStamina(self.getStamina()-10)

class Archer(Personnage):
        
        def __init__(self):
            super().__init__()
            self.setCrit(4)

        def equiperWeapon(self, arme):
            if (isinstance(arme, Arc.__class__)):
                self.equiperArme(arme)
            else:
                print("Cette arme ne me sied guère ")

        def equiperArmor(self, armure):
            if (isinstance(armure, ArmureLégère.__class__)):
                self.equiperArme(armure)
                self.setDef(self.getDef()+armure.getProtection())
            else:
                print("Cette armure ne me convient pas")

        def tir(self, ennemi):
            randomInt = randint(0,10)
            if (randomInt > ennemi.getAgi()):
                randomInt = randint(0,10)
                if (randomInt <= self.getCrit()) :
                    ennemi.setHp(ennemi.getHp() - ((self.getForce() + self.getDegatArme())*2 - (ennemi.getDef() + ennemi.getProtectArmure())/self.getDefPen()))
                    self.setStamina(self.getStamina()-10)
                else :
                    ennemi.setHp(ennemi.getHp() - ((self.getForce() + self.getDegatArme()) - (ennemi.getDef() + ennemi.getProtectArmure())/self.getDefPen()))
                    self.setStamina(self.getStamina()-10)

class Gladiateur(Personnage):

    def __init__(self):
        super().__init__()
        self.setPenArmure(1.2)
    
    def equiperWeapon(self, arme):
        if (isinstance(arme, Epee.__class__)):
            self.equiperArme(arme)
            self.setForce(self.getForce()+self.getDegatArme())
        else:
            print("Cette arme ne me sied guère ")

    def equiperArmor(self, armure):
        if (isinstance(armure, ArmureLourde.__class__)):
            self.equiperArme(armure)
            self.setDef(self.getDef())
        else:
            print("Cette armure ne me convient pas")

    def estoc(self, ennemi):
        randomInt = randint(0,10)
        if (randomInt > ennemi.getAgi()):
            randomInt = randint(0,10)
            if (randomInt <= self.getCrit()) :
                ennemi.setHp(ennemi.getHp() - ((self.getForce() + self.getDegatArme())*2 - (ennemi.getDef() + ennemi.getProtectArmure())/self.getDefPen()))
                self.setStamina(self.getStamina()-10)
            else :
                ennemi.setHp(ennemi.getHp() - ((self.getForce() + self.getDegatArme()) - (ennemi.getDef() + ennemi.getProtectArmure())/self.getDefPen()))
                self.setStamina(self.getStamina()-10)

class Paladin(Personnage):

    def __init__(self):
        super().__init__()
        self.setPenArmure(1.2)
    
    def equiperWeapon(self, arme):
        if (isinstance(arme, BouclierLance.__class__)):
            self.equiperArme(arme)
            self.setForce(self.getForce()+self.getDegatArme())
        else:
            print("Cette arme ne me sied guère ")

    def equiperArmor(self, armure):
        if (isinstance(armure, ArmureLourde.__class__)):
            self.equiperArme(armure)
            self.setDef(self.getDef())
        else:
            print("Cette armure ne me convient pas")

    def parade(self, ennemi):
        randomInt = randint(0,10)
        if (randomInt > ennemi.getAgi()):
            randomInt = randint(0,10)
            if (randomInt <= self.getCrit()) :
                self.setDef(self.getDef()+self.getDegatArme()*2)
                self.setStamina(self.getStamina()-10)
            else :
                self.setDef(self.getDef()+self.getDegatArme())
                self.setStamina(self.getStamina()-10)

class RPG :
    
    def chooseClass():
        
        print("Choississez votre classe \n 1. Gladiateur \n 2. Archer \n 3. Voleur \n 4. Mage")
        playerClass = int(input())
        while (playerClass <1 or playerClass >4):
            print("Ce que vous avez entrer n'est pas correct.")
            playerClass = int(input())
        if (playerClass == 1):
            player = Gladiateur()
            print("Vous avez choisi la classe Gladiateur.")
        elif (playerClass == 2):
            player = Archer()
            print("Vous avez choisi la classe Archer.")
        elif (playerClass == 3):
            player = Voleur()
            print("Vous avez choisi la classe Voleur.")
        elif (playerClass == 4):
            player = Mage()
            print("Vous avez choisi la classe Mage.")
        RPG.playGame(player, playerClass)

    def playGame(player, playerClass):

        nbEnemiVaincu = 0
        palierNiveau = [1,2]

        while (player.estVivant() != False):

            enemyClass = randint(0,4)
            if (enemyClass == 1):
                ennemi = Gladiateur()
                print("Vous allez affronter un Gladiateur.")
            elif (enemyClass == 2):
                ennemi = Archer()
                print("Vous allez affronter un Archer.")
            elif (enemyClass == 3):
                ennemi = Voleur()
                print("Vous allez affronter un Voleur.")
            elif (enemyClass == 4):
                ennemi = Mage()
                print("Vous allez affronter un Mage.")

            print("Voulez vous voir vos statistiques ? \n 1. Oui \n 2. Non")
            stat = int(input())
            while(stat < 1 or stat > 2):
                print("Ce que vous avez entrer n'est pas correct.")
                stat = int(input())
            if (stat == 1):
                if (playerClass == 4):
                    print("Voici vos statistiques :", "Niveau :" ,player.getNiveau(), ", vous avez",  player.getHp(), "Hp,", "vous avez",player.getForce(), "points de force,", "vous avez", player.getDef(), "points de def,", "vous avez", player.getAgi(), "points d'agilité,", "vous avez",player.getCrit(), "points de chance critique,","vous avez", player.getMagie() , "points de magie")
                else :
                    print("Voici vos statistiques :", "Niveau :" ,player.getNiveau(), ", vous avez",  player.getHp(), "Hp,", "vous avez",player.getForce(), "points de force,", "vous avez", player.getDef(), "points de def,", "vous avez", player.getAgi(), "points d'agilité,", "vous avez",player.getCrit(), "points de chance critique,","vous avez", player.getStamina() , "points de stamina")
            elif( stat == 2):
                print("Vous allez donc directement passer au combat.")

            while (ennemi.estVivant() == True):
                print("Il reste", ennemi.getHp(), "pv à l'ennemi")
                print("Que voulez vous faire ? \n 1. Attaquer \n 2. Magie \n 3. Objets \n 4. Autre")
                action = int(input())
                if (action == 1):
                    if (playerClass == 1):
                        print("Quelle attaque voulez vous utiliser ? \n 1. Attaque normale \n 2. Estoc (Consomme de la stamina)")
                        choix = int(input())
                        if (choix == 1):
                            player.attaquer(ennemi)
                        elif (choix == 2):
                            player.estoc(ennemi)
                    elif (playerClass == 2):
                        print("Quelle attaque voulez vous utiliser ? \n 1. Attaque normale \n 2. Tir (Consomme de la stamina)")
                        choix = int(input())
                        if (choix == 1):
                            player.attaquer(ennemi)
                        elif (choix == 2):
                            player.tir(ennemi)
                    elif (playerClass == 3):
                        print("Quelle attaque voulez vous utiliser ? \n 1. Attaque normale \n 2. Attaque rapide (Consomme de la stamina)")
                        choix = int(input())
                        if (choix == 1):
                            player.attaquer(ennemi)
                        elif (choix == 2):
                            player.attaqueRapide(ennemi)
                        elif (choix == 3):
                            player.backstab(ennemi)
                    elif (playerClass == 4):
                        print("Quelle attaque voulez vous utiliser ? \n 1. Attaque normale \n 2. Sort de feu (Consomme de la magie) \n 3. Sort de glace (Consomme de la magie) \n 4. Sort d'eau (Consomme de la magie) \n 5. Sort de mort (Consomme de la magie) \n 6. Sort de vie (Consomme de la magie)")
                        choix = int(input())
                        if (choix == 1):
                            player.attaquer(ennemi)
                        elif (choix == 2):
                            player.lancerSortFeu(ennemi)
                        elif (choix == 3):
                            player.lancerSortCryo(ennemi)
                        elif (choix == 4):
                            player.lancerSortHydro(ennemi)
                        elif (choix == 5):
                            player.lancerSortDeath(ennemi)
                        elif (choix == 6):
                            player.lancerSortLife(ennemi)

                elif (action == 2):
                    print("Quel sort voulez vous utiliser ?")
                elif (action == 3):
                    print("Quelle potion voulez vous utiliser ? \n 1. Potion de mana \n 2. Potion de force \n 3. Potion de defense \n 4. Potion de soin \n 5. Potion de stamina \n 6. Potion de chance critique \n 7. Potion de d'agilite (chance d'esquiver)")
                    choix = int(input())
                    if(choix == 1):
                        Potions().setPotMana(-1)
                        player.setMagie(player.getMagieMax() * (10/player.getMagieMax))
                    elif(choix == 2):
                        Potions().setPotForce(-1)
                        player.setForce(player.getForce() * (10/player.getForce()))
                    elif(choix == 3):
                        Potions().setPotDef(-1)
                        player.setDef(player.getDef() * (10/player.getDef()))
                    elif(choix == 4):
                        Potions().setPotSoin(-1)
                        player.setHp(player.getHp() * (10/player.getHp()))
                    elif(choix == 5):
                        Potions().setPotStamina(-1)
                        player.setStamina(player.getStamina() * (10/player.getStamina()))
                    elif(choix == 6):
                        Potions().setPotCrit(-1)
                        player.setCrit(player.getCrit() * (10/player.getCrit()))
                    elif(choix == 7):
                        Potions().setPotAgi(-1)
                        player.setAgi(player.getAgi() * (10/player.getAgi()))
                elif(action == 4) :
                    print("Que voulez vous faire ? \n 1. Voir vos statistiques.\n 2. Voir vos potions.")
                    choix = int(input())
                    if(choix == 1):
                        if (playerClass == 4):
                            print("Voici vos statistiques :", "Niveau :" ,player.getNiveau(), ", vous avez",  player.getHp(), "Hp,", "vous avez",player.getForce(), "points de force,", "vous avez", player.getDef(), "points de def,", "vous avez", player.getAgi(), "points d'agilité,", "vous avez",player.getCrit(), "points de chance critique,","vous avez", player.getMagie(), "points de magie")
                        else :
                            print("Voici vos statistiques :", "Niveau :" ,player.getNiveau(), ", vous avez",  player.getHp(), "Hp,", "vous avez",player.getForce(), "points de force,", "vous avez", player.getDef(), "points de def,", "vous avez", player.getAgi(), "points d'agilité,", "vous avez",player.getCrit(), "points de chance critique,","vous avez", player.getStamina(), "points de Stamina")
                    elif(choix == 2):
                        print("Vous avez", Potions().getPotMana(), "potions de mana,", "vous avez", Potions().getPotForce(), "potions de force,", "vous avez", Potions().getPotDef(), "potions de defense,", "vous avez", Potions().getPotSoin(), "potions de soin,",  "vous avez", Potions().getPotStamina(), "potions de stamina,", "vous avez", Potions().getPotCrit(), "potions de chance critique,", "vous avez", Potions().getPotAgi(), "potions de d'agilite.")
                    elif (choix == 3):
                        exit()
            
            if (ennemi.estVivant()==False):
                print("Vous avez vaincu l'ennemi !")
                nbEnemiVaincu +=1
                if (nbEnemiVaincu == 1 or nbEnemiVaincu == 2):
                    player.setNiveau(player.getNiveau() +1)
                    print("Vous êtes maintenant niveau", player.getNiveau() ,"!")
                elif(nbEnemiVaincu == (palierNiveau[len(palierNiveau)-2] + palierNiveau[len(palierNiveau)-1])):
                    player.setNiveau(player.getNiveau() +1)
                    print("Vous êtes maintenant niveau", player.getNiveau() ,"!")
                    palierNiveau.append(nbEnemiVaincu)

RPG.chooseClass()