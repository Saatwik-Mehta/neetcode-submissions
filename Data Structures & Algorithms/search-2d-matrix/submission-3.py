class Solution:
    def findCoords(self, index, col):
        # Assuming, that we are treating the multi-dimensional array as a 1D array
        # we need to calculate it's actual coords for the given index.
        # To calculate that we need to the index in the 1D array (hypothetical),
        # and calculate indeces of the 2D array
        # row ->> index//col
        # col ->> index%col
        return (index//col, index%col)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        l = 0
        r = (n * m) - 1
        
        while l <= r:
            mid = (l + r)//2
            row, col = self.findCoords(mid, m)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False