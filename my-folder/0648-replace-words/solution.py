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
        for i in range(len(word)):
            c = word[i]
            if not current.children[ord(c) - ord('a')]:
                return word
            current = current.children[ord(c) - ord('a')]
            if current.isEnd:
                return word[:i+1]
        
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        arr = sentence.split(" ")
        root = Trie()
        for word in dictionary:
            root.insert(word)
        
        for word in range(len(arr)):
            arr[word] = root.shortest_path(arr[word])
        
        return " ".join(arr)
