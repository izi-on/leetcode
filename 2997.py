class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        def get_bit_list(num: int):
            num_of_bits = 32
            res = []
            while num_of_bits > 0:
                res.append(num % 2)
                num //= 2
                num_of_bits -= 1
            return res

        def xor(num1: list[int], num2: list[int]):
            return [num1[i] ^ num2[i] for i in range(32)]

        # get current bits required for nums
        target = get_bit_list(k)

        cur = get_bit_list(nums[0])
        for num in nums[1:]:
            cur = xor(cur, get_bit_list(num))

        return sum(xor(cur, target))
