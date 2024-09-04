"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:

    def find_tailing_zeroes(self, number: int) -> int | str:
        if number < 0:
            return "number can not be negative"
        
        count = 0
        i = 5
        
        while number >= i:
            count += number // i
            print(count)
            i *= 5
            print(i)

        
        return count

# Example usage:
solution = Solution()

print(solution.find_tailing_zeroes(7))    # Output: 1
print(solution.find_tailing_zeroes(-10))  # Output: "number can not be negative"
