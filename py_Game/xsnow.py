import pygame
import random
import math
import sys

# Bildschirmgröße
WIDTH, HEIGHT = 1200, 700
SNOWFLAKE_COUNT = 300


class Snowflake:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(-HEIGHT, 0)
        self.speed_y = random.uniform(1.0, 3.5)
        self.speed_x = random.uniform(-0.5, 0.5)
        self.size = random.randint(1, 3)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Wenn unten raus -> oben neu erscheinen
        if self.y > HEIGHT:
            self.reset()
            self.y = random.uniform(-50, -10)

        # Seitlicher Wrap
        if self.x < 0:
            self.x = WIDTH
        elif self.x > WIDTH:
            self.x = 0

    def draw(self, surface):
        pygame.draw.circle(
            surface,
            (240, 240, 255),
            (int(self.x), int(self.y)),
            self.size
        )


class Sleigh:
    def __init__(self):
        self.width = 220
        self.height = 80
        self.y = HEIGHT * 0.35
        self.x = -self.width - 100  # startet links außerhalb
        self.speed = 3.0

    def update(self):
        # leichte sinusförmige Bewegung (Wellenflug)
        t = pygame.time.get_ticks() / 1000.0
        self.y = HEIGHT * 0.35 + math.sin(t * 0.8) * 30

        self.x += self.speed
        if self.x > WIDTH + self.width:
            self.x = -self.width - 100  # wieder links hinaus

    def draw(self, surface):
        # Farben
        color_sleigh = (180, 0, 0)
        color_runner = (120, 60, 20)
        color_reindeer = (160, 120, 80)
        color_harness = (230, 230, 0)

        # Schlittenkörper
        body_rect = pygame.Rect(0, 0, self.width * 0.45, self.height * 0.4)
        body_rect.midleft = (self.x + self.width * 0.25,
                             self.y)
        pygame.draw.rect(surface, color_sleigh, body_rect, border_radius=8)

        # Rückenlehne
        back_rect = pygame.Rect(0, 0, self.width * 0.18, self.height * 0.5)
        back_rect.midleft = (body_rect.left - self.width * 0.05,
                             body_rect.centery)
        pygame.draw.rect(surface, color_sleigh, back_rect, border_radius=8)

        # Kufen
        runner_y = body_rect.bottom + 10
        pygame.draw.line(
            surface, color_runner,
            (body_rect.left, runner_y),
            (body_rect.right, runner_y),
            6
        )
        pygame.draw.arc(
            surface, color_runner,
            (body_rect.right - 40, runner_y - 20, 40, 40),
            math.pi / 2, 2 * math.pi, 4
        )

        # Drei Rentiere vor dem Schlitten
        base_y = body_rect.centery
        spacing = self.width * 0.3
        start_x = body_rect.right + self.width * 0.15

        for i in range(3):
            rx = start_x + i * spacing
            ry = base_y + math.sin((pygame.time.get_ticks() / 400.0) + i) * 15
            self._draw_reindeer(surface, rx, ry, color_reindeer, color_harness)

        # Zügel (Linien vom Schlitten zum ersten Rentier)
        first_rx = start_x
        first_ry = base_y
        pygame.draw.line(
            surface, color_harness,
            (body_rect.right, body_rect.centery - 10),
            (first_rx - 20, first_ry - 5),
            2
        )

    def _draw_reindeer(self, surface, x, y, color_body, color_harness):
        # Körper
        body_rect = pygame.Rect(0, 0, 60, 25)
        body_rect.center = (x, y)
        pygame.draw.ellipse(surface, color_body, body_rect)

        # Kopf
        head_rect = pygame.Rect(0, 0, 28, 20)
        head_rect.midleft = (body_rect.right, body_rect.centery - 8)
        pygame.draw.ellipse(surface, color_body, head_rect)

        # Hals
        pygame.draw.line(
            surface, color_body,
            (body_rect.right - 5, body_rect.centery - 5),
            (head_rect.left + 5, head_rect.centery),
            4
        )

        # Beine
        leg_y = body_rect.bottom
        for offset in (-15, -5, 5, 15):
            pygame.draw.line(
                surface, color_body,
                (body_rect.centerx + offset, leg_y),
                (body_rect.centerx + offset, leg_y + 18),
                3
            )

        # Geweih (simple Linien)
        horn_base = (head_rect.right - 2, head_rect.top + 3)
        pygame.draw.line(surface, color_body, horn_base,
                         (horn_base[0] + 10, horn_base[1] - 12), 3)
        pygame.draw.line(surface, color_body,
                         (horn_base[0] + 5, horn_base[1] - 5),
                         (horn_base[0] + 15, horn_base[1] - 15), 2)

        # Geschirr
        pygame.draw.line(
            surface, color_harness,
            (body_rect.left, body_rect.centery - 5),
            (head_rect.centerx, head_rect.centery),
            2
        )


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Rentierschlitten im Schnee (Pygame)")
    clock = pygame.time.Clock()

    # Hintergrundfarbe (dunkler Nachthimmel)
    background_color = (10, 10, 40)

    # Mond
    moon_pos = (WIDTH - 120, 120)
    moon_radius = 50

    # Schneeflocken erzeugen
    snowflakes = [Snowflake() for _ in range(SNOWFLAKE_COUNT)]

    sleigh = Sleigh()

    running = True
    while running:
        # Ereignisse behandeln
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Logik
        for flake in snowflakes:
            flake.update()
        sleigh.update()

        # Zeichnen
        screen.fill(background_color)

        # Mond
        pygame.draw.circle(screen, (250, 250, 210), moon_pos, moon_radius)

        # Schneeflocken
        for flake in snowflakes:
            flake.draw(screen)

        # Schlitten + Rentiere
        sleigh.draw(screen)

        pygame.display.flip()
        clock.tick(60)  # 60 FPS

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
