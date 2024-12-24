# 2469. Convert the Temperature
# https://leetcode.com/problems/convert-the-temperature/description/ 

def function(input):
    # return kelvin + fahrenheit
    return [input + 273.15, (input * 1.80) + 32]

# Test Case 1
input_1 = 36.50
expected_output_1 = [309.65000,97.70000]

# Test Case 2
input_2 = 122.11
expected_output_2 = [395.26000,251.79800]

# Test Case 3
input_3 = []
expected_output_3 = []

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    #assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))