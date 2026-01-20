import pyxel

class Plateau:
    def __init__(self):
        pyxel.init(200, 200, title="Plateau d'échecs")
        self.cell_size = 25
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        for ligne in range(8):
            for col in range(8):
                x = col * self.cell_size
                y = ligne * self.cell_size

                # Couleurs alternées
                if (ligne + col) % 2 == 0:
                    color = 7  # blanc
                else:
                    color = 0  # bleu (ou mets 0/5/etc)

                pyxel.rect(x, y, self.cell_size, self.cell_size, color)

Plateau()
