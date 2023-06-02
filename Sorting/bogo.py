import random
from matplotlib import pyplot


def bogo(a):
    is_sorted = False
    while not is_sorted:
        i = random.randint(0, len(a) - 1)
        j = random.randint(0, len(a) - 1)
        a[i], a[j] = a[j], a[i]

        yield a

        is_sorted = True
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                is_sorted = False
                break


def visualize(sorting_algo, n):
    array = random.sample(range(1, n+1), n)
    sorting_process = sorting_algo(array)

    for i in sorting_process:
        pyplot.bar(x=range(1, len(array) + 1), height=i)
        pyplot.axis("off")
        pyplot.pause(0.1)
        pyplot.clf()
    pyplot.show()


visualize(bogo, 4)



