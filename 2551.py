class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pairs = []
        for i in range(len(weights) - 1):
            pairs.append(weights[i] + weights[i + 1])
        pairs = sorted(pairs)
        answer = 0
        for i in range(k - 1):
            answer += pairs[len(weights) - 2 - i] - pairs[i]
        return answer
