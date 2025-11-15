class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        prev = [-1] * (n + 1)  # linked list from 0 to 0 backwards, closest
        for i in range(1, n):
            if s[i - 1] == "0":
                prev[i] = i - 1
            else:
                prev[i] = prev[i - 1]

        ans = 0
        for end_idx in range(n):
            count0 = int(s[end_idx] == "0")
            count1 = int(s[end_idx] == "1")
            cur_zero_pos = end_idx  # start it at end_idx regardless
            while (
                prev[cur_zero_pos] != -1 and (end_idx + 1) - count0 >= count0**2
            ):  # while we still have more previous 0s, and we don't have too many 0s
                old_zero = cur_zero_pos  # keep track of prev start_idx
                cur_zero_pos = prev[cur_zero_pos]
                start_idx = cur_zero_pos + 1
                count1 = end_idx - start_idx + 1 - count0
                if count1 >= count0**2:
                    number_of_shifts_to_left = (
                        old_zero + 1
                    ) - start_idx  # old_zero +1 is the old start_idx
                    number_of_start_idx_that_contributed_to_total_count = (
                        count1 - count0**2
                    ) + 1
                    # why do we need to keep track of both of the above?
                    # because suppose when we added the new 0 from the previous iteration,
                    # our inequality was temporarily broken (count0** 2 > count1), then some
                    # of the 1s did NOT contribute to adding to the total amount of subarrays
                    #
                    # on the other hand, suppose when we added the new 0, our inequality was still holding.
                    # then every single added element counts as a new subarray, so we just count the amount by which
                    # we shifted
                    ans += min(
                        number_of_shifts_to_left,
                        number_of_start_idx_that_contributed_to_total_count,
                    )
                count0 += 1  # add the zero

            # if we run out of previous 0s, then the previous values are all 1s
            if prev[cur_zero_pos] == -1:
                count1 += cur_zero_pos  # add the remaining 1s
                if count1 >= count0**2:
                    ans += min(
                        cur_zero_pos + 1, count1 - count0**2 + 1
                    )  # same logic, but cur_zero_pos+1 is just the shifts to the left

        return ans
