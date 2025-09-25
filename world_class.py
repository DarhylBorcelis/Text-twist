import pygame as PY
import Constant as C


class World():
    def __init__(self):
        self.designs = []
        self.text_lis = []
        self.background_img = ""

    def clear(self):
        self.designs = []
        self.text_lis = []

    def text(self, name="", color=C.WHITE, x_cord=0, y_cord=0, font="", f_size=22):
        FONT = PY.font.Font(font, f_size)
        txt = FONT.render(name, True, color)
        self.text_lis.append({
            "text": txt,
            "x_cord": x_cord,
            "y_cord": y_cord
        })

    def Set_bg(self, img):
        background = PY.image.load(img)
        self.background_img = PY.transform.scale(
            background, (C.SCREEN_WIDTH, C.SCREEN_HIGHT))

    def add_design(self, image, x, y, width, height):
        image = PY.image.load(image)
        image = PY.transform.scale(image, (width, height))
        rect = image.get_rect(topleft=(x, y))
        self.designs.append((image, rect))

    def Draw(self, SCREEN):
        # Draw background only if available
        if self.background_img:
            SCREEN.blit(self.background_img, (0, 0))

        # Draw all designs
        for img, rect in self.designs:
            SCREEN.blit(img, rect)

        # Draw all texts
        for item in self.text_lis:
            SCREEN.blit(item["text"], (item["x_cord"], item["y_cord"]))
