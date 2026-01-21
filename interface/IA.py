import random

class IA:
    def __init__(self, couleur):
        self.couleur = couleur 

    def jouer(self, plateau):
        coups = self.generer_coups(plateau)

        if not coups:
            print("IA bloquée")
            return

        (y1, x1, y2, x2) = random.choice(coups)

        piece = plateau[y1][x1]

        plateau[y2][x2] = piece
        plateau[y1][x1] = None

    def generer_coups(self, plateau):
        coups = []

        for y in range(8):
            for x in range(8):
                piece = plateau[y][x]
                if piece is None:
                    continue
                if piece[0] != self.couleur:
                    continue

                for y2 in range(8):
                    for x2 in range(8):
                        if (y2, x2) == (y, x):
                            continue

                        if self.coup_valide(piece, x, y, x2, y2, plateau):
                            coups.append((y, x, y2, x2))

        return coups

    def coup_valide(self, piece, x1, y1, x2, y2, plateau):
        # Interdit de manger sa propre pièce
        cible = plateau[y2][x2]
        if cible is not None and cible[0] == self.couleur:
            return False

        dx = x2 - x1
        dy = y2 - y1

        type_p = piece[1]

        if type_p == 'P':
            direction = 1 if self.couleur == 'b' else -1
            if dx == 0 and dy == direction and plateau[y2][x2] is None:
                return True

        elif type_p == 'R':
            if dx == 0 or dy == 0:
                return self.chemin_libre(x1, y1, x2, y2, plateau)

        elif type_p == 'B':
            if abs(dx) == abs(dy):
                return self.chemin_libre(x1, y1, x2, y2, plateau)

        elif type_p == 'Q':
            if dx == 0 or dy == 0 or abs(dx) == abs(dy):
                return self.chemin_libre(x1, y1, x2, y2, plateau)

        elif type_p == 'N':
            if (abs(dx), abs(dy)) in [(1,2),(2,1)]:
                return True

        elif type_p == 'K':
            if abs(dx) <= 1 and abs(dy) <= 1:
                return True

        return False

    def chemin_libre(self, x1, y1, x2, y2, plateau):
        pas_x = (x2 - x1)
        pas_y = (y2 - y1)

        if pas_x != 0: pas_x = pas_x // abs(pas_x)
        if pas_y != 0: pas_y = pas_y // abs(pas_y)

        cx = x1 + pas_x
        cy = y1 + pas_y

        while (cx, cy) != (x2, y2):
            if plateau[cy][cx] is not None:
                return False
            cx += pas_x
            cy += pas_y

        return True
