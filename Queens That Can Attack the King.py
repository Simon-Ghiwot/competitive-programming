class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        result = []
        directions = [[0,-1],[0,1],[-1,0],[1,0],[-1,-1],[1,-1],[-1,1],[1,1]]

        for direction in directions:
            row, col = king[0], king[1]

            while row >= 0 and col >= 0 and row < 8 and col < 8:
                current = [row, col]
                if current in queens:
                    result.append(current)
                    break
                row += direction[0]
                col += direction[1]

        return result
