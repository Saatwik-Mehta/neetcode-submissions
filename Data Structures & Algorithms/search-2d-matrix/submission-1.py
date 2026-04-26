class Solution:

    def search_t_in_row(self, row, target):
        size = len(row)
        l = 0
        r = size - 1
        while l <= r:
            mid = (l + r)//2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
            
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if i[-1] < target:
                continue
            return self.search_t_in_row(i, target)
        return False