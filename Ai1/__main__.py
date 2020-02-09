from p5 import *
import time

from Ai1.Generator import Generator

TEXT_SIZE = 16
HEIGHT = 1366
WIDTH = 768

flag = False
generator = None
st, ft = 0, 0


def setup():
    global generator
    size(HEIGHT, WIDTH)

    max_pop = 200
    mutation_rate = 0.2
    target = "uma moeda e uma moeda independente do lado que esteja virada"
    # target = "banana"

    generator = Generator(max_pop, mutation_rate, target)
    helvetica = create_font("/home/axe/Documents/GitHub/Ai1/helvetica.otf", TEXT_SIZE)
    text_font(helvetica)
    # generator.print_pop()


def draw():
    global flag, st, ft
    if mouse_is_pressed:
        flag = True
        st = time.time()
    if flag:

        background(255)
        global generator

        generator.calc_fitness()

        display()

        if generator.check():
            ft = time.time()
            print("FOI")
            print(ft - st)
            no_loop()
            return
        else:
            generator.next_gen()


def display():
    global generator
    med_fit = 0
    for d in generator.pop:
        med_fit += d.fitness
    med_fit /= len(generator.pop)

    fill(0)
    text("Generation: %d" % generator.gen_count, (10, 200))
    text("Fitness média: %.5f" % med_fit, (10, 200 + TEXT_SIZE))

    x = 200
    y = 10
    for d in generator.pop:
        text(d.s, (x, y))
        text("%.2f" % d.fitness, (x + 10 + text_width(d.s), y))
        y += TEXT_SIZE

        if y + TEXT_SIZE >= HEIGHT:
            y = 10
            x += text_width(generator.target) + 100


if __name__ == '__main__':
    run()
