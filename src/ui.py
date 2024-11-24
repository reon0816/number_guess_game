import pygame
from settings import FONT, BLACK, GRAY

def draw_text(screen, text, x, y, font=FONT, color=BLACK):
    """テキストを描画"""
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def draw_buttons(screen, buttons):
    """ボタンを描画"""
    for button in buttons:
        pygame.draw.rect(screen, GRAY, button["rect"])
        draw_text(screen, button["text"], button["rect"].x + 10, button["rect"].y + 10)