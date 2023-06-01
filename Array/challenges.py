"""
Challenge #1:

Write a function that retrieves the last n elements from a list:

Examples:
    - last([1,2,3,4,5], 1) -> [5]
    - last([4,3,9,9,7,6], 3)  -> [9,7,6]
    - last([1,2,3,4,5], 7) -> "invalid"
    - last([1,2,3,4,5], 0) -> []

Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0


def last(l: list, n: int) -> []:
    if n > len(l):
        return "invalid"
    elif n < 1:
        return []
    else:
        return l[-n:]

"""

"""
Challenge #2:

Given a list of numbers, create a function that returns the list but with each
element's index in the list added to itself. You should add 0 to the number at
index 0, add 1 to the number at index1, etc.

Examples:
- add_indexes([0,0,0,0,0]) -> [0,1,2,3,4]
- add_indexes([1,2,3,4,5]) -> [1,3,5,7,9]

Notes:
- The input list will only contain integers.


def add_indexes(numbers: list) -> list:
    return [idx+num for idx, num in enumerate(numbers)]
"""

"""
Challenge #3:

Given a string of numbers separated by a comma and space, return the product of the numbers.

Examples:
- multiply_nums("2, 3") -> 6
- multiply_nums("1, 2, 3, 4") -> 24
- multiply_nums("54, 75, 453, 0") -> 0
- multiply_nums("10, -2") -> -20

Notes:
- Bonus: Try to complete this challenge in on line!


from functools import reduce
from operator import mul

def multiply_nums(numbers: str) -> int:
    nums = numbers.split(', ')
    return reduce(mul, map(int, nums))
"""

"""
Challenge #4:

Return the number (count) of vowels in the given string.

We will consider 'a,e,i,o,u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.


sentence = 'auidah kEoLmno'

def get_count(sentence: str) -> int:
    return sum(map(lambda x: x.lower() in "aeiou", sentence))

"""

"""
Challenge #5:

Given s string of space separated integers, write a function that return
the maximum and minimum integers.

Example:
- max_and_min("1 2 3 4 5") -> "5 1"
- max_and_min("1 2 -3 4 5") -> "5 -3"

Notes:
- All inputs are valid integers.
- There will always be at least one number in the input string.
- The return string must be two numbers separated by a single space, and
the maximum number is first.

def max_and_min(input_str: str) -> str:
    nums = list(map(int, input_str.split(' ')))
    return f"{max(nums)} {min(nums)}"
"""

"""
Describe the difference between an in-place algorithm and out-of-place algorithm.

def double_nums_in_place(int_list):
    # in place will modify the array that's passed in to the function
    # Save space / faster
    # https://en.wikipedia.org/wiki/In-place_algorithm
    for idx, item in enumerate(int_list):
        int_list[idx] = item * 2


def double_nums_out_of_place(int_list):
    # Create a new array, and modify it, then we must return it.
    return list(map(lambda item: item * 2, int_list))
"""

"""
Challenge #6:

Given an array of integers 'nums', define a function that returns the "pivot" index of the array.

The "pivot" index is where the sum of all the numbers on the left of that index is equal
to the sum of all the numbers on the right of that index.

If the input array does not have a "pivot" index, then the function should return '-1'.
If there are more than one "pivot" indexes, then you should return the left-most "pivot" index.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of hte numbers to the left of index 3 (1 + 7 + 3 = 11) is equal
to the sum of numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.

Example 2:
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.


# BigO -> O(n^2)
def pivot_index(nums: list[int]) -> int:
    for idx in range(len(nums)):
        # all numbers to the left of index
        left = nums[:idx]
        # all numbers to the right
        right = nums[idx + 1:]
        # sum the numbers to the left & right
        if sum(left) == sum(right):
            return idx
        else:
            continue
    return -1

# BigO -> O(n)
def pivot_index_reflect(nums: list[int]) -> int:
    left_sum = 0
    right_sum = sum(nums)
    for idx in range(len(nums)):
        # Everytime we get to a new index
        # subtract that index, from the right_sum
        right_sum -= nums[idx]
        if left_sum == right_sum:
            return idx
        # Add the index to the left_sum
        left_sum += nums[idx]
    return -1
"""

"""
# https://leetcode.com/problems/plus-one/

def plus_one(digits: list[int]) -> list[int]:
    for idx in range(len(digits) - 1, -1, -1):
        if digits[idx] < 9:
            digits[idx] += 1
            return digits
        else:
            digits[idx] = 0
    digits.insert(0, 1)
    return digits
"""
