import pygame

pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.mixer.init()

hit_sound = pygame.mixer.Sound("sound/hit.mp3")
miss_sound = pygame.mixer.Sound("sound/miss.mp3")
sink_sound = pygame.mixer.Sound("sound/sink.mp3")

class Audio:
    @classmethod
    def play_hit(cls):
        hit_sound.play()

    @classmethod
    def play_miss(cls):
        miss_sound.play()

    @classmethod
    def play_sink(cls):
        sink_sound.play()
