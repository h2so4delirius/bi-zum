from random import randrange
import copy

def create_fild(n:int):
    arr = []
    for _ in range(0, n):
        arr_g = []
        for _ in range(0, n):
            arr_g.append('*')
        arr.append(arr_g)
    return arr



def show_fild(array:list):
    print('+', end = '')
    for i in range(0, len(array)):
        print('-', end = '')
    print('+')
    for i in array:
        print('|', end = '')
        for j in i:
            print(j, end = '')
        print('|')
    print('+', end = '')
    for i in range(0, len(array)):
        print('-', end = '')
    print('+')

def create_fild_with(array, population, res_all, first):
    
    for i in range(0,len(population)):
        arr_n = copy.deepcopy(array)
        for j in range(0,len(population)*2-1, 2):
            arr_n[population[i][j]][population[i][j+1]] = 'D'
        show_fild(arr_n)
    print(res_all, '<-', first)



def Initial_populationv(n:int):
    arr = []
    for _ in range(0, n):
        arr_hrom = []
        for _ in range(0, n*2):
            arr_hrom.append(randrange(n))
        arr.append(arr_hrom)
    return arr
    

def Fitness_function(population:list):
    result_fit = []
    for i in population:
        fit = 0
        for j in range(0, len(i), 2):
            for p in range(0, len(i), 2):
                if i[j] == i[p]:
                    fit +=1
            fit-=1
        for j in range(1, len(i), 2):
            for p in range(1, len(i), 2):
                if i[j] ==i[p]:
                    fit +=1
            fit-=1
        result_fit.append(fit)
    return result_fit        

def takeSecond(elem):
    return elem[1]

def Selection(population:list, fit_population:list):
    new_arr = []
    for i in range(0, len(population)):
        new_arr.append([population[i], fit_population[i]])
    new_arr.sort(key = takeSecond)
    return new_arr

def create_gruop(n:int, couunt_group:int):
    arr = []
    for i in range(0, couunt_group):
        if n==1:
            break
        arr.append([n])
        n=n//2
        arr[i].append(n)
    return arr
        
def roll(best_fit:list, arr_groupe:list):
    x = randrange(100)
    if x<51:
        #print(randrange(arr_groupe[2][1]-1,arr_groupe[2][0]))
        return best_fit[randrange(arr_groupe[2][1]-1,arr_groupe[2][0])]
    elif x>50 and x<85:
        #print(randrange(arr_groupe[1][1]-1,arr_groupe[1][0]))
        return best_fit[randrange(arr_groupe[1][1]-1,arr_groupe[1][0])]
    elif x>84:
        #print(randrange(arr_groupe[0][1]-1,arr_groupe[0][0]))
        return best_fit[randrange(arr_groupe[0][1]-1,arr_groupe[0][0])]
    return best_fit[0]

def Crossover(best_fit:list, arr_groupe:list):
    new_population = []
    for _ in range(0, len(best_fit)):
        a=[]
        b=[]
        new_gen = []
        while True:
            a = roll(best_fit, arr_groupe)
            b = roll(best_fit, arr_groupe)
            if a!=b:
                break
        for i in range(0,len(best_fit)*2):
            r = randrange(2)
            if r==0:
                new_gen.append(a[0][i])
            else:
                new_gen.append(b[0][i])
        new_population.append(new_gen)
    return new_population



    

def Mutation(new_population):
    for i in range(0, len(new_population)):
        for j in range(0, len(new_population)*2):
            if randrange(100) < 8:
                new_population[i][j] = randrange(len(new_population))
    return new_population




def start():
    n = 0
    while True:
        n = int(input('zadejte cisli hran :'))
        x = int(input('pocet iteraci :'))
        arr_groupe = create_gruop(n, 4)
        #print(arr_groupe)
        #print(n)
        if n < 4:
            break
        array = create_fild(n)
        res_all = []
        #show_fild(array)
        population = Initial_populationv(n)
        fit_population_f = Fitness_function(population)
        for i in range(0, x):
            fit_population = Fitness_function(population)
            res_all = fit_population
            best_fit = Selection(population, fit_population)
            new_population = Crossover(best_fit, arr_groupe)
            population = new_population
            #print(population)
        create_fild_with(array, population, res_all,fit_population_f)
        #print(new_population)
        #print(population)
        #print(fit_population)
        #print(best_fit)



start()
















