import pygame, sys, player, map

pygame.init()

p_id = int(input("id: "))

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
p = player.Player((1, 4), 2, p_id)
enemyes = {"2": player.Player((15, 15), 2, 2)}
clock = pygame.time.Clock()

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            sys.exit()

        vals = p.events(event, maze)
    try:
        for val in vals:
            enemyes[str(val[0])].pos[0] = val[0][0]
            enemyes[str(val[0])].pos[1] = val[0][1]
            print(enemyes.pos)
    except TypeError:
        pass

    p.render_vision(screen, maze, screen_size)
    map.render_minimap(screen, maze, screen_size, 5)
    #print(map.encode_maze(maze))
    #print(p.pos, p.looking)

    clock.tick()
    pygame.display.update()
    