import pygame
import random

pygame.init()

# Window
screen_width, screen_hight = 1000, 600
SCREEN = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("Text Twist")

# Fonts
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
    BACKGROUND_IMAGE = "assets/button/background.png"
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

        # for keyboard
        self.key = key

        if self.font and self.text != "":
            self.text_surface = self.font.render(
                self.text, True, self.text_color)
            self.text_rect = self.text_surface.get_rect(
                center=self.rect.center)
        else:
            self.text_surface = None

    def draw(self, SCREEN):
        action = False
        # Draw buttons
        SCREEN.blit(self.image, self.rect)

        # Draw text
        if self.text_surface:
            SCREEN.blit(self.text_surface, self.text_rect)

        # Get mouse position
        pos = pygame.mouse.get_pos()

        # Check if click
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                action = True
                self.click = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.click = False

        # --- Keyboard input ---
        keys = pygame.key.get_pressed()
        if self.key:
            if keys[self.key] and not self.key_click:
                action = True
                self.key_click = True
            if not keys[self.key]:
                self.key_click = False

        return action


class World:
    def __init__(self):
        # Keep a list of all "design"
        self.designs = []

    def text():
        pass

    def add_design(self, image, x, y, width, height):
        image = pygame.image.load(image)
        image = pygame.transform.scale(image, (width, height))
        rect = image.get_rect(topleft=(x, y))
        self.designs.append((image, rect))

    def draw(self, SCREEN):
        for img, rect in self.designs:
            SCREEN.blit(img, rect)


class Game_play:
    def __init__(self, category, game_level):
        self.letters = []
        self.category = category
        self.level_words = category[game_level]
        self.Ans_word = ""
        self.choices = ""

    def update(self, SCREEN):
        for img, rect, text_surface, text_rect, Active in self.letters:
            SCREEN.blit(img, rect)
            SCREEN.blit(text_surface, text_rect)

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
        while shuffled == self.Ans_word:  # make sure it changes
            random.shuffle(letters)
            shuffled = "".join(letters)
        self.choices = shuffled

    def Draw_ans(self):
        # Clear previous letters
        self.letters = []

        base_img = pygame.image.load("assets/button/letters.png")
        base_img = pygame.transform.scale(base_img, (80, 50))

        x_cord = (1000 - (len(self.choices) * 90)) // 2
        y_cord = 470
        for i, char in enumerate(self.choices):
            img = base_img.copy()
            rect = img.get_rect()
            rect.x = x_cord + i * 90
            rect.y = y_cord

            # Correct font render (second param = anti-aliasing)
            text_surface = FONT.render(char, True, WHITE)
            text_rect = text_surface.get_rect(center=rect.center)

            self.letters.append((img, rect, text_surface, text_rect, True))


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

            self.levels.append([img, rect, text_surface, text_rect, True])

    def draw(self, SCREEN):
        for img, rect, text_surface, text_rect, active in self.levels:
            SCREEN.blit(img, rect)
            SCREEN.blit(text_surface, text_rect)


# Buttons
Menu_play_btn = Button(430, 280, PLAY_IMAGE, (120, 60),
                       "Play", key=pygame.K_RETURN)
Menu_exit_btn = Button(430, 350, PLAY_IMAGE, (120, 60),
                       "Exit", key=pygame.K_ESCAPE)

Game_enter_btn = Button(690, -15, BUTTON_IMAGE, (400, 350),
                        "Enter", key=pygame.K_RETURN)
Game_delete_btn = Button(690, 35, BUTTON_IMAGE, (400, 350),
                         "Delete", key=pygame.K_DELETE)
Game_shuffle_btn = Button(690, 85, BUTTON_IMAGE, (400, 350),
                          "Shuffle", key=pygame.K_s)

Level_food_btn = Button(430, 60, PLAY_IMAGE, (120, 40), "Food")
Level_animal_btn = Button(430, 230, PLAY_IMAGE, (120, 40), "animal")
Level_place_btn = Button(430, 400, PLAY_IMAGE, (120, 40), "Place")

# World
world = World()
# Add designs
world.add_design(BACKGROUND_IMAGE, 0,
                 0, screen_width, screen_hight)  # Background
world.add_design(BOARD_IMAGE, 150, -190, 700, 800)   # Black Board
world.add_design(BANER_IMAGE, 50, 30, 130, 210)  # Banner
world.add_design(PLACEHOLDER_IMAGE, 250, 400, 500, 50)  # Ans Placeholder

# Level
level_word = World()
level_word.add_design("assets/button/top_level.png", 5, -5, 1000, 80)
level_word.add_design("assets/button/buttom_level.png", 5, 550, 1000, 80)

food_level = Level(FOOD_BANNER, 100, 230, FOOD)
animal_level = Level(ANIMAL_BANNER, 270, 230, ANIMAL)
place_level = Level(PLACE_BANNER, 440, 230, PLACE)


# Game loop
run = True
while run:

    if game_state == "Main_Menu":
        # Background image
        background = pygame.image.load("assets/button/main_menu.png")
        background = pygame.transform.scale(
            background, (screen_width, screen_hight))
        SCREEN.blit(background, (0, 0))  # Draw background

        if Menu_play_btn.draw(SCREEN):
            game_state = "Level_Menu"
        if Menu_exit_btn.draw(SCREEN):
            run = False

    elif game_state == "Level_Menu":
        # Background image
        background = pygame.image.load("assets/button/level_menu.png")
        background = pygame.transform.scale(
            background, (screen_width, screen_hight))
        SCREEN.blit(background, (0, 0))  # Draw background

        level_word.draw(SCREEN)

        food_level.draw(SCREEN)
        animal_level.draw(SCREEN)
        place_level.draw(SCREEN)

        if Level_animal_btn.draw(SCREEN):
            game_category = "Animal"
            CATEGORY = load_category(game_category)
            game_level = 1

            gameplay = Game_play(CATEGORY, game_level)
            if gameplay.Rand_Level_Words(player_ans):  # pick a word
                gameplay.Shuffled()                    # shuffle it
                gameplay.Draw_ans()                    # build letter boxes

            game_state = "Gameplay"

        if Level_food_btn.draw(SCREEN):
            game_category = "Food"
            CATEGORY = load_category(game_category)
            game_level = 1

            gameplay = Game_play(CATEGORY, game_level)
            if gameplay.Rand_Level_Words(player_ans):  # pick a word
                gameplay.Shuffled()                    # shuffle it
                gameplay.Draw_ans()

            game_state = "Gameplay"

        if Level_place_btn.draw(SCREEN):
            game_category = "Place"
            CATEGORY = load_category(game_category)
            game_level = 1

            gameplay = Game_play(CATEGORY, game_level)
            if gameplay.Rand_Level_Words(player_ans):  # pick a word
                gameplay.Shuffled()                    # shuffle it
                gameplay.Draw_ans()

            game_state = "Gameplay"

    elif game_state == "Gameplay":
        world.draw(SCREEN)
        gameplay.update(SCREEN)

        if Game_enter_btn.draw(SCREEN):
            pass

        if Game_delete_btn.draw(SCREEN):
            pass

        if Game_shuffle_btn.draw(SCREEN):
            if gameplay.Rand_Level_Words(player_ans):  # pick a word
                gameplay.Shuffled()                    # shuffle it
                gameplay.Draw_ans()

    # Game Condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
