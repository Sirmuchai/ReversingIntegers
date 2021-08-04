"""
Given a signed 32-bit integer x, return x with its digits reversed.
 If reversing x causes the value to go outside the signed 32-bit 
 integer range [-231, 231 - 1], then return 0.
"""

class Solution:
    def reverse(self, x: int) -> int:
                
        if (pow(-2,31) >= x >=  (pow(2,31))):
            return 0
        else:            
            reversedValue =0
            if x < 0:
                x = abs(x)            
                temp_x = x
                while temp_x > 0:
                    reversedValue = reversedValue*10 + temp_x%10
                    temp_x//=10
                if reversedValue >=pow(2,31):
                    return 0
            
                return -reversedValue
            else:
                temp_x = x
                while temp_x >0:
                    reversedValue = reversedValue*10 + temp_x%10
                    temp_x//=10
                if reversedValue >=pow(2,31):
                    return 0                  
                return int(reversedValue)

test = Solution()
test.my_num = 12345
print(test.reverse(test.my_num))