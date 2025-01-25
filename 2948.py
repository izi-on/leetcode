import heapq


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        nums2 = sorted(nums)
        cur_group = [nums2[0]]
        val_to_group = {nums2[0]: cur_group}
        for i in range(1, len(nums2)):
            if nums2[i] - nums2[i - 1] > limit:
                cur_group = []
            heapq.heappush(cur_group, nums2[i])
            val_to_group[nums2[i]] = cur_group

        ans = []
        for i in range(len(nums)):
            val = nums[i]
            group = val_to_group[val]
            smallest = heapq.heappop(group)
            ans.append(smallest)
        return ans
