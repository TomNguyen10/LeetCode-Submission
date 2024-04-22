class TrieNode {

    Map<Character, TrieNode> children;
    boolean check;

    public TrieNode() {
        children = new HashMap<>();
        check = false;
    }

}


class Trie {

    TrieNode parent;

    public Trie() {
        parent = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode current = this.parent;
        for (char c : word.toCharArray()) {
            if (!current.children.containsKey(c)) {
                current.children.put(c, new TrieNode());
            }
            current = current.children.get(c);
        }
        current.check = true;
    }
    
    public boolean search(String word) {
        TrieNode current = this.parent;
        for (char c : word.toCharArray()) {
            if (!current.children.containsKey(c)) {
                return false;
            }
            current = current.children.get(c);
        }
        return current.check;
    }
    
    public boolean startsWith(String prefix) {
        TrieNode current = this.parent;
        for (char c : prefix.toCharArray()) {
            if (!current.children.containsKey(c)) {
                return false;
            }
            current = current.children.get(c);
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
