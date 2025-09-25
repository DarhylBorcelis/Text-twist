import pygame as PY
import Constant as C
from world_class import World
from button_class import Button
from level_class import Level
from game_play_class import Game_play
from Category_data import ANIMAL_CATEGORY, FOOD_CATEGORY, PLACE_CATEGORY

PY.init()

# Draw Window
SCREEN = PY.display.set_mode((C.SCREEN_WIDTH, C.SCREEN_HIGHT))
PY.display.set_caption("TEXT TWIST")

# Font
FONT = PY.font.Font(C.Seagram_tfb, 22)
BIG_FONT = PY.font.Font(C.Seagram_tfb, 70)
TITLE_SCREEN_BTN_FONT = PY.font.Font(C.Hevilla, 22)
HINT_FONT = PY.font.Font(C.Hevilla, 28)

# Variable
game_state = "Title_screen"
game_category = "Animal"
game_level = 1
player_ans = []
CATEGORY = {}

unlocked_food = 1
unlocked_animal = 1
unlocked_place = 1


def load_category(game_category):
    if game_category == "Animal":
        return ANIMAL_CATEGORY

    elif game_category == "Food":
        return FOOD_CATEGORY

    elif game_category == "Place":
        return PLACE_CATEGORY


def Background_img(game_category, game_level):
    if game_category == "Animal":
        Game_play_world.add_design(
            C.ANIMAL_BOARD, 120, 5, 730, 430)   # Black Board
        Game_play_world.add_design(
            C.ANIMAL_BANNER_1, 50, 30, 130, 210)  # Banner
        Game_play_world.add_design(
            C.ANIMAL_ANS, 250, 390, 500, 70)  # Ans Placeholder

        Game_play_world.text(game_category, color=C.WHITE, x_cord=80,
                             y_cord=80, font=C.Seagram_tfb, f_size=22)
        Game_play_world.text(str(game_level), color=C.WHITE, x_cord=95,
                             y_cord=100, font=C.Seagram_tfb, f_size=70)

        Game_play_world.Set_bg(C.ANIMAL_BG)

    elif game_category == "Food":
        Game_play_world.add_design(
            C.FOOD_BOARD, 150, -180, 700, 800)   # Black Board
        Game_play_world.add_design(
            C.FOOD_BANNER_1, 50, 30, 130, 210)  # Banner
        Game_play_world.add_design(
            C.FOOD_ANS, 250, 390, 500, 70)  # Ans Placeholder

        Game_play_world.text(game_category, color=C.WHITE, x_cord=88,
                             y_cord=81, font=C.Seagram_tfb, f_size=22)
        Game_play_world.text(str(game_level), color=C.WHITE, x_cord=95,
                             y_cord=100, font=C.Seagram_tfb, f_size=70)

        Game_play_world.Set_bg(C.FOOD_BG)

    elif game_category == "Place":
        Game_play_world.add_design(
            C.PLACE_BOARD, 150, -190, 700, 800)   # Black Board
        Game_play_world.add_design(
            C.PLACE_BANNER_1, 50, 30, 130, 210)  # Banner
        Game_play_world.add_design(
            C.PLACE_ANS, 250, 390, 500, 70)  # Ans Placeholder

        Game_play_world.text(game_category, color=C.WHITE, x_cord=88,
                             y_cord=75, font=C.Seagram_tfb, f_size=22)
        Game_play_world.text(str(game_level), color=C.WHITE, x_cord=95,
                             y_cord=100, font=C.Seagram_tfb, f_size=70)

        Game_play_world.Set_bg(C.PLACE_BG)


def build_levels():
    global food_level, animal_level, place_level
    food_level = Level(C.FOOD_BANNER, 100, 20, FOOD, unlocked_food)
    animal_level = Level(C.ANIMAL_BANNER, 270, 20, ANIMAL, unlocked_animal)
    place_level = Level(C.PLACE_BANNER, 440, 20, PLACE, unlocked_place)


