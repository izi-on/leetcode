class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        net = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(net) < 0:
            return -1
        idx = 0
        cur_start = 0
        cur_track = 0
        for _ in net:
            cur_track += net[idx]
            if cur_track < 0:
                cur_start = (idx + 1) % len(net)
                cur_track = 0
        return cur_start
