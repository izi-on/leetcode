from collections import defaultdict
from typing import List


class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        peaks = [(peak[0], peak[1]) for peak in peaks]
        gpeaks = defaultdict(int)
        for peak in peaks:
            gpeaks[peak] += 1
        gpeaks = sorted(gpeaks.items())
        monostack = []

        def right(peak):
            return peak[0] + peak[1]

        def left(peak):
            return peak[0] - peak[1]

        for peak, count in gpeaks:
            lp = left(peak)
            rp = right(peak)
            while monostack and monostack[-1][0] >= lp:
                monostack.pop()

            if not monostack or monostack[-1][1] < rp:
                overlap_count = int(count > 1)
                monostack.append((left(peak), right(peak), overlap_count))

        return len(monostack) - sum([x[2] for x in monostack])
