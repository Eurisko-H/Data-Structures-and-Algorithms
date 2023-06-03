from matplotlib import pyplot
import random


def visualize(sorting_algo, n):
    array = random.sample(range(1, n + 1), n)
    sorting_process = sorting_algo(array)

    for i, slow, fast, finish in sorting_process:
        pyplot.clf()
        bars = pyplot.bar(x=range(1, len(array) + 1), height=i)
        for h in slow:
            bars[h].set_color("red")
        for h in fast:
            bars[h].set_color("orange")
        for h in finish:
            bars[h].set_color("green")
        pyplot.axis("off")
        pyplot.pause(0.1)
    pyplot.show()
