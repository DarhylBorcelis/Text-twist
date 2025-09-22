import pygame
import random

pygame.init()

# Window
screen_width, screen_hight = 1000, 600
SCREEN = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("Text Twist")

# Fonts
ULTRA_BIG_FONT = pygame.font.Font("assets/font/Hevilla.ttf", 90)
BIG_FONT = pygame.font.Font("assets/font/Seagram_tfb.ttf", 70)
FONT = pygame.font.Font("assets/font/Seagram_tfb.ttf", 22)

HINT_FONT = pygame.font.Font("assets/font/Hevilla.ttf", 28)
GAME_BTN_FONT = pygame.font.Font("assets/font/Seagram_tfb.ttf", 22)
MAIN_MENU_BTN_FONT = pygame.font.Font("assets/font/Hevilla.ttf", 22)
TITLE_FONT = pygame.font.Font("assets/font/Hevilla.ttf", 90)
PLACEHOLDER_FONT = pygame.font.Font("assets/font/Augusta.ttf", 22)

# Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Sound
CLICK_SOUND = pygame.mixer.Sound("assets/sound/click.mp3")
CLICK_SOUND.set_volume(0.5)


# Variables
game_state = "Main_Menu"
game_category = "Animal"
game_level = 1
player_ans = []
CATEGORY = {}


