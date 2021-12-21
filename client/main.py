import pygame, sys, player, map, conect

pygame.init()

#p_id = int(input("id: "))

screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)

with open("ip.txt", "r") as f:
    ip = f.read()
    
maze = """################
#--------------#
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
#--------------#
################"""
maze = map.load_maze(maze, (16, 16))
p = conect.start(ip)
enemies = []
clock = pygame.time.Clock()

maze[p.pos[0]][p.pos[1]] = 2

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            sys.exit()

        enemies, maze = p.events(event, maze, enemies)
    p.render_vision(screen, maze, screen_size)
    map.render_minimap(screen, maze, screen_size, 5)

    p.render_stats(screen, screen_size)

    clock.tick()
    pygame.display.update()
    