# Load Category
FOOD = load_category("Food")
ANIMAL = load_category("Animal")
PLACE = load_category("Place")

#############################
""" Create a Title Screen """
#############################
# Create World
Title_screen = World()
Title_screen.Set_bg(C.TITLE_BG_IMG)
# Create Button
Title_play_btn = Button(410, 280, C.TITLE_PLAY_BTN, (160, 110),
                        TITLE_SCREEN_BTN_FONT, "Play", key=PY.K_RETURN)
Title_exit_btn = Button(440, 390, C.TITLE_EXIT_BTN, (100, 40),
                        TITLE_SCREEN_BTN_FONT, "Exit", key=PY.K_ESCAPE)

#############################
""" Create a Level Screen """
#############################
# Create World
Level_screen = World()
Level_screen.Set_bg(C.LEVEL_BG_IMG)
# Design
Level_screen.add_design("assets/Background/top_level.png", 5, -5, 1000, 80)
Level_screen.add_design("assets/Background/buttom_level.png", 5, 550, 1000, 80)
Level_screen.add_design(C.TITLE_EXIT_BTN, 430, 60, 120, 40)
Level_screen.add_design(C.TITLE_EXIT_BTN, 430, 230, 120, 40)
Level_screen.add_design(C.TITLE_EXIT_BTN, 430, 400, 120, 40)
# Text
Level_screen.text("Food", C.WHITE, 465, 65, C.Seagram_tfb, 22)
Level_screen.text("Animal", C.WHITE, 455, 235, C.Seagram_tfb, 22)
Level_screen.text("Place", C.WHITE, 460, 405, C.Seagram_tfb, 22)
# Create Level banner
build_levels()


#################################
""" Create a Game play Screen """
#################################
# Create World
Game_play_world = World()

