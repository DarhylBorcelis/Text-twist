import pygame
import random

pygame.init()

# Window
screen_width, screen_hight = 1000, 600
SCREEN = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("Text Twist")

# Fonts
ULTRA_BIG_FONT = pygame.font.Font("assets/font/Hevilla.ttf", 90)
BIG_FONT = pygame.font.Font("assets/font/Hevilla.ttf", 70)
FONT = pygame.font.Font("assets/font/Hevilla.ttf", 22)

# Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Variables
game_state = "Main_Menu"
game_category = "Animal"
game_level = 1
player_ans = []
CATEGORY = {}


def load_category(game_category):  # Dictionary
    if game_category == "Animal":
        return {
            1: ["CAT", "DOG", "COW", "PIG", "BAT", "RAT", "FOX", "HEN", "ANT", "OWL"],
            2: ["LION", "BEAR", "WOLF", "FROG", "DEER", "DUCK", "GOAT", "CRAB", "SWAN", "TOAD"],
            3: ["HORSE", "SHEEP", "MOUSE", "TIGER", "ZEBRA", "PANDA", "SNAKE", "LLAMA", "EAGLE", "SHARK"],
            4: ["MONKEY", "DONKEY", "RABBIT", "SPIDER", "TURTLE", "PARROT", "SALMON", "JAGUAR", "CAMEL", "GIRAFFE"],
            5: ["DOLPHIN", "BUFFALO", "LEOPARD", "CHICKEN", "GORILLA", "PELICAN", "OSTRICH", "COYOTE", "PIGEON", "DRAGON"]
        }
    elif game_category == "Food":
        return {
            1: ["RICE", "BREAD", "SOUP", "CORN", "CAKE", "FISH", "MEAT", "EGGS", "MILK", "BEAN"],
            2: ["APPLE", "MANGO", "PEACH", "GRAPE", "LEMON", "ONION", "PIZZA", "PASTA", "BERRY", "CHILI"],
            3: ["BANANA", "TOMATO", "ORANGE", "CARROT", "PEANUT", "BURGER", "COOKIE", "HONEY", "JUICE", "SALAD"],
            4: ["CHERRY", "PUMPKIN", "GARLIC", "COFFEE", "DONUTS", "NOODLE", "BUTTER", "SPINACH", "CHEESE", "SUGAR"],
            5: ["POTATOE", "CHICKEN", "CHOCOLATE", "CABBAGE", "ICECREAM", "SANDWICH", "PANCAKE", "CEREALS", "YOGURT", "SEAFOOD"]
        }
    elif game_category == "Place":
        return {
            1: ["PARK", "MALL", "HOME", "ROOM", "FARM", "CITY", "BANK", "SHOP", "POOL", "PORT"],
            2: ["RIVER", "FIELD", "BEACH", "HOTEL", "SCHOOL", "MARKET", "CHURCH", "BRIDGE", "MUSEUM", "STREET"],
            3: ["CASTLE", "FOREST", "OFFICE", "TEMPLE", "ISLAND", "STADIUM", "PRISON", "TUNNEL", "TOWER", "PALACE"],
            4: ["VILLAGE", "HOSPITAL", "AIRPORT", "STATION", "MARKETS", "THEATER", "FACTORY", "HARBOR", "CHURCHES", "GARDENS"],
            5: ["MOUNTAIN", "LIBRARY", "COTTAGE", "UNIVERSITY", "RESTAURANT", "APARTMENT", "PLAYGROUND", "CEMETERY", "WAREHOUSE", "SUBWAY"]
        }


FOOD = load_category("Food")
ANIMAL = load_category("Animal")
PLACE = load_category("Place")

# Image
FOOD_BANNER = "assets/button/food_banner.png"
PLACE_BANNER = "assets/button/place_banner.png"
ANIMAL_BANNER = "assets/button/animal_banner.png"