def load_category(game_category):
    if game_category == "Animal":
        return {
            1: [("CAT", "A pet that says meow"),
                ("DOG", "A pet that barks"),
                ("COW", "Gives us milk"),
                ("PIG", "Likes mud"),
                ("BAT", "A flying mammal"),
                ("RAT", "A rodent"),
                ("FOX", "Clever wild animal"),
                ("HEN", "Lays eggs"),
                ("ANT", "Tiny insect"),
                ("OWL", "Sees at night")],
            2: [("LION", "King of the jungle"),
                ("BEAR", "Big furry animal"),
                ("WOLF", "Howls at the moon"),
                ("FROG", "Jumps, says ribbit"),
                ("DEER", "Has antlers"),
                ("DUCK", "Says quack"),
                ("GOAT", "Likes grass"),
                ("CRAB", "Has claws"),
                ("SWAN", "Graceful white bird"),
                ("TOAD", "Like a frog")],
            3: [("HORSE", "You can ride it"),
                ("SHEEP", "Gives us wool"),
                ("MOUSE", "Small rodent"),
                ("TIGER", "Striped big cat"),
                ("ZEBRA", "Striped horse-like"),
                ("PANDA", "Eats bamboo"),
                ("SNAKE", "Slithers on ground"),
                ("LLAMA", "South American animal"),
                ("EAGLE", "Large bird of prey"),
                ("SHARK", "Big fish with sharp teeth")],
            4: [("MONKEY", "Loves bananas"),
                ("DONKEY", "Carries loads"),
                ("RABBIT", "Has long ears"),
                ("SPIDER", "Has eight legs"),
                ("TURTLE", "Has a shell"),
                ("PARROT", "Talks like humans"),
                ("SALMON", "Fish that swims upstream"),
                ("JAGUAR", "Spotted big cat"),
                ("BLOBFISH", "Ugly deep-sea fish"),
                ("GIRAFFE", "Has a long neck")],
            5: [("ECHIDNA", "Spiny anteater"),
                ("BUFFALO", "Large wild ox"),
                ("LEOPARD", "Spotted big cat"),
                ("MARKHOR", "Wild goat with spiral horns"),
                ("GORILLA", "Largest primate"),
                ("PELICAN", "Bird with large beak pouch"),
                ("OSTRICH", "Big bird that can’t fly"),
                ("COYOTE", "Wild dog of North America"),
                ("PIGEON", "Common city bird"),
                ("AXOLOTL", "Smiling salamander")]
        }

    elif game_category == "Food":
        return {
            1: [("RICE", "Staple food in Asia"),
                ("BREAD", "Made from flour"),
                ("SOUP", "Hot liquid meal"),
                ("CORN", "Yellow kernels"),
                ("CAKE", "Sweet baked dessert"),
                ("FISH", "Lives in water, eaten as food"),
                ("MEAT", "From animals"),
                ("EGGS", "Laid by hens"),
                ("MILK", "White drink from cows"),
                ("BEAN", "Small protein seed")],
            2: [("APPLE", "Keeps the doctor away"),
                ("MANGO", "Tropical sweet fruit"),
                ("PEACH", "Fuzzy fruit"),
                ("GRAPE", "Used for wine"),
                ("LEMON", "Sour yellow fruit"),
                ("ONION", "Makes you cry"),
                ("PIZZA", "Italian flatbread"),
                ("PASTA", "Italian noodles"),
                ("BERRY", "Small juicy fruit"),
                ("CHILI", "Very spicy")],
            3: [("BANANA", "Yellow curved fruit"),
                ("TOMATO", "Red fruit used in salad"),
                ("ORANGE", "Citrus fruit"),
                ("CARROT", "Orange vegetable"),
                ("PEANUT", "Nut in a shell"),
                ("BURGER", "Bread with meat patty"),
                ("COOKIE", "Sweet baked snack"),
                ("HONEY", "Sweet food from bees"),
                ("JUICE", "Drink from fruits"),
                ("SALAD", "Mix of vegetables")],
            4: [("CHERRY", "Small red fruit"),
                ("PUMPKIN", "Big orange vegetable"),
                ("GARLIC", "Strong-smelling bulb"),
                ("COFFEE", "Bitter morning drink"),
                ("DONUTS", "Sweet fried bread"),
                ("NOODLE", "Long thin pasta"),
                ("BUTTER", "Made from milk"),
                ("SPINACH", "Leafy green vegetable"),
                ("CHEESE", "Made from milk"),
                ("SUGAR", "Sweet crystals")],
            5: [("POTATOE", "Used for fries"),
                ("CHICKEN", "Common white meat"),
                ("CHOCOLATE", "Sweet made from cocoa"),
                ("CABBAGE", "Leafy vegetable"),
                ("ICECREAM", "Frozen dessert"),
                ("SANDWICH", "Two breads with filling"),
                ("PANCAKE", "Flat breakfast food"),
                ("CEREALS", "Breakfast grain"),
                ("YOGURT", "Fermented milk"),
                ("SEAFOOD", "Food from the sea")]
        }

    elif game_category == "Place":
        return {
            1: [("PARK", "Place to play outside"),
                ("MALL", "Shopping center"),
                ("HOME", "Where you live"),
                ("ROOM", "Part of a house"),
                ("FARM", "Where crops grow"),
                ("CITY", "Big town"),
                ("BANK", "Keeps money safe"),
                ("SHOP", "Small store"),
                ("POOL", "Place to swim"),
                ("LOBBY", "Entrance hall")],
            2: [("RIVER", "Flows with water"),
                ("FIELD", "Open land"),
                ("BEACH", "Sandy shore"),
                ("HOTEL", "Stay when traveling"),
                ("SCHOOL", "Place to study"),
                ("MARKET", "Place to buy things"),
                ("CHURCH", "Place of worship"),
                ("BRIDGE", "Connects two sides"),
                ("MUSEUM", "Keeps history"),
                ("STREET", "Road in a city")],
            3: [("CASTLE", "Home of kings"),
                ("FOREST", "Many trees"),
                ("OFFICE", "Place to work"),
                ("TEMPLE", "Sacred building"),
                ("ISLAND", "Land in water"),
                ("STADIUM", "Sports arena"),
                ("PRISON", "Holds criminals"),
                ("TUNNEL", "Underground passage"),
                ("TOWER", "Tall building"),
                ("PALACE", "Home of royalty")],
            4: [("VILLAGE", "Small community"),
                ("HOSPITAL", "Doctors work here"),
                ("AIRPORT", "Planes take off"),
                ("STATION", "Trains stop here"),
                ("MARKETS", "Places to buy goods"),
                ("THEATER", "Watch plays or movies"),
                ("FACTORY", "Makes products"),
                ("HARBOR", "Where ships dock"),
                ("CHURCHES", "More than one church"),
                ("GARDENS", "Where plants grow")],
            5: [("MOUNTAIN", "Tall landform"),
                ("LIBRARY", "Keeps books"),
                ("COTTAGE", "Small house"),
                ("UNIVERSITY", "Place of higher study"),
                ("RESTAURANT", "Place to eat"),
                ("APARTMENT", "Many homes in one building"),
                ("PLAYGROUND", "Children play here"),
                ("CEMETERY", "Where people are buried"),
                ("WAREHOUSE", "Stores goods"),
                ("SUBWAY", "Underground train")]
        }


