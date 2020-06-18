import random
import string
import copy

# f = open("ga.csv", "a+")

ELITE = 9
POP = (ELITE+1)*ELITE
PRINTABLE = string.ascii_letters + string.digits + ', .-;:_!"#%&/()=?@${[]}'

def genetic():
    pop = init(l)
    best, best_score, all_score = optimal(pop)
    cnt = 0
    while best_score != l:
        pop = select(all_score, pop)
        pop = crossover(pop)
        pop = mutate(pop)
        best, best_score, all_score = optimal(pop)
        # print("Generation: {} String: {} Fitness: {}".format(cnt, best, l-best_score))
        cnt += 1
    # f.write("{}\n".format(cnt))
    return best

def init(l):
    pop = []
    for _ in range(POP):
        # pop.append(''.join(random.choice(string.printable) for j in range(l)))
        pop.append(''.join(random.choice(PRINTABLE) for j in range(l)))
    return pop

def select(all_score, pop):
    new_pop = []
    for _ in range(ELITE):
        tmp = pop[all_score.index(max(all_score))]
        all_score.remove(max(all_score))
        new_pop.append(tmp)
        pop.remove(tmp)
    return new_pop

def optimal(pop):
    all_score = [fitness(i) for i in pop]
    best_score = max(all_score)
    best = pop[all_score.index(best_score)]
    return best, best_score, all_score

def crossover(pop):
    new_pop = []
    for i in range(ELITE):
        for j in range(i, ELITE):
            p1 = pop[i]
            p2 = pop[j]
            tmp = ''
            for k in range(l):
                if random.random() < 0.5:
                    tmp += p1[k]
                else:
                    tmp += p2[k]
            new_pop.append(tmp)
    return new_pop

def mutate(pop):
    mutate_pop = copy.deepcopy(pop)
    for i in mutate_pop:
        k = random.randint(0, l-1)
        tmp = i[0:k] + random.choice(string.printable) + i[k+1:l]
        pop.append(tmp)
    return pop

def fitness(single_pop):
    # print(single_pop)
    cnt = 0
    for i in range(l):
        # print(len(single_pop))
        if(single_pop[i] == code[i]):
            cnt += 1
    return cnt

def edit_distance():
    pass

def main():
    global l
    global code
    code = "I love GeeksforGeeks"
    # code = input("Input your string: \n")
    l = len(code)
    ans = genetic()

if __name__ == "__main__":
    main()