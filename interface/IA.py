import random
import copy

class IA:
    def __init__(self, couleur):
        self.couleur = couleur

    def jouer(self, plateau):
        coups = self.generer_coups(plateau)
        if not coups:
            return

        piece, x, y = random.choice(coups)

        ox, oy = piece.x, piece.y
        cible = plateau[y][x]

        if cible:
            piece.manger(cible)

        plateau[oy][ox] = None
        plateau[y][x] = piece
        piece.x = x
        piece.y = y

    def generer_coups(self, plateau):
        coups = []

        for y in range(8):
            for x in range(8):
                piece = plateau[y][x]
                if piece is None:
                    continue

                if piece.couleur != self.couleur:
                    continue

                for ny in range(8):
                    for nx in range(8):

                        plateau_test = copy.deepcopy(plateau)

                        piece_test = plateau_test[y][x]

                        if piece_test.avancer(nx, ny, plateau_test):
                            coups.append((piece, nx, ny))

        return coups
