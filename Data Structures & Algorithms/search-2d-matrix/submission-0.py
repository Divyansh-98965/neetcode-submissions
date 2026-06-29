class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Brute force solution
        for i in matrix:
            for j in i:
                if j == target :
                    return  True
                    
        return False 

        
        
        #traverse the array
        """let's start with an idea that the array is sorted so 
        let's get the last element of each subbarry if it is less than target 
        look for last element in next array if it is greater than target look 
        in that array """ 

