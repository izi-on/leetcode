class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memoized = {}

        def helper(i):
            if i >= len(questions):
                return 0
            if i in memoized:
                return memoized[i]
            question = questions[i]
            points, brainpower = question
            memoized[i] = max(helper(i + 1), points + helper(i + brainpower + 1))
            return memoized[i]

        return helper(0)
