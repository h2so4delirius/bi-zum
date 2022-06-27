
from world_logik.world import *




if __name__ == "__main__":
    while True:
        inp = int(input('1-start 2-exit: '))
        if inp==2:
            break
        if inp==1:
            World = world(10,10)
            file = input('create world write enter or read from file (write name): ')
            if file == '':
                World.create_map()
                World.show_map()
                World.create_robots(6)
                World.create_way()
                World.show_all()
                
            
