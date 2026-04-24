import pygame
import os

class MusicPlayer:
    def __init__(self, folder):
        self.folder = folder
        self.tracks = [f for f in os.listdir(folder) if f.endswith(".wav")]
        self.index = 0
        pygame.mixer.init()

    def play(self):
        if self.tracks:
            pygame.mixer.music.load(os.path.join(self.folder, self.tracks[self.index]))
            pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def next(self):
        self.index = (self.index + 1) % len(self.tracks)
        self.play()

    def prev(self):
        self.index = (self.index - 1) % len(self.tracks)
        self.play()

    def current_track(self):
        if self.tracks:
            return self.tracks[self.index]
        return "No tracks"