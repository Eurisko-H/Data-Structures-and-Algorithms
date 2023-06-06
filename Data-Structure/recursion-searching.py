# Liner search
def linear_search(arr, target):
    for i in arr:
        if i == target:
            return True
    return False


# Recursive version of linear search
def linear_search_recursive(arr, target):
    # base case
    if len(arr) == 0:
        return False
    elif arr[0] == target:
        return True
    else:
        found = linear_search_recursive(arr[1:], target)
    return found


# binary search BigO -> O(log n)
def binary_search(arr, target):
    min_val = 0
    max_val = len(arr) - 1
    while not max_val < min_val:
        guess = (max_val + min_val) // 2
        if arr[guess] == target:
            return guess
        elif arr[guess] < target:
            min_val = guess + 1
        else:
            max_val = guess - 1
    return -1


# binary search BigO -> O(log n)
def find_rotation_point(array: list[str]):
    floor = 0
    ceiling = len(array) - 1

    while floor < ceiling:
        guess = (ceiling + floor) // 2
        if array[guess] > array[floor]:
            floor = guess
        else:
            ceiling = guess

        if array[floor + 1] == array[ceiling]:
            return array[ceiling]


surnames = [
    'glover',
    'kennedy',
    'liu',
    'mcdowell',
    'nixon',
    'sparks',
    'zhang',
    'ahmed',  # <-- rotates here
    'brandt',
    'davenport',
    'farley',
]


# Return the nth fibonacci number: BigO -> O(2^n) Exponential Time
def recursive_fib(n: int):
    # base case
    if n <= 1:
        return n
    else:
        return recursive_fib(n - 1) + recursive_fib(n - 2)


def iterative_fib(n):
    n_1 = 1
    n_2 = 0
    current_n = n_1 + n_2
    if n <= 1:
        return n
    for i in range(2, n):
        n_2 = n_1
        n_1 = current_n
        current_n = n_1 + n_2
    return current_n


# palindrome recursively
def is_palindrome(s: str):
    # base case
    if len(s) <= 1:
        return True
    else:
        return (s[0] == s[len(s) - 1]) and (is_palindrome(s[1:-1]))


"""
For a given possible integer (n) determine if it can be represented as a sum of two Fibonacci numbers
(possibly equal)

Example:
- For n = 1  -> fibonacci_simple_sum_2(n) =  True  (1 = 0 + 1)
- For n = 11 -> fibonacci_simple_sum_2(n) =  True  (11 = 8 + 3)
- For n = 60 -> fibonacci_simple_sum_2(n) =  True  (60 = 5 + 55)
- For n = 66 -> fibonacci_simple_sum_2(n) =  False 
"""


# In every searching problems you have to think about, searching for what? and where?
def fibonacci_simple_sum_2(target):
    useful_nums = set()
    fib_index = 0
    while True:
        fib_num = iterative_fib(fib_index)
        if fib_num > target:
            break
        useful_nums.add(fib_num)
        fib_index += 1

    for num in useful_nums:
        if (target - num) in useful_nums:
            return True
    return False
