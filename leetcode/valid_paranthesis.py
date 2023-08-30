"""
Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false



"""


class Solution:
    def isValid(self, s: str) -> bool:
        check_dict = {")" : "(", "}" : "{", "]" : "["}
        str_list = [i for i in s]
        print("Input str_list : {}".format(str_list))
        
        for i in str_list:
            print(f"i = {i}")
            if i in check_dict:
                str_list.remove(i)
                str_list.remove(check_dict[i])
            print()

        print("str_list : {}".format(str_list))
        if str_list:
            return "invalid"
        else:
            return "valid"





if __name__ == "__main__":
    s = """()[]{}"""
    test = Solution()
    print(test.isValid(s))