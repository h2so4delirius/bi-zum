from random import randrange
from world_logik.Robot import *
from world_logik.find_way import *
from colorama import *
import operator
import os



class world:
    def __init__(self, y, x, count_robots=5):
        self.x=x
        self.y=y

    def create_map(self):
        self.world_map=[]
        for i in range(0,self.y):
            map_x=[]
            for j in range(0,self.x):
                if i==0 or i==self.y-1 or j==0 or j==self.x-1:
                    map_x.append('#')
                elif randrange(5)==0:
                    map_x.append('#')
                else:
                    map_x.append(' ')
            self.world_map.append(map_x)
    def show_map(self):
        print(' ',end=' ')
        for i in range(0,len(self.world_map[0])):
            print(i,end=' ')
        print()
        p=0
        for i in self.world_map:
            print(p,end=' ')
            p+=1
            for j in i:
                print(j,end=' ')
            print()




    def create_robots(self, n):
        self.arr_robots = []
        arr = []
        for i in range(0,n):

            r = robot(None,self.world_map,[self.y,self.x],arr)
            r.set_priority(i)
            arr.append(r.arr_of_purpose[0])
            #print(r.arr_of_purpose)
            self.arr_robots.append(r)



    def create_way(self):
        self.arr_robots.sort(key=lambda e:e.priority)
        f = find_way()
        #print()
        j=0
        for i in self.arr_robots:
            #print(i.priority)
            i.set_way(f.create_way_Astar(i.arr_of_purpose,self.world_map,self.arr_robots,j))
            j+=1
        print('ok')
        for i in self.arr_robots:
            print(i.way)
        flag_f = True
        while flag_f:
            #print('g')
            count = 0
            for i in range(0,10000):
                flag= False
                arrr = []
                for j in self.arr_robots:
                    if len(j.way)>i:
                        flag = True
                        
                        for pop in arrr:
                            if j.way[i]==pop:
                                #print('   ||||',i)
                                #j.way.insert(i,j.way[i-1])
                                j.way = j.way[:i] + [j.way[i-1]] + j.way[i:]
                                count+=1
                        arrr.append(j.way[i])
                if not flag:
                    break
            if count==0:
                break
                            
                    

            
    


    def show_all(self):
        input()
        os.system('cls||clear')
        
        for p in range(0,1000000):
            flag_main=False
            os.system('sleep 0.5')
            os.system('clear')
            for i in range(0,len(self.world_map)):
                for j in range(0,len(self.world_map)):
                    flag=False
                    for k in self.arr_robots:
                        if len(k.get_way())>p:
                            if k.get_way()[p]==[i,j]:
                                print(Fore.YELLOW+'N',end='')
                                flag=True
                                flag_main=True
                                #break
                    if not flag:        
                        print(Fore.BLUE+self.world_map[i][j],end='')
                print()
            if not flag_main:
                break


        

        


    
