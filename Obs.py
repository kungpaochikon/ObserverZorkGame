#Author: Gary Fleming

#Guidance From:
#https://docs.python.org/2/library/abc.html

import abc;

'''
Observer and Observable basic structure

Observable keeps track of instances that
need to be notified of changes.

Observer serves only to be updated
when an observable signals and update
'''

class Observer(object):
    #Make Abstract
    __metaclas__ = abc.ABCMeta;
    
    #Interface Method
    @abc.abstractmethod
    def update(self):
        pass;

class Observable(object):
    def __init__(self):
        self.observers = list();

    def addObserver(self,obs):
        self.observers.append(obs);

    def updateObservers(self):
        for obs in self.observers:
            obs.update();
