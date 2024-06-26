class Solution {
    public int compress(char[] chars) {
        int anchor = 0, write = 0;
        
        for (int read = 0; read < chars.length; read++) {
            if (read + 1 == chars.length || chars[read + 1] != chars[read]) {
                chars[write] = chars[anchor];
                write++;
                if (read > anchor) {
                    for (char c : Integer.toString(read - anchor + 1).toCharArray()) {
                        chars[write] = c;
                        write++;
                    }
                }
                anchor = read + 1;
            }
        }
        return write;
    }
}
