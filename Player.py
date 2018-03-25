#Author: Gary Fleming
from Actor import Actor;
import random;
from Weapon import HersheyKiss,SourStraw,ChocolateBar,NerdBomb;
class Player(Actor):

    def __init__(self):
        super().__init__("Player",100,125,10,20);
        self.inv = list();
        self.invMax = 10;
        self.inv.append(HersheyKiss());
        for i in range(9):
            roll = random.randint(0,2);
            item = NerdBomb();
            if(roll==0):
                item = SourStraw();
            elif(roll==1):
                item = ChocolateBar();
            self.inv.append(item);


    def printInv(self):
        print("inv:");
        for i in range(len(self.inv)):
            print("" + str(i) + ".) "+str(self.inv[i].getUses())+" - "+self.inv[i].getTitle());

    def getInv(self):
        return self.inv;

    def modInv(self,slot,val):
        if(not isinstance(self.inv[slot],HersheyKiss)):
            self.inv[slot].modUses(-1);

    def updateInv(self):
        #for i in range(len(self.inv)):
        #    if(self.inv[i].getUses()<1):
        #        del self.inv[i];
        #        i = i-1;
        #DOESN"T WORK

        #Learned how to do this from:
        #https://stackoverflow.com/questions/1207406/how-to-remove-items-from-a-list-while-iterating/1207427
        self.inv = [x for x in self.inv if not x.getUses()<1];
            
            
