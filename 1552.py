class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position = sorted(position)

        def is_possible(min_force):
            m_l = m - 1
            prev = position[0]
            for p in position[1:]:
                if p - prev >= min_force:
                    m_l -= 1
                    prev = p
                if m_l == 0:
                    return True
            return False

        def solve():
            l_, r = 1, (position[-1] - position[0]) // (m - 1)
            max_force = 1
            while l_ <= r:
                mid = (l_ + r) // 2
                # print("is ", mid, "possible")
                if is_possible(mid):
                    # print("possible")
                    max_force = mid
                    l_ = mid + 1
                else:
                    # print("impossible")
                    r = mid - 1
            return max_force

        return solve()
