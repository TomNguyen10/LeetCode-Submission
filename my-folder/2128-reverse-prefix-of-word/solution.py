class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        pointer = -1
        for i in range(len(word)):
            if word[i] == ch:
                pointer = i
                break
        if pointer == -1:
            return word
        return word[:pointer+1][::-1] + word[pointer+1:]
