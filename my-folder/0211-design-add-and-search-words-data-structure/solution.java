class WordDictionary {

    WordDictionary[] children;
    boolean check;

    public WordDictionary() {
        children = new WordDictionary[26];
        check = false;
    }
    
    public void addWord(String word) {
        WordDictionary current = this;
        for (char c : word.toCharArray()) {
            if (current.children[c - 'a'] == null) {
                current.children[c - 'a'] = new WordDictionary();
            }
            current = current.children[c - 'a'];
        }
        current.check = true;
    }
    
    public boolean search(String word) {
        WordDictionary current = this;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (c == '.') {
                for (WordDictionary child : current.children) {
                    if (child != null && child.search(word.substring(i+1, word.length()))) {
                        return true;
                    }
                }
                return false;
            }
            else {
                if (current.children[c - 'a'] == null) {
                    return false;
                }
            }
            current = current.children[c - 'a'];
        }
        return current != null && current.check;
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */
