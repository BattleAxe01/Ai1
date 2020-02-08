from random import randint

from Ai1.Dna import Dna


def rand_char():
    return chr(randint(32, 126))


class Generator:
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
