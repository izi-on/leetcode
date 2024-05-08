class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = [None] * len(score)
        score = sorted([(s, i) for (i, s) in enumerate(score)], reverse=True)
        for i, t in enumerate(score):
            pos = ""
            match i:
                case 0:
                    pos = "Gold Medal"
                case 1:
                    pos = "Silver Medal"
                case 2:
                    pos = "Bronze Medal"
                case _:
                    pos = str(i + 1)
            rank[t[1]] = pos
        return rank
