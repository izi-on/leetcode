class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        s = []
        for i in range(len(nums)):
            num = nums[i]
            l, r = 0, len(s) - 1
            ans = len(s)
            while l <= r:
                mid = (l + r) // 2
                if num <= s[mid]:
                    ans = mid
                    r = mid - 1
                else:
                    l = mid + 1

            if ans == len(s):
                s.append(num)
            else:
                s[ans] = num
        return len(s)
