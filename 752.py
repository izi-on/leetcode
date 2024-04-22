from collections import deque
from types import new_class


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = [0, 0, 0, 0]
        target_tuple = list(map(int, target))
        bfs = deque()
        bfs.append(start)
        count_turn = 0
        visited = set()
        deadends = set(deadends)
        while len(bfs) > 0:
            n = len(bfs)
            for _ in range(n):
                cur_state: list[int] = bfs.popleft()
                print("at ", cur_state)
                cur_state_str = "".join(list(map(str, cur_state)))
                if cur_state_str in visited or cur_state_str in deadends:
                    continue
                visited.add(cur_state_str)
                if cur_state == target_tuple:
                    return count_turn
                for i in range(len(cur_state)):
                    new_state_up = cur_state.copy()
                    new_state_up[i] = (new_state_up[i] + 1) % 10
                    bfs.append(new_state_up)
                    new_state_down = cur_state.copy()
                    new_state_down[i] = (new_state_down[i] - 1) % 10
                    bfs.append(new_state_down)
            count_turn += 1
        return -1
