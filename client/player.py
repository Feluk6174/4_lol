import pygame

class Player():
    def __init__(self, pos: tuple, looking: int):
        self.pos = [pos[0], pos[1]]
        #0: front, 1: right, 2: back, 3: left
        self.looking = looking

    def draw_left(self, screen:pygame.display, screen_size:tuple):
        points = ((0, 0), (int(screen_size[0]/4), 0), (0, screen_size[1]-2), (int(screen_size[0]/4), screen_size[1]-2))
        
        for point_0 in points:
            for points_1 in points:
                pygame.draw.line(screen, (255, 255, 255), point_0, points_1)
    
    def draw_center(self, screen:pygame.display, screen_size:tuple):
        points = ((int(screen_size[0]/4), 0), (3*int(screen_size[0]/4), 0), (int(screen_size[0]/4), screen_size[1]-2), (3*int(screen_size[0]/4), screen_size[1]-2))

        for point_0 in points:
            for points_1 in points:
                pygame.draw.line(screen, (255, 255, 255), point_0, points_1)

    def draw_right(self, screen:pygame.display, screen_size:tuple):
        points = ((3*int(screen_size[0]/4), 0), (screen_size[0]-2, 0), (3*int(screen_size[0]/4), screen_size[1]-2), (screen_size[0]-2, screen_size[1]-2))

        for point_0 in points:
            for points_1 in points:
                pygame.draw.line(screen, (255, 255, 255), point_0, points_1)

    def render_vision(self, screen:pygame.display, maze:list, screen_size:tuple):
        #Renders the vision of the player
        #The vision contains the 3 squares in fron of the player

        if self.looking == 0:
            if maze[self.pos[0]-1][self.pos[1]+1] == 1:
                self.draw_left(screen, screen_size)
            if maze[self.pos[0]-1][self.pos[1]] == 1:
                self.draw_center(screen, screen_size)
            if maze[self.pos[0]-1][self.pos[1]-1] == 1:
                self.draw_right(screen, screen_size)
    
        elif self.looking == 1:
            if maze[self.pos[0]-1][self.pos[1]+1] == 1:
                self.draw_left(screen, screen_size)
            if maze[self.pos[0]][self.pos[1]+1] == 1:
                self.draw_center(screen, screen_size)
            if maze[self.pos[0]+1][self.pos[1]+1] == 1:
                self.draw_right(screen, screen_size)

        elif self.looking == 2:
            if maze[self.pos[0]+1][self.pos[1]+1] == 1:
                self.draw_left(screen, screen_size)
            if maze[self.pos[0]+1][self.pos[1]] == 1:
                self.draw_center(screen, screen_size)
            if maze[self.pos[0]+1][self.pos[1]-1] == 1:
                self.draw_right(screen, screen_size)
    
        elif self.looking == 3:
            if maze[self.pos[0]-1][self.pos[1]-1] == 1:
                self.draw_right(screen, screen_size)
            if maze[self.pos[0]][self.pos[1]-1] == 1:
                self.draw_center(screen, screen_size)
            if maze[self.pos[0]+1][self.pos[1]-1] == 1:
                self.draw_left(screen, screen_size)

    def events(self, event:pygame.event, maze:list):
        print(event)
        if event.type == pygame.KEYUP:
            print("t")
            if event.key == pygame.K_e:
                self.looking = self.looking + 1 if self.looking < 3 else 0
            elif event.key == pygame.K_q:
                self.looking = self.looking - 1 if self.looking > 0 else 3
            elif event.key == pygame.K_w:
                if self.looking == 0 or self.looking == 3:
                    mult = -1
                else:
                    mult = 1

                if self.looking == 2 or self.looking == 0:
                    if maze[self.pos[0]+mult][self.pos[1]] == 0:
                        self.pos[0] += mult
                else:
                    if maze[self.pos[0]][self.pos[1]+mult] == 0:
                        self.pos[1] += mult

                

if __name__ == "__name__":
    import main