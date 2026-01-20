import pyxel
from PIL import Image

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
            self.pieces[1][i] = 'bP'  
            self.pieces[6][i] = 'wP' 
        self.pieces[0][0] = self.pieces[0][7] = 'bR'
        self.pieces[7][0] = self.pieces[7][7] = 'wR'
        self.pieces[0][1] = self.pieces[0][6] = 'bN'
        self.pieces[7][1] = self.pieces[7][6] = 'wN'
        self.pieces[0][2] = self.pieces[0][5] = 'bB'
        self.pieces[7][2] = self.pieces[7][5] = 'wB'
        self.pieces[0][3] = 'bQ'
        self.pieces[7][3] = 'wQ'
        self.pieces[0][4] = 'bK'
        self.pieces[7][4] = 'wK'
        self.images = {}
        self.load_images()
        pyxel.run(self.update, self.draw)

    def load_images(self):
        pieces_files = ["bP","wP","bR","wR","bN","wN","bB","wB","bQ","wQ","bK","wK"]
        for name in pieces_files:
            img = Image.open(f"images/{name}.png").resize((self.cell_size, self.cell_size))
            self.images[name] = pyxel.image(0).load(0, 0, img)    
    
    def update(self):
        pass

    def draw(self):
        pyxel.cls(13)
        for ligne in range(8):
            for col in range(8):
                x = self.offset_x + col * self.cell_size
                y = self.offset_y + ligne * self.cell_size

                color = 7 if (ligne + col) % 2 == 0 else 0
                pyxel.rect(x, y, self.cell_size, self.cell_size, color)

                piece = self.pieces[ligne][col]
                if piece:
                    pyxel.blt(x, y, 0, 0, 0, self.cell_size, self.cell_size, 0)

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
