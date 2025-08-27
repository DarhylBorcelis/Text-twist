import pygame
import random

pygame.init()

width, height = 700, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Any Game")

font = pygame.font.SysFont("arial", 38)
small_font = pygame.font.SysFont("arial", 22)

background = (181, 101, 29)
white = (255, 255, 255)
rect_border_color = (0, 0, 0)
font_color = (0, 0, 0)

WORDS = {
    "SHAME": {"same", "seam", "sham", "ham", "ash", "she", "me"},
    "STONE": {"tone", "one", "not", "son", "note", "set"},
    "GAMES": {"game", "same", "gem", "gas", "ages"},
    "TRAIN": {"rain", "rant", "tin", "ant", "art"},
    "PLANE": {"plan", "pane", "pen", "nap", "ape"},
    "MOUSE": {"some", "sue", "use", "mou", "sum"},
    "CRATE": {"race", "care", "tear", "act", "cat"},
    "WORLD": {"word", "lord", "row", "owl", "old"},
    "HEART": {"earth", "heat", "rat", "ear", "hat"},
    "LIGHT": {"hit", "lit", "git", "tig", "til"}
}
guests = []

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


def ans(ans):
    start_x, start_y = 50, 50
    gap_x = 40
    gap_y = 40

    for row, word in enumerate(ans):
        y = start_y + row * gap_y
        for i, char in enumerate(word):
            x = start_x + i * gap_x
            rect = pygame.Rect(x, y, 35, 35)
            pygame.draw.rect(screen, (255, 255, 255), rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 2)


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
        
def btn_shuffle():
    x, y = 500, 400
    shuffle = pygame.Rect(x, y, 80, 50)
    pygame.draw.rect(screen, (250, 220, 180), shuffle)
    pygame.draw.rect(screen, rect_border_color, shuffle, 2)
    txt = small_font.render("Shuffle", True, font_color)
    screen.blit(txt, (shuffle.x + 6, shuffle.y + 10))
    return shuffle


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




main_word = random.choice(list(WORDS.keys()))
shuffled = shuffle_letter(main_word)
letters = position(shuffled)
solve = list(WORDS[main_word])
shuffle_btn = btn_shuffle()

run = True
while run:
    screen.fill(background)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            
            for letter_data in letters:
                char, rect, active = letter_data
                if active and rect.collidepoint(pos):
                    letter_data[2] = False
                    guests.append(char)
                    
            if shuffle_btn.collidepoint(pos):
                shuffled = shuffle_letter(main_word)
                letters = position(shuffled)
                guests = []

    draw_game(letters,solve)
    btn_shuffle()

    pygame.display.update()

pygame.quit()
