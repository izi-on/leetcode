# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         cache = {}
#
#         def dfs(i):
#             nonlocal cache
#             if i == len(nums):
#                 return 0
#             if i in cache.keys():
#                 return cache[i]
#             track_max = 0
#             for j in range(i + 1, len(nums)):
#                 if nums[j] > nums[i]:
#                     track_max = max(track_max, dfs(j))
#             cache[i] = track_max + 1
#             return cache[i]
#
#         return max([dfs(i) for i in range(len(nums))])
    
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
