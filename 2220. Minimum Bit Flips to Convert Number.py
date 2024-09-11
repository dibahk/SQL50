class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        bg = list(bin(goal)[2:])
        bs = list(bin(start)[2:])
        count = 0
        if goal > start:
            for _ in range(len(bg)-len(bs)):
                bs.insert(0, '0')
        else:
            for _ in range(len(bs)-len(bg)):
                bg.insert(0, '0')

        bg.reverse()
        bs.reverse()

        for i in range(len(bg)):
            if bg[i] != bs[i]:
                count+=1
                bs[i] = bg[i]
            if bg == bs:
                break
        return count
