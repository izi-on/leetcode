from typing import List
import heapq


class Task:
    def __init__(self, user_id, task_id, priority):
        self.user_id = user_id
        self.task_id = task_id
        self.priority = priority
        self.removed = False

    def _compare_tuple(self):
        return (-self.priority, -self.task_id, self.user_id)

    def __lt__(self, other):
        return self._compare_tuple().__lt__(other._compare_tuple())

    def remove(self):
        self.removed = True

    def is_removed(self):
        return self.removed

    def __repr__(self):
        return f"Task({self.user_id}, {self.task_id}, {self.priority}, {self.removed})"


class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.task_heap = []
        self.task_id_to_task = {}

        for task in tasks:
            self.add(task[0], task[1], task[2])

    def add(self, userId: int, taskId: int, priority: int) -> None:
        task = Task(userId, taskId, priority)
        self.task_id_to_task[taskId] = task
        heapq.heappush(self.task_heap, task)

    def edit(self, taskId: int, newPriority: int) -> None:
        old_task = self.task_id_to_task[taskId]
        self.add(old_task.user_id, taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        task = self.task_id_to_task[taskId]
        task.remove()

    def _is_outdated(self, task):
        return task != self.task_id_to_task[task.task_id]

    def execTop(self) -> int:
        if not self.task_heap:
            return -1

        highest_priority_task = self.task_heap[0]
        while self.task_heap and (
            highest_priority_task.is_removed()
            or self._is_outdated(highest_priority_task)
        ):
            heapq.heappop(self.task_heap)
            highest_priority_task = self.task_heap[0] if self.task_heap else None

        if not self.task_heap:
            return -1

        highest_priority_task = self.task_heap[0]
        highest_priority_task.remove()
        return highest_priority_task.user_id


# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
