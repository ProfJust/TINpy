#!/usr/bin/env python3
"""
Farbiger ASCII-Tannenbaum mit Glitzer (Konsole).
- ANSI-Farben, zufälliger Glitzer
- optional animiert (mehrere Frames)
"""

import os
import random
import sys
import time


# ---------- ANSI Farben ----------
RESET = "\033[0m"
BOLD = "\033[1m"

FG_RED = "\033[31m"
FG_GREEN = "\033[32m"
FG_YELLOW = "\033[33m"
FG_BLUE = "\033[34m"
FG_MAGENTA = "\033[35m"
FG_CYAN = "\033[36m"
FG_WHITE = "\033[37m"

FG_BRIGHT_WHITE = "\033[97m"
FG_BRIGHT_YELLOW = "\033[93m"
FG_BRIGHT_CYAN = "\033[96m"
FG_BRIGHT_MAGENTA = "\033[95m"

# Cursor / Screen control
CLEAR = "\033[2J"
HOME = "\033[H"


def supports_ansi() -> bool:
    """Best-effort ANSI support check (keine Garantie)."""
    if sys.platform != "win32":
        return True
    # Windows: viele Terminals unterstützen ANSI; VSCode, Windows Terminal etc.
    return "WT_SESSION" in os.environ or "TERM" in os.environ


def colored(text: str, color: str) -> str:
    return f"{color}{text}{RESET}"


def build_tree_lines(height: int, width: int, sparkle_prob: float) -> list[str]:
    """
    Erzeugt Zeilen des Tannenbaums.
    - height: Höhe der Krone
    - width: Basisbreite (ungerade)
    - sparkle_prob: Wahrscheinlichkeit für Glitzer pro 'Nadel'-Zeichen
    """
    if width % 2 == 0:
        width += 1

    lines: list[str] = []

    # Stern
    star = colored("★", FG_BRIGHT_YELLOW + BOLD) if supports_ansi() else "*"
    lines.append(" " * (width // 2) + star)

    # Krone
    for i in range(height):
        # aktuelle Breite (ungerade)
        w = 1 + 2 * i
        if w > width:
            w = width

        pad = (width - w) // 2
        row_chars = []

        for _ in range(w):
            # Grundzeichen (Nadel)
            ch = "▲"  # sieht oft schöner aus als "*"
            # Glitzer?
            if random.random() < sparkle_prob:
                sparkle_char = random.choice(["✦", "✧", "•", "◦", "✺"])
                sparkle_color = random.choice(
                    [FG_BRIGHT_WHITE, FG_BRIGHT_CYAN, FG_BRIGHT_MAGENTA, FG_BRIGHT_YELLOW]
                )
                if supports_ansi():
                    row_chars.append(colored(sparkle_char, sparkle_color + BOLD))
                else:
                    row_chars.append(random.choice(["*", ".", "+"]))
            else:
                if supports_ansi():
                    # leichte Farbvariation für "tiefe"
                    green = random.choice([FG_GREEN, "\033[92m"])  # normal/bright green
                    row_chars.append(colored(ch, green))
                else:
                    row_chars.append("^")

        lines.append(" " * pad + "".join(row_chars) + " " * pad)

    # Stamm
    trunk_w = max(3, width // 7)
    if trunk_w % 2 == 0:
        trunk_w += 1
    trunk_h = max(2, height // 5)
    trunk_pad = (width - trunk_w) // 2

    trunk_block = "█"
    for _ in range(trunk_h):
        if supports_ansi():
            # "Holz" in gelb/braun (annähernd)
            wood = FG_YELLOW
            lines.append(" " * trunk_pad + colored(trunk_block * trunk_w, wood) + " " * trunk_pad)
        else:
            lines.append(" " * trunk_pad + ("|" * trunk_w) + " " * trunk_pad)

    # Boden / Gruß
    if supports_ansi():
        lines.append(colored("Frohe Weihnachten!", FG_RED + BOLD))
    else:
        lines.append("Frohe Weihnachten!")

    return lines


def render_tree(height: int = 14, width: int = 31, sparkle_prob: float = 0.12,
                frames: int = 30, fps: int = 8) -> None:
    """
    Rendert optional animiert (Glitzer blinkt durch neue Frames).
    frames=1 => statisch.
    """
    delay = 1.0 / max(1, fps)

    for frame in range(frames):
        # Bildschirm "sauber" machen für Animation
        if frames > 1 and supports_ansi():
            sys.stdout.write(CLEAR + HOME)
        elif frames > 1:
            os.system("cls" if os.name == "nt" else "clear")

        lines = build_tree_lines(height=height, width=width, sparkle_prob=sparkle_prob)
        print("\n".join(lines))

        if frames > 1:
            time.sleep(delay)


if __name__ == "__main__":
    # Parameter nach Geschmack anpassen:
    # - height: Baumhöhe
    # - width: Basisbreite (ungerade)
    # - sparkle_prob: Glitzer-Dichte
    # - frames: 1 = statisch, >1 = animiert
    render_tree(height=32, width=65, sparkle_prob=0.14, frames=200, fps=10)
