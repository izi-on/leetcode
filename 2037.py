class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)
        answer = 0
        for i in range(len(seats)):
            answer += abs(seats[i] - students[i])
        return answer
