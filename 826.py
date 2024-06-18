class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        jobs = []
        for i in range(len(difficulty)):
            jobs.append((profit[i], difficulty[i]))
        jobs = sorted(jobs, reverse=True)
        worker = sorted(worker, reverse=True)
        max_profit = 0
        job_ptr = 0
        for w in worker:
            while job_ptr < len(jobs) and w < jobs[job_ptr][1]:
                job_ptr += 1
            if job_ptr >= len(jobs):
                break
            max_profit += jobs[job_ptr][1]
        return max_profit
