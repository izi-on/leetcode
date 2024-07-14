from collections import deque, defaultdict


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def get_multiplier(s_i):
            st = s_i
            while s_i < len(formula) and formula[s_i].isdigit():
                s_i += 1
            return formula[st:s_i]

        def helper(start_idx):
            count_atoms = defaultdict(int)
            i = start_idx
            while i < len(formula):
                if formula[i] == "(":
                    end_idx, s_count_atoms = helper(i + 1)
                    i = end_idx + 1
                    multiplier_str = get_multiplier(i)
                    multiplier = int(multiplier_str) if multiplier_str else 1
                    for k, v in s_count_atoms.items():
                        count_atoms[k] += v * multiplier
                    i += len(multiplier_str)
                elif formula[i] == ")":
                    return i, count_atoms
                elif formula[i].isalpha():
                    a_s_i = i
                    while (
                        i + 1 < len(formula)
                        and formula[i + 1].isalpha()
                        and formula[i + 1].islower()
                    ):
                        i += 1
                    atom = formula[a_s_i : i + 1]
                    multiplier_str = get_multiplier(i + 1)
                    multiplier = int(multiplier_str) if multiplier_str else 1
                    count_atoms[atom] += multiplier
                    i += len(multiplier_str) + 1
            return i, count_atoms

        _, answer = helper(0)
        l_ans = []
        for k, v in answer.items():
            l_ans.append((k, v))
        return "".join(
            [str(item) for t in sorted(l_ans) for item in t if str(item) != "1"]
        )
