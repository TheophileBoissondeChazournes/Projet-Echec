from piece import *


class Dame(Piece) : 
    def __init__(self) : 
        self.image

    def avancer(self, new_x, new_y) : 
        if (new_x == self.x and new_y != self.y) or  (new_y == self.y  and new_y != self.y) or ( abs(new_x - self.x) == abs(new_y - self.y)): 
            self.x = new_x
            self.y = new_y


class Tour(Piece) : 
    def avancer(self, new_x, new_y) : 
        if (new_x == self.x and new_y != self.y) or  (new_y == self.y  and new_y != self.y) : 
            self.x = new_x
            self.y = new_y
        self.selectionne = False
    

class Fou(Piece) : 

    def avancer(self, new_x, new_y) : 
        if abs(new_x - self.x) == abs(new_y - self.y) : 
            self.x = new_x
            self.y = new_y
        self.selectionne = False


class Roi(Piece) : 

    def avancer(self, new_x, new_y) : 
        if (abs(new_x - self.x) == 1 )or (abs(new_y - self.y) == 1 ) : 
            self.x = new_x
            self.y = new_y
        self.selectionne = False

class Pion(Piece) : 

    def avancer(self, new_x, new_y) : 
        gap = 2 if self.y == 2 else 1
        if new_x - self.x ==  gap: 
            self.x = new_x
            self.y = new_y

        self.selectionne = False


