# Why do arrays have constant time access?
# Dynamic Vs Static arrays -> https://www.geeksforgeeks.org/implementation-of-dynamic-array-in-python/

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
"""


def last(array: list, n: int) -> []:
    if n > len(array):
        return "invalid"
    elif n < 1:
        return []
    else:
        return array[-n:]


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
"""


def add_indexes(numbers: list) -> list:
    return [idx + num for idx, num in enumerate(numbers)]


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
"""

from functools import reduce
from operator import mul


def multiply_nums(numbers: str) -> int:
    nums = numbers.split(', ')
    return reduce(mul, map(int, nums))


"""
Challenge #4:

Return the number (count) of vowels in the given string.

We will consider 'a,e,i,o,u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.
"""


# sentence = 'auidah kEoLmno'


def get_count(sentence: str) -> int:
    return sum(map(lambda x: x.lower() in "aeiou", sentence))


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
"""


def max_and_min(input_str: str) -> str:
    nums = list(map(int, input_str.split(' ')))
    return f"{max(nums)} {min(nums)}"


# Describe the difference between an in-place algorithm and out-of-place algorithm.
def double_nums_in_place(int_list):
    # in place will modify the array that's passed in to the function
    # Save space / faster -> But they have side effects
    # https://en.wikipedia.org/wiki/In-place_algorithm
    for idx, item in enumerate(int_list):
        int_list[idx] = item * 2


def double_nums_out_of_place(int_list):
    # Create a new array, and modify it, then we must return it.
    return list(map(lambda item: item * 2, int_list))


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
"""


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
# Challenge #7:
A palindrome is a word, phrase, number, or another sequence of characters that reads the
same backward or forward. This includes capital letters, punctuation. and other special character.

Given a string. write a unction that checks if the input is valid palindrome.

Examples:
- "race car"    -> True
- "anna"       -> True
- "12345"      -> False
- "12321"      -> True
- "race a car" -> False
- "do geese see god" -> True (from young sheldon)

Notes:
- Try to solve this challenge without using the reverse of the input string; use a for loop
to iterate through the string and make the neccessary companions
"""


# BigO -> O(n)
def is_palindrome(word: str) -> bool:
    word = ''.join(filter(str.isalnum, word)).lower()
    start_index, end_index = 0, len(word) - 1
    while start_index < end_index:
        if word[start_index] != word[end_index]:
            return False
        start_index += 1
        end_index -= 1
    return True


# https://leetcode.com/problems/palindrome-number/

def is_palindrome_for_integer(num: int) -> bool:
    if num < 0:
        return False
    div = 1
    while num >= 10 * div:
        div *= 10
    print(div)
    while num:
        right = num % 10
        left = num // div
        if right != left:
            return False
        num = (num % div) // 10
        div = div / 100
    return True


# https://leetcode.com/problems/plus-one/
# BigO -> O(n)
def plus_one(digits: list[int]) -> list[int]:
    for idx in range(len(digits) - 1, -1, -1):
        if digits[idx] < 9:
            digits[idx] += 1
            return digits
        else:
            digits[idx] = 0
    digits.insert(0, 1)
    return digits


# https://leetcode.com/problems/maximum-subarray/

# BigO -> O(n^2)
def max_sub_array_brute_force(nums: list[int]) -> int:
    max_sub = nums[0]
    for size in range(1, len(nums) + 1):
        for i in range(0, len(nums) - size + 1):
            sub_sum = sum(nums[i: i + size])
            if sub_sum > max_sub:
                max_sub = sub_sum
    return max_sub


# BigO -> O(n)
def max_sub_array_clever(nums: list[int]) -> int:
    best_sum = nums[0]
    current_best_sum = nums[0]
    # loop through each value
    for num in nums[1:]:
        # every time we see a new value, we have to learn something
        # We have to decide, to add the new number to our current best sum
        if current_best_sum + num > num:
            current_best_sum = current_best_sum + num
        else:
            # Or,start fresh, with just this number as our new current best sum
            current_best_sum = num
            # if current_best_sum is even bigger that best_sum
        if current_best_sum > best_sum:
            best_sum = current_best_sum
    return best_sum


# https://leetcode.com/problems/move-zeroes/
# BigO -> O(n)
def move_zeroes(nums: list[int]) -> None:
    # Do not return anything, modify nums in-place instead.

    zero_count = nums.count(0)
    zero_index = 0
    # O(n)
    for num in nums:
        if num != 0:
            nums[zero_index] = num
            zero_index += 1
    for zero in range(1, zero_count + 1):
        nums[-zero] = 0


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=list&envId=regnb1dt
# BigO -> O(n)
def max_profit(prices: list[int]) -> int:
    current_buy = prices[0]
    profit = 0
    for price in prices:
        if price < current_buy:
            current_buy = price
        elif (price - current_buy) > profit:
            profit = price - current_buy
    return profit


# https://leetcode.com/problems/two-sum/?envType=list&envId=regnb1dt

# BigO -> O(n^2)
def two_sum_brute_force(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# BigO -> O(n)
def two_sum_dic_way(nums: list[int], target: int) -> list[int]:
    seen = {}
    for idx, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], idx]
        elif num not in seen:
            seen[num] = idx


# https://leetcode.com/problems/jump-game/?envType=list&envId=regnb1dt
# BigO -> O(n)
def can_jump_greedy(nums: list[int]) -> bool:
    goal = nums[-1]
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    return True if goal == 0 else False


# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
def remove_duplicates(nums: list[int]) -> int:
    left_pointer = 1
    for right_pointer in range(1, len(nums)):
        if nums[right_pointer] != nums[right_pointer - 1]:
            nums[left_pointer] = nums[right_pointer]
            left_pointer += 1
    return left_pointer


# https://leetcode.com/problems/length-of-last-word/?envType=list&envId=regnb1dt
def length_of_last_word(s: str) -> int:
    count = 0
    for letter in s[::-1]:
        if letter != " ":
            count += 1
        if letter == " " and count >= 1:
            return count
    return count


# https://leetcode.com/problems/merge-sorted-array/?envType=list&envId=regnb1dt
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    empty_element = m + n - 1
    while m > 0 and n > 0:
        if nums2[n - 1] > nums1[m - 1]:
            nums1[empty_element] = nums2[n - 1]
            n -= 1
        else:
            nums1[empty_element] = nums1[m - 1]
            m -= 1
        empty_element -= 1
    while n > 0:
        nums1[empty_element] = nums2[n - 1]
        empty_element, n = empty_element - 1, n - 1
