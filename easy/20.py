# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/

def isValid(s):
    paranthesis_dict = {'(': ')', '{': '}', '[': ']'}
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

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("[{}]"))