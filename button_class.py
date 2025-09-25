import pygame as PY
import Constant as C


class Button:
    def __init__(self, x, y, image, scale, font, text="", text_color=C.WHITE, key=None, cooldown=300):
        self.image = PY.image.load(image)
        self.image = PY.transform.scale(self.image, scale)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.text = text
        self.font = font
        self.text_color = text_color

        if self.font and self.text != "":
            self.text_surface = self.font.render(
                self.text, True, self.text_color)
            self.text_rect = self.text_surface.get_rect(
                center=self.rect.center)
        else:
            self.text_surface = None

        # keyboard
        self.key = key
        self.cooldown = cooldown
        self.last_press = 0
        self.held = False

    def Event_handler(self):
        action = False
        current_time = PY.time.get_ticks()

        if self.key:
            keys = PY.key.get_pressed()
            if keys[self.key]:
                if not self.held:
                    action = True
                    self.last_press = current_time
                    self.held = True
                elif current_time - self.last_press >= self.cooldown:
                    action = True
                    self.last_press = current_time
            else:
                self.held = False

        return action

    def Draw(self, SCREEN):
        # Draw button
        SCREEN.blit(self.image, self.rect)
        # Draw text
        if self.text_surface:
            SCREEN.blit(self.text_surface, self.text_rect)
