import random;
class Actor():

    def __init__(self,title,hpLower,hpUpper,dmgLower,dmgUpper):
        self.hp = random.randint(hpLower,hpUpper);
        self.dmgLower = dmgLower;
        self.dmgUpper = dmgUpper;
        self.title = title;

    def getDamage(self):
        return random.randint(self.dmgLower,self.dmgUpper);

    def modHP(self,val):
        self.hp += val;
        if self.hp<1:
            #do stuff when dead
            pass;

    def getTitle(self):
        return self.title;

    def getHP(self):
        return self.hp;
