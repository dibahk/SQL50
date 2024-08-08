class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
        r, c = rStart, cStart
        step = 1
        i = 0
        ans = []
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while len(ans) < rows* cols:
            for _ in range(2): #every 2 times the step should be increased by 1
                dr, dc = directions[i]
                for _ in range(step):
                    if (0 <= r < rows and 0 <= c < cols):
                        ans.append([r, c])    
                    r += dr
                    c += dc
                i = (i+1)%4
            step += 1
        return ans
