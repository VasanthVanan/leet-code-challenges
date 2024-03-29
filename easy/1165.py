# 1165. Single-Row Keyboard
# https://leetcode.com/problems/single-row-keyboard/description/

def function(inputs):
    keyboard, word = inputs[0], inputs[1]
    sum, prev = 0, 0
    for char in word:
        if char in keyboard:
            # if the character is in the keyboard, then we need to calculate the distance
            sum += abs(keyboard.index(char) - prev)
            prev = keyboard.index(char)
    return sum

# Test Case 1
input_1 = ["abcdefghijklmnopqrstuvwxyz", "cba"]
expected_output_1 = 4

# Test Case 2
input_2 = ["pqrstuvwxyzabcdefghijklmno", "leetcode"]
expected_output_2 = 73

# Test Case 3
# input_3 = []
# expected_output_3 = []

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    #assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))