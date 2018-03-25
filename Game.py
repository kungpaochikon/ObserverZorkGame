#Author: Gary Fleming
from Neighborhood import Neighborhood;
from Player import Player;
import sys;
from Obs import Observer;

class Game(Observer):
    def __init__(self):
        self.running = True;
        self.x = 0;
        self.y = 0;
        self.nbh = Neighborhood(5,5);
        self.nbh.addObserver(self);
        self.monsterCount = self.nbh.getMonsterCount();
        self.player = Player();
        self.go();


    def go(self):
        print();
        print("Welcome to ZorkGame!");

        while(self.running):
            print("");
            self.displayMap();
            print("");
            print("You are at X:"+str(self.x)+", Y:"+str(self.y));
            print(str(self.monsterCount) + " Monsters Remain in Total!");
            print("You have "+str(self.player.getHP())+" HP Remaining!");
            print("");
            print("Choices:\n"
                  "1.) Combat\n"
                  "2.) Move\n"
                  "3.) House Details\n"
                  "4.) Quit\n");
            print("");
            choice = -1;
            try:
                choice = int(input("?: "));
            except ValueError:
                print("Input Error: Please only type valid int.");
            #Attack House
            if(choice==1):
                print("Choose Weapon:");
                self.player.printInv();
                slot = -1;
                try:
                    slot = int(input("?: "));
                except ValueError:
                    print("Input Error: Please only type vlaid int.");
                    continue;
                if(slot>=0 and slot<len(self.player.getInv())):
                    pass;
                else:
                    print("Not a valid choice!");
                    continue;
                damage = self.player.getDamage();
                damage *= self.player.getInv()[slot].getMod();
                damage = round(damage,2);
                print("");
                print("You swung for : "+str(damage)+" Damage!!!");
                myDmg = self.nbh.attackHome(self.x,self.y,damage,self.player.getInv()[slot].getTitle());
                self.player.modInv(slot,-1);
                self.player.updateInv();
                self.player.modHP(-myDmg);
                print("You took "+str(myDmg)+" damage!!!");
                
            #Move to Different House
            elif(choice==2):
                print("Choose X Coordinate: ");
                try:
                    choiceX = int(input("?: "));
                except ValueError:
                    print("Input Error: Please only type valid int.");
                    continue;
                if(choiceX>=self.nbh.getRow() or choiceX<0):
                    print("Out of bounds!");
                    continue;
                print("Choose Y Coordinate: ");
                try:
                    choiceY = int(input("?: "));
                except ValueError:
                    print("Input Error: Please only type valid int.");
                    continue;
                if(choiceY>=self.nbh.getCol() or choiceY<0):
                    print("Out of bounds!");
                    continue;
                self.x = choiceX;
                self.y = choiceY;
            #Display Monsters
            elif(choice==3):
                print("");
                self.nbh.printHomeDetails(self.x,self.y);
            #Quit Game
            elif(choice==4):
                print("Thanks for playing!");
                sys.exit();

            if(self.monsterCount<1):
                print("!!!!!!!!!!!!!!!!!!!!!!!!!");
                print("        YOU WIN!!!!      ");
                print("!!!!!!!!!!!!!!!!!!!!!!!!!");
                sys.exit();
            if(self.player.getHP()<1):
                print("!!!!!!!!!!!!!!!!!!!!!!!!!");
                print("        YOU LOSE!!!!     ");
                print("!!!!!!!!!!!!!!!!!!!!!!!!!");
                sys.exit();

    def update(self):
        self.monsterCount-=1;
        print("A monster has been restored to a person!");

    def displayMap(self):
        for i in range(self.nbh.getRow()):
            for j in range(self.nbh.getCol()):
                if(self.nbh.getHomePop(i,j)>0):
                    print("X",end=" ");
                else:
                    print("O",end=" ");
            print("");
        

        
        
