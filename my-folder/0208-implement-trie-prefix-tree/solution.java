class TrieNode {

    Map<Character, TrieNode> children;
    boolean isChecked;

    public TrieNode() {
        children = new HashMap<>();
        isChecked = false;
    }

}

class Trie {

    TrieNode parent;

    public Trie() {
        parent = new TrieNode();
    }
    
    public void insert(String word) {
        char[] arr = word.toCharArray();
        TrieNode current = this.parent;
        for (char c : arr) {
            if (!current.children.containsKey(c)) {
                current.children.put(c, new TrieNode());
            }
            current = current.children.get(c);
        }
        current.isChecked = true;
    }
    
    public boolean search(String word) {
        TrieNode current = this.parent;
        char[] arr = word.toCharArray();
        for (char c : arr) {
            if (!current.children.containsKey(c)) {
                return false;
            }
            current = current.children.get(c);
        }
        return current.isChecked;
    }
    
    public boolean startsWith(String prefix) {
       TrieNode current = this.parent;
        char[] arr = prefix.toCharArray();
        for (char c : arr) {
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
