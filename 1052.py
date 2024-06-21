class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        c_during_g = [
            customers[i] if grumpy[i] == 1 else 0 for i in range(len(customers))
        ]
        max_interval = sum(c_during_g[:minutes])
        m_i_idx = 0
        cur_interval = max_interval
        for i in range(minutes, len(c_during_g)):
            cur_interval -= c_during_g[i - minutes]
            cur_interval += c_during_g[i]
            print(i - minutes + 1, cur_interval)
            if cur_interval > max_interval:
                m_i_idx = i - minutes + 1
                max_interval = cur_interval
        satisfied = 0
        for i in range(m_i_idx):
            if not grumpy[i]:
                satisfied += customers[i]
        for i in range(m_i_idx, m_i_idx + minutes):
            satisfied += customers[i]
        for i in range(m_i_idx + minutes, len(customers)):
            if not grumpy[i]:
                satisfied += customers[i]
        return satisfied
