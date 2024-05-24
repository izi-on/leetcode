from collections import defaultdict


class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        letter_freq = defaultdict(int)
        for letter in letters:
            letter_freq[letter] += 1

        word_score = {}
        for word in words:
            # get score of cur word
            cur_score = 0
            for letter in word:
                cur_score += score[ord(letter) - ord("a")]
            word_score[word] = cur_score

        max_score = 0

        def helper(idx, cur_freq, cur_score):
            nonlocal max_score, letter_freq, word_score
            if idx == len(words):
                # print("got to end of word, cur score is", cur_score)
                max_score = max(max_score, cur_score)
                return
            # print("skipping word", words[idx])
            helper(idx + 1, cur_freq, cur_score)

            # print("adding word", words[idx])
            # add to freq
            to_unroll = False
            for letter in words[idx]:
                cur_freq[letter] += 1
                if cur_freq[letter] > letter_freq[letter]:
                    # print("cannot add another", letter, "skipping")
                    # print(cur_freq, letter_freq)
                    to_unroll = True

            if to_unroll:
                # unroll
                for letter in words[idx]:
                    cur_freq[letter] -= 1
                return

            cur_score += word_score[words[idx]]

            helper(idx + 1, cur_freq, cur_score)

            # unroll
            for letter in words[idx]:
                cur_freq[letter] -= 1

        helper(0, defaultdict(int), 0)
        return max_score
