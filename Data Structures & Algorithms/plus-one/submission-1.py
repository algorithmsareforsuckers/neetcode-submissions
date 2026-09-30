class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for n in range(1, len(digits)+1):
            nc = (digits[-n] + carry) // 10
            digits[-n] = (digits[-n] + carry) % 10
            carry = nc
        
        if carry == 1:
            return [1] + digits
        return digits