# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/description/

def function(inputs):

    s = inputs[0][::-1] # reverse the string
    count = 0
    findCharacter = False

    # Naive Method
    for i in range(len(s)):
        if(s[i] != ' '):
            # check if the character is a letter
            findCharacter = True
        if(s[i] == ' ' and findCharacter):
            break
        if findCharacter: 
            count += 1

    return count

    # Python inbuilt Method
    # return [len(s.strip().split(' ')[-1])]


# Test Case 1
input_1 = ["Hello World"]
expected_output_1 = 5

# Test Case 2
input_2 = ["   fly me   to   the moon  "]
expected_output_2 = 4

# Test Case 3
input_3 = ["luffy is still joyboy"]
expected_output_3 = 6

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))