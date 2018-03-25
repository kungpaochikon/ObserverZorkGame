from Actor import Actor;
from Obs import Observable;

class NPC(Actor, Observable):

    def __init__(self,title,hpLower,hpUpper,dmgLower,dmgUpper):
        super().__init__(title,hpLower,hpUpper,dmgLower,dmgUpper);
        Observable.__init__(self);

    def calcDamage(self,val,wpnTitle):
        self.modHP(-val);

    def check(self):
        if(self.hp<1):
            self.updateObservers();


class Person(NPC):
    def __init__(self):
        super().__init__("Person",100,100,-1,-1);

    def calcDamage(self,val,wpnTitle):
        pass;

class Zombie(NPC):
    def __init__(self):
        super().__init__("Zombie",50,100,0,10);

    def calcDaamge(self,val,wpnTitle):
        if(wpnTitle=="SourStraw"):
            super().calcDamage(val*2,wpnTitle);
        else:
            super().calcDamage(val,wpnTitle);

class Vampire(NPC):
    def __init__(self):
        super().__init__("Vampire",100,200,10,20);

    def calcDaamge(self,val,wpnTitle):
        if(wpnTitle=="ChocolateBar"):
            super().calcDamage(0,wpnTitle);
        else:
            super().calcDamage(val,wpnTitle);

class Ghoul(NPC):
    def __init__(self):
        super().__init__("Ghoul",40,80,15,30);

    def calcDaamge(self,val,wpnTitle):
        if(wpnTitle=="NerdBomb"):
            super().calcDamage(val*5,wpnTitle);
        else:
            super().calcDamage(val,wpnTitle);

class Werewolf(NPC):
    def __init__(self):
        super().__init__("Werewolf",200,200,0,40);

    def calcDaamge(self,val,wpnTitle):
        if(wpnTitle=="SourStraw" or wpnTitle=="ChocolateBar"):
            super().calcDamage(0,wpnTitle);
        else:
            super().calcDamage(val,wpnTitle);
