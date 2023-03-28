import pygame


class Electrode(pygame.sprite.Sprite):
    def __init__(self, path, spawn, typ):
        super().__init__()
        self.sprites = []
        self.spawn = spawn
        if typ == "square":
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/square/square1.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/square/square2.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/square/square3.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/square/square4.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/square/square5.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/square/square6.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/square/square7.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/square/square8.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/square/square9.png"), (30, 30)))

        elif typ == "stair":
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/stairs/stairs1.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/stairs/stairs2.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/stairs/stairs3.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/stairs/stairs4.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/stairs/stairs5.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/stairs/stairs6.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/stairs/stairs7.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/stairs/stairs8.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/stairs/stairs9.png"), (30, 30)))

        elif typ == "checker":
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/checkers/checkers1.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/checkers/checkers2.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/checkers/checkers3.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/checkers/checkers4.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/checkers/checkers5.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/checkers/checkers6.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/checkers/checkers7.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/checkers/checkers8.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/checkers/checkers9.png"), (30, 30)))

        else:
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/spark/spark1.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/spark/spark2.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/spark/spark3.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/spark/spark4.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/spark/spark5.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/spark/spark6.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/spark/spark7.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/spark/spark8.png"), (30, 30)))
            self.sprites.append(pygame.transform.scale(pygame.image.load(path + "/spark/spark9.png"), (30, 30)))

        self.image = self.sprites[0]
        self.rect = self.image.get_rect(center=self.spawn)
        self.sprite_state = 0

    def update(self):
        self.sprite_state += 0.2
        if self.sprite_state >= 9:
            self.sprite_state = 0
        self.image = self.sprites[int(self.sprite_state)]
