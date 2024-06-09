class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None] * 26
    

class Trie:
    def __init__(self):
        self.root = TrieNode()
    

    def insert(self, word):
        current = self.root
        for c in word:
            if not current.children[ord(c) - ord('a')]:
                current.children[ord(c) - ord('a')] = TrieNode()
            current = current.children[ord(c) - ord('a')]
        current.isEnd = True
    

    def shortest_path(self, word):
        current = self.root
        res = ""
        for c in word:
            if not current.children[ord(c) - ord('a')]:
                return word
            current = current.children[ord(c) - ord('a')]
            res += c
            if current.isEnd:
                return res
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = Trie()
        for word in dictionary:
            root.insert(word)
        arr = sentence.split(" ")
        for i in range(len(arr)):
            arr[i] = root.shortest_path(arr[i])
        return " ".join(arr) 
