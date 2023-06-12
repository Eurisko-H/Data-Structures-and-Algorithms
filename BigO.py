"""
1. O(1), Constant Time (the lowest order)
2. O(log n), Logarithmic Time
3. O(n), Linear Time
4. O(n log n), N-Log-N Time
5. O(n^2), Polynomial Time
6. O(2^n), Exponential Time
7. O(n!), Factorial Time (the highest order)
"""

"""
O(1), Constant Time
Finding out “Is the bookshelf empty?” is a constant time operation. It
doesn't matter how many books are on the shelf; one glance tells us
whether or not the bookshelf is empty. The number of books can vary,
but the runtime remains constant, because as soon as we see one book
on the shelf, we can stop looking. The n value is irrelevant to the speed
of the task, which is why there is no n in O(1). You might also see constant
time written as O(c).
"""

"""
O(log n), Logarithmic
Logarithms are the inverse of exponentiation: the exponent 24, or 2 × 2 × 2 × 2,
equals 16, whereas the logarithm log2(16) (pronounced “log base 2 of 16”)
equals 4. In programming, we often assume base 2 to be the logarithm base,
which is why we write O(log n) instead of O(log2 n).
Searching for a book on an alphabetized bookshelf is a logarithmic
time operation. To find one book, you can check the book in the middle of
the shelf. If that is the book you’re searching for, you’re done. Otherwise,
you can determine whether the book you’re searching for comes before or
after this middle book. By doing so, you’ve effectively reduced the range
of books you need to search in half. You can repeat this process again,
checking the middle book in the half that you expect to find it. We call this
the binary search algorithm, and there’s an example of it in “Big O Analysis
Examples” later in this chapter.
The number of times you can split a set of n books in half is log2 n.
On a shelf of 16 books, it will take at most four steps to find the right one.
Because each step reduces the number of books you need to search by one
half, a bookshelf with double the number of books takes just one more step
to search. If there were 4.2 billion books on the alphabetized bookshelf, it
would still only take 32 steps to find a particular book.
Log n algorithms usually involve a divide and conquer step, which selects
half of the n input to work on and then another half from that half, and so
on. Log n operations scale nicely: the workload n can double in size, but the
runtime increases by only one step.
"""

"""
O(n), Linear Time
Reading all the books on a bookshelf is a linear time operation. If the
books are roughly the same length and you double the number of books
on the shelf, it will take roughly double the amount of time to read all the
books. The runtime increases in proportion to the number of books n.
"""

"""
O(n log n), N-Log-N Time
Sorting a set of books into alphabetical order is an n-log-n time operation.
This order is the runtime of O(n) and O(log n) multiplied together. You
can think of a O(n log n) task as a O(log n) task that must be performed n
times. Here’s a casual description of why.
Start with a stack of books to alphabetize and an empty bookshelf.
Follow the steps for a binary search algorithm, as detailed in “O(log n),
Logarithmic” to find where a single book belongs on the
shelf. This is an O(log n) operation. With n books to alphabetize, and each
book taking log n steps to alphabetize, it takes n × log n, or n log n, steps
to alphabetize the entire set of books. Given twice as many books, it takes
a bit more than twice as long to alphabetize all of them, so n log n algorithms scale fairly well.
In fact, all of the efficient general sorting algorithms are O(n log n):
merge sort, quicksort, heapsort, and Timsort. (Timsort, invented by Tim
Peters, is the algorithm that Python’s sort() method uses.)
"""

"""
O(n^2), Polynomial Time
Checking for duplicate books on an unsorted bookshelf is a polynomial
time operation. If there are 100 books, you could start with the first book
and compare it with the 99 other books to see whether they’re the same.
Then you take the second book and check whether it’s the same as any of
the 99 other books. Checking for a duplicate of a single book is 99 steps
(we’ll round this up to 100, which is our n in this example). We have to
do this 100 times, once for each book. So the number of steps to check
for any duplicate books on the bookshelf is roughly n × n, or n^2 . (This
approximation to n^2 still holds even if we were clever enough not to repeat
comparisons.)
The runtime increases by the increase in books squared. Checking
100 books for duplicates is 100 × 100, or 10,000 steps. But checking twice
that amount, 200 books, is 200 × 200, or 40,000 steps: four times as
much work.
In my experience writing code in the real world, I’ve found the most com-
mon use of big O analysis is to avoid accidentally writing an O(n^2) algorithm
when an O(n log n) or O(n) algorithm exists. The O(n^2) order is when algorithms dramatically slow down,
so recognizing your code as O(n^2) or higher
should give you pause. Perhaps there’s a different algorithm that can solve the
problem faster. In these cases, taking a data structure and algorithms (DSA)
course, We also call O(n^2) quadratic time. Algorithms could have O(n^3), or cubic
time, which is slower than O(n^2); O(n^4), or quartic time, which is slower than
O(n^3); or other polynomial time complexities.
"""

"""
O(2^n), Exponential Time
Taking photos of the shelf with every possible combination of books on it is
an exponential time operation. Think of it this way: each book on the shelf
can either in be included in the photo or not included. Figure 13-1 shows
every combination where n is 1, 2, or 3. If n is 1, there are two possible pho-
tos: with the book and without. If n is 2, there are four possible photos: both
books on the shelf, both books off, the first on and second off, and the sec-
ond on and first off. When you add a third book, you’ve once again doubled
the amount of work you have to do: you need to do every subset of two books
that includes the third book (four photos) and every subset of two books
that excludes the third book (another four photos, for 23 or eight photos).
Each additional book doubles the workload. For n books, the number of
photos you need to take (that is, the amount of work you need to do) is 2n .
"""

"""O(n!), Factorial Time
Taking a photo of the books on the shelf in every conceivable order is a
factorial time operation. We call every possible order the permutation of n
books. This results in n!, or n factorial, orderings. The factorial of a number
is the multiplication product of all positive integers up to the number. For
example, 3! is 3 × 2 × 1, or 6. Figure 13-2 shows every possible permutation
of three books.
"""


# Examples:
# O(n), Linear Time
def reading_list(books):
    print('Here are the books I will read:')  # 1 step
    number_of_books = 0  # 1 step
    for book in books:  # n * steps in the loop
        print(book)  # 1 step
        number_of_books += 1  # 1 step
    print(number_of_books, 'books total.')  # 1 step


# O(n^2), Polynomial Time
def quadratic_example(someData):
    for i in someData:
        for j in someData:
            print('Something')
            print('Something')
            print('Something')


#  O(n), Linear Time
def linear_example(someData):
    for i in someData:
        for k in range(1000):
            print('Something')


# O(1), Constant Time
def i_love_books(books):
    for i in range(10):
        print('I LOVE BOOKS!!!')
        print('BOOKS ARE GREAT!!!')


# O(n2) polynomial time operation
def find_duplicate_books(books):
    for i in range(len(books) - 1):
        for j in range(i + 1, len(books)):
            if books[i] == books[j]:
                print('Duplicate:', books[i])


book_titles = []

with open('books.txt', 'r') as rf:
    for title in rf:
        book_titles.append(title.strip())

# Test the above function to see by yourself:
