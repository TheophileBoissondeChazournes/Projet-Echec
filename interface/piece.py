
class Piece():
    def __init__(self, x, y, couleur) : 
        self.x = x
        self.y = y
        self.couleur = couleur
        self.selectionne = False
        self.vivant = True
        self.saute_obstacle= False 

    def manger (self, piece2 : 'Piece'):
            # On vérifie qu'on ne mange pas ses propres pieces
            if self.couleur != piece2.couleur:
                # On tue l'autre pièce
                piece2.vivant = False 
               
    def chemin_est_possible (self, depart: tuple, arrivee: tuple, plateau):
        
        x1, y1 = depart
        x2, y2 = arrivee

        if not (0 <= x2 < 8 and 0 <= y2 < 8):
            return False

        # on vérifie que la pièce n'est pas un cavalier :
        if not self.saute_obstacle : 
    
            # On calcule le sens du déplacement (-1, 0 ou 1)
            
            if x2 > x1: pas_x = 1
            elif x2 < x1: pas_x = -1
            else: pas_x = 0 # Mouvement vertical
            
            if y2 > y1: pas_y = 1
            elif y2 < y1: pas_y = -1
            else: pas_y = 0 # Mouvement horizontal
            
            # On commence à la première case après le départ
            #curr_x, curr_y = x1 + pas_x, y1 + pas_y
            
            # Tant qu'on n'est pas arrivé à la destination
            while (x1, y1) != (x2, y2):

                if plateau[y1][x1] is not None:
                    return False # Obstacle 
            
                x1 += pas_x
                y1 += pas_y

        if plateau[y2][x2] is None : 
             return True 
        else :
            piece_arrivee = plateau[y2][x2]
            if piece_arrivee.couleur == self.couleur : 
                 return False 
            

        
                