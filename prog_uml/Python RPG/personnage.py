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

class Personnage :

    __niveauMax = 100

    def __init__(self, niveau = 1, force = 10, defense = 5, hp = 100, hpMax = 100) :
        self.__niveau = niveau
        self.__force = force
        self.__defense = defense
        self.__hp = hp
        self.__hpMax = hpMax
        self.__armeEquiper = Armes()
        self.__armureEquiper = Armures()

    def estVivant(self) : 
        return self.__hp > 0 

    def equiperArme(self, arme):
        self.__armeEquiper = arme

    def equiperArmure(self, armure):
        self.__armureEquiper = armure
    
    def attaquer(self, ennemie) :
        ennemie.__hp -= ((self.__force + self.getDegatArme()) - (ennemie.__defense + ennemie.__armureEquiper.getProtection()))

    
    #region getter Personnage
    def getHp(self):
        return self.__hp
    
    def getForce(self):
        return self.__force

    def getDef(self):
        return self.__defense
    
    def getNivMax():
        return Personnage.__niveauMax

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
    
    def setForce(self, force):
        self.__force = force

    def setDef(self, defense):
        self.__defense = defense
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


class ArmureLourde(Armures):
    def __init__(self, protection=6):
        super().__init__(self)

class ArmureLégère(Armures):
    def __init__(self, protection=3):
        super().__init__(self)


class Mage(Personnage, Elements) : 
    
    def __init__(self):
        Personnage.__init__(self)
        Elements.__init__(self)
        self.__magie = 100

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

    #region sortMage
    def lancerSortFeu(self, ennemie) :
        ennemie.setHp(ennemie.getHp() - ((self.getForce() + self.getPyro()) - ennemie.getDef()))

    def lancerSortCryo(self, ennemie) :
        ennemie.setHp(ennemie.getHp() - ((self.getForce() + self.getCryo()) - ennemie.getDef()))

    def lancerSortHydro(self, ennemie) :
        ennemie.setHp(ennemie.getHp() - ((self.getForce() + self.getHydro()) - ennemie.getDef()))

    def lancerSortDeath(self, ennemie) :
        ennemie.setHp(ennemie.getHp() - ((self.getForce() + self.getDeath()) - ennemie.getDef()))

    def lancerSortLife(self, ennemie) :
        ennemie.setHp(ennemie.getHp() - ((self.getForce() + self.getLife()) - ennemie.getDef()))
    #endregion

    #region getter Mage
    def getMagie(self):
        return self.__magie
    #endregion

class Pretre(Personnage) :
    
    def __init__(self):
        super().__init__()
        self.__magie = 100
    
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
    
    def Heal(self, allier) :
        allier.setHp(allier.getHp()+5)

class Voleur(Personnage):

    def __init__(self):
        super().__init__()

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

    def backstab(self, ennemie):
        ennemie.setHp(ennemie.getHp() - ennemie.getHp())

class Archer(Personnage):
        
        def __init__(self):
            super().__init__()
            self.__dexterite = 10

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

        def tir(self, ennemie):
            ennemie.setHp(ennemie.getHp() - (5-ennemie.getDef()))

class Gladiateur(Personnage):

    def __init__(self):
        super().__init__()
    
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

class RPG :
    
    def playTheGame():
        voleur = Voleur()
        mage = Mage()
        archer = Archer()
        gladiateur = Gladiateur()
        print(gladiateur.getForce())
        gladiateur.equiperArme(Epee())
        print(gladiateur.getDegatArme())
        gladiateur.equiperArmure(ArmureLourde())
        gladiateur.attaquer(mage)
        print(mage.getHp())



RPG.playTheGame()