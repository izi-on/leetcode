class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        track_cur_num_arr = [0 for _ in range(32)]

        def convert_to_bit_arr(num):
            bit_arr = []
            while num:
                bit_arr.append(num & 1)
                num = num >> 1
            bit_arr += [0] * (32 - len(bit_arr))
            return bit_arr

        def convert_bit_arr_to_num(bit_arr):
            ans = 0
            for i in range(len(bit_arr)):
                ans += min(bit_arr[i], 1) * (2**i)
            return ans

        tail_idx = -1
        ans = float("inf")
        for i in range(len(nums)):
            cur_num = nums[i]
            cur_num_arr = convert_to_bit_arr(cur_num)
            track_cur_num_arr = list(
                map(lambda x: sum(x), zip(track_cur_num_arr, cur_num_arr))
            )
            while convert_bit_arr_to_num(track_cur_num_arr) >= k and tail_idx < i:
                print(convert_bit_arr_to_num(track_cur_num_arr), k)
                ans = min(ans, i - tail_idx)
                tail_idx += 1
                tail_num_arr = convert_to_bit_arr(nums[tail_idx])
                track_cur_num_arr = list(
                    map(lambda x: x[0] - x[1], zip(track_cur_num_arr, tail_num_arr))
                )

        if ans == float("inf"):
            return -1
        return ans
