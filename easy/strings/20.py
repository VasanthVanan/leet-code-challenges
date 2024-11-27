# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/

def function(s):
    paranthesis_dict = { '(' : ')', '[' : ']', '{' : '}'}
    stack = []
    comparer = ''

    if not s:
        return False
    
    for i in s:
        
        # if the current character is a closing paranthesis, pop the last character from the stack
        if(comparer and i == comparer[-1]):
            stack.pop()
            comparer = comparer[:-1]
        else:
            stack.append(i)
            if(paranthesis_dict.get(i, None) == None):
                return False
            comparer += paranthesis_dict[i] # set the comparer to the current character
    
    # if the stack is empty and the comparer is empty, return true
    if(len(stack) == 0 and comparer == ''):
        return True
    else:
        return False


# Test Case 1
input_1 = "()"
expected_output_1 = True

# Test Case 2
input_2 = "()[]{}"
expected_output_2 = True

# Test Case 3
input_3 = "(]"
expected_output_3 = False

# Test Case 4
input_4 = "[{}]"
expected_output_4 = True

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    assert function(input_4) == expected_output_4, f'Test Case 4 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))