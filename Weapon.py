import random;
class Weapon():
    def __init__(self,modLower,modUpper,uses,title):
        self.modLower = modLower;
        self.modUpper = modUpper;
        self.uses = uses;
        self.title = title;

    def modUses(self,val):
        self.uses += val;

    def getUses(self):
        return self.uses;

    def getMod(self):
        return random.uniform(self.modLower,self.modUpper);

    def getTitle(self):
        return self.title;


class HersheyKiss(Weapon):
    def __init__(self):
        super().__init__(1,1,1,"HersheyKiss");

class SourStraw(Weapon):
    def __init__(self):
        super().__init__(1,1.75,2,"SourStraw");

class ChocolateBar(Weapon):
    def __init__(self):
        super().__init__(2,2.4,4,"ChocolateBar");

class NerdBomb(Weapon):
    def __init__(self):
        super().__init__(3.5,5,1,"NerdBomb");
