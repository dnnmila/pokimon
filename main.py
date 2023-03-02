from button import Button
import pygame
import sys
import mainfun
import GloVar
import BTFun
import pygame_gui
GloVar.init()

pygame.init()

SCREEN = pygame.display.set_mode((1400, 900))
CLOCK = pygame.time.Clock()
MANAGER = pygame_gui.UIManager((1400, 900))
global user_text
user_text = ""

pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")
BG_BATTLE = pygame.image.load("assets/BackgroundBattle.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def printPokemon(pokemon):
    PLAY_TEXT = get_font(24).render(
        (pokemon + " selected"), True, "White")
    PLAY_RECT = PLAY_TEXT.get_rect(center=(740, 50))
    SCREEN.blit(PLAY_TEXT, PLAY_RECT)


def show_text(text_to_show):
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        SCREEN.fill("White")
        # new_text = pygame.font.SysFont("bahnschrift", 24).render(
        #     f"{text_to_show}", True, "white")

        # new_rect = new_text.get_rect(center=(700, 40))
        # SCREEN.blit(new_text, new_rect)
        # CLOCK.tick(60)
        pygame.display.update()


def selectPokemon(player):
    global user_text
    while True:
        SCREEN.blit(BG_BATTLE, (0, 0))

        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_TEXT = get_font(24).render(
            (player + " select Pokemon ."), True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(740, 50))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(1300, 50),
                           text_input="BACK", font=get_font(24), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        PLAY_NEXT = Button(image=None, pos=(1300, 800),
                           text_input="Scan", font=get_font(24), base_color="RED", hovering_color="white")

        PLAY_NEXT.changeColor(PLAY_MOUSE_POS)
        PLAY_NEXT.update(SCREEN)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if PLAY_NEXT.checkForInput(PLAY_MOUSE_POS):
                    if player == "P1":
                        pokedex = input("Player 1 Enter Pokedex ID")
                        BTFun.selectPokemon(player, pokedex)
                        pokemon_text = get_font(24).render(
                            f"{GloVar.P1}", True, "White")
                        pokemon_rect = pokemon_text.get_rect(center=(240, 450))
                        SCREEN.blit(pokemon_text, pokemon_rect)
                        pygame.display.update()
                        pygame.time.wait(5000)
                        return GloVar.Phase + 1

                    if player == "P2":
                        pokedex = input("Player 2 Enter Pokedex ID")
                        BTFun.selectPokemon(player, pokedex)
                        pokemon_text = get_font(24).render(
                            f"{GloVar.P2}", True, "White")
                        pokemon_rect = pokemon_text.get_rect(
                            center=(1040, 450))
                        SCREEN.blit(pokemon_text, pokemon_rect)
                        pygame.display.update()
                        pygame.time.wait(5000)
                        return GloVar.Phase + 1

        text_surface = get_font(24).render(
            user_text, True, "White")
        SCREEN.blit(text_surface, (100, 600))
        pygame.display.update()


def selectAttack(player):
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(BG_BATTLE, (0, 0))

        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_TEXT = get_font(24).render(
            (player + " select Attack ."), True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(740, 50))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(1300, 50),
                           text_input="BACK", font=get_font(24), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        PLAY_ATTACK1 = Button(image=None, pos=(200, 800),
                              text_input="ATTACK 1", font=get_font(24), base_color="YELLOW", hovering_color="WHITE")

        PLAY_ATTACK2 = Button(image=None, pos=(700, 800),
                              text_input="ATTACK 2", font=get_font(24), base_color="GREEN", hovering_color="WHITE")

        PLAY_ATTACKTM = Button(image=None, pos=(1200, 800),
                               text_input="ATTACK TM", font=get_font(24), base_color="BLUE", hovering_color="WHITE")

        PLAY_ATTACK1.changeColor(PLAY_MOUSE_POS)
        PLAY_ATTACK1.update(SCREEN)
        PLAY_ATTACK2.changeColor(PLAY_MOUSE_POS)
        PLAY_ATTACK2.update(SCREEN)
        PLAY_ATTACKTM.changeColor(PLAY_MOUSE_POS)
        PLAY_ATTACKTM.update(SCREEN)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if PLAY_ATTACK1 .checkForInput(PLAY_MOUSE_POS):

                    return GloVar.Phase + 1
                if PLAY_ATTACK2 .checkForInput(PLAY_MOUSE_POS):

                    return GloVar.Phase + 1
                if PLAY_ATTACKTM .checkForInput(PLAY_MOUSE_POS):

                    return GloVar.Phase + 1

        pygame.display.update()


def battle():
    GloVar.Phase = 0
    battleFinished = False
    phase = 0
    while battleFinished == False:

        if GloVar.Phase == 0:
            GloVar.Phase = selectPokemon("P1")

        elif GloVar.Phase == 1:
            print(GloVar.P1)
            GloVar.Phase = selectPokemon("P1")

        elif GloVar.Phase == 2:

            print(GloVar.P2)
            pygame.time.wait(5000)

            pass

            battleFinished = True


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render(
            "This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Pokimon", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(700, 100))
        MENU_TEXT_v = get_font(24).render("V1.0", True, "#b68f40")
        MENU_RECT_v = MENU_TEXT_v.get_rect(center=(700, 170))

        BATTLE_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(700, 300),
                               text_input="BATTLE", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(700, 450),
                                text_input="OPTIONS", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(700, 600),
                             text_input="QUIT", font=get_font(60), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        SCREEN.blit(MENU_TEXT_v, MENU_RECT_v)

        for button in [BATTLE_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BATTLE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    battle()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
