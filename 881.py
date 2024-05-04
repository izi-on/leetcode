import heapq


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        left, right = 0, len(people) - 2
        boat_count = 0
        while left < right:
            res = people[left] + people[right]
            if res > limit:
                right -= 1
            elif res <= limit:
                left += 1
                right -= 1
            boat_count += 1
        if left == right:
            boat_count += 1
        return boat_count
