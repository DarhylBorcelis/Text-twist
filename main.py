import pygame
import random

pygame.init()

width, height = 700, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Any Game")

font = pygame.font.Font("assets/Font/Hevilla.ttf", 38)
small_font = pygame.font.Font("assets/Font/Hevilla.ttf", 22)

background = (181, 101, 29)
white = (255, 255, 255)
rect_border_color = (0, 0, 0)
font_color = (0, 0, 0)

WORDS = {
    "level 1": {"SHAME": {"same", "seam", "sham", "ham", "ash", "she", "me"}},
    "level 2": {"STONE": {"tone", "one", "not", "son", "note", "set"}},
    "level 3": {"GAMES": {"game", "same", "gem", "gas", "ages"}},
    "level 4": {"TRAIN": {"rain", "rant", "tin", "ant", "art"}},
    "level 5": {"PLANE": {"plan", "pane", "pen", "nap", "ape"}},
    "level 6": {"MOUSE": {"some", "sue", "use", "mou", "sum"}},
    "level 7": {"CRATE": {"race", "care", "tear", "act", "cat"}},
    "level 8": {"WORLD": {"word", "lord", "row", "owl", "old"}},
    "level 9": {"HEART": {"earth", "heat", "rat", "ear", "hat"}},
    "level 10": {"LIGHT": {"hit", "lit", "git", "tig", "til"}}
}


game_state = "menu"
selected_level = None
main_word = ""
shuffled = ""
letters = []
solve = []
guests = []
player_ans = []


def level_box(levels):
    level_li = []
    start_x, start_y = 155, 100
    x_gap = 130
    y_gap = 80

    for i, num in enumerate(levels):
        x = start_x + (i % 3) * x_gap
        y = start_y + (i // 3) * y_gap
        rect = pygame.Rect(x, y, 120, 50)
        level_li.append([num, rect, True])
    return level_li


def shuffle_letter(word):
    letter = list(word)
    random.shuffle(letter)
    return "".join(letter)


def position(word):
    letters = []
    start_x, y = 180, 400
    gap = 60

    for i, char in enumerate(word):
        x = start_x + i * gap
        rect = pygame.Rect(x, y, 55, 50)
        letters.append([char, rect, True])
    return letters


def ans(solve):
    start_x, start_y = 50, 50
    gap_x, gap_y = 40, 40

    sorted_words = sorted(solve, key=lambda w: (len(w), w))

    for row, word in enumerate(sorted_words):
        y = start_y + row * gap_y
        for i, char in enumerate(word):
            x = start_x + i * gap_x
            rect = pygame.Rect(x, y, 35, 35)
            pygame.draw.rect(screen, (255, 255, 255), rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 2)

            if word in player_ans:
                txt = small_font.render(char, True, font_color)
                screen.blit(txt, (rect.x + 8, rect.y + 5))


def btn(x, y, name):
    enter = pygame.Rect(x, y, 80, 50)
    pygame.draw.rect(screen, (250, 220, 180), enter, border_radius=10)
    pygame.draw.rect(screen, rect_border_color, enter, 2, border_radius=10)
    txt = small_font.render(name, True, font_color)
    screen.blit(txt, (enter.x + 6, enter.y + 10))
    return enter


def lines(letters):
    start_x, y = 180, 385
    gap = 60

    for i, (char, rect, active) in enumerate(letters):
        x = start_x + i * gap
        pygame.draw.line(screen, (0, 0, 0), (x, y), (x + 55, y), 2)

    new_y = y - 50
    for i, char in enumerate(guests):
        x = start_x + i * gap
        new_rect = pygame.Rect(x, new_y, 55, 50)
        pygame.draw.rect(screen, (250, 220, 180), new_rect)
        pygame.draw.rect(screen, rect_border_color, new_rect, 2)
        txt = font.render(char, True, font_color)
        screen.blit(txt, (new_rect.x + 13, new_rect.y + 5))


def draw_game(letters, solve):
    for char, rect, active in letters:
        if active:
            pygame.draw.rect(screen, (250, 220, 180), rect)
            pygame.draw.rect(screen, rect_border_color, rect, 2)
            txt = font.render(char, True, font_color)
            screen.blit(txt, (rect.x+13, rect.y+5))
        else:
            pygame.draw.rect(screen, (100, 100, 100), rect)

    lines(letters)
    ans(solve)


def draw_menu(lvl):
    for num, rect, active in lvl:
        if active:
            pygame.draw.rect(screen, (250, 220, 180), rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 2)
            txt = font.render(num, True, (0, 0, 0))
            screen.blit(txt, (rect.x+9, rect.y+5))
        else:
            pygame.draw.rect(screen, (100, 100, 100), rect)


level_names = list(WORDS.keys())
lvl = level_box(level_names)

run = True
while run:
    screen.fill(background)

    if game_state == "menu":
        draw_menu(lvl)
    elif game_state == "play":
        draw_game(letters, solve)
        shuffle_btn = btn(x=500, y=400, name="Shuffle")
        enter_btn = btn(x=500, y=340, name="Enter")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if game_state == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                for level_data in lvl:
                    name, rect, active = level_data
                    if active and rect.collidepoint(pos):
                        selected_level = name
                        main_word = list(WORDS[selected_level].keys())[0]
                        shuffled = shuffle_letter(main_word)
                        letters = position(shuffled)
                        solve = list(WORDS[selected_level][main_word])
                        guests = []
                        player_ans = []
                        game_state = "play"

        elif game_state == "play":
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                for letter_data in letters:
                    char, rect, active = letter_data
                    if active and rect.collidepoint(pos):
                        letter_data[2] = False
                        guests.append(char)

                if enter_btn.collidepoint(pos):
                    now = "".join(guests).lower()
                    if now in solve and now not in player_ans:
                        player_ans.append(now)
                    guests = []
                    letters = position(shuffled)

                if shuffle_btn.collidepoint(pos):
                    shuffled = shuffle_letter(main_word)
                    letters = position(shuffled)
                    guests = []

    pygame.display.update()

pygame.quit()
