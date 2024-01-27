class Solution:
    def __init__(self):
        self.permutations = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(options, cur_perm):
            if not options:
                self.permutations.append(cur_perm.copy())
                return
            for option in list(options):
                options.remove(option)
                cur_perm.append(option)
                dfs(options, cur_perm)
                cur_perm.pop()
                options.add(option)

        dfs(set(nums), [])
        return self.permutations
