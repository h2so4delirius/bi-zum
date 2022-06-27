import time
from random import*


class Osnovoy():
    def start(self):
        while True:
            self.start_end=[]
            self.mtx1=[]
            self.mtx2=[]
            print("nazev souboru")
            self.str = input()
            if not self.str:
                return 
            self.f = open(self.str, 'r')
            self.size()
            print("1.bfs\n2.dfs\n3.Random Search\n4.Greedy Search\n5.Dijkstrův algoritmus\n6.A*\n7.exit")
            self.f.close()
            self.hight=len(self.mtx1)
            self.weight=len(self.mtx1[0])
            #print(self.hight," ",self.weight)
            self.vyber=input()
            if int(self.vyber)==7:
                break
            if int(self.vyber)==1:
                self.bfs()
            if int(self.vyber)==2:
                self.dfs()
            if int(self.vyber)==5:
                self.Dijkstruv()
            if int(self.vyber)==6:
                self.A()
            if int(self.vyber)==4:
                self.GreedySearch()
            if int(self.vyber)==3:
                self.RandomSearch()



        



    def prnt(self):
        for i in range(0,len(self.mtx1)):
            for j in range(0,len(self.mtx1[i])):
                print(self.mtx1[i][j],end='')
                #print(f'\033[{i};{j}H', end='', flush=True)
            print()


    def size(self):
        while True:
            char = self.f.read(1)
            if char != 'X' and char != ' ' and char != '\n':
                break
            if char == 'X' or char == ' ':
                self.mtx2.append(char)
            if char == '\n':
               self.mtx1.append(self.mtx2)
               self.mtx2=[]
        for line in self.f:
            strok=""
            for i in line:
                if strok != "" and not '0' <= i <= '9':
                    self.start_end.append(int(strok))
                    strok=""
                if '0' <= i <= '9':
                    strok+=i
        #print(self.start_end)
            
    def bfs(self):
        if self.se():
            self.prnt()
            #print("res")
            return 

        start ,end = [self.start_end[1],self.start_end[0],[]], [self.start_end[3],self.start_end[2]]
        
        self.list = []
        self.list.append(start)
        p=0
        while self.list:
            if self.list[0][0] == end[0] and self.list[0][1] == end[1]:
                #print(self.list[0][2])
                for i in self.list[0][2]:
                    self.mtx1[i[0]][i[1]] = 'O'
                self.mtx1[self.list[0][0]][self.list[0][1]] = 'E'
                self.mtx1[start[0]][start[1]] = 'S'
                self.prnt()
                print("\n\nPath length-> ",len(self.list[0][2]))
                print("Nodes expanded-> ",p)
                return
            self.pohyb(self.list[0][0],self.list[0][1],self.list[0][2])
            self.list.pop(0) 
            p+=1
        return
        





    def dfs(self):
        if self.se():
            self.prnt()
            print("res")
            return 

        start ,end = [self.start_end[1],self.start_end[0],[]], [self.start_end[3],self.start_end[2]]
        
        self.list = []
        self.list.append(start)
        p=0
        while self.list:
            pop=len(self.list)-1
            #print(pop)
            if self.list[pop][0] == end[0] and self.list[pop][1] == end[1]:
                #print(self.list[pop][2])
                for i in self.list[pop][2]:
                    self.mtx1[i[0]][i[1]] = 'O'
                self.mtx1[self.list[pop][0]][self.list[pop][1]] = 'E'
                self.mtx1[start[0]][start[1]] = 'S'
                self.prnt()
                print("\n\nPath length-> ",len(self.list[pop][2]))
                print("Nodes expanded-> ",p)
                return
            self.pohyb(self.list[pop][0],self.list[pop][1],self.list[pop][2])
            self.list.pop(pop) 
            p+=1
        return

    def RandomSearch(self):
        if self.se():
            self.prnt()
            #print("res")
            return 

        start ,end = [self.start_end[1],self.start_end[0],[]], [self.start_end[3],self.start_end[2]]
        
        self.list = []
        self.list.append(start)
        p=0
        while self.list:
            pop=len(self.list)-1
            pop=randrange(len(self.list))
            #print(pop)
            if self.list[pop][0] == end[0] and self.list[pop][1] == end[1]:
                #print(self.list[pop][2])
                for i in self.list[pop][2]:
                    self.mtx1[i[0]][i[1]] = 'O'
                self.mtx1[self.list[pop][0]][self.list[pop][1]] = 'E'
                self.mtx1[start[0]][start[1]] = 'S'
                self.prnt()
                print("\n\nPath length-> ",len(self.list[pop][2]))
                print("Nodes expanded-> ",p)
                return
            self.pohyb(self.list[pop][0],self.list[pop][1],self.list[pop][2])
            self.list.pop(pop) 
            p+=1
        return

    def GreedySearch(self):
        if self.se():
            self.prnt()
            print("res")
            return

        start ,end = [self.start_end[1],self.start_end[0],[]], [self.start_end[3],self.start_end[2]]
        min=90000000
        self.list = []
        self.list.append(start)
        self.mtx1[start[0]][start[1]] = 'S'
        pop=0
        p=0
        while self.list:
            #self.prnt()
            
            for i in range(len(self.list)-1):
                if (self.vert_go(self.list[i][0],self.list[i][0],end[1],end[0])) < min:
                    min = self.vert_go(self.list[i][0],self.list[i][0],end[1],end[0])
                    p = i
            if self.list[p][0] == end[0] and self.list[p][1] == end[1]:
                #print(self.list[p][2])
                for i in self.list[p][2]:
                    self.mtx1[i[0]][i[1]] = 'O'
                self.mtx1[self.list[p][0]][self.list[p][1]] = 'E'
                self.mtx1[start[0]][start[1]] = 'S'
                self.prnt()
                print("\n\nPath length-> ",len(self.list[p][2]))
                print("Nodes expanded-> ",pop)
                return
            self.pohyb(self.list[p][0],self.list[p][1],self.list[p][2])
            pop+=1
            self.list.pop(p)
        return

    def Dijkstruv(self):
        if self.se():
            self.prnt()
            #print("res")
            return

        start ,end = [self.start_end[1],self.start_end[0],[]], [self.start_end[3],self.start_end[2]]
        min=90000000
        self.list = []
        self.list.append(start)
        self.mtx1[start[0]][start[1]] = 'S'
        pop=0
        p=0
        while self.list:
            #self.prnt()
            
            for i in range(len(self.list)-1):
                if (len(self.list[i])) < min:
                    min = (len(self.list[i]))
                    p = i
            if self.list[p][0] == end[0] and self.list[p][1] == end[1]:
                #print(self.list[p][2])
                for i in self.list[p][2]:
                    self.mtx1[i[0]][i[1]] = 'O'
                self.mtx1[self.list[p][0]][self.list[p][1]] = 'E'
                self.mtx1[start[0]][start[1]] = 'S'
                self.prnt()
                print("\n\nPath length-> ",len(self.list[p][2]))
                print("Nodes expanded-> ",pop)
                return
            self.pohyb(self.list[p][0],self.list[p][1],self.list[p][2])
            pop+=1
            self.list.pop(p)
        return

    def A(self):
        if self.se():
            self.prnt()
            #print("res")
            return

        start ,end = [self.start_end[1],self.start_end[0],[]], [self.start_end[3],self.start_end[2]]
        min=90000000
        self.list = []
        self.list.append(start)
        self.mtx1[start[0]][start[1]] = 'S'
        pop=0
        p=0
        while self.list:
            #self.prnt()
            
            for i in range(len(self.list)-1):
                if (len(self.list[i]) + self.vert_go(self.list[i][0],self.list[i][0],end[1],end[0])) < min:
                    min = (len(self.list[i]) + self.vert_go(self.list[i][0],self.list[i][0],end[1],end[0]))
                    p = i
            if self.list[p][0] == end[0] and self.list[p][1] == end[1]:
                #print(self.list[p][2])
                for i in self.list[p][2]:
                    self.mtx1[i[0]][i[1]] = 'O'
                self.mtx1[self.list[p][0]][self.list[p][1]] = 'E'
                self.mtx1[start[0]][start[1]] = 'S'
                self.prnt()
                print("\n\nPath length-> ",len(self.list[p][2]))
                print("Nodes expanded-> ",pop)
                return
            self.pohyb_astar(self.list[p][0],self.list[p][1],self.list[p][2],end)
            pop+=1
            self.list.pop(p)
        return

        

    def se(self):
        if self.start_end[0] == self.start_end[2] and self.start_end[1] == self.start_end[3]:
            self.mtx1[self.start_end[1]][self.start_end[0]] = '#'
            return True
        return False

    def pohyb_astar(self,y,x,cesta,end):
        #print(x," ",y)
        min=999999990
        q=[]
        if self.mtx1[y][x+1] == ' ' and self.weight - 1 >= x:
            if self.vert_go(x+1,y,end[1],end[0])<min:
                min=self.vert_go(x+1,y,end[1],end[0])
                q.append([y,x+1,cesta+[[y,x]]])
        if self.mtx1[y][x-1] == ' ' and x > 0:
            if self.vert_go(x-1,y,end[1],end[0])<min:
                min=self.vert_go(x-1,y,end[1],end[0])
                q.append([y,x-1,cesta+[[y,x]]])
        if self.mtx1[y+1][x] == ' ' and self.hight >= y:
            if self.vert_go(x,y+1,end[1],end[0])<min:
                min=self.vert_go(x,y+1,end[1],end[0])
                q.append([y+1,x,cesta+[[y,x]]])
        if self.mtx1[y-1][x] == ' ' and y > 0:
            if self.vert_go(x,y-1,end[1],end[0])<min:
                min=self.vert_go(x,y-1,end[1],end[0])
                q.append([y-1,x,cesta+[[y,x]]])
        if q:
            self.list.append(q[len(q)-1])
            self.mtx1[q[len(q)-1][0]][q[len(q)-1][1]] = '#'


    def pohyb(self,y,x,cesta):
        if self.mtx1[y][x+1] == ' ' and self.weight - 1 >= x:
            self.mtx1[y][x+1] = '#'
            self.list.append([y,x+1,cesta+[[y,x]]])
        if self.mtx1[y][x-1] == ' ' and x > 0:
            self.mtx1[y][x-1] = '#'
            self.list.append([y,x-1,cesta+[[y,x]]])
        if self.mtx1[y+1][x] == ' ' and self.hight >= y:
            self.mtx1[y+1][x] = '#'
            self.list.append([y+1,x,cesta+[[y,x]]])
        if self.mtx1[y-1][x] == ' ' and y > 0:
            self.mtx1[y-1][x] = '#'
            self.list.append([y-1,x,cesta+[[y,x]]])


    def vert_go(self,x1,y1,x2,y2):
        return abs(x1-x2)+abs(y1-y2)




        
        




if __name__ == "__main__":
    osn = Osnovoy()
    osn.start()
