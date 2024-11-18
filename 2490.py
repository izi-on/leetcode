class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        for i in range(len(words)):
            prev_word = i - 1
            next_word = (i + 1) % len(words)
            if (
                words[prev_word][-1] != words[i][0]
                or words[i][-1] != words[next_word][0]
            ):
                return False
        return True
