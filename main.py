import pygame, sys, player, map

pygame.init()

screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)

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
maze = map.load_maze(maze, (16, 16))
p = player.Player((1, 5), 1)
clock = pygame.time.Clock()

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    maze[p.pos[0]][p.pos[1]] = 2
    p.render_vision(screen, maze, screen_size)

    print(map.encode_maze(maze)+"\n")

    clock.tick()
    pygame.display.update()
    