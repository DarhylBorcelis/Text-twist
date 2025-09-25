import pygame as PY
import Constant as C


class Level:
    def __init__(self, image, y, x, category, unlocked_levels=1):
        # store (image, rect, text_surface, text_rect, active, locked_img)
        self.levels = []

        # Load the level button background
        base_img = PY.image.load(image)
        base_img = PY.transform.scale(base_img, (90, 130))

        # Load the lock image
        self.lock_img = PY.image.load(C.LOCK_IMG)
        self.lock_img = PY.transform.scale(self.lock_img, (100, 100))

        # Calculate positioning
        x_cord = x
        y_cord = y

        for i, level_num in enumerate(category.keys()):
            img = base_img.copy()
            rect = img.get_rect()
            rect.x = x_cord + i * 110
            rect.y = y_cord

            FONT = PY.font.Font(C.Seagram_tfb, 70)

            # render the level number
            text_surface = FONT.render(str(level_num), True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=rect.center)

            # locked if higher than unlocked_levels
            active = level_num <= unlocked_levels

            self.levels.append({
                "img": img,
                "rect": rect,
                "lvl": level_num,
                "text_surface": text_surface,
                "text_rect": text_rect,
                "active": active
            })

    def update(self, event):
        clicked_level = None
        pos = PY.mouse.get_pos()
        for level in self.levels:
            if level["rect"].collidepoint(pos):
                if event.type == PY.MOUSEBUTTONDOWN and event.button == 1:
                    if level["active"]:  # only clickable if active
                        clicked_level = level["lvl"]

        return clicked_level

    def draw(self, SCREEN):
        for level in self.levels:
            SCREEN.blit(level["img"], level["rect"])

            if level["active"]:
                # show level number
                SCREEN.blit(level["text_surface"], level["text_rect"])
            else:
                # show lock image instead
                lock_rect = self.lock_img.get_rect(center=level["rect"].center)
                SCREEN.blit(self.lock_img, lock_rect)
