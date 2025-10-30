def min_max(nums):
    if isinstance(nums, list) and len(nums) != 0 and all(isinstance(element, (int, float)) for element in nums):
        return min(nums), max(nums)
    return 'ValueError'

print('min_max')
print(min_max([3, -1, 5, 6, 0]))
print(min_max([52]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([2.5, -2, 2.1, 3.1]))


def unique_sorted(nums):
    if isinstance(nums, list) and len(nums) != 0 and all(isinstance(element, (int, float)) for element in nums):
        return sorted(set(nums))
    return nums

print('unique_sorted')
print(unique_sorted([3, 2, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.6, 2.4, 0]))


def flatten(mat):
    if isinstance(mat, (list, tuple)) and len(mat) != 0 and all(isinstance(element, (list, tuple)) for element in mat):
        result = []
        for element in mat:
            result.extend(element)
        return result
    return 'TypeError'

print('flatten')
print(flatten([[2, 3], [4, 5]]))
print(flatten(([2, 3], (4, 5, 6))))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "gg"]))