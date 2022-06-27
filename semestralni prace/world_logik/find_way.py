class find_way:
    def __init__(self):
        self.way = []
    def find_next_step(self,position,world):
        res = []
        if world[position[0]-1][position[1]] != '#':
            res.append([position[0]-1,position[1]])
        if world[position[0]+1][position[1]] != '#':
            res.append([position[0]+1,position[1]])
        if world[position[0]][position[1]-1] != '#':
            res.append([position[0],position[1]-1])
        if world[position[0]][position[1]+1] != '#':
            res.append([position[0],position[1]+1])


        if world[position[0]+1][position[1]+1] != '#':
            res.append([position[0]+1,position[1]+1])
        if world[position[0]+1][position[1]-1] != '#':
            res.append([position[0]+1,position[1]-1])
        if world[position[0]-1][position[1]+1] != '#':
            res.append([position[0]-1,position[1]+1])
        if world[position[0]-1][position[1]-1] != '#':
            res.append([position[0]-1,position[1]-1])
        return res




    def find_next_step_priority(self,arr_new_position,pos_array,pos,robots,x_y):
        flag = False
        dell = []
        for i in range(len(arr_new_position)-1,-1,-1):

            for j in range(0,pos):
                if len(robots[j].way)-1>pos_array and i<len(arr_new_position):
                    #print('         ',len(robots[j].way),pos_array,len(arr_new_position),i)
                    if robots[j].way[pos_array] == arr_new_position[i]:
                        #print(22)
                        dell.append(arr_new_position.pop(i))
                        flag=True
                        #break
        if flag:
            #arr_new_position.clear()
            arr_new_position.append(x_y)
            #print(arr_new_position,'=', x_y,'=',dell,pos_array,pos)
            #print(33)
        return arr_new_position





        
    #def Astart(self,start,end,world,arr_robots:list):
    #    queue = [[start[0],start[1]]]
    #    path = [[]]
    #    while queue:
    #        arr_new_position = self.find_next_step(queue[len(queue)-1],world)
            





    
    def ret_way(self,tree):
        res = []
        i = len(tree)-1
        #print(tree)
        while i:
            #print(tree[i][0])
            res.insert(0,tree[i][0])
            i = tree[i][1]
        return res




    def create_tree(self,start,end,world,arr_robots,pos,position_on_way):
        tree = [[start,None]]
        #tree = [[[x,y],prev]]
        #print('start -',start,' end -',end)
        for i in range(0,10000000):
            #print(1)
            arr_new_position = self.find_next_step(tree[i][0],world)
            arr_new_position = self.find_next_step_priority(arr_new_position,i+position_on_way-1,pos,arr_robots,tree[i][0])
            for j in arr_new_position:

                tree.append([j,i])
                if j==end:
                    return self.ret_way(tree)
                    
                #print(tree)
            
            
        


    def create_way_Astar(self,way, world,arr_robots,pos):
        all_way = []
        all_way.append(way[0])
        position_on_way=0
        for i in range(0,len(way)-1):
            k = self.create_tree(way[i],way[i+1],world,arr_robots,pos,position_on_way)
            #all_way.append(way[i])
            position_on_way+=len(all_way)
            if k:
                for j in k:
                    all_way.append(j)
            else:
                print('cant find')
                return []
            #print(1)
        print(way,'\n\n',all_way,'\nend\n')
        return all_way
            
