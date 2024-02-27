# 1108. Defanging an IP Address
# https://leetcode.com/problems/defanging-an-ip-address/description/

import re 

def function(inputs):
    # check if the string contains any digits using regex
    if(re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', inputs)[0]):
        return inputs.replace('.','[.]')

# Test Case 1
input_1 = "1.1.1.1"
expected_output_1 = "1[.]1[.]1[.]1"

# Test Case 2
input_2 = "255.100.50.0"
expected_output_2 = "255[.]100[.]50[.]0"

# Test Case 3
input_3 = "51.74.12.208"
expected_output_3 = "51[.]74[.]12[.]208"

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))