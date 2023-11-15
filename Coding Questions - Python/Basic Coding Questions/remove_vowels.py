"""
remove small letters vowels from a statement, capital letters vowels should remain
input_str = "I love coding in python"
output_str = "I lv cdng n pythn"

"""



input_str = "I love coding in python"





## Method 2

import re

result2 = re.sub(r'[aeiou]', '', input_str)
print("result from method2 = ", result2)




## My Method
vowels = "aeiou"
for i in vowels:
    if i in input_str:
        input_str = input_str.replace(i, "")
print("result from My method = ", input_str)