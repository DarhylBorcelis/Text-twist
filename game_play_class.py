import pygame as PY
import random
import Constant as C


class Game_play:
    def __init__(self, category, game_level):
        self.letters = []
        self.used_stack = []
        self.letters = []
        self.used_stack = []
        self.category = category
        self.level_words = category[game_level]
        self.guest = []
        self.Ans_word = ""
        self.choices = ""
        self.hint = ""
        self.hint_active = False

    def clear(self, category, game_level):
        self.letters = []
        self.used_stack = []
        self.letters = []
        self.used_stack = []
        self.category = category
        self.level_words = category[game_level]
        self.guest = []
        self.Ans_word = ""
        self.choices = ""
        self.hint = ""
        self.hint_active = False

    def draw_answers(self, SCREEN, player_ans):
        font = PY.font.Font(C.Hevilla, 25)
        x_start = 260
        y_start = 120
        line_height = 50

        if not player_ans:  # nothing to draw
            return

        # Measure longest word width
        longest_word = max(player_ans, key=len)
        text_width, _ = font.size(longest_word)

        if text_width > 110:
            cols = 3
            col_width = 160
        elif text_width > 50:
            cols = 4
            col_width = 120
        else:
            cols = 5
            col_width = 100

        for i, word in enumerate(player_ans):
            row = i // cols
            col = i % cols

            x = x_start + col * col_width
            y = y_start + row * line_height

            txt_surface = font.render(word, True, C.WHITE)
            SCREEN.blit(txt_surface, (x, y))

    def Update_keyboard(self, event):
        if event.type == PY.KEYDOWN:
            key_name = PY.key.name(
                event.key).upper()  # convert to uppercase
            # Only accept if the key is one of the letters in choices
            for i, letter in enumerate(self.letters):
                if letter["char"] == key_name and letter["active"]:
                    self.guest.append(letter["char"])
                    letter["active"] = False
                    self.used_stack.append(i)
                    break

    def Update_2(self, event):
        # Mouse input
        if event.type == PY.MOUSEBUTTONDOWN and event.button == 1:
            pos = event.pos
            for i, letter in enumerate(self.letters):
                if letter["rect"].collidepoint(pos) and letter["active"]:
                    self.guest.append(letter["char"])
                    letter["active"] = False
                    self.used_stack.append(i)
                    break

    def Draw(self, SCREEN):
        font = PY.font.Font(C.AUGUSTUS, 25)
        for letter in self.letters:
            SCREEN.blit(letter["img"], letter["rect"])
            if letter["active"]:
                SCREEN.blit(letter["text_surface"], letter["text_rect"])

        guess_text = "".join(self.guest)
        x_cord = (1000 - (len(self.choices) * 30)) // 2
        txt_surf = font.render(guess_text, True, C.WHITE)
        SCREEN.blit(txt_surf, (x_cord, 413))

    def draw_hint(self, SCREEN):
        if self.hint_active:
            font = PY.font.Font(C.Hevilla, 28)
            txt = font.render("Hint: "+self.hint, True, C.WHITE)
            SCREEN.blit(txt, (280, 60))

    def Rand_Level_Words(self, player_ans):
        available_words = [
            w for w, h in self.level_words if w not in player_ans]
        if not available_words:
            self.Ans_word = ""
            self.hint = ""
            return False
        else:
            word, hint = random.choice(self.level_words)
            while word in player_ans:
                word, hint = random.choice(self.level_words)
            self.Ans_word = word
            self.hint = hint
            return True

    def Shuffled(self):
        if not self.Ans_word:
            return
        letters = list(self.Ans_word)
        shuffled = "".join(letters)
        while shuffled == self.Ans_word:
            random.shuffle(letters)
            shuffled = "".join(letters)
        self.choices = shuffled

    def Update_ans(self, category):
        # Clear previous letters and used stack
        self.letters = []
        self.used_stack = []
        self.guest = []

        if category == "Food":
            font = PY.font.Font(C.AUGUSTUS, 25)
            img = C.FOOD_GP_BTN
            color = C.WHITE
            x_size, y_size = 90, 60
        elif category == "Animal":
            font = PY.font.Font(C.AUGUSTUS, 25)
            img = C.ANIMAL_GP_BTN
            color = C.WHITE
            x_size, y_size = 90, 60
        elif category == "Place":
            font = PY.font.Font(C.AUGUSTUS, 25)
            img = C.PLACE_GP_BTN
            color = C.WHITE
            x_size, y_size = 90, 60

        base_img = PY.image.load(img)
        base_img = PY.transform.scale(base_img, (x_size, y_size))

        x_cord = (1000 - (len(self.choices) * 90)) // 2
        y_cord = 470
        for i, char in enumerate(self.choices):
            img = base_img.copy()
            rect = img.get_rect()
            rect.x = x_cord + i * 90
            rect.y = y_cord

            text_surface = font.render(char, True, color)
            text_rect = text_surface.get_rect(center=rect.center)

            # store and name
            self.letters.append({
                "img": img,
                "rect": rect,
                "char": char,
                "text_surface": text_surface,
                "text_rect": text_rect,
                "active": True
            })

    def delete_last_letter(self):
        if not self.guest or not self.used_stack:
            return
        # pop last guessed char
        self.guest.pop()
        # restore the most recently used letter
        last_index = self.used_stack.pop()
        self.letters[last_index]["active"] = True

    def reset_all_letters(self):
        self.guest = []
        # restore all letters to active
        for i in self.used_stack:
            self.letters[i]["active"] = True
        # clear the stack
        self.used_stack = []
