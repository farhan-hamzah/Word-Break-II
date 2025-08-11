from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)  # biar lookup lebih cepat
        memo = {}

        def dfs(start):
            # Kalau sudah sampai akhir string, kembalikan list kosong (menandakan akhir kalimat)
            if start == len(s):
                return [""]

            if start in memo:
                return memo[start]

            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    rest_sentences = dfs(end)
                    for sentence in rest_sentences:
                        if sentence:  # kalau bukan string kosong
                            sentences.append(word + " " + sentence)
                        else:
                            sentences.append(word)

            memo[start] = sentences
            return sentences

        return dfs(0)
