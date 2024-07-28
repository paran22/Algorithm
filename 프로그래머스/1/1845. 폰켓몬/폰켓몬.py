def solution(nums):
    unique_nums = set(nums)
    return min(len(unique_nums), len(nums) // 2)