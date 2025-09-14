from collections import defaultdict


class Encrypter:
    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.keys = keys
        self.values = values
        self.dictionary = set(dictionary)
        self.map_c_to_key_idx = {}
        self.map_substr_to_possible_idx = defaultdict(list)
        for i, c in enumerate(keys):
            self.map_c_to_key_idx[c] = i
        for i, substr in enumerate(values):
            self.map_substr_to_possible_idx[substr].append(i)

    def encrypt(self, word1: str) -> str:
        enc_str = []
        for c in word1:
            i = self.map_c_to_key_idx[c]
            enc_str.append(self.values[i])
        return "".join(enc_str)

    def decrypt(self, word2: str) -> int:
        possibilities = []

        def helper(cur_word, at_idx):
            if at_idx == len(word2):
                possibilities.append("".join(cur_word))
                return
            poss_idx = self.map_substr_to_possible_idx[cur_word[at_idx : at_idx + 2]]
            for idx in poss_idx:
                cur_word.append(self.keys[idx])
                helper(cur_word, at_idx + 2)
                cur_word.pop()

        return len(list(filter(lambda poss: poss in self.dictionary, possibilities)))


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)
