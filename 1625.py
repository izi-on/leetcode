class Solution:
    def gcd(a, b):
        if a > b:
            return gcd(b, a)
        if a == 0:
            return b
        return gcd(b % a, a)

    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        step_amt_a = gcd(a, 10)
        step_amt_b = gcd(b, n)

        ress = []

        if step_amt_b % 2 == 1:
            for i in range(0, n, step_amt_b):
                min_val = 11
                min_times_fs = -1
                for k in range(10):
                    s_i = (int(s[(i) % n]) + k * a) % 10
                    if s_i < min_val:
                        min_val = s_i
                        min_times_fs = k

                min_val = 11
                min_times_snd = -1
                for k in range(10):
                    s_i = (int(s[(i + 1) % n]) + k * a) % 10
                    if s_i < min_val:
                        min_val = s_i
                        min_times_snd = k

                cand = []
                for j in range(0, n):
                    s_i = int(s[(i + j) % n])
                    if j % 2 == 0:
                        cand.append((s_i + a * min_times_fs) % 10)
                    else:
                        cand.append((s_i + a * min_times_snd) % 10)
                ress.append("".join(str(x) for x in cand))
        else:
            for i in range(0, n, step_amt_b):
                min_val = 11
                min_times_snd = -1
                for k in range(10):
                    s_i = (int(s[(i + 1) % n]) + k * a) % 10
                    if s_i < min_val:
                        min_val = s_i
                        min_times_snd = k

                cand = []
                for j in range(0, n):
                    s_i = int(s[(i + j) % n])
                    if j % 2 == 0:
                        cand.append(s_i)
                    else:
                        cand.append((s_i + a * min_times_snd) % 10)
                ress.append("".join(str(x) for x in cand))

        return min(ress)
