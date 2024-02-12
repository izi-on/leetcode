class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        track_last = {}
        for i, c in enumerate(s):
            track_last[c] = i
        ans = []
        start_ptr = 0
        while start_ptr < len(s):
            last_ptr = track_last[s[start_ptr]]
            ptr = start_ptr + 1
            while ptr < last_ptr:
                last_occurence_idx = track_last[s[ptr]]
                if last_occurence_idx > last_ptr:
                    last_ptr = last_occurence_idx
                ptr += 1
            ans.append(last_ptr + 1 - start_ptr)
            start_ptr = last_ptr + 1
        return ans
