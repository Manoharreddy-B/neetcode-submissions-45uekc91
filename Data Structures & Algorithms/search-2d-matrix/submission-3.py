class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # two recursions
        # 1st recursion I will find the row in which I need to search
        # 2nd recursion I will find the target in the row found in 1st recursion

        def findRow(start, end):
            if start > end:
                return None
            
            mid = (start + end)//2
            print(mid, start, end)
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                print(matrix[mid][0],matrix[mid][-1])
                return mid
            elif target < matrix[mid][0]:
                print("target < matrix[mid][0]",matrix[mid][0],matrix[mid][-1])
                return findRow(start, mid-1)
            elif target > matrix[mid][-1]:
                print("target > matrix[mid][-1]", matrix[mid][0],matrix[mid][-1])
                return findRow(mid+1, end)

        def checkTarget(rowIndex, start, end):
            print("entered")
            if start > end:
                return False

            mid = (start + end)//2
            print(target, matrix[rowIndex][mid])
            if target == matrix[rowIndex][mid]:
                print("matrix[rowIndex][mid]", target, matrix[rowIndex][mid])
                return True
            elif target >= matrix[rowIndex][mid]:
                print("target >= matrix[rowIndex][mid]",target, matrix[rowIndex][mid])
                return checkTarget(rowIndex, mid+1, end)
            elif target <= matrix[rowIndex][mid]:
                print("target <= matrix[rowIndex][mid]", target, matrix[rowIndex][mid])
                return checkTarget(rowIndex, start, mid-1)

        rowIndex = findRow(0,len(matrix)-1)
        
        return checkTarget(rowIndex, 0, len(matrix[rowIndex])-1) if rowIndex is not None else False

