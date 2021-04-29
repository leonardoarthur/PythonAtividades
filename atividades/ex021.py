import pygame
# colocando uma música dentro do programa WOW
pygame.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()):pass