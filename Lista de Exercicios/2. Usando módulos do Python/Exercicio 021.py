# Faça um programa em pyhton que abra e reproduza o audio de um arquivo mp3

import pygame
pygame.init()
pygame.mixer.music.load('ex021_relax.mp3')
pygame.mixer.music.play()
pygame.event.wait()



