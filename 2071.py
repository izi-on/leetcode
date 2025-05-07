class Solution:
    def maxTaskAssign(
        self, tasks: List[int], workers: List[int], pills: int, strength: int
    ) -> int:
        # first, use greedy
        tasks = sorted(tasks)
        workers = sorted(tasks)
        remaining_workers = set()
        remaining_tasks = set()
        for i in range(len(tasks) - 1, -1, -1):
            cur_task = tasks[i]

            # get tightest bound worker
            l, r = 0, len(workers) - 1
