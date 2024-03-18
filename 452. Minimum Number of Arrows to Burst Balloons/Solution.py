class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrow = 1
        points.sort(key=lambda x: x[0])
        end = points[0][1]
        for balloon in points[1:]:
            if balloon[0] > end:
                arrow += 1
                end = balloon[1]
            else:
                end = min(balloon[1], end)
        return arrow
