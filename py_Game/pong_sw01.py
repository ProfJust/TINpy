# https://www.python-lernen.de/pygame-animation.htm
# Importieren der Pygame-Bibliothek
import pygame, math

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
pygame.display.set_caption("Unser erstes Pygame-Spiel")

# solange die Variable True ist, soll das Spiel laufen
spielaktiv = True

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()

# Definieren der Variablen/Konstanten
ballpos_x = 10
ballpos_y = 30

BALL_DURCHMESSER = 20

bewegung_x = 4
bewegung_y = 4

# Schleife Hauptprogramm
while spielaktiv:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False

    # Spiellogik hier integrieren

    # Spielfeld löschen
    screen.fill(SCHWARZ)

    # Spielfeld/figuren zeichnen
    pygame.draw.ellipse(screen, WEISS, [ballpos_x, ballpos_y, BALL_DURCHMESSER, BALL_DURCHMESSER])

    # bewegen unseres Kreises
    ballpos_x += bewegung_x
    ballpos_y += bewegung_y

    if ballpos_y > FENSTERHOEHE - BALL_DURCHMESSER or ballpos_y < 0:
        bewegung_y = bewegung_y * -1

    if ballpos_x > FENSTERBREITE - BALL_DURCHMESSER or ballpos_x < 0:
        bewegung_x = bewegung_x * -1

    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)

pygame.quit()