if game_category == "Animal":
    BUTTON_IMAGE = "assets/button/button.png"
    BACKGROUND_IMAGE = "assets/button/game_play.png"
    PLAY_IMAGE = "assets/button/ans.png"
    BANER_IMAGE = "assets/button/banner.png"
    BOARD_IMAGE = "assets/button/bord.png"
    PLACEHOLDER_IMAGE = "assets/button/ans.png"


class Button:
    def __init__(self, x, y, image, scale, text="", font=FONT, text_color=WHITE, key=None):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.click = False

        # Text setup
        self.text = text
        self.font = font
        self.text_color = text_color

        # Keyboard
        self.key = key
        self.key_click = False   # initialize here

        if self.font and self.text != "":
            self.text_surface = self.font.render(
                self.text, True, self.text_color
            )
            self.text_rect = self.text_surface.get_rect(
                center=self.rect.center
            )
        else:
            self.text_surface = None

    def event_handler(self):
        action = False
        # Keyboard input
        keys = pygame.key.get_pressed()
        if self.key:
            if not keys[self.key] and self.key_click:
                action = True
                self.key_click = False
            elif keys[self.key]:
                self.key_click = True

        return action

    def draw(self, SCREEN):
        # Draw button
        SCREEN.blit(self.image, self.rect)
        # Draw text
        if self.text_surface:
            SCREEN.blit(self.text_surface, self.text_rect)


class World:
    def __init__(self, img):
        # Keep a list of all "design"
        self.designs = []
        self.text_lis = []
        background = pygame.image.load(img)
        self.background_img = pygame.transform.scale(background, (1000, 600))

    def text(self, name="", color=WHITE, x_cord=0, y_cord=0, font=BIG_FONT):
        txt = font.render(name, True, color)
        self.text_lis.append({
            "text": txt,
            "x_cord": x_cord,
            "y_cord": y_cord
        })

    def add_design(self, image, x, y, width, height):
        image = pygame.image.load(image)
        image = pygame.transform.scale(image, (width, height))
        rect = image.get_rect(topleft=(x, y))
        self.designs.append((image, rect))

    def draw(self, SCREEN):
        SCREEN.blit(self.background_img, (0, 0))  # Draw background

        # Draw all texts
        for item in self.text_lis:
            SCREEN.blit(item["text"], (item["x_cord"], item["y_cord"]))
        # Draw all designs
        for img, rect in self.designs:
            SCREEN.blit(img, rect)


class Game_play:
    def __init__(self, category, game_level):
        self.letters = []
        self.used_stack = []
        self.category = category
        self.level_words = category[game_level]
        self.guest = []
        self.Ans_word = ""
        self.choices = ""

    def Update_2(self, event):
        # Mouse input
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = event.pos
            for i, letter in enumerate(self.letters):
                if letter["rect"].collidepoint(pos) and letter["active"]:
                    self.guest.append(letter["char"])
                    letter["active"] = False
                    self.used_stack.append(i)
                    break

    def Draw(self, SCREEN):
        for letter in self.letters:
            SCREEN.blit(letter["img"], letter["rect"])
            if letter["active"]:
                SCREEN.blit(letter["text_surface"], letter["text_rect"])

        guess_text = "".join(self.guest)
        x_cord = (1000 - (len(self.choices) * 30)) // 2
        txt_surf = FONT.render(guess_text, True, WHITE)
        SCREEN.blit(txt_surf, (x_cord, 413))

    def Rand_Level_Words(self, player_ans):
        available_words = [w for w in self.level_words if w not in player_ans]
        if not available_words:
            self.Ans_word = ""  # no words left
            return False
        else:
            self.Ans_word = random.choice(available_words)
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

    def Update_ans(self):
        # Clear previous letters and used stack
        self.letters = []
        self.used_stack = []
        self.guest = []

        base_img = pygame.image.load("assets/button/letters.png")
        base_img = pygame.transform.scale(base_img, (80, 50))

        x_cord = (1000 - (len(self.choices) * 90)) // 2
        y_cord = 470
        for i, char in enumerate(self.choices):
            img = base_img.copy()
            rect = img.get_rect()
            rect.x = x_cord + i * 90
            rect.y = y_cord

            text_surface = FONT.render(char, True, WHITE)
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


