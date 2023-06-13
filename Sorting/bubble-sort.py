from visualize import visualize


def bubble_sort(nums: list[int]) -> list[int]:
    for i in range(len(nums) - 1):
        for j in range(0, len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                yield nums, [j + 1], [], list(range(len(nums) - i, len(nums)))


visualize(bubble_sort, 30)
