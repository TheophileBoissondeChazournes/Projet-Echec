import pyxel
from pions import *


class Plateau:
    def __init__(self):
        # Activation de la souris
        pyxel.init(250, 250, title="Plateau d'échecs")
        pyxel.mouse(True) 
        
        # Dimensions
        self.cell_size = 27
        self.board_size = self.cell_size * 8
        self.offset_x = (250 - self.board_size) // 2 
        self.offset_y = (250 - self.board_size) // 2
        
        self.pieces = [[None for _ in range(8)] for _ in range(8)]
        self.tour = 'w'       # 'w' pour les blancs, 'b' pour les noirs
        self.selection = None 
        
        # Placement initial
        for i in range(8):
            self.pieces[1][i] = Pion(i,1,'b')
            self.pieces[6][i] = Pion(i,6,'w')
        placement = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        for i in ['w', 'b'] : 
            ligne = 7 if i == 'w' else 0
            for j in range(8):
                type_piece = placement[j]
                if type_piece == 'R':
                    self.pieces[ligne][j] = Tour(j, ligne, i)
                elif type_piece == 'N':
                    self.pieces[ligne][j] = Cavalier(j, ligne, i)
                elif type_piece == 'B':
                    self.pieces[ligne][j] = Fou(j, ligne, i)
                elif type_piece == 'Q':
                    self.pieces[ligne][j] = Dame(j, ligne, i)
                elif type_piece == 'K':
                    self.pieces[ligne][j] = Roi(j, ligne, i)
            

        #  DESSINS
        self.modeles_pieces = {
            "Pion": [(7,3),(8,3),(6,4),(7,4),(8,4),(9,4),(5,5),(6,5),(7,5),(8,5),(9,5),(10,5),(6,6),(7,6),(8,6),(9,6),(7,7),(8,7),(5,8),(6,8),(7,8),(8,8),(9,8),(10,8),(5,9),(6,9),(7,9),(8,9),(9,9),(10,9)],
            "Tour": [(5, 2), (7, 2), (9, 2),(5, 3), (6, 3), (7, 3), (8, 3), (9, 3),(6, 4), (7, 4), (8, 4),(6, 5), (7, 5), (8, 5),(6, 6), (7, 6), (8, 6),(6, 7), (7, 7), (8, 7),(6, 8), (7, 8), (8, 8),(6, 9), (7, 9), (8, 9),(6, 10), (7, 10), (8, 10),(6, 11), (7, 11), (8, 11),(5, 12), (6, 12), (7, 12), (8, 12), (9, 12),(4, 13), (5, 13), (6, 13), (7, 13), (8, 13), (9, 13), (10, 13)],
            "Cavalier": [(7, 3),(6, 4), (7, 4), (8, 4),(5, 5), (6, 5), (7, 5), (8, 5), (9, 5),(5, 6), (6, 6), (7, 6), (8, 6), (9, 6),(10,6),(5, 7), (6, 7), (7, 7), (8, 7),(5, 8), (6, 8), (7, 8), (8, 8),(5, 9), (6, 9), (7, 9), (8, 9),(5, 10), (6, 10), (7, 10), (8, 10), (9, 10),(5, 11), (6, 11), (7, 11), (8, 11), (9, 11),(5, 12), (6, 12), (7, 12), (8, 12), (9, 12),(4, 13), (5, 13), (6, 13), (7, 13), (8, 13), (9, 13), (10, 13)],
            "Fou": [(7, 2),(6, 3), (7, 3), (8, 3),(6, 4), (7, 4), (8, 4),(5, 5), (6, 5), (7, 5), (8, 5), (9, 5),(5, 6), (6, 6), (7, 6), (8, 6), (9, 6),(6, 7), (7, 7), (8, 7),(6, 8), (7, 8), (8, 8),(6, 9), (7, 9), (8, 9),(6, 10), (7, 10), (8, 10),(6, 11), (7, 11), (8, 11),(5, 12), (6, 12), (7, 12), (8, 12), (9, 12),(4, 13), (5, 13), (6, 13), (7, 13), (8, 13), (9, 13), (10, 13)],
            "Dame": [(5, 2), (7, 2), (9, 2), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3),(6, 4), (7, 4), (8, 4), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5),(6, 6), (7, 6), (8, 6), (6, 7), (7, 7), (8, 7), (6, 8), (7, 8), (8, 8),(6, 9), (7, 9), (8, 9), (6, 10), (7, 10), (8, 10), (6, 11), (7, 11), (8, 11),(5, 12), (6, 12), (7, 12), (8, 12), (9, 12),(4, 13), (5, 13), (6, 13), (7, 13), (8, 13), (9, 13), (10, 13)],
            "Roi": [(7, 0),(6, 1), (7, 1), (8, 1),(7, 2),(6, 3), (7, 3), (8, 3),(5, 4), (6, 4), (7, 4), (8, 4), (9, 4),(6, 5), (7, 5), (8, 5),(6, 6), (7, 6), (8, 6),(6, 7), (7, 7), (8, 7),(6, 8), (7, 8), (8, 8),(6, 9), (7, 9), (8, 9),(6, 10), (7, 10), (8, 10),(6, 11), (7, 11), (8, 11),(5, 12), (6, 12), (7, 12), (8, 12), (9, 12),(4, 13), (5, 13), (6, 13), (7, 13), (8, 13), (9, 13), (10, 13)]
        }
        #self.map_noms = {'P': 'pion', 'R': 'tour', 'N': 'cavalier', 'B': 'fou', 'Q': 'dame', 'K': 'roi'}

        pyxel.run(self.update, self.draw)

    def update(self):

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            mx = pyxel.mouse_x
            my = pyxel.mouse_y
            
            col = (mx - self.offset_x) // self.cell_size
            ligne = (my - self.offset_y) // self.cell_size
            
            # Vérifier si on a cliqué DANS le plateau
            if 0 <= col < 8 and 0 <= ligne < 8:
                contenu_case = self.pieces[ligne][col]
                
                #Rien n'est sélectionné 
                if self.selection is None:
                    if contenu_case is not None:
                        # On vérifie que la pièce appartient au joueur dont c'est le tour
                        if contenu_case.couleur == self.tour:
                            self.selection = (ligne, col)
                
                # Une pièce est déjà sélectionnée 
                else:
                    sel_l, sel_c = self.selection
                    piece_selectionnee = self.pieces[sel_l][sel_c]
                        
                    # Si on clique sur la MEME case 
                    if (ligne, col) == (sel_l, sel_c):
                        self.selection = None
                        
                    #On vérifie que le déplacement est possible
                    elif  piece_selectionnee.avancer(col, ligne):
                        # On gère la capture si nécessaire
                        cible = self.pieces[ligne][col]
                        if cible is not None:
                            piece_selectionnee.manger(cible)
                            
                        # 1. On déplace la pièce
                        self.pieces[ligne][col] = piece_selectionnee
                        self.pieces[sel_l][sel_c] = None
                        
                        piece_selectionnee.x = col
                        piece_selectionnee.y = ligne

                        # 2. On change de tour
                        self.tour = 'b' if self.tour == 'w' else 'w'
                            
                        # 3. On désélectionne
                        self.selection = None

                    # Si on clique sur une pièce AMIE 
                    elif contenu_case is not None and contenu_case.couleur == self.tour:
                        self.selection = (ligne, col)
                        

    def draw(self):
        pyxel.cls(13)
        
        # Dessin du damier et des pièces
        for ligne in range(8):
            for col in range(8):
                x_case = self.offset_x + col * self.cell_size
                y_case = self.offset_y + ligne * self.cell_size
                couleur_sol = 6 if (ligne + col) % 2 == 0 else 1
                
                if self.selection == (ligne, col):
                    couleur_sol = 10
                
                pyxel.rect(x_case, y_case, self.cell_size, self.cell_size, couleur_sol)

                # Dessin de la pièce
                code_piece = self.pieces[ligne][col]
                if code_piece:
                    couleur_p = code_piece.couleur
                    type_p = code_piece.__class__.__name__  # nom de la classe
                    col_pixel = 7 if couleur_p == 'w' else 0
                    pixels = self.modeles_pieces[type_p]
                    for px, py in pixels:
                        pyxel.pset(x_case + px + 6, y_case + py + 6, col_pixel)

        
        msg = "Tour: BLANCS" if self.tour == 'w' else "Tour: NOIRS"
        col_txt = 7 if self.tour == 'w' else 0
        pyxel.text(5, 5, msg, col_txt)
        
        # Coordonnées
        for col in range(8):
            lettre = chr(ord("A") + col)
            x = self.offset_x + col * self.cell_size + 11
            y = self.offset_y + 8 * self.cell_size + 5
            pyxel.text(x, y, lettre, 0)

        for ligne in range(8):
            nb = str(8 - ligne)
            x = self.offset_x - 10
            y = self.offset_y + ligne * self.cell_size + 11
            pyxel.text(x, y, nb, 0)

Plateau()