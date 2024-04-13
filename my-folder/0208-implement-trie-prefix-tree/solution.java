class TrieNode {
    
    public Map<Character, TrieNode> children;
    public boolean checked;

    public TrieNode() {
        children = new HashMap<>();
        checked = false;
    }

}

class Trie {

    private TrieNode parent;

    public Trie() {
        parent = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode curr = this.parent;
        for (char letter : word.toCharArray()) {
            if (!curr.children.containsKey(letter)) {
                curr.children.put(letter, new TrieNode());
            }
            curr = curr.children.get(letter);
        }
        curr.checked = true;
     }
    
    public boolean search(String word) {
        TrieNode curr = this.parent;
        for (char letter : word.toCharArray()) {
            if (!curr.children.containsKey(letter)) {
                return false;
            }
            curr = curr.children.get(letter);
        }
        return curr.checked;
    }
    
    public boolean startsWith(String prefix) {
        TrieNode curr = this.parent;
        for (char letter : prefix.toCharArray()) {
            if(!curr.children.containsKey(letter)) {
                return false;
            }
            curr = curr.children.get(letter);
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
