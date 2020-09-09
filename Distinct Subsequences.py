class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        def numDistinctTabulation(str1, str2, m, n):
            """
            str1 -> source str
            str2 -> target str
            m -> length of source str
            n -> length of target str            
            """
            table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

            for i in range(m + 1):
                for j in range(n + 1):
                    if j == 0:
                        table[i][j] = 1
                    elif i == 0:
                        table[i][j] = 0
                    else:
                        if str1[i - 1] == str2[j - 1]:
                            table[i][j] = table[i - 1][j] + table[i - 1][j - 1]
                        else:
                            table[i][j] = table[i - 1][j]
            return table[m][n]

        
        # return numDistinctRecursive(s, t, len(s), len(t))
        
        # memoize = [[None for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        # return numDistinctMemoization(s, t, len(s), len(t))
        
        return numDistinctTabulation(s, t, len(s), len(t))
