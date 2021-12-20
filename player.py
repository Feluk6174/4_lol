import pygame

class Player():
    def __init__(self, pos: tuple, looking: int):
        self.pos = [pos[0], pos[1]]
        #1: front, 2: right, 3: back, 4: left
        self.looking = looking

    def render_vision(self, screen:pygame.display, maze:list, screen_size:tuple):
        #Renders the vision of the player
        #The vision contains the 3 squares in fron of the player

        if self.looking == 0:
            if maze[self.pos[0]-1][self.pos[1]-1] == 1:
                pygame.draw.rect(screen, (255, 0, 0), (0, 0, int(screen_size[0]/4), screen_size[1]))
            if maze[self.pos[0]][self.pos[1]-1] == 1:
                pygame.draw.rect(screen, (255, 0, 0), (int(screen_size[0]/4), 0, int(screen_size[0]/2), screen_size[1]))
            if maze[self.pos[0]+1][self.pos[1]-11] == 1:
                pygame.draw.rect(screen, (255, 0, 0), (3*int(screen_size[0]/4), 0, int(screen_size[0]/4), screen_size[1]))

        elif self.looking == 1:
            if maze[self.pos[0]+1][self.pos[1]-1] == 1:
                pygame.draw.rect(screen, (255, 0, 0), (0, 0, int(screen_size[0]/4), screen_size[1]))
            if maze[self.pos[0]+1][self.pos[1]] == 1:
                pygame.draw.rect(screen, (255, 0, 0), (int(screen_size[0]/4), 0, int(screen_size[0]/2), screen_size[1]))
            if maze[self.pos[0]+1][self.pos[1]+1] == 1:
                pygame.draw.rect(screen, (255, 0, 0), (3*int(screen_size[0]/4), 0, int(screen_size[0]/4), screen_size[1]))