class Level:
    def __init__(self, image, y, x, category):
        # store (image, rect, text_surface, text_rect, active)
        self.levels = []

        # Load the level button background
        base_img = pygame.image.load(image)
        base_img = pygame.transform.scale(base_img, (90, 130))

        # Calculate positioning
        x_cord = x
        y_cord = y

        for i, level_num in enumerate(category.keys()):
            img = base_img.copy()
            rect = img.get_rect()
            rect.x = x_cord + i * 110
            rect.y = y_cord

            # render the level number as text
            text_surface = BIG_FONT.render(str(level_num), True, WHITE)
            text_rect = text_surface.get_rect(center=rect.center)

            self.levels.append({
                "img": img,
                "rect": rect,
                "lvl": level_num,
                "text_surface": text_surface,
                "text_rect": text_rect,
                "active": True
            })

    def update(self, event):
        # Mouse input
        clicked_level = None
        pos = pygame.mouse.get_pos()
        for level in self.levels:
            if level["rect"].collidepoint(pos):
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if level["active"]:   # only selectable if still active
                        clicked_level = level["lvl"]

        return clicked_level

    def draw(self, SCREEN):
        for Level in self.levels:
            SCREEN.blit(Level["img"], Level["rect"])
            SCREEN.blit(Level["text_surface"], Level["text_rect"])


# main menu Buttons
Menu_play_btn = Button(430, 280, PLAY_IMAGE, (120, 60),
                       "Play", key=pygame.K_RETURN)
Menu_exit_btn = Button(430, 350, PLAY_IMAGE, (120, 60),
                       "Exit", key=pygame.K_ESCAPE)

# Game play buttons
Game_enter_btn = Button(800, 95, BUTTON_IMAGE, (150, 50),
                        "Enter", key=pygame.K_RETURN)
Game_delete_btn = Button(800, 145, BUTTON_IMAGE, (150, 50),
                         "Delete", key=pygame.K_DELETE)
Game_shuffle_btn = Button(800, 195, BUTTON_IMAGE, (150, 50),
                          "Shuffle", key=pygame.K_s)
Game_back_btn = Button(800, -10, BUTTON_IMAGE, (100, 50),
                       "Back", key=pygame.K_ESCAPE)

# level buttons
Level_back_btn = Button(690, -10, BUTTON_IMAGE, (100, 50),
                        "Back", key=pygame.K_ESCAPE)
Level_food_btn = Button(430, 60, PLAY_IMAGE, (120, 40), "Food", key=pygame.K_f)
Level_animal_btn = Button(430, 230, PLAY_IMAGE,
                          (120, 40), "animal", key=pygame.K_a)
Level_place_btn = Button(430, 400, PLAY_IMAGE,
                         (120, 40), "Place", key=pygame.K_p)

# game play World
Game_play_world = World("assets/button/game_play.png")
Game_play_world.add_design(BACKGROUND_IMAGE, 0,
                           0, screen_width, screen_hight)  # Background
Game_play_world.add_design(BOARD_IMAGE, 150, -190, 700, 800)   # Black Board
Game_play_world.add_design(BANER_IMAGE, 50, 30, 130, 210)  # Banner
Game_play_world.add_design(PLACEHOLDER_IMAGE, 250,
                           400, 500, 50)  # Ans Placeholder

# Level world
level_word = World("assets/button/level_menu.png")
level_word.add_design("assets/button/top_level.png", 5, -5, 1000, 80)
level_word.add_design("assets/button/buttom_level.png", 5, 550, 1000, 80)

food_level = Level(FOOD_BANNER, 100, 230, FOOD)
animal_level = Level(ANIMAL_BANNER, 270, 230, ANIMAL)
place_level = Level(PLACE_BANNER, 440, 230, PLACE)

