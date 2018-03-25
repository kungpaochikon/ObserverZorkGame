#Author: Gary Fleming
from Home import Home;
from Obs import Observable, Observer;

'''
Neighborhood contains a 2d grid of homes.
Observes homes and is observed by game.
updates when home is update and essentially
delivers the population change to the game.
'''

class Neighborhood(Observable, Observer):
    def __init__(self,row,col):
        super().__init__();
        self.row = row;
        self.col = col;
        self.homes = list();
        for i in range(self.row):
            temp = list();
            for j in range(self.col):
                myHome = Home();
                myHome.addObserver(self);
                temp.append(myHome);
            self.homes.append(temp);
                
        

    def getCol(self):
        return self.col;

    def getRow(self):
        return self.row;

    def getHomePop(self,x,y):
        return self.homes[x][y].getPopMonsters();

    def printHomeDetails(self,x,y):
        self.homes[x][y].fullDisplay();

    def attackHome(self,x,y,dmg,wpnTitle):
        self.homes[x][y].damagePop(dmg,wpnTitle);
        self.homes[x][y].updatePop();
        return self.homes[x][y].getPopDamage();

    def getMonsterCount(self):
        count = 0;
        for i in range(self.row):
            for j in range(self.col):
                count+=self.homes[i][j].getPopMonsters();
        return count;

    def update(self):
        self.updateObservers();
                
    
