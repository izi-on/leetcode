class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        def divide_and_conquer(arr, gen):
            if len(arr) <= 1:
                return arr
            l = list(filter(lambda x: x & (1 << gen) == 0, arr))
            r = list(filter(lambda x: x & (1 << gen) == 1, arr))
            print(l)
            print(r)
            return divide_and_conquer(l, gen + 1) + divide_and_conquer(r, gen + 1)

        return divide_and_conquer([i + 1 for i in range(n)], 0)
