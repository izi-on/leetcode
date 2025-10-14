class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        first_free_at = 0
        last_free_at = 0
        skill_sum = sum(skill)
        first_skill = skill[0]
        for potion in mana:
            time_for_potion = skill_sum * potion
            optimal_start = last_free_at - time_for_potion
            min_start = first_free_at
            potion_start = max(min_start, optimal_start)
            first_free_at = potion_start + first_skill * potion
            last_free_at = potion_start + time_for_potion
        return last_free_at
