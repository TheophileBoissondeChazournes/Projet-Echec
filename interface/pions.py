from piece import *


class Dame(Piece) : 
    def avancer(self, new_x, new_y) : 
        if (new_x == self.x and new_y != self.y) or  (new_y == self.y  and new_x != self.x) or ( abs(new_x - self.x) == abs(new_y - self.y)): 
            self.x = new_x
            self.y = new_y
            return True


class Tour(Piece) : 
    def avancer(self, new_x, new_y) : 
        if (new_x == self.x and new_y != self.y) or  (new_y == self.y  and new_x != self.x) : 
            self.x = new_x
            self.y = new_y
            return True 

        self.selectionne = False
    

class Fou(Piece) : 

    def avancer(self, new_x, new_y) : 
        if abs(new_x - self.x) == abs(new_y - self.y) : 
            self.x = new_x
            self.y = new_y
            return True 

        self.selectionne = False


class Roi(Piece) : 

    def avancer(self, new_x, new_y) : 
        if abs(new_x - self.x) <= 1 and abs(new_y - self.y) <= 1 and not (new_x == self.x and new_y == self.y):     
            self.y = new_y
            return True 

        self.selectionne = False

class Pion(Piece) : 

    def avancer(self, new_x, new_y) : 
        gap = 2 if (self.y == 1) or (self.y == 6) else 1
        if (abs(new_y - self.y) ==  gap or abs(new_y - self.y )==  1) and (new_x == self.x) : 
            self.x = new_x
            self.y = new_y
            return True 


        self.selectionne = False


class Cavalier(Piece): 

    def avancer(self, new_x, new_y): 
        # Vérifie si le mouvement est en "L" :
        dx = abs(new_x - self.x)
        dy = abs(new_y - self.y)

        if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
            self.x = new_x
            self.y = new_y
            return True 

        
        self.selectionne = False