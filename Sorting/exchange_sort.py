from visualize import visualize


# O(n^2), Polynomial Time
def exchange_sort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                yield a, [i], [j], list(range(0, i))


visualize(exchange_sort, 30)
