import pygame, sys
import PONGSETTINGS as settings
import PADDLE as pad
import BALL as b
from pygame.locals import *


def startMenu(window):
    menuClock = pygame.time.Clock()
    menuballs = pygame.sprite.Group()
    for i in range(30):
        menuballs.add(b.Ball("MENU"))

    while True:
        window.fill((0, 0, 0))
        menuballs.draw(window)
        menuballs.update()
        surfaces_to_print, surfaces_rects = prepareMenuOptions()
        option_choosed = ""

        # change collor when cursos collision
        for key in surfaces_rects:
            if surfaces_rects[key].collidepoint(pygame.mouse.get_pos()):
                new_c = (80, 80, 80)
                if key == "onePlayerOpt":
                    surfaces_to_print, surfaces_rects = prepareMenuOptions(onep_c=new_c)
                if key == "twoPlayerOpt":
                    surfaces_to_print, surfaces_rects = prepareMenuOptions(twop_c=new_c)
                if key == "instructionsOpt":
                    surfaces_to_print, surfaces_rects = prepareMenuOptions(
                        instr_c=new_c
                    )
                if key == "soundOpt":
                    surfaces_to_print, surfaces_rects = prepareMenuOptions(
                        sound_c=new_c
                    )
                if key == "musicOpt":
                    surfaces_to_print, surfaces_rects = prepareMenuOptions(
                        music_c=new_c
                    )
                option_choosed = key

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                if event.button == 1 and option_choosed in surfaces_rects.keys():
                    return option_choosed

        window.blits(surfaces_to_print)
        pygame.display.update()

        menuClock.tick(60)


