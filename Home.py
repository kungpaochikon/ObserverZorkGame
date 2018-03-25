import random;
from Obs import Observer, Observable;
from NPC import Person, Zombie, Vampire, Ghoul, Werewolf;
class Home(Observable, Observer):
    def __init__(self):
        super().__init__();
        self.popMonsters = random.randint(0,10);
        self.popPeople = 0;
        self.npcs = list();
        for i in range(self.popMonsters):
            roll = random.randint(0,3);
            npc = Zombie();
            if(roll==0):
                npc = Vampire();
            elif(roll==1):
                npc = Ghoul();
            elif(roll==2):
                npc = Werewolf();
            npc.addObserver(self);
            self.npcs.append(npc);

    def getPopMonsters(self):
        return self.popMonsters;

    def getPopPeople(self):
        return self.popPeople;

    def getPopDamage(self):
        dmg = 0;
        for i in self.npcs:
            dmg += i.getDamage();
        return dmg;

    def damagePop(self,dmg,wpnTitle):
        for i in self.npcs:
            i.calcDamage(dmg,wpnTitle);

    def updatePop(self):
        for i in range(len(self.npcs)):
            self.npcs[i].check();
            if(self.npcs[i].getHP()<1):
                self.npcs[i] = Person();

    def fullDisplay(self):
        print("Details: ");
        for i in self.npcs:
            print(i.getTitle() + ": " + str(i.getHP()) + "HP.");

    def update(self):
        self.popMonsters -= 1;
        self.updateObservers();
