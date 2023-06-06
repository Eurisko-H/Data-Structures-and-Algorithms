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


# Return the nth fibonacci number
def fib(n: int):
    # base case
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# palindrome recursively
def is_palindrome(s: str):
    # base case
    if len(s) <= 1:
        return True
    else:
        return (s[0] == s[len(s) - 1]) and (is_palindrome(s[1:-1]))
