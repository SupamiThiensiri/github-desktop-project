class Solution:

    def number_to_roman(self, number: int) -> str:
        if number <= 0:
            return "number can not less than 0"
        
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        
        roman_text = ""
        i = 0
        
        while number > 0:
            for _ in range(number // val[i]):
                roman_text += syb[i]
                number -= val[i]
            i += 1
        
        return roman_text

# ตัวอย่างการใช้งาน:
solution = Solution()

print(solution.number_to_roman(12))  # Output: "CI"
print(solution.number_to_roman(-1))   # Output: "number can not less than 0"
