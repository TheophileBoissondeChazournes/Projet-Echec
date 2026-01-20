
class Piece():
    def __init__(self, x, y, couleur) : 
        self.x = x
        self.y = y
        self.couleur = couleur
        self.image = None   
        self.selectionne = False
        self.vivant = True



class Dame(Piece) : 

    def avancer(self, new_x, new_y) : 
        if (new_x == self.x and new_y != self.y) or  (new_y == self.y  and new_y != self.y) or ( abs(new_x - self.x) == abs(new_y - self.y)): 
            self.x = new_x
            self.y = new_y

    def mourir(self) : 
        self.vivant = False


class Tour(Piece) : 
    def avancer(self, new_x, new_y) : 
        if (new_x == self.x and new_y != self.y) or  (new_y == self.y  and new_y != self.y) : 
            self.x = new_x
            self.y = new_y
        self.selectionne = False
    
    def mourir(self) : 
        self.vivant = False
