import pygame

maze = """################
#-----#--#-----#
#--#--#--#--#--#
#-----#--#-----#
#####------#####
#------##------#
#-#####--#####-#
#-#####--#####-#
#------##------#
#####------#####
#-----#--#-----#
#--#--#--#--#--#
#-----#--#-----#
################"""

def load_maze(maze:str, size:tuple):
    #Loads a maze from a string.

    res_maze = [[] for i in range(size[0])]

    for i, line in enumerate(maze.split("\n")):
        for char in line:
            if char == "-":
                res_maze[i].append(0)
            elif char == "#":
                res_maze[i].append(1)

    return res_maze

def encode_maze(maze:list):
    #Encodes a maze into a string.

    res = ""

    for line in maze:
        for char in line:
            if char == 0:
                res += "-"
            elif char == 1:
                res += "#"
            elif char == 2:
                res += "X"

        res += "\n"

    return res

if __name__ == "__main__":
    print(maze)
    print("")
    print(encode_maze(load_maze(maze, (16, 16))))


def render_minimap(screen:pygame.display, maze:list, screen_size:tuple, size:int): 
    for y, line in enumerate(maze):
        for x, tile in enumerate(line):
            if tile == 1:
                pygame.draw.rect(screen, (255, 255, 255), (screen_size[0] - len(maze)*size + x*size, screen_size[1] - len(maze)*size + y*size, 5, 5))
            elif tile == 2:
                pygame.draw.rect(screen, (255, 0, 0), (screen_size[0] - len(maze)*size + x*size, screen_size[1] - len(maze)*size + y*size, 5, 5))
