from typing import List


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        def to_bit_list(num):
            return list(map(int, bin(num)[2:]))[::-1]

        def bl_to_bit(bl):
            return [1 if num else 0 for num in bl]

        cur_acc = [0 for _ in range(30)]
        tail = -1
        ans = set()
        for i in range(len(arr)):
            num = arr[i]
            print("--------------")
            print("at ", num)
            new_acc = list(map(sum, zip(cur_acc, to_bit_list(num))))
            print("acc", new_acc, "tail", tail)
            while tail < i and bl_to_bit(new_acc) == bl_to_bit(cur_acc):
                cur_acc = new_acc
                tail += 1
                new_acc = list(
                    map(sum, zip(new_acc, [-num for num in to_bit_list(arr[tail])]))
                )
            ans.add(new_acc)
            cur_acc = new_acc
            print("new acc", new_acc, "tail", tail)
            print("--------------")
        return len(ans)