# This func could be created as class of options but im too lazy to recerate it
def prepareMenuOptions(
    onep_c=(255, 255, 255),
    twop_c=(255, 255, 255),
    instr_c=(255, 255, 255),
    sound_c=(255, 255, 255),
    music_c=(255, 255, 255),
):
    pygame.font.init()

    title_c = (255, 255, 255)
    window_center = settings.WIDTH // 2

    # title
    titleFont = pygame.font.SysFont("courier", 100, True)
    title = titleFont.render("PONG", True, title_c)
    title_rect = title.get_rect()
    title_rect.center = (window_center, 100)

    # options
    optionFont = pygame.font.SysFont("courier", 40)

    # 1p
    onePlayerOpt = optionFont.render("1-P Mode", True, (0, 0, 0))
    temp_sur = pygame.Surface((settings.WIDTH - 110, 45))
    temp_sur.fill(onep_c)
    temp_sur.blit(
        onePlayerOpt,
        ((temp_sur.get_rect().width - onePlayerOpt.get_rect().width) // 2, 0),
    )
    onePlayerOpt = temp_sur
    onePlayerOpt_rect = onePlayerOpt.get_rect()
    onePlayerOpt_rect.top = title_rect.bottom + 30
    onePlayerOpt_rect.centerx = window_center

    # 2p
    twoPlayerOpt = optionFont.render("2-P Mode", True, (0, 0, 0))
    temp_sur = pygame.Surface((settings.WIDTH - 110, 45))
    temp_sur.fill(twop_c)
    temp_sur.blit(
        twoPlayerOpt,
        ((temp_sur.get_rect().width - twoPlayerOpt.get_rect().width) // 2, 0),
    )
    twoPlayerOpt = temp_sur
    twoPlayerOpt_rect = twoPlayerOpt.get_rect()
    twoPlayerOpt_rect.top = onePlayerOpt_rect.bottom + 10
    twoPlayerOpt_rect.centerx = window_center

    # Instructions
    instructionsOpt = optionFont.render("Instructions", True, (0, 0, 0))
    temp_sur = pygame.Surface((settings.WIDTH - 110, 45))
    temp_sur.fill(instr_c)
    temp_sur.blit(
        instructionsOpt,
        ((temp_sur.get_rect().width - instructionsOpt.get_rect().width) // 2, 0),
    )
    instructionsOpt = temp_sur
    instructionsOpt_rect = instructionsOpt.get_rect()
    instructionsOpt_rect.top = twoPlayerOpt_rect.bottom + 10
    instructionsOpt_rect.centerx = window_center

    # Sound
    soundOpt = optionFont.render("Sounds:" + str(settings.sounds), True, (0, 0, 0))
    temp_sur = pygame.Surface((settings.WIDTH - 110, 45))
    temp_sur.fill(sound_c)
    temp_sur.blit(
        soundOpt, ((temp_sur.get_rect().width - soundOpt.get_rect().width) // 2, 0)
    )
    soundOpt = temp_sur
    soundOpt_rect = soundOpt.get_rect()
    soundOpt_rect.top = instructionsOpt_rect.bottom + 10
    soundOpt_rect.centerx = window_center

    # Music
    musicOpt = optionFont.render("Music:" + str(settings.music), True, (0, 0, 0))
    temp_sur = pygame.Surface((settings.WIDTH - 110, 45))
    temp_sur.fill(music_c)
    temp_sur.blit(
        musicOpt, ((temp_sur.get_rect().width - musicOpt.get_rect().width) // 2, 0)
    )
    musicOpt = temp_sur
    musicOpt_rect = musicOpt.get_rect()
    musicOpt_rect.top = soundOpt_rect.bottom + 10
    musicOpt_rect.centerx = window_center

    # list of surfaces to print
    surfaces = [
        (title, title_rect.topleft),
        (onePlayerOpt, onePlayerOpt_rect),
        (twoPlayerOpt, twoPlayerOpt_rect),
        (instructionsOpt, instructionsOpt_rect),
        (soundOpt, soundOpt_rect),
        (musicOpt, musicOpt_rect),
    ]

    # dict of rect
    rects = {
        "title": title_rect,
        "onePlayerOpt": onePlayerOpt_rect,
        "twoPlayerOpt": twoPlayerOpt_rect,
        "instructionsOpt": instructionsOpt_rect,
        "soundOpt": soundOpt_rect,
        "musicOpt": musicOpt_rect,
    }

    return surfaces, rects


def onePlayerMode(window):
    onePlayerClock = pygame.time.Clock()
    player = pad.Paddle()

    # setup fonts
    score_font = pygame.font.SysFont("courier", 20, True)
    gameover_font = pygame.font.SysFont("courier", 30, True)
    text_font = pygame.font.SysFont("courier", 20)

    ball = b.Ball()
    game_start = False
    while player.lifes > 0:
        window.fill((0, 0, 0))
        new_round = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == K_a:
                    player.left = True
                if event.key == K_RIGHT or event.key == K_d:
                    player.right = True
            if event.type == KEYUP:
                if event.key == K_q:
                    return
                if event.key == K_RETURN:
                    game_start = True
                if event.key == K_LEFT or event.key == K_a:
                    player.left = False
                if event.key == K_RIGHT or event.key == K_d:
                    player.right = False

        if not ball.ball_on_board:
            player.lifes -= 1
            ball = b.Ball()
            player.reset_position()
            if player.lifes != 0:
                new_round = True

        # draw elements
        ball.draw(window)
        player.draw(window)
        lifes = score_font.render("LIFES:" + "♥" * player.lifes, True, (0, 255, 255))
        score = score_font.render("SCORE:" + str(player.score), True, (0, 255, 255))
        score_rect = score.get_rect()
        window.blit(score, (settings.WIDTH // 2 - score_rect.width // 2, 40))
        window.blit(lifes, (settings.WIDTH // 2 - 50, 20))

        # update elements if true
        if game_start == True:
            player.update()
            player.ball_hitted(ball)
            ball.update()

        else:
            text = text_font.render("Press 'ENTER' to start", True, (255, 255, 255))
            text_rect = text.get_rect()
            window.blit(
                text,
                (
                    settings.WIDTH // 2 - text_rect.width // 2,
                    settings.HEIGHT // 2 - text_rect.height // 2 - 40,
                ),
            )

        pygame.display.update()

        if new_round:
            pygame.time.wait(500)
        onePlayerClock.tick(60)

    game_ended = True
    settings.play_sound("gameover")

    while game_ended:
        window.fill((0, 0, 0))

        score = score_font.render(
            "Your score: " + str(player.score), True, (0, 255, 255)
        )
        score_rect = score.get_rect()
        gameover = gameover_font.render("GAMEOVER", True, (0, 255, 255))
        gameover_rect = gameover.get_rect()
        ending = text_font.render("Press any key to go to menu", True, (255, 255, 255))
        ending_rect = ending.get_rect()
        window.blit(
            gameover,
            (
                settings.WIDTH // 2 - gameover_rect.width // 2,
                settings.HEIGHT // 2 - gameover_rect.height // 2 - 60,
            ),
        )
        window.blit(
            score,
            (
                settings.WIDTH // 2 - score_rect.width // 2,
                settings.HEIGHT // 2 - score_rect.height // 2 - 35,
            ),
        )

        window.blit(
            ending,
            (
                settings.WIDTH // 2 - ending_rect.width // 2,
                settings.HEIGHT // 2 - ending_rect.height // 2,
            ),
        )

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                game_ended = False

        pygame.display.update()
        onePlayerClock.tick(60)


def twoPlayerMode(window):
    twoPlayerClock = pygame.time.Clock()
    p1 = pad.Paddle()
    p2 = pad.Paddle("P2")

    ball = b.Ball("2P")

    text_font = pygame.font.SysFont("courier", 20)
    score_font = pygame.font.SysFont("courier", 20, True)
    scored_font = pygame.font.SysFont("courier", 30, True)

    game_start = False

    while p1.lifes > 0 and p2.lifes > 0:
        window.fill((0, 0, 0))
        new_round = False

        if not ball.ball_on_board:
            who_scored = ball.who_scored()
            if who_scored == "P1":
                p2.lifes -= 1
            if who_scored == "P2":
                p1.lifes -= 1

            scored = scored_font.render(who_scored + " SCORED!", True, (0, 255, 255))
            scored_rect = scored.get_rect()
            window.blit(
                scored,
                (
                    settings.WIDTH // 2 - scored_rect.width // 2,
                    settings.HEIGHT // 2 - 40,
                ),
            )

            ball = b.Ball("2P")
            p1.reset_position()
            p2.reset_position()
            new_round = True

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                # p1
                if event.key == K_LEFT:
                    p1.left = True
                if event.key == K_RIGHT:
                    p1.right = True
                # p2
                if event.key == K_a:
                    p2.left = True
                if event.key == K_d:
                    p2.right = True
            if event.type == KEYUP:
                if event.key == K_q:
                    return
                if event.key == K_RETURN:
                    game_start = True
                # p1
                if event.key == K_LEFT:
                    p1.left = False
                if event.key == K_RIGHT:
                    p1.right = False
                # p2
                if event.key == K_a:
                    p2.left = False
                if event.key == K_d:
                    p2.right = False

        # draw elements
        p1_score = "P1:" + "♥" * p1.lifes
        p2_score = "P2:" + "♥" * p2.lifes
        score_p1 = score_font.render(p1_score, True, (0, 255, 255))
        score_p2 = score_font.render(p2_score, True, (0, 255, 255))
        window.blit(
            score_p1,
            (
                settings.WIDTH // 5,
                settings.HEIGHT // 2 - score_p1.get_rect().height // 2,
            ),
        )
        window.blit(
            score_p2,
            (
                (settings.WIDTH // 5) * 3,
                settings.HEIGHT // 2 - score_p2.get_rect().height // 2,
            ),
        )
        p1.draw(window)
        p2.draw(window)
        ball.draw(window)

        # update elements if true
        if game_start == True:
            p1.update()
            p2.update()
            p1.ball_hitted(ball)
            p2.ball_hitted(ball)
            ball.update()

        else:
            text = text_font.render("Press 'ENTER' to start", True, (255, 255, 255))
            text_rect = text.get_rect()
            window.blit(
                text,
                (
                    settings.WIDTH // 2 - text_rect.width // 2,
                    settings.HEIGHT // 2 - text_rect.height // 2 - 40,
                ),
            )

        pygame.display.update()
        if new_round:
            pygame.time.wait(500)
        twoPlayerClock.tick(60)

    game_ended = True
    settings.play_sound("gameover")

    while game_ended:
        window.fill((0, 0, 0))

        if p1.lifes > p2.lifes:
            winner = "P1"
        else:
            winner = "P2"
        winner = scored_font.render(winner + " WIN!", True, (0, 255, 255))
        ending = text_font.render("Press any key to go to menu", True, (255, 255, 255))
        ending_rect = ending.get_rect()
        winner_rect = winner.get_rect()
        window.blit(
            ending,
            (
                settings.WIDTH // 2 - ending_rect.width // 2,
                settings.HEIGHT // 2 - ending_rect.height // 2,
            ),
        )
        window.blit(
            winner,
            (
                settings.WIDTH // 2 - winner_rect.width // 2,
                settings.HEIGHT // 2 - ending_rect.height // 2 - 60,
            ),
        )

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                game_ended = False

        pygame.display.update()
        twoPlayerClock.tick(60)


def instructions(window):
    instrClock = pygame.time.Clock()

    instruction_font = pygame.font.SysFont("courier", 15, True)
    instruction = [
        "               INSTRUCTIONS",
        "",
        "When you hit ball when paddle goes same",
        "way as ball right -> right/ left -> left",
        "ball speeds up, other way ball slow down.",
        "When you hit ball while not moving, speed",
        "stays the same",
        "",
        "   1P MODE",
        "← or a - go left",
        "→ or d - go right",
        "   2P MMODE",
        "Player 1 -> ← and →",
        "Player 2 -> a and d",
        "   All modes",
        "Press 'q' to go to menu anytime",
        "",
        "",
        "Press q to go back",
    ]

    window.fill((0, 0, 0))
    for i in range(len(instruction)):
        instruction_text = instruction_font.render(
            instruction[i], True, (255, 255, 255)
        )
        window.blit(instruction_text, (10, 25 * i))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_q:
                    return
        instrClock.tick(60)


if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    pygame.display.set_caption("Pong")
    while True:
        game_mode = startMenu(window)
        if game_mode == "onePlayerOpt":
            onePlayerMode(window)
        if game_mode == "twoPlayerOpt":
            twoPlayerMode(window)
        if game_mode == "instructionsOpt":
            instructions(window)
        if game_mode == "soundOpt":
            if settings.sounds == "on":
                settings.sounds = "off"
            else:
                settings.sounds = "on"
        if game_mode == "musicOpt":
            if settings.music == "on":
                settings.music = "off"
                pygame.mixer.music.stop()
            else:
                settings.music = "on"
                pygame.mixer.music.play()
