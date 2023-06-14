from visualize import visualize


# The basic idea is to eliminate turtles, or small values near the end of the list
# Comb sort improves on bubble sort
# https://en.wikipedia.org/wiki/Comb_sort

def determine_next_gap(gap):
    return max(1, int(gap / 1.3))


def comb_sort(nums: list[int]) -> list[int]:
    gap = len(nums)
    is_sorted = False
    while not is_sorted or gap != 1:
        gap = determine_next_gap(gap)
        is_sorted = True
        for i in range(0, len(nums) - gap):
            yield nums, [i], [i + gap], []
            if nums[i] > nums[i + gap]:
                nums[i], nums[i + gap] = nums[i + gap], nums[i]
                is_sorted = False


visualize(comb_sort, 30)
