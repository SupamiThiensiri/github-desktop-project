class Solution:

    def number_to_thai(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        
        if number == 0:
            return "ศูนย์"
        
        units = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
        positions = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]
        
        result = ""
        str_num = str(number)
        length = len(str_num)

        for i in range(length):
            digit = int(str_num[i])
            pos = length - i - 1
            
            if pos == 1 and digit == 1:
                result += "สิบ"
            elif pos == 1 and digit == 2:
                result += "ยี่สิบ"
            elif pos == 0 and digit == 1 and length > 1:
                result += "เอ็ด"
            else:
                result += units[digit]
                if digit != 0:
                    result += positions[pos]
        
        return result

# ตัวอย่างการใช้งาน:
solution = Solution()

print(solution.number_to_thai(101))  # Output: "หนึ่งร้อยเอ็ด"
print(solution.number_to_thai(-1))   # Output: "number can not less than 0"
