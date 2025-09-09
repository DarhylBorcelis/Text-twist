import pygame
import random

pygame.init()

# Window
SCREEN = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Any Game")

# Fonts
FONT = pygame.font.Font("assets/Font/Hevilla.ttf", 22)

# Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Image
CHOICES_IMAGE = "assets/button/letters.png"
BACKGROUND_IMAGE = "assets/button/background.png"
PLAY_IMAGE = "assets/button/ans.png"
LEVEL_IMAGE = "assets/button/ans.png"
BORD_IMAGE = "assets/button/bord.png"
PLACEHOLDER_IMAGE = "assets/button/ans.png"
BUTTON_IMAGE = "assets/button/button.png"
LIFE_IMAGE = "assets/button/life.png"
BANER_IMAGE = "assets/button/baner.png"

# Backround image
background = pygame.image.load(BACKGROUND_IMAGE)
background = pygame.transform.scale(background, (1000, 600))

# Dictionary
FOODS = {
    1: ["CAT", "DOG", "COW", "PIG", "BAT", "RAT", "FOX", "HEN", "ANT", "OWL"],
    2: ["LION", "BEAR", "WOLF", "FROG", "DEER", "DUCK", "GOAT", "CRAB", "SWAN", "TOAD"],
    3: ["HORSE", "SHEEP", "MOUSE", "TIGER", "ZEBRA", "PANDA", "SNAKE", "LLAMA", "EAGLE", "SHARK"],
    4: ["MONKEY", "DONKEY", "RABBIT", "SPIDER", "TURTLE", "PARROT", "SALMON", "JAGUAR", "CAMEL", "GIRAFFE"],
    5: ["DOLPHIN", "BUFFALO", "LEOPARD", "CHICKEN", "GORILLA", "PELICAN", "OSTRICH", "COYOTE", "PIGEON", "DRAGON"],
    6: ["ELEPHANT", "CROCODILE", "KANGAROO", "FLAMINGO", "ALLIGATOR", "CHAMELEON", "ANTELOPE", "SQUIRREL", "SEAHORSE", "ARMADILLO"],
    7: ["HIPPOPOTAMUS", "RHINOCEROS", "PORCUPINE", "WILDEBEEST", "ORANGUTAN", "WOODPECKER", "CATERPILLAR", "HEDGEHOG", "COCKROACH", "FIREFLY"],
    8: ["CHIMPANZEE", "CROCODILIAN", "BUTTERFLY", "JELLYFISH", "GRASSHOPPER", "SCORPION", "DRAGONFLY", "ANTEATER", "STARFISH", "WATERFOWL"],
    9: ["ARCHAEOPTERYX", "PTERODACTYL", "STEGOCEPHALUS", "TRICERATOPS", "BRONTOSAURUS", "TYRANNOSAURUS", "ICHNEUMONID", "SPINOSAURUS", "MEGALODON", "ANKYLOSAURUS"]
}

# Database
category = FOODS
game_state = "Level"
current_level = 1
letters = []
choices = []
guests = []
player_ans = []


class Box:  # Create box
    def __init__(self, x_cord, y_cord, width, height, name, image, font):
        self.rect = pygame.Rect(x_cord, y_cord, width, height)
        self.letter = name
        self.font = font
        self.active = True
        self.image = pygame.transform.scale(
            pygame.image.load(image), (width, height))
        self.name = font.render(name, True, BLACK)

    def update_text(self, name=None, visible=True, color=BLACK):
        if name is not None:
            self.letter = name

        if visible:
            self.name = self.font.render(self.letter, True, color)
            self.active = True
        else:
            self.name = self.font.render("", True, color)
            self.active = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        text_rect = self.name.get_rect(center=self.rect.center)
        surface.blit(self.name, text_rect)


def rand_Level_Words(Level_Words, player_ans):
    global letters
    available_words = [w for w in Level_Words if w not in player_ans]
    if not available_words:
        return []  # all words found
    word = random.choice(available_words)
    letters = list(word)
    shuffled = list(word)
    random.shuffle(shuffled)
    return shuffled


def choices_box(shuffled_letters):  # Create choices box
    rect = []
    start_x = (1000 - (len(shuffled_letters) * 90)) // 2
    y_cord = 470
    for i, char in enumerate(shuffled_letters):
        now = Box(
            x_cord=start_x + i * 90,
            y_cord=y_cord,
            width=80,
            height=50,
            name=char,
            image=CHOICES_IMAGE,
            font=FONT
        )
        rect.append(now)
    return rect


# def level_box():  # Create Level box
#     rect = []
#     for i in range(1, 10):
#         level = LEVELS[i]

