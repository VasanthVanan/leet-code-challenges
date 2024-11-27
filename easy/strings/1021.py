# 1021. Remove Outermost Parentheses
# https://leetcode.com/problems/remove-outermost-parentheses/description/ 

def function(inputs):
    opened, prev, flag = 0, 0, False
    result = ""
    for i, char in enumerate(inputs):
        # if we have opened parentheses, then we need to keep track of it
        if char == '(':
            opened += 1
            # if we have opened parentheses and we have not seen a closing parentheses yet, then we need to keep track of it
            if(opened >= 2 and not flag):
                flag = True
        else:
            # if we have a closing parentheses, then we need to keep track of it
            opened -= 1

        # if we have closed all the opened parentheses, then we need to add the substring to the result
        if(opened == 0 and flag):
            result += inputs[prev+1: i]
            prev, flag = i + 1, False
        # if we have not closed all the opened parentheses, then we need to keep track of the previous index
        elif(opened == 0 and not flag):
            prev = i + 1
    
    return result

# Test Case 1
input_1 = "(()())(())"
expected_output_1 = "()()()"

# Test Case 2
input_2 = "(()())(())(()(()))"
expected_output_2 = "()()()()(())"

# Test Case 3
input_3 = "()()"
expected_output_3 = ""

# Test Case 4
input_4 = "()()()()(())"
expected_output_4 = "()"

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))