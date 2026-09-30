class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        dim = len(matrix)
    
        # Left and right boundaries for the current ring
        l, r = 0, dim - 1
        
        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                
                top_left = matrix[top][l + i]
                matrix[top][l + i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = top_left
                
            # Move inward to the next ring
            l += 1
            r -= 1