from math import *
from random import *

from Ai1.Dna import Dna


def rand_char():
    c = randint(97, 123)
    if c == 123:
        c = 32
    return chr(c)


def rand_elem(v):
    n = random()
    esq, dir, r = 0, len(v) - 1, len(v) - 1
    while esq <= dir:
        mid = (esq + dir) // 2
        if v[mid] >= n:
            r = mid
            dir = mid - 1
        else:
            esq = mid + 1
    return r


class Generator:
    gen_count = 0
    pop = []
    max_pop = 0
    mutation_rate = 0
    target = ""

    def __init__(self, max_pop, mutation_rate, target):
        self.max_pop = max_pop
        self.mutation_rate = mutation_rate
        self.target = target
        self.generate_random_pop()

    def generate_random_pop(self):
        self.gen_count = 0
        for i in range(self.max_pop):
            s = ""
            for j in range(len(self.target)):
                s += rand_char()

            self.pop.append(Dna(s))

    def print_pop(self):
        print(self.pop)

    def check(self):
        for d in self.pop:
            if d.s == self.target:
                return True

    def calc_fitness(self):
        for d in self.pop:
            d.fitness = 0

            for i in range(len(self.target)):
                if d.s[i] == self.target[i]:
                    d.fitness += 1
            d.fitness /= len(self.target)

    def next_gen(self):
        self.gen_count += 1
        pre = []

        soma = 0
        for d in self.pop:
            pre.append(d.fitness)
            soma += d.fitness

        # print(soma)
        # print(pre)

        for i in range(len(pre)):
            pre[i] /= soma

        for i in range(1, len(pre)):
            pre[i] += pre[i - 1]

        # print(pre)

        new_pop = []
        for i in range(self.max_pop):
            p1 = self.pop[rand_elem(pre)]
            p2 = self.pop[rand_elem(pre)]

            s = ""
            for j in range(len(self.target)):
                if random() < self.mutation_rate:
                    s += rand_char()
                else:
                    r = randint(0, 1)
                    s += p1.s[j] if r == 0 else p2.s[j]
            new_pop.append(Dna(s))

        self.pop = new_pop