# Main menu world
Main_menu_world = World("assets/button/main_menu.png")
Main_menu_world.text("TEXT TWIST", color=BLACK, x_cord=285,
                     y_cord=40, font=ULTRA_BIG_FONT)


# Game loop
run = True
while run:

    # Game Condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if game_state == "Main_Menu":
            # draw world
            Main_menu_world.draw(SCREEN)

            # draw btn
            Menu_play_btn.draw(SCREEN)
            Menu_exit_btn.draw(SCREEN)

            # event handler
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if Menu_play_btn.event_handler() or Menu_play_btn.rect.collidepoint(pos):
                    game_state = "Level_Menu"
                if Menu_exit_btn.event_handler() or Menu_exit_btn.rect.collidepoint(pos):
                    run = False

        elif game_state == "Level_Menu":
            # Level World design
            level_word.draw(SCREEN)

            # Level Category
            food_level.draw(SCREEN)
            animal_level.draw(SCREEN)
            place_level.draw(SCREEN)

            # Level btn
            Level_back_btn.draw(SCREEN)
            Level_animal_btn.draw(SCREEN)
            Level_food_btn.draw(SCREEN)
            Level_place_btn.draw(SCREEN)

            # event handler
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                if Level_back_btn.event_handler() or Level_back_btn.rect.collidepoint(pos):
                    game_state = "Main_Menu"

                clicked_food_level = food_level.update(event)
                clicked_animal_level = animal_level.update(event)
                clicked_place_level = place_level.update(event)

                if clicked_food_level:
                    game_level = clicked_food_level
                    game_category = "Food"
                    CATEGORY = load_category(game_category)
                    gameplay = Game_play(CATEGORY, game_level)
                    if gameplay.Rand_Level_Words(player_ans):
                        gameplay.Shuffled()
                        gameplay.Update_ans()
                    game_state = "Gameplay"

                elif clicked_animal_level:
                    game_level = clicked_animal_level
                    game_category = "Animal"
                    CATEGORY = load_category(game_category)
                    gameplay = Game_play(CATEGORY, game_level)
                    if gameplay.Rand_Level_Words(player_ans):
                        gameplay.Shuffled()
                        gameplay.Update_ans()
                    game_state = "Gameplay"

                elif clicked_place_level:
                    game_level = clicked_place_level
                    game_category = "Place"
                    CATEGORY = load_category(game_category)
                    gameplay = Game_play(CATEGORY, game_level)
                    if gameplay.Rand_Level_Words(player_ans):
                        gameplay.Shuffled()
                        gameplay.Update_ans()
                    game_state = "Gameplay"

        elif game_state == "Gameplay":
            # Draw game design
            Game_play_world.draw(SCREEN)
            gameplay.Draw(SCREEN)
            gameplay.Update_2(event)

            # draw btn
            Game_enter_btn.draw(SCREEN)
            Game_delete_btn.draw(SCREEN)
            Game_shuffle_btn.draw(SCREEN)
            Game_back_btn.draw(SCREEN)

            # Event handler
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                if Game_enter_btn.event_handler() or Game_enter_btn.rect.collidepoint(pos):
                    if "".join(gameplay.guest) == gameplay.Ans_word:
                        player_ans.append(gameplay.Ans_word)
                        if gameplay.Rand_Level_Words(player_ans):  # pick a word
                            gameplay.Shuffled()
                            gameplay.Update_ans()
                        gameplay.reset_all_letters()
                    else:
                        gameplay.reset_all_letters()

                if Game_delete_btn.event_handler() or Game_delete_btn.rect.collidepoint(pos):
                    gameplay.delete_last_letter()

                if Game_shuffle_btn.event_handler() or Game_shuffle_btn.rect.collidepoint(pos):
                    if gameplay.Rand_Level_Words(player_ans):  # pick a word
                        gameplay.Shuffled()
                        gameplay.Update_ans()

                if Game_back_btn.event_handler() or Game_back_btn.rect.collidepoint(pos):
                    game_state = "Level_Menu"

    pygame.display.update()

pygame.quit()