def Background_img(game_category, game_level):
    if game_category == "Animal":
        Game_play_world.add_design(
            "assets/button/bord2.png", 120, 5, 730, 430)   # Black Board
        Game_play_world.add_design(
            "assets/button/animal_banner2.png", 50, 30, 130, 210)  # Banner
        Game_play_world.add_design("assets/button/ans2.png", 250,
                                   390, 500, 70)  # Ans Placeholder

        Game_play_world.text(game_category, color=WHITE, x_cord=80,
                             y_cord=80, font=FONT)
        Game_play_world.text(str(game_level), color=WHITE, x_cord=95,
                             y_cord=100, font=BIG_FONT)

        Game_play_world.set_background("assets/button/gameplay.png")

    elif game_category == "Food":
        Game_play_world.add_design(
            "assets/button/bord1.png", 150, -180, 700, 800)   # Black Board
        Game_play_world.add_design(
            "assets/button/animal_banner1.png", 50, 30, 130, 210)  # Banner
        Game_play_world.add_design("assets/button/ans1.png", 250,
                                   390, 500, 70)  # Ans Placeholder

        Game_play_world.text(game_category, color=WHITE, x_cord=88,
                             y_cord=81, font=FONT)
        Game_play_world.text(str(game_level), color=WHITE, x_cord=95,
                             y_cord=100, font=BIG_FONT)

        Game_play_world.set_background("assets/button/gameplay1.png")

    elif game_category == "Place":
        Game_play_world.add_design(
            "assets/button/bord.png", 150, -190, 700, 800)   # Black Board
        Game_play_world.add_design(
            "assets/button/animal_banner3.png", 50, 30, 130, 210)  # Banner
        Game_play_world.add_design("assets/button/ans.png", 250,
                                   390, 500, 70)  # Ans Placeholder

        Game_play_world.text(game_category, color=WHITE, x_cord=88,
                             y_cord=75, font=FONT)
        Game_play_world.text(str(game_level), color=WHITE, x_cord=95,
                             y_cord=100, font=BIG_FONT)

        Game_play_world.set_background("assets/button/gameplay3.png")


FOOD = load_category("Food")
ANIMAL = load_category("Animal")
PLACE = load_category("Place")

# Image
# Level image
FOOD_BANNER = "assets/button/food_banner.png"
PLACE_BANNER = "assets/button/Place_banner.png"
ANIMAL_BANNER = "assets/button/animal_banner.png"
# Menu image
MAIN_MENU_BTN = "assets/button/Start_btn.png"
PLAY_IMAGE = "assets/button/ans.png"
BUTTON_IMAGE = "assets/button/button.png"


class Button:
    def __init__(self, x, y, image, scale, text="", font=FONT, text_color=WHITE, key=None, cooldown=300):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, scale)
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

    def event_handler(self):
        action = False
        current_time = pygame.time.get_ticks()

        if self.key:
            keys = pygame.key.get_pressed()
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

    def draw(self, SCREEN):
        # Draw button
        SCREEN.blit(self.image, self.rect)
        # Draw text
        if self.text_surface:
            SCREEN.blit(self.text_surface, self.text_rect)


