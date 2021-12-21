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
p = player.Player((1, 4), 2)
clock = pygame.time.Clock()

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            sys.exit()

        p.events(event, maze)

    maze[p.pos[0]][p.pos[1]] = 2
    p.render_vision(screen, maze, screen_size)

    print(map.encode_maze(maze))
    print(p.pos, p.looking)

    clock.tick()
    pygame.display.update()
    