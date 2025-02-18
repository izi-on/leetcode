class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def helper(cur_arr: list, pidx, avail_nums: list):
            if len(cur_arr) == 0:
                # print(avail_nums)
                og_avail = avail_nums.copy()
                for num in og_avail:
                    cur_arr.append(num)
                    avail_nums.remove(num)
                    # print(cur_arr)
                    ans = helper(cur_arr, pidx, avail_nums)
                    if ans:
                        return ans
                    avail_nums = og_avail.copy()
                    cur_arr.pop()
                return []

            if pidx == len(pattern):
                return cur_arr

            to_try = []
            if pattern[pidx] == "I":
                to_try = list(filter(lambda x: x > cur_arr[-1], avail_nums))
            else:
                to_try = list(filter(lambda x: x < cur_arr[-1], avail_nums))
            og_avail = avail_nums.copy()
            for t in to_try:
                cur_arr.append(t)
                avail_nums.remove(t)
                att = helper(cur_arr, pidx + 1, avail_nums)
                if att:
                    return att
                avail_nums = og_avail.copy()
                cur_arr.pop()
            return []

        return "".join(
            list(map(lambda x: str(x), helper([], 0, [i for i in range(1, 10)])))
        )
