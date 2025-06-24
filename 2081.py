class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def base_k(num):
            res = ""
            pow = 0
            while num:
                rem = num % k
                num //= k
                res += str(rem)
            return res[::-1]

        def is_mirror(num_str):
            ptr1, ptr2 = 0, len(num_str) - 1
            while ptr1 <= ptr2:
                if num_str[ptr1] != num_str[ptr2]:
                    return False
                ptr1 += 1
                ptr2 -= 1
            return True

        def create_mirror(num_int, is_odd):
            num = num_int
            num_rem = num_int
            if is_odd:
                num_rem //= 10
            while num_rem:
                num = num * 10 + num_rem % 10
                num_rem //= 10
            return num

        cur_pref = 1
        pref_len = 0
        even_d = False
        ans = 0
        left, right = 1, 0
        while n:
            right = left * 10
            for _ in range(left, right):
                mirr_num = create_mirror(cur_pref, True)
                bk = base_k(mirr_num)
                # print(mirr_num, bk, is_mirror(bk))
                if is_mirror(bk):
                    ans += mirr_num
                    n -= 1
                    if n == 0:
                        return ans
                cur_pref += 1

            cur_pref //= 10

            for _ in range(left, right):
                mirr_num = create_mirror(cur_pref, False)
                bk = base_k(mirr_num)
                # print(mirr_num, bk, is_mirror(bk))
                if is_mirror(bk):
                    ans += mirr_num
                    n -= 1
                    if n == 0:
                        return ans
                cur_pref += 1

            left = right
