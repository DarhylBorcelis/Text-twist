import pygame
import random

pygame.init()

width, height = 700, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Any Game")

font = pygame.font.SysFont("arial", 38)
small_font = pygame.font.SysFont("arial", 22)

background = (181, 101, 29)

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


def shuffle_letter(word):
    letter = list(word)
    random.shuffle(letter)
    return "".join(letter)


def position(word):
    letters = []
    start_x, y = 180, 350
    gap = 60

    for i, char in enumerate(word):
        x = start_x + i * gap
        rect = pygame.Rect(x, y, 55, 50)
        letters.append([char, rect, True])
    return letters


def draw_game(letters):
    for char, rect, active in letters:
        pygame.draw.rect(screen, (250, 220, 180), rect)
        pygame.draw.rect(screen, (0, 0, 0), rect, 2)
        txt = font.render(char, True, (0, 0, 0))
        screen.blit(txt, (rect.x+13, rect.y+5))


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


main_word = random.choice(list(WORDS.keys()))
shuffled = shuffle_letter(main_word)
letters = position(shuffled)
solve = list(WORDS[main_word])

run = True
while run:
    screen.fill(background)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    ans(solve)
    draw_game(letters)

    pygame.display.update()

pygame.quit()
