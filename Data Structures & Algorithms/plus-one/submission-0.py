class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        carry = 1
        for i, val in enumerate(digits):
            digits[i] = (val + carry) % 10
            if val + carry >= 10:
                carry = 1
            else:
                carry = 0
        if carry == 1:
            digits.append(1)
        return digits[::-1]