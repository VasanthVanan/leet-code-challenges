# 1021. Remove Outermost Parentheses
# https://leetcode.com/problems/remove-outermost-parentheses/description/ 

def function(inputs):
    opened, prev, flag = 0, 0, False
    result = ""
    for i, char in enumerate(inputs):
        if char == '(':
            opened += 1
            if(opened >= 2 and not flag):
                flag = True
        else:
            opened -= 1

        if(opened == 0 and flag):
            result += inputs[prev+1: i]
            prev, flag = i + 1, False
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
    assert function(input_1) == expected_output_1, f"Test Case 1 Failed"
    assert function(input_2) == expected_output_2, f"Test Case 2 Failed"
    assert function(input_3) == expected_output_3, f"Test Case 3 Failed"
    assert function(input_4) == expected_output_4, f"Test Case 4 Failed"
    print("\033[92m\nAll test cases passed!\n\033[0m")
except AssertionError as e:
    print("\033[91m\nError: {}\033[0m".format(e))