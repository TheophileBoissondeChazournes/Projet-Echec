import pyxel
from pions import *
from IA import IA


class Plateau:
    def __init__(self):
        pyxel.init(250, 250, title="Plateau d'échecs")
        pyxel.mouse(True)

        self.ia = IA('b')  # IA joue les noirs

        # Dimensions
        self.cell_size = 27
        self.board_size = self.cell_size * 8
        self.offset_x = (250 - self.board_size) // 2
        self.offset_y = (250 - self.board_size) // 2

        self.pieces = [[None for _ in range(8)] for _ in range(8)]
        self.tour = 'w'  
        self.selection = None

        # Placement initial
        for i in range(8):
            self.pieces[1][i] = Pion(i, 1, 'b')
            self.pieces[6][i] = Pion(i, 6, 'w')

        placement = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        for couleur in ['w', 'b']:
            ligne = 7 if couleur == 'w' else 0
            for j in range(8):
                t = placement[j]
                if t == 'R':
                    self.pieces[ligne][j] = Tour(j, ligne, couleur)
                elif t == 'N':
                    self.pieces[ligne][j] = Cavalier(j, ligne, couleur)
                elif t == 'B':
                    self.pieces[ligne][j] = Fou(j, ligne, couleur)
                elif t == 'Q':
                    self.pieces[ligne][j] = Dame(j, ligne, couleur)
                elif t == 'K':
                    self.pieces[ligne][j] = Roi(j, ligne, couleur)

        # Dessins
        self.modeles_pieces = {
            "Pion": [(7,3),(8,3),(6,4),(7,4),(8,4),(9,4),(5,5),(6,5),(7,5),(8,5),(9,5),(10,5),(6,6),(7,6),(8,6),(9,6),(7,7),(8,7),(5,8),(6,8),(7,8),(8,8),(9,8),(10,8),(5,9),(6,9),(7,9),(8,9),(9,9),(10,9)],
            "Tour": [(5, 2),(7, 2),(9, 2),(5, 3),(6, 3),(7, 3),(8, 3),(9, 3),(6, 4),(7, 4),(8, 4),(6, 5),(7, 5),(8, 5),(6, 6),(7, 6),(8, 6),(6, 7),(7, 7),(8, 7),(6, 8),(7, 8),(8, 8),(6, 9),(7, 9),(8, 9),(6, 10),(7, 10),(8, 10),(6, 11),(7, 11),(8, 11),(5, 12),(6, 12),(7, 12),(8, 12),(9, 12),(4, 13),(5, 13),(6, 13),(7, 13),(8, 13),(9, 13),(10, 13)],
            "Cavalier": [(7, 3),(6, 4),(7, 4),(8, 4),(5, 5),(6, 5),(7, 5),(8, 5),(9, 5),(5, 6),(6, 6),(7, 6),(8, 6),(9, 6),(10,6),(5, 7),(6, 7),(7, 7),(8, 7),(5, 8),(6, 8),(7, 8),(8, 8),(5, 9),(6, 9),(7, 9),(8, 9),(5, 10),(6, 10),(7, 10),(8, 10),(9, 10),(5, 11),(6, 11),(7, 11),(8, 11),(9, 11),(5, 12),(6, 12),(7, 12),(8, 12),(9, 12),(4, 13),(5, 13),(6, 13),(7, 13),(8, 13),(9, 13),(10, 13)],
            "Fou": [(7, 2),(6, 3),(7, 3),(8, 3),(6, 4),(7, 4),(8, 4),(5, 5),(6, 5),(7, 5),(8, 5),(9, 5),(5, 6),(6, 6),(7, 6),(8, 6),(9, 6),(6, 7),(7, 7),(8, 7),(6, 8),(7, 8),(8, 8),(6, 9),(7, 9),(8, 9),(6, 10),(7, 10),(8, 10),(6, 11),(7, 11),(8, 11),(5, 12),(6, 12),(7, 12),(8, 12),(9, 12),(4, 13),(5, 13),(6, 13),(7, 13),(8, 13),(9, 13),(10, 13)],
            "Dame": [(5, 2),(7, 2),(9, 2),(5, 3),(6, 3),(7, 3),(8, 3),(9, 3),(6, 4),(7, 4),(8, 4),(5, 5),(6, 5),(7, 5),(8, 5),(9, 5),(6, 6),(7, 6),(8, 6),(6, 7),(7, 7),(8, 7),(6, 8),(7, 8),(8, 8),(6, 9),(7, 9),(8, 9),(6, 10),(7, 10),(8, 10),(6, 11),(7, 11),(8, 11),(5, 12),(6, 12),(7, 12),(8, 12),(9, 12),(4, 13),(5, 13),(6, 13),(7, 13),(8, 13),(9, 13),(10, 13)],
            "Roi": [(7, 0),(6, 1),(7, 1),(8, 1),(7, 2),(6, 3),(7, 3),(8, 3),(5, 4),(6, 4),(7, 4),(8, 4),(9, 4),(6, 5),(7, 5),(8, 5),(6, 6),(7, 6),(8, 6),(6, 7),(7, 7),(8, 7),(6, 8),(7, 8),(8, 8),(6, 9),(7, 9),(8, 9),(6, 10),(7, 10),(8, 10),(6, 11),(7, 11),(8, 11),(5, 12),(6, 12),(7, 12),(8, 12),(9, 12),(4, 13),(5, 13),(6, 13),(7, 13),(8, 13),(9, 13),(10, 13)]
        }

        pyxel.run(self.update, self.draw)

    def update(self):
        if self.tour == 'b':
            self.ia.jouer(self.pieces)
            self.tour = 'w'
            return

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            mx, my = pyxel.mouse_x, pyxel.mouse_y
            col = (mx - self.offset_x) // self.cell_size
            ligne = (my - self.offset_y) // self.cell_size

            if not (0 <= col < 8 and 0 <= ligne < 8):
                return

            contenu = self.pieces[ligne][col]

            if self.selection is None:
                if contenu and contenu.couleur == self.tour:
                    self.selection = (ligne, col)
            else:
                sl, sc = self.selection
                piece = self.pieces[sl][sc]

                if (ligne, col) == (sl, sc):
                    self.selection = None

                elif piece.avancer(col, ligne, self.pieces):
                    cible = self.pieces[ligne][col]
                    if cible:
                        piece.manger(cible)

                    self.pieces[ligne][col] = piece
                    self.pieces[sl][sc] = None
                    piece.x = col
                    piece.y = ligne

                    # Promotion pion
                    if isinstance(piece, Pion):
                        if (piece.couleur == 'w' and ligne == 0) or (piece.couleur == 'b' and ligne == 7):
                            self.pieces[ligne][col] = Dame(col, ligne, piece.couleur)

                    self.tour = 'b'
                    self.selection = None

                elif contenu and contenu.couleur == self.tour:
                    self.selection = (ligne, col)

    def draw(self):
        pyxel.cls(13)

        for ligne in range(8):
            for col in range(8):
                x = self.offset_x + col * self.cell_size
                y = self.offset_y + ligne * self.cell_size
                couleur = 6 if (ligne + col) % 2 == 0 else 1
                if self.selection == (ligne, col):
                    couleur = 10
                pyxel.rect(x, y, self.cell_size, self.cell_size, couleur)

                piece = self.pieces[ligne][col]
                if piece:
                    pixels = self.modeles_pieces[piece.__class__.__name__]
                    colpix = 7 if piece.couleur == 'w' else 0
                    for px, py in pixels:
                        pyxel.pset(x + px + 6, y + py + 6, colpix)


Plateau()
