#Author: Gary Fleming
import abc;
class Observer(object):
    __metaclas__ = abc.ABCMeta;
    @abc.abstractmethod
    def update(self):
        pass;

class Observable(object):
    def __init__(self):
        self.observers = list();

    def addObserver(self,obs):
        self.observers.append(obs);

    def delObserver(self,obs):
        if obs in self.observers:
            self.observers.remove(obs);

    def updateObservers(self):
        for obs in self.observers:
            obs.update();
