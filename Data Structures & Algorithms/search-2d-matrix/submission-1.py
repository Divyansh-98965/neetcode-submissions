class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # #Brute force solution
        # for i in matrix:
        #     for j in i:
        #         if j == target :
        #             return  True
                    
        # return False
        #optimize solution
        """let's start with an idea that the array is sorted so 
        let's get the last element of each subbarry if it is less than target 
        look for last element in next array if it is greater than target look 
        in that array """ 
        left1 = 0
        right1 = len(matrix) - 1 
        
        while left1 <= right1:
            mid1 = left1 + ((right1 - left1)//2)
            left2 = 0
            right2 = len(matrix[mid1]) - 1
            
            if matrix[mid1][right2] == target:
                return True

            elif matrix[mid1][right2] < target:
                left1 = mid1 + 1

            elif matrix[mid1][right2] > target:
                if matrix[mid1][left2] == target:
                    return True
                
                elif matrix[mid1][left2] < target:
                    while left2 <= right2:
                        mid2 = left2 +((right2 - left2)//2)
                        if matrix[mid1][mid2] == target:
                            return True

                        elif matrix[mid1][mid2] < target:
                            left2 = mid2 + 1

                        elif matrix[mid1][mid2] > target:
                            right2 = mid2 - 1

                right1 = mid1 - 1

        
        return False

            