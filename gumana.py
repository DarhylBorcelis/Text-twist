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

# Background image
background = pygame.image.load("assets/button/background.png")
background = pygame.transform.scale(background, (screen_width, screen_hight))


# Variables
game_state = "Main_Menu"
game_category = "Animal"
game_level = 1
player_ans = []
CATEGORY = {}

# Dictionary
if game_category == "Animal":
    CATEGORY = {
        1: ["CAT", "DOG", "COW", "PIG", "BAT", "RAT", "FOX", "HEN", "ANT", "OWL"],
        2: ["LION", "BEAR", "WOLF", "FROG", "DEER", "DUCK", "GOAT", "CRAB", "SWAN", "TOAD"],
        3: ["HORSE", "SHEEP", "MOUSE", "TIGER", "ZEBRA", "PANDA", "SNAKE", "LLAMA", "EAGLE", "SHARK"],
        4: ["MONKEY", "DONKEY", "RABBIT", "SPIDER", "TURTLE", "PARROT", "SALMON", "JAGUAR", "CAMEL", "GIRAFFE"],
        5: ["DOLPHIN", "BUFFALO", "LEOPARD", "CHICKEN", "GORILLA", "PELICAN", "OSTRICH", "COYOTE", "PIGEON", "DRAGON"]
    }


# Image
if game_category == "Animal":
    BUTTON_IMAGE = "assets/button/button.png"
    BACKGROUND_IMAGE = "assets/button/background.png"
    PLAY_IMAGE = "assets/button/ans.png"
    BANER_IMAGE = "assets/button/banner.png"
    BOARD_IMAGE = "assets/button/bord.png"
    PLACEHOLDER_IMAGE = "assets/button/ans.png"


class Button:
    def __init__(self, x, y, image, scale, text="", font=FONT, text_color=WHITE):
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

        if self.font and self.text != "":
            self.text_surface = self.font.render(
                self.text, True, self.text_color)
            self.text_rect = self.text_surface.get_rect(
                center=self.rect.center)
        else:
            self.text_surface = None

    def draw(self, SCREEN):
        action = False
        # Draw button
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


class Game_play():
    def __init__(self, category, game_level):
        image = pygame.image.load("assets/button/letters.png")
        image = image = pygame.transform.scale(image, (80, 50))

    def rand_Level_Words(self):
        self.word = random.choice(self.available_word)
        self.shuffled = random.shuffle(list(self.word))


def Rand_Level_Words(word, player_ans):
    available_words = [w for w in word if w not in player_ans]
    if not available_words:
        return []  # all words found
    else:
        return random.choice(available_words)


def Shuffled(ans_word):
    letters = list(ans_word)
    shuffled = "".join(letters)
    while shuffled == ans_word:
        random.shuffle(letters)
        shuffled = "".join(letters)
    return shuffled


# Update var
Level_words = CATEGORY[game_level]
Ans_word = Rand_Level_Words(Level_words, player_ans)
choices = Shuffled(Ans_word)


# Buttons
Menu_play_btn = Button(430, 280, PLAY_IMAGE, (120, 60), "Play")
Menu_exit_btn = Button(430, 350, PLAY_IMAGE, (120, 60), "Exit")
Game_enter_btn = Button(690, -15, BUTTON_IMAGE, (400, 350), "Enter")
Game_delete_btn = Button(690, 35, BUTTON_IMAGE, (400, 350), "Delete")
Game_shuffle_btn = Button(690, 85, BUTTON_IMAGE, (400, 350), "Shuffle")
Level_food_btn = Button(50, 10, BANER_IMAGE, (110, 180), "Food")
Level_animal_btn = Button(50, 185, BANER_IMAGE, (110, 180), "animal")
Level_place_btn = Button(50, 360, BANER_IMAGE, (110, 180), "Place")

# World
world = World()
# Add designs
world.add_design("assets/background/menu_2.png", 0,
                 0, screen_width, screen_hight)  # Background
world.add_design(BOARD_IMAGE, 150, -190, 700, 800)   # Black Board
world.add_design(BANER_IMAGE, 50, 30, 130, 210)  # Banner
world.add_design(PLACEHOLDER_IMAGE, 250, 400, 500, 50)  # Ans Placeholder


# Game loop
run = True
while run:

    if game_state == "Main_Menu":
        SCREEN.blit(background, (0, 0))  # Draw background
        if Menu_play_btn.draw(SCREEN):
            game_state = "Level_Menu"
        if Menu_exit_btn.draw(SCREEN):
            run = False

    elif game_state == "Level_Menu":
        SCREEN.blit(background, (0, 0))  # Draw background
        if Level_animal_btn.draw(SCREEN):
            game_category = "Animal"
            game_state = "Gameplay"
        if Level_food_btn.draw(SCREEN):
            game_category = "Food"
            game_state = "Gameplay"
        if Level_place_btn.draw(SCREEN):
            game_category = "Place"
            game_state = "Gameplay"

    elif game_state == "Gameplay":
        world.draw(SCREEN)
        if Game_enter_btn.draw(SCREEN):
            pass
        if Game_delete_btn.draw(SCREEN):
            pass
        if Game_shuffle_btn.draw(SCREEN):
            pass

    # Game Condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
