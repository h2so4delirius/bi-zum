from random import randrange
y=0
x=1


class robot:
    def __init__(self,arr_of_purpose,word_map, size,arr):
        self.way = []
        self.arr_of_purpose=arr_of_purpose
        if not arr_of_purpose==0:
                self.arr_of_purpose = []
                for _ in range(0, randrange(2,8)):
                    while True:
                        y_1 = randrange(size[y])
                        x_1 = randrange(size[x])
                        flag=False
                        for i in arr:
                            if i[0]==y_1 and i[1]==x_1:
                                flag=True
                        
                        if word_map[y_1][x_1] != '#' and not flag:
                            self.arr_of_purpose.append([y_1,x_1])
                            break
    def set_priority(self, priority):
        self.priority = priority
    def set_way(self, way):
        self.way = way
    def get_way(self):
        return self.way
