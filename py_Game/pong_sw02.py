# Importieren der Pygame-Bibliothek
import pygame, math
from pygame.locals import *

# initialisieren von pygame
pygame.init()

# genutzte Farbe
ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

FENSTERBREITE = 640
FENSTERHOEHE = 480

# Fenster öffnen
screen = pygame.display.set_mode((FENSTERBREITE, FENSTERHOEHE))

# Titel für Fensterkopf
windowSurface = pygame.display.set_caption("Unser erstes Pygame-Spiel")
spielaktiv = True

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()

# Definieren der Variablen/Konstanten
ballpos_x = 10
ballpos_y = 30

BALL_DURCHMESSER = 20

bewegung_x = 4
bewegung_y = 4

spielfigur_1_x = 20
spielfigur_1_y = 20
spielfigur_1_bewegung = 0

spielfigur_2_x = FENSTERBREITE - (2 * 20)
spielfigur_2_y = 20
spielfigur_2_bewegung = 0

schlaegerhoehe = 220

ballwechsel = 0

# Schleife Hauptprogramm
while spielaktiv:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            spielaktiv = False
            print("Spieler hat Quit-Button angeklickt")
        if event.type == pygame.KEYDOWN:
            print("Spieler hat Taste gedrückt")

            # Taste für Spieler 1
            if event.key == pygame.K_UP:
                print("Spieler hat Pfeiltaste runter gedrückt")
                spielfigur_1_bewegung = -6
            elif event.key == pygame.K_DOWN:
                print("Spieler hat Pfeiltaste runter gedrückt")
                spielfigur_1_bewegung = 6

            # Taste für Spieler 2
            elif event.key == pygame.K_w:
                print("Spieler 2 hat w für hoch gedrückt")
                spielfigur_2_bewegung = -6
            elif event.key == pygame.K_s:
                print("Spieler 2 hat s für runter gedrückt")
                spielfigur_2_bewegung = 6

        # zum Stoppen der Spielerbewegung
        if event.type == pygame.KEYUP:
            print("Spieler hat Taste losgelassen")

            # Tasten für Spieler 1
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                print("Spieler 1 stoppt bewegung")
                spielfigur_1_bewegung = 0

            # Tasten für Spieler 2
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                print("Spieler 1 stoppt bewegung")
                spielfigur_2_bewegung = 0

    # Spiellogik
    if spielfigur_1_bewegung != 0:
        spielfigur_1_y += spielfigur_1_bewegung

    if spielfigur_1_y < 0:
        spielfigur_1_y = 0

    if spielfigur_1_y > FENSTERHOEHE - schlaegerhoehe:
        spielfigur_1_y = FENSTERHOEHE - schlaegerhoehe

    if spielfigur_2_bewegung != 0:
        spielfigur_2_y += spielfigur_2_bewegung

    if spielfigur_2_y < 0:
        spielfigur_2_y = 0

    if spielfigur_2_y > FENSTERHOEHE - schlaegerhoehe:
        spielfigur_2_y = FENSTERHOEHE - schlaegerhoehe

    # Spielfeld löschen
    screen.fill(SCHWARZ)

    # Spielfeld/figuren zeichnen
    # -- Ball
    ball = pygame.draw.ellipse(screen, WEISS, [ballpos_x, ballpos_y, BALL_DURCHMESSER, BALL_DURCHMESSER])

    # -- Spielerfigur 1
    player1 = pygame.draw.rect(screen, WEISS, [spielfigur_1_x, spielfigur_1_y, 20, schlaegerhoehe])
    # -- Spielerfigur 2
    player2 = pygame.draw.rect(screen, WEISS, [spielfigur_2_x, spielfigur_2_y, 20, schlaegerhoehe])

    # bewegen unseres Balls/Kreises
    ballpos_x += bewegung_x
    ballpos_y += bewegung_y

    if ballpos_y > FENSTERHOEHE - BALL_DURCHMESSER or ballpos_y < 0:
        bewegung_y = bewegung_y * -1

    if ballpos_x > FENSTERBREITE - BALL_DURCHMESSER or ballpos_x < 0:
        bewegung_x = bewegung_x * -1

    # if ball.colliderect(player1):
    if player1.colliderect(ball):
        print("Zusammenstoß P1")
        bewegung_x = bewegung_x * -1
        ballpos_x = 40
        ballwechsel += 1
        schlaegerhoehe -= 5

    if player2.colliderect(ball):
        print("Zusammenstoß P2")
        bewegung_x = bewegung_x * -1
        ballpos_x = 570
        ballwechsel += 1
        schlaegerhoehe -= 5

    ausgabetext = "Ballwechsel: " + str(ballwechsel)
    font = pygame.font.SysFont(None, 70)
    text = font.render(ausgabetext, True, ROT)
    screen.blit(text, [100, 10])    

    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)

pygame.quit()