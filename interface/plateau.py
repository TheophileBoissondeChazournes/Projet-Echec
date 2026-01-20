import pyxel

class Plateau:
    def __init__(self):
        pyxel.init(250, 250, title="Plateau d'échecs")
        self.cell_size = 27
        self.board_size = self.cell_size * 8
        total_size = self.board_size 
        self.offset_x = (250- total_size) // 2 
        self.offset_y = (250 - total_size) // 2
        self.pieces = [[None for _ in range(8)] for _ in range(8)]
        for i in range(8):
            self.pieces[1][i] = 'p'  
            self.pieces[6][i] = 'P'  
        self.pieces[0][0] = self.pieces[0][7] = 't'
        self.pieces[7][0] = self.pieces[7][7] = 'T'
        self.pieces[0][1] = self.pieces[0][6] = 'c'
        self.pieces[7][1] = self.pieces[7][6] = 'C'
        self.pieces[0][2] = self.pieces[0][5] = 'f'
        self.pieces[7][2] = self.pieces[7][5] = 'F'
        self.pieces[0][3] = 'q'
        self.pieces[7][3] = 'Q'
        self.pieces[0][4] = 'k'
        self.pieces[7][4] = 'K'
     
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(13)
        for ligne in range(8):
            for col in range(8):
                x = self.offset_x + col * self.cell_size
                y = self.offset_y + ligne * self.cell_size

                # Couleurs alternées
                if (ligne + col) % 2 == 0:
                    color = 7  
                else:
                    color = 0  

                pyxel.rect(x, y, self.cell_size, self.cell_size, color)
                
                piece = self.pieces[ligne][col]
                if piece:
                    coord_x, coord_y = PIECE_COORD[piece]
                    pyxel.blt(
                        x, y,                
                        0,                  
                        coord_x * self.cell_size,
                        coord_y * self.cell_size,
                        self.cell_size,
                        self.cell_size,
                        0                    
                    )

        for col in range(8):
            lettre = chr(ord("A") + col)
            x = self.offset_x + col * self.cell_size + 9
            y = self.offset_y + 8 * self.cell_size + 5
            pyxel.text(x, y, lettre, 0)

        for ligne in range(8):
            nb = str(8 - ligne)
            x = self.offset_x - 15
            y = self.offset_y + ligne * self.cell_size + 9
            pyxel.text(x, y, nb, 0)

Plateau()


PIECE_COORD = {
    'P': (0, 1),  
    'p': (0, 0),  
    'T': (1, 1),  
    't': (1, 0),  
    'C': (2, 1),  
    'c': (2, 0),  
    'F': (3, 1),  
    'f': (3, 0),  
    'Q': (4, 1),  
    'q': (4, 0),  
    'K': (5, 1),  
    'k': (5, 0),  
}