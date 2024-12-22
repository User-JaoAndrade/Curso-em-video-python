"""
Abra um arquivo mp3 e reproduza-o
"""

import pygame

pygame.init()
pygame.mixer.music.load("BuryTheLight.mp3")
pygame.mixer.music.play()
pygame.event.wait()