class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        Use backtracking approach explore all possibilities of partitioning string
        Optimize the palindrome checking process by precomputing whether substrings are palindrome
        1. Create a 2D list dp where dp[i][j] denotes whether s[i][j+1] is a palindrome
        2. All single char are palindromes so dp[i][i] = True
        3. For substring of length 2 set dp[i][i+1] to True if s[i] == s[i+1]
        4. For longer one check if s[i] == s[j] and dp[i+1][j-1] = True
        5. Write backtring function with the base case as start index == len(s)
        6. Iterate over all possible positions from start to len(s), for each one use precomputed dp table to check if s[start:end+1] is a palindrome
        7. If it is, continue backtrack 
        '''

        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
        
        for length in range(2, n+1): # Length of substring
            for i in range(n - length + 1):
                j = i + length - 1 # Calculate the end index
                if s[i] == s[j]:
                    if length == 2 or dp[i+1][j-1]:
                        dp[i][j] = True
        
        def backtrack(start, path):
            if start == n:
                result.append(path[:])
                return
            for end in range(start, n):
                if dp[start][end]:
                    backtrack(end + 1, path + [s[start:end+1]])

        result = []
        backtrack(0, [])
        return result
                    