class World:
    def __init__(self, img=None):
        # Keep a list of all "design" and texts
        self.designs = []
        self.text_lis = []
        self.background_img = None   # Default = no background

        if img:  # Only load if an image was given
            self.set_background(img)

    def clear(self):
        self.designs = []
        self.text_lis = []

    def text(self, name="", color=WHITE, x_cord=0, y_cord=0, font=BIG_FONT):
        txt = font.render(name, True, color)
        self.text_lis.append({
            "text": txt,
            "x_cord": x_cord,
            "y_cord": y_cord
        })

    def set_background(self, img):
        background = pygame.image.load(img)
        self.background_img = pygame.transform.scale(background, (1000, 600))

    def add_design(self, image, x, y, width, height):
        image = pygame.image.load(image)
        image = pygame.transform.scale(image, (width, height))
        rect = image.get_rect(topleft=(x, y))
        self.designs.append((image, rect))

    def draw(self, SCREEN):
        # Draw background only if available
        if self.background_img:
            SCREEN.blit(self.background_img, (0, 0))

        # Draw all designs
        for img, rect in self.designs:
            SCREEN.blit(img, rect)

        # Draw all texts
        for item in self.text_lis:
            SCREEN.blit(item["text"], (item["x_cord"], item["y_cord"]))


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
        font = pygame.font.Font("assets/font/Hevilla.ttf", 25)
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

            txt_surface = font.render(word, True, WHITE)
            SCREEN.blit(txt_surface, (x, y))

    def Update_keyboard(self, event):
        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(
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
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = event.pos
            for i, letter in enumerate(self.letters):
                if letter["rect"].collidepoint(pos) and letter["active"]:
                    self.guest.append(letter["char"])
                    letter["active"] = False
                    self.used_stack.append(i)
                    break

    def Draw(self, SCREEN):
        font = pygame.font.Font("assets/font/AUGUSTUS.TTF", 25)
        for letter in self.letters:
            SCREEN.blit(letter["img"], letter["rect"])
            if letter["active"]:
                SCREEN.blit(letter["text_surface"], letter["text_rect"])

        guess_text = "".join(self.guest)
        x_cord = (1000 - (len(self.choices) * 30)) // 2
        txt_surf = font.render(guess_text, True, WHITE)
        SCREEN.blit(txt_surf, (x_cord, 413))

    def draw_hint(self, SCREEN):
        if self.hint_active:
            font = pygame.font.Font("assets/font/Hevilla.ttf", 28)
            txt = font.render("Hint: "+self.hint, True, WHITE)
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
            font = pygame.font.Font("assets/font/AUGUSTUS.TTF", 25)
            img = "assets/button/letters2.png"
            color = WHITE
            x_size, y_size = 90, 60
        elif category == "Animal":
            font = pygame.font.Font("assets/font/AUGUSTUS.TTF", 25)
            img = "assets/button/letters1.png"
            color = WHITE
            x_size, y_size = 90, 60
        elif category == "Place":
            font = pygame.font.Font("assets/font/AUGUSTUS.TTF", 25)
            img = "assets/button/letters3.png"
            color = WHITE
            x_size, y_size = 90, 60

        base_img = pygame.image.load(img)
        base_img = pygame.transform.scale(base_img, (x_size, y_size))

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
Menu_play_btn = Button(410, 280, MAIN_MENU_BTN, (160, 110),
                       "Play", key=pygame.K_RETURN, font=MAIN_MENU_BTN_FONT)
Menu_exit_btn = Button(440, 390, PLAY_IMAGE, (100, 40),
                       "Exit", key=pygame.K_ESCAPE, font=MAIN_MENU_BTN_FONT)

# Game play buttons

Game_next_btn = Button(800, 295, BUTTON_IMAGE, (150, 50),
                       "Next Level", key=pygame.K_2, font=GAME_BTN_FONT)
Game_back_btn = Button(850, 10, BUTTON_IMAGE, (100, 50),
                       "Back", key=pygame.K_ESCAPE, font=GAME_BTN_FONT)


# level buttons
Level_back_btn = Button(690, -10, BUTTON_IMAGE, (100, 50),
                        "Back", key=pygame.K_ESCAPE)
Level_food_btn = Button(430, 60, PLAY_IMAGE, (120, 40), "food", key=pygame.K_f)
Level_animal_btn = Button(430, 230, PLAY_IMAGE,
                          (120, 40), "animal", key=pygame.K_a)
Level_place_btn = Button(430, 400, PLAY_IMAGE,
                         (120, 40), "place", key=pygame.K_p)

# game play World
Game_play_world = World()

# Level world
level_word = World()
level_word.set_background("assets/button/level_menu.png")
level_word.add_design("assets/button/top_level.png", 5, -5, 1000, 80)
level_word.add_design("assets/button/buttom_level.png", 5, 550, 1000, 80)

food_level = Level(FOOD_BANNER, 100, 230, FOOD)
animal_level = Level(ANIMAL_BANNER, 270, 230, ANIMAL)
place_level = Level(PLACE_BANNER, 440, 230, PLACE)

# Main menu world
Main_menu_world = World()
Main_menu_world.set_background("assets/button/main_menu.png")
Main_menu_world.text("TEXT TWIST", color=BLACK, x_cord=280,
                     y_cord=70, font=ULTRA_BIG_FONT)


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

            # keybord
            if Menu_play_btn.event_handler():
                game_state = "Level_Menu"
            if Menu_exit_btn.event_handler():
                run = False

            # event handler
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if Menu_play_btn.rect.collidepoint(pos):
                    game_state = "Level_Menu"
                    CLICK_SOUND.play()
                if Menu_exit_btn.rect.collidepoint(pos):
                    run = False

        elif game_state == "Level_Menu":

            # Level World design
            level_word.draw(SCREEN)

            # Level Category
            food_level.draw(SCREEN)
            animal_level.draw(SCREEN)
            place_level.draw(SCREEN)

            # Level btn
            Level_animal_btn.draw(SCREEN)
            Level_food_btn.draw(SCREEN)
            Level_place_btn.draw(SCREEN)

            # Keyboard
            if Level_back_btn.event_handler():
                game_state = "Main_Menu"

            # event handler
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                if Level_back_btn.rect.collidepoint(pos):
                    game_state = "Main_Menu"

                clicked_food_level = food_level.update(event)
                clicked_animal_level = animal_level.update(event)
                clicked_place_level = place_level.update(event)

                if clicked_food_level:
                    CLICK_SOUND.play()

                    game_level = clicked_food_level
                    game_category = "Food"

                    Game_enter_btn = Button(800, 95, "assets/button/button2.png", (150, 50),
                                            "Enter", key=pygame.K_RETURN, font=GAME_BTN_FONT)
                    Game_delete_btn = Button(800, 145, "assets/button/button2.png", (150, 50),
                                             "Delete", key=pygame.K_BACKSPACE, font=GAME_BTN_FONT)
                    Game_shuffle_btn = Button(800, 195, "assets/button/button2.png", (150, 50),
                                              "Shuffle", key=pygame.K_SPACE, font=GAME_BTN_FONT)
                    Game_hint_btn = Button(800, 245, "assets/button/button2.png", (150, 50),
                                           "Hint", key=pygame.K_1, font=GAME_BTN_FONT)

                    CATEGORY = load_category(game_category)
                    gameplay = Game_play(CATEGORY, game_level)

                    Background_img(game_category, game_level)

                    if gameplay.Rand_Level_Words(player_ans):
                        gameplay.Shuffled()
                        gameplay.Update_ans(game_category)
                    game_state = "Gameplay"

                elif clicked_animal_level:
                    CLICK_SOUND.play()

                    game_level = clicked_animal_level
                    game_category = "Animal"

                    Game_enter_btn = Button(800, 95, "assets/button/button1.png", (150, 50),
                                            "Enter", key=pygame.K_RETURN, font=GAME_BTN_FONT)
                    Game_delete_btn = Button(800, 145, "assets/button/button1.png", (150, 50),
                                             "Delete", key=pygame.K_BACKSPACE, font=GAME_BTN_FONT)
                    Game_shuffle_btn = Button(800, 195, "assets/button/button1.png", (150, 50),
                                              "Shuffle", key=pygame.K_SPACE, font=GAME_BTN_FONT)
                    Game_hint_btn = Button(800, 245, "assets/button/button1.png", (150, 50),
                                           "Hint", key=pygame.K_1, font=GAME_BTN_FONT)

                    CATEGORY = load_category(game_category)
                    gameplay = Game_play(CATEGORY, game_level)

                    Background_img(game_category, game_level)

                    if gameplay.Rand_Level_Words(player_ans):
                        gameplay.Shuffled()
                        gameplay.Update_ans(game_category)
                    game_state = "Gameplay"

                elif clicked_place_level:
                    CLICK_SOUND.play()

                    game_level = clicked_place_level
                    game_category = "Place"

                    Game_enter_btn = Button(800, 95, "assets/button/button3.png", (150, 50),
                                            "Enter", key=pygame.K_RETURN, font=GAME_BTN_FONT)
                    Game_delete_btn = Button(800, 145, "assets/button/button3.png", (150, 50),
                                             "Delete", key=pygame.K_BACKSPACE, font=GAME_BTN_FONT)
                    Game_shuffle_btn = Button(800, 195, "assets/button/button3.png", (150, 50),
                                              "Shuffle", key=pygame.K_SPACE, font=GAME_BTN_FONT)
                    Game_hint_btn = Button(800, 245, "assets/button/button3.png", (150, 50),
                                           "Hint", key=pygame.K_1, font=GAME_BTN_FONT)

                    CATEGORY = load_category(game_category)
                    gameplay = Game_play(CATEGORY, game_level)

                    Background_img(game_category, game_level)

                    if gameplay.Rand_Level_Words(player_ans):
                        gameplay.Shuffled()
                        gameplay.Update_ans(game_category)
                    game_state = "Gameplay"

        elif game_state == "Gameplay":
            # Draw game design
            Game_play_world.draw(SCREEN)
            gameplay.Draw(SCREEN)
            gameplay.draw_hint(SCREEN)

            # Handle inputs
            gameplay.Update_2(event)          # mouse click
            gameplay.Update_keyboard(event)   # keyboard press

            # Draw solved answers inside the board
            gameplay.draw_answers(SCREEN, player_ans)

            # draw btn
            Game_enter_btn.draw(SCREEN)
            Game_delete_btn.draw(SCREEN)
            Game_shuffle_btn.draw(SCREEN)
            Game_hint_btn.draw(SCREEN)

            # draw hint
            words_left = len(gameplay.level_words) - len(player_ans)
            words_surface = HINT_FONT.render(
                f"{words_left} Words left", True, WHITE)
            SCREEN.blit(words_surface, (810, 60))

            if words_left == 0:
                Game_next_btn.draw(SCREEN)

                if Game_next_btn.event_handler():
                    player_ans = []
                    Game_play_world.clear()
                    game_level += 1
                    Background_img(game_category, game_level)
                    gameplay.clear(CATEGORY, game_level)

            # Keyboard
            if Game_enter_btn.event_handler():
                CLICK_SOUND.play()
                if "".join(gameplay.guest) == gameplay.Ans_word:
                    if gameplay.Ans_word != "":
                        player_ans.append(gameplay.Ans_word)
                    if gameplay.Rand_Level_Words(player_ans):  # pick a word
                        gameplay.Shuffled()
                        gameplay.Update_ans(game_category)
                else:
                    gameplay.reset_all_letters()

            if Game_delete_btn.event_handler():
                CLICK_SOUND.play()
                gameplay.delete_last_letter()

            if Game_shuffle_btn.event_handler():
                CLICK_SOUND.play()
                if gameplay.Rand_Level_Words(player_ans):  # pick a word
                    gameplay.Shuffled()
                    gameplay.Update_ans(game_category)

            if Game_hint_btn.event_handler():
                CLICK_SOUND.play()
                if gameplay.hint_active:
                    gameplay.hint_active = False
                else:
                    gameplay.hint_active = True

            if Game_back_btn.event_handler():
                CLICK_SOUND.play()
                player_ans = []
                Game_play_world.clear()
                game_state = "Level_Menu"

            # Mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                if words_left == 0:
                    Game_next_btn.draw(SCREEN)
                    if Game_next_btn.rect.collidepoint(pos):
                        player_ans = []
                        Game_play_world.clear()
                        game_level += 1
                        Background_img(game_category, game_level)
                        gameplay.clear(CATEGORY, game_level)

                if Game_enter_btn.rect.collidepoint(pos):
                    CLICK_SOUND.play()
                    if "".join(gameplay.guest) == gameplay.Ans_word:
                        if gameplay.Ans_word != "":
                            player_ans.append(gameplay.Ans_word)
                        if gameplay.Rand_Level_Words(player_ans):
                            gameplay.Shuffled()
                            gameplay.Update_ans(game_category)
                    else:
                        gameplay.reset_all_letters()

                if Game_delete_btn.rect.collidepoint(pos):
                    CLICK_SOUND.play()
                    gameplay.delete_last_letter()

                if Game_shuffle_btn.rect.collidepoint(pos):
                    CLICK_SOUND.play()
                    if gameplay.Rand_Level_Words(player_ans):  # pick a word
                        gameplay.Shuffled()
                        gameplay.Update_ans(game_category)

                if Game_hint_btn.rect.collidepoint(pos):
                    CLICK_SOUND.play()
                    if gameplay.hint_active:
                        gameplay.hint_active = False
                    else:
                        gameplay.hint_active = True

                if Game_back_btn.rect.collidepoint(pos):
                    CLICK_SOUND.play()
                    player_ans = []
                    Game_play_world.clear()
                    game_state = "Level_Menu"

    pygame.display.update()

pygame.quit()
