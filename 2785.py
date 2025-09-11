class Solution:
    def sortVowels(self, s: str) -> str:
        def is_vowel(c):
            # print(c)
            return c.lower() in ["a", "e", "i", "o", "u"]

        def is_consonant(c):
            return not is_vowel(c) and c.isalpha()

        vowels = sorted(list(filter(lambda x: is_vowel(x), s)), key=lambda x: ord(x))[
            ::-1
        ]
        # print(vowels)
        t = [c if is_consonant(c) else None for c in s]
        for i, c in enumerate(t):
            if t[i] is None:
                t[i] = vowels.pop()
        return "".join(t)