def button_box():
    ans = "".join(guests)

    black_bord = Box(200, 60, 600, 300, " ", BORD_IMAGE, FONT)
    ans_placeholder = Box(250, 400, 500, 50, ans, PLACEHOLDER_IMAGE, FONT)
    life = Box(830, 30, 140, 50, "", LIFE_IMAGE, FONT)
    baner = Box(0, 30, 200, 220, "", BANER_IMAGE, FONT)

    enter = Box(850, 100, 100, 50, "Enter", BUTTON_IMAGE, FONT)
    delete = Box(850, 170, 100, 50, "Delete", BUTTON_IMAGE, FONT)
    shuffle = Box(850, 240, 100, 50, "Shuffle", BUTTON_IMAGE, FONT)

    # Draw Design
    black_bord.draw(SCREEN)
    life.draw(SCREEN)
    baner.draw(SCREEN)

    # Update answer placeholder before drawing
    ans_placeholder.update_text(name=ans, color=WHITE)
    ans_placeholder.draw(SCREEN)

    # Draw buttons
    enter.draw(SCREEN)
    delete.draw(SCREEN)
    shuffle.draw(SCREEN)

    return enter, delete, shuffle


def draw_game(choices):  # Draw game
    for box in choices:
        if box.active:
            box.update_text(visible=True)
        else:
            box.update_text(visible=False)
        box.draw(SCREEN)


# def draw_level():
#     level_1 = Box(x_cord=120, y_cord=280, width=80, height=50,
#                   name="Level", image=LEVEL_IMAGE, font=FONT)

# Variables
Level_Words = FOODS[current_level]  # all the word in level
shuffled_letters = rand_Level_Words(
    Level_Words, player_ans)  # shuffled_letters
choices = choices_box(shuffled_letters)  # put the shuffled_letters in box

# Button
play = Box(x_cord=120, y_cord=280, width=80, height=50,
           name="play", image=PLAY_IMAGE, font=FONT)

# Game loop
run = True
while run:
    SCREEN.blit(background, (0, 0))

    # Game state : Menu
    if game_state == "Menu":
        play.draw(SCREEN)

    # Game state : Play
    elif game_state == "Play":
        pass
        # draw_level()

    # Game state : Level
    elif game_state == "Level":
        enter_btn, delete_btn, shuffle_btn = button_box()
        draw_game(choices)

    # Game Condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if game_state == "Menu":
            # Mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if play.rect.collidepoint(pos):
                    game_state = "Play"

            # Keyboard
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Enter
                    game_state = "Play"

        elif game_state == "Play":
            # Mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if play.rect.collidepoint(pos):
                    game_state = "Level"

            # Keyboard
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Enter
                    game_state = "Level"

        elif game_state == "Level":

            # Mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                for box in choices:  # for letters
                    if box.active and box.rect.collidepoint(pos):
                        guests.append(box.letter)
                        box.active = False

                if shuffle_btn.rect.collidepoint(pos):  # for shuffle
                    shuffled_letters = rand_Level_Words(
                        Level_Words, player_ans)
                    choices = choices_box(shuffled_letters)
                    guests = []

                if enter_btn.rect.collidepoint(pos):  # for Enter
                    now = "".join(guests).upper()
                    guests = []
                    if now in Level_Words and now not in player_ans:
                        player_ans.append(now)
                        shuffled_letters = rand_Level_Words(
                            Level_Words, player_ans)
                        if shuffled_letters:
                            choices = choices_box(shuffled_letters)
                        else:
                            print("You win")
                    else:
                        for box in choices:
                            box.active = True

            # Keyboard
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    guests = []
                    for box in choices:
                        box.active = True
                    game_state = "Menu"

                elif event.key == pygame.K_SPACE:
                    guests = []
                    for box in choices:
                        box.active = True

                elif event.key == pygame.K_BACKSPACE:
                    if guests:
                        removed_letter = guests.pop()
                        for box in choices:
                            if box.letter == removed_letter and not box.active:
                                box.active = True
                                break

                elif event.key == pygame.K_RETURN:
                    now = "".join(guests).upper()
                    guests = []
                    if now in Level_Words and now not in player_ans:
                        player_ans.append(now)
                        shuffled_letters = rand_Level_Words(
                            Level_Words, player_ans)
                        if shuffled_letters:
                            choices = choices_box(shuffled_letters)
                        else:
                            print("You win")
                    else:
                        for box in choices:
                            box.active = True

                else:
                    typed_char = event.unicode.upper()
                    for box in choices:
                        if box.active and box.letter == typed_char:
                            guests.append(typed_char)
                            box.active = False
                            break

    pygame.display.update()

pygame.quit()
