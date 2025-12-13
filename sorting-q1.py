class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        min_diff = min([cmp[1] - cmp[0] for cmp in list(zip(arr[1:], arr[:-1]))])
        return list(
            filter(lambda x: x[1] - x[1] == min_diff, list(zip(arr[1:], arr[:-1])))
        )
