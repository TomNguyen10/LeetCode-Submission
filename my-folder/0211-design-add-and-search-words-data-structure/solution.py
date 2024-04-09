class WordDictionary:

    def __init__(self):
        self.children = [None] * 26
        self.check = False


    def addWord(self, word: str) -> None:
        curr = self
        for letter in word:
            if not curr.children[ord(letter) - ord('a')]:
                curr.children[ord(letter) - ord('a')] = WordDictionary()
            curr = curr.children[ord(letter) - ord('a')]
        curr.check = True


    def search(self, word: str) -> bool:
        curr = self
        for i in range(len(word)):
            char = word[i]
            if char == '.':
                for child in curr.children:
                    if child and child.search(word[i+1:]):
                        return True
                return False
            if not curr.children[ord(char) - ord('a')]:
                return False
            curr = curr.children[ord(char) - ord('a')]

        return curr and curr.check

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
