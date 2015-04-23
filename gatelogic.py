#!/usr/bin/env python


class LogicGate:
    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.PinA = None
        self.PinB = None

    def getPinA(self):
        return int(input("Enter Pin A input for gate %s:" % self.getLabel()))
    def getPinB(self):
        return int(input("Enter Pin B input for gate %s:" % self.getLabel()))

class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.Pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate %s:" % self.getLabel()))

class AndGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if ( a and b):
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if (a or b):
            return 1
        else:
            return 0

class NotGate(UnaryGate):
    def __init__(self,n):
        UnaryGate.__init__(self,n)
    def performGateLogic(self):
        a = self.getPin()
        if a == 1:
            return 0
        else:
            return 1


g1 = AndGate("Gate1")
g2 = NotGate("Gate2")
print(g1.getOutput())
print(g2.getOutput())

