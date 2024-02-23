class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length=len(digits)
        power = 0
        value = 0
        for i in range(length - 1, -1, -1):  
            value += digits[i] * (10 ** power)
            power += 1
        value+=1
        digits.clear()
        while value>0:
            new_value=value%10
            digits.insert(0,new_value)
            value //=10
        return digits
        