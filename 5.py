class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = "#" + "#".join(s) + "#"

        track_rad = [0 for _ in range(len(s))]
        cur_center = None

        for i in range(len(track_rad)):
            if cur_center:
                mirror_idx = cur_center - (i - cur_center)

                if mirror_idx >= 0 and track_rad[mirror_idx] + i >= len(s):
                    track_rad[i] = len(s) - i - 1
                    continue

                if (
                    mirror_idx >= 0
                    and track_rad[cur_center] + cur_center > track_rad[mirror_idx] + i
                ):
                    track_rad[i] = track_rad[mirror_idx]
                    continue

                if (
                    mirror_idx >= 0
                    and track_rad[cur_center] + cur_center <= track_rad[mirror_idx] + 1
                ):
                    track_rad[i] = track_rad[mirror_idx]

            while 0 <= i - track_rad[i] and i + track_rad[i] < len(s):
                if s[i - track_rad[i]] == s[i + track_rad[i]]:
                    track_rad[i] += 1
                else:
                    break

            if not cur_center or i + track_rad[i] > cur_center + track_rad[cur_center]:
                cur_center = i

        max_track = max(track_rad)
        idx_ans = track_rad.index(max_track)

        return "".join(
            list(
                filter(
                    lambda x: x != "#",
                    s[idx_ans - track_rad[idx_ans] : idx_ans - track_rad[idx_ans] + 1],
                )
            )
        )
