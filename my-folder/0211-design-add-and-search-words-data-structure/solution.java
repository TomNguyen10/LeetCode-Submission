class WordDictionary {

    public WordDictionary[] children;
    public boolean end;

    public WordDictionary() {
        children = new WordDictionary[26];
        end = false;
    }
    
    public void addWord(String word) {
        WordDictionary current = this;
        for (char letter : word.toCharArray()) {
            if (current.children[letter - 'a'] ==  null) {
                current.children[letter - 'a'] = new WordDictionary();
            }
            current = current.children[letter - 'a'];
        }
        current.end = true;
    }
    
    public boolean search(String word) {
        WordDictionary current = this;
        for (int i = 0; i < word.length(); i++) {
            char letter = word.charAt(i);
            if (letter == '.') {
                for (WordDictionary child : current.children) {
                    if (child != null && child.search(word.substring(i+1, word.length()))) {
                        return true;
                    }
                }
                return false;
            }
            else {
                if (current.children[letter - 'a'] == null) {
                    return false;
                }
            }
            current = current.children[letter - 'a'];
        }
        return current != null && current.end;
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */
