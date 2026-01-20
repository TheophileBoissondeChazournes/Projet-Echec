import pyxel

class Plateau:
    def __init__(self):
        pyxel.init(250, 250, title="Plateau d'échecs")
        self.cell_size = 25
        self.board_size = self.cell_size * 8
        total_size = self.board_size 
        self.offset_x = (250- total_size) // 2 
        self.offset_y = (250 - total_size) // 2
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
