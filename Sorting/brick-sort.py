from visualize import visualize


# O(n^2), Polynomial Time
# https://en.wikipedia.org/wiki/Odd%E2%80%93even_sort
def brick_sort(nums: list[int]) -> list[int]:
    is_sorted = False
    while not is_sorted:
        for i in range(0, len(nums) - 1, 2):
            yield nums, [i], [], []
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                is_sorted = False
        # assume that the array is sorted
        is_sorted = True

        for i in range(1, len(nums) - 1, 2):
            yield nums, [], [i], []
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                is_sorted = False


visualize(brick_sort, 30)