run = True
while run:
    for event in PY.event.get():
        if event.type == PY.QUIT:
            run = False

        ###############################
        # """ Game state if Title """ #
        ###############################
        if game_state == "Title_screen":
            Title_screen.Draw(SCREEN)
            Title_play_btn.Draw(SCREEN)
            Title_exit_btn.Draw(SCREEN)

            if Title_play_btn.Event_handler():
                game_state = "Level_screen"
            if Title_exit_btn.Event_handler():
                run = False

            if event.type == PY.MOUSEBUTTONDOWN:
                pos = event.pos
                if Title_play_btn.rect.collidepoint(pos):
                    Level_menu_btn = Button(850, 40, C.MENU, (100, 50),
                                            FONT, "Menu", key=PY.K_ESCAPE)
                    game_state = "Level_screen"
                if Title_exit_btn.rect.collidepoint(pos):
                    run = False

        ###############################
        # """ Create a Level Screen """
        ###############################
        elif game_state == "Level_screen":
            Level_screen.Draw(SCREEN)

            food_level.draw(SCREEN)
            animal_level.draw(SCREEN)
            place_level.draw(SCREEN)

            Level_menu_btn.Draw(SCREEN)

            clicked_food_level = food_level.update(event)
            clicked_animal_level = animal_level.update(event)
            clicked_place_level = place_level.update(event)

            if Level_menu_btn.Event_handler():
                game_state = "Title_screen"

            if event.type == PY.MOUSEBUTTONDOWN:
                pos = event.pos

                if Level_menu_btn.rect.collidepoint(pos):
                    game_state = "Title_screen"

                if clicked_food_level:
                    game_level = clicked_food_level
                    game_category = "Food"

                    Game_enter_btn = Button(800, 95, C.FOOD_BTN, (150, 50),
                                            FONT, "Enter", key=PY.K_RETURN)
                    Game_delete = Button(800, 145, C.FOOD_BTN, (150, 50),
                                         FONT, "Delete", key=PY.K_BACKSPACE)
                    Game_shuffle = Button(800, 195, C.FOOD_BTN, (150, 50),
                                          FONT, "Shuffle", key=PY.K_SPACE)
                    Game_hint_btn = Button(800, 245, C.FOOD_BTN, (150, 50),
                                           FONT, "Hint", key=PY.K_1)
                    Game_next_btn = Button(800, 295, C.FOOD_BTN, (150, 50),
                                           FONT, "Next Level", key=PY.K_2)
                    Game_back_btn = Button(850, 10, C.FOOD_BTN, (100, 50),
                                           FONT, "Back", key=PY.K_ESCAPE)

                    CATEGORY = load_category(game_category)
                    gameplay = Game_play(CATEGORY, game_level)

                    Background_img(game_category, game_level)

                    if gameplay.Rand_Level_Words(player_ans):
                        gameplay.Shuffled()
                        gameplay.Update_ans(game_category)
                    game_state = "Gameplay"

                elif clicked_animal_level:
                    game_level = clicked_animal_level
                    game_category = "Animal"

                    Game_enter_btn = Button(800, 95, C.ANIMAL_BTN, (150, 50),
                                            FONT, "Enter", key=PY.K_RETURN)
                    Game_delete = Button(800, 145, C.ANIMAL_BTN, (150, 50),
                                         FONT, "Delete", key=PY.K_BACKSPACE)
                    Game_shuffle = Button(800, 195, C.ANIMAL_BTN, (150, 50),
                                          FONT, "Shuffle", key=PY.K_SPACE)
                    Game_hint_btn = Button(800, 245, C.ANIMAL_BTN, (150, 50),
                                           FONT, "Hint", key=PY.K_1)
                    Game_next_btn = Button(800, 295, C.ANIMAL_BTN, (150, 50),
                                           FONT, "Next Level", key=PY.K_2)
                    Game_back_btn = Button(850, 10, C.ANIMAL_BTN, (100, 50),
                                           FONT, "Back", key=PY.K_ESCAPE)

                    CATEGORY = load_category(game_category)
                    gameplay = Game_play(CATEGORY, game_level)

                    Background_img(game_category, game_level)

                    if gameplay.Rand_Level_Words(player_ans):
                        gameplay.Shuffled()
                        gameplay.Update_ans(game_category)
                    game_state = "Gameplay"

                elif clicked_place_level:
                    game_level = clicked_place_level
                    game_category = "Place"

                    Game_enter_btn = Button(800, 95, C.PLACE_BTN, (150, 50),
                                            FONT, "Enter", key=PY.K_RETURN)
                    Game_delete = Button(800, 145, C.PLACE_BTN, (150, 50),
                                         FONT, "Delete", key=PY.K_BACKSPACE)
                    Game_shuffle = Button(800, 195, C.PLACE_BTN, (150, 50),
                                          FONT, "Shuffle", key=PY.K_SPACE)
                    Game_hint_btn = Button(800, 245, C.PLACE_BTN, (150, 50),
                                           FONT, "Hint", key=PY.K_1)
                    Game_next_btn = Button(800, 295, C.PLACE_BTN, (150, 50),
                                           FONT, "Next Level", key=PY.K_2)
                    Game_back_btn = Button(850, 10, C.PLACE_BTN, (100, 50),
                                           FONT, "Back", key=PY.K_ESCAPE)

                    CATEGORY = load_category(game_category)
                    gameplay = Game_play(CATEGORY, game_level)

                    Background_img(game_category, game_level)

                    if gameplay.Rand_Level_Words(player_ans):
                        gameplay.Shuffled()
                        gameplay.Update_ans(game_category)
                    game_state = "Gameplay"

        ###############################
        # """ Create a Level Screen """
        ###############################
        elif game_state == "Gameplay":
            # Draw game design
            Game_play_world.Draw(SCREEN)
            gameplay.Draw(SCREEN)
            gameplay.draw_hint(SCREEN)

            # Handle inputs
            gameplay.Update_2(event)          # mouse click
            gameplay.Update_keyboard(event)   # keyboard press

            # Draw solved answers inside the board
            gameplay.draw_answers(SCREEN, player_ans)

            # draw btn
            Game_enter_btn.Draw(SCREEN)
            Game_delete.Draw(SCREEN)
            Game_shuffle.Draw(SCREEN)
            Game_hint_btn.Draw(SCREEN)
            Game_back_btn.Draw(SCREEN)

            # draw hint
            words_left = len(gameplay.level_words) - len(player_ans)
            words_surface = HINT_FONT.render(
                f"{words_left} Words left", True, C.WHITE)
            SCREEN.blit(words_surface, (810, 60))

            if words_left == 0:
                Game_next_btn.Draw(SCREEN)
                if Game_next_btn.Event_handler():
                    player_ans = []
                    Game_play_world.clear()
                    game_level += 1

                    # Unlock next level
                    if game_category == "Food" and game_level > unlocked_food:
                        unlocked_food = game_level
                    elif game_category == "Animal" and game_level > unlocked_animal:
                        unlocked_animal = game_level
                    elif game_category == "Place" and game_level > unlocked_place:
                        unlocked_place = game_level

                    build_levels()

                    Background_img(game_category, game_level)
                    gameplay.clear(CATEGORY, game_level)

            # Keyboard
            if Game_enter_btn.Event_handler():
                if "".join(gameplay.guest) == gameplay.Ans_word:
                    if gameplay.Ans_word != "":
                        player_ans.append(gameplay.Ans_word)
                    if gameplay.Rand_Level_Words(player_ans):  # pick a word
                        gameplay.Shuffled()
                        gameplay.Update_ans(game_category)
                else:
                    gameplay.reset_all_letters()

            if Game_delete.Event_handler():
                gameplay.delete_last_letter()

            if Game_shuffle.Event_handler():
                if gameplay.Rand_Level_Words(player_ans):  # pick a word
                    gameplay.Shuffled()
                    gameplay.Update_ans(game_category)

            if Game_hint_btn.Event_handler():
                if gameplay.hint_active:
                    gameplay.hint_active = False
                else:
                    gameplay.hint_active = True

            if Game_back_btn.Event_handler():
                player_ans = []
                Game_play_world.clear()
                build_levels()
                game_state = "Level_screen"

            # Mouse
            if event.type == PY.MOUSEBUTTONDOWN:
                pos = event.pos

                if words_left == 0:
                    Game_next_btn.Draw(SCREEN)
                    if Game_next_btn.rect.collidepoint(pos):
                        player_ans = []
                        Game_play_world.clear()
                        game_level += 1

                        # Unlock next level
                        if game_category == "Food" and game_level > unlocked_food:
                            unlocked_food = game_level
                        elif game_category == "Animal" and game_level > unlocked_animal:
                            unlocked_animal = game_level
                        elif game_category == "Place" and game_level > unlocked_place:
                            unlocked_place = game_level

                        build_levels()

                        Background_img(game_category, game_level)
                        gameplay.clear(CATEGORY, game_level)

                if Game_enter_btn.rect.collidepoint(pos):
                    if "".join(gameplay.guest) == gameplay.Ans_word:
                        if gameplay.Ans_word != "":
                            player_ans.append(gameplay.Ans_word)
                        if gameplay.Rand_Level_Words(player_ans):
                            gameplay.Shuffled()
                            gameplay.Update_ans(game_category)
                    else:
                        gameplay.reset_all_letters()

                if Game_delete.rect.collidepoint(pos):
                    gameplay.delete_last_letter()

                if Game_shuffle.rect.collidepoint(pos):
                    if gameplay.Rand_Level_Words(player_ans):  # pick a word
                        gameplay.Shuffled()
                        gameplay.Update_ans(game_category)

                if Game_hint_btn.rect.collidepoint(pos):
                    if gameplay.hint_active:
                        gameplay.hint_active = False
                    else:
                        gameplay.hint_active = True

                if Game_back_btn.rect.collidepoint(pos):
                    player_ans = []
                    Game_play_world.clear()
                    build_levels()
                    game_state = "Level_screen"

    PY.display.update()
PY.quit()
