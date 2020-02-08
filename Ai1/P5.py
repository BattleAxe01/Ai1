from p5 import *

from Ai1.Generator import Generator

generator = None
font = None


def setup():
    global generator, font
    size(1366, 768)

    max_pop = 10
    mutation_rate = 0.1
    target = "Uma moeda é uma moeda independente cuso o qual esteja virada"

    generator = Generator(max_pop, mutation_rate, target)

    font = create_font("Georgia", 16)
    generator.print_pop()


def draw():
    background(255)

    global generator
    generator.calc_fitness()

    display()


def display():
    global generator, font
    med_fit = 0
    for d in generator.pop:
        med_fit += d.fitness
    med_fit / len(generator.pop)

    fill(0)
    # text_font(font, 16)
    text(str(med_fit), (10, 200))


run()
