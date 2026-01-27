from piece import *


class Dame(Piece) : 
    def avancer(self, new_x, new_y, plateau) : 
        if (new_x == self.x and new_y != self.y) or  (new_y == self.y  and new_x != self.x) or ( abs(new_x - self.x) == abs(new_y - self.y)): 
            self.x = new_x
            self.y = new_y
            return True


class Tour(Piece) : 
    def avancer(self, new_x, new_y, plateau) : 
        if (new_x == self.x and new_y != self.y) or  (new_y == self.y  and new_x != self.x) : 
            self.x = new_x
            self.y = new_y
            return True 

        self.selectionne = False
    

class Fou(Piece) : 

    def avancer(self, new_x, new_y, plateau) : 
        if abs(new_x - self.x) == abs(new_y - self.y) : 
            self.x = new_x
            self.y = new_y
            return True 

        self.selectionne = False


class Roi(Piece) : 

    def avancer(self, new_x, new_y, plateau) : 
        if abs(new_x - self.x) <= 1 and abs(new_y - self.y) <= 1 and not (new_x == self.x and new_y == self.y):     
            self.y = new_y
            return True 

        self.selectionne = False

class Pion(Piece): 

    def avancer(self, new_x, new_y, plateau): 
        direction = -1 if self.couleur == 'w' else 1
        
        diff_x = new_x - self.x
        diff_y = new_y - self.y
        
        cible = plateau[new_y][new_x]

       # Aller tout droit  
        if diff_x == 0:
            if diff_y == direction:
                if cible is None: # personne devant
                    self.x = new_x
                    self.y = new_y
                    return True

            start_row = 6 if self.couleur == 'w' else 1
            if self.y == start_row and diff_y == 2 * direction:
                # Il faut que la cible soit vide et la case intermédiaire aussi
                intermediaire = plateau[self.y + direction][self.x]
                if cible is None and intermediaire is None:
                    self.x = new_x
                    self.y = new_y
                    return True
    #aller en diagnolae
        elif abs(diff_x) == 1 and diff_y == direction:
            if cible is not None and cible.couleur != self.couleur:
                self.x = new_x
                self.y = new_y
                return True

        # Si aucun cas ne marche
        self.selectionne = False
        return False

class Cavalier(Piece): 

    def avancer(self, new_x, new_y , plateau): 
        # Vérifie si le mouvement est en "L" :
        dx = abs(new_x - self.x)
        dy = abs(new_y - self.y)

        if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
            self.x = new_x
            self.y = new_y
            return True 

        
        self.selectionne = False