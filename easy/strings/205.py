# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/description/

def function(inputs):
    mappings = {}
    # iterate two strings
    for a, b in zip(inputs[0], inputs[1]):
        
        # if new, insert it to hashmap
        if a not in mappings:
            mappings[a] = b  
        elif a in mappings and b != mappings[a]:  
                return False

    # check if values are unique with equal length
    return len(set(mappings.values())) == len(mappings.values())


# Test Case 1
input_1 = ["egg","add"] 
expected_output_1 = True

# Test Case 2
input_2 = ["foo", "bar"]
expected_output_2 = False

# Test Case 3
input_3 = ["paper", "title"]
expected_output_3 = True

# Test Case 4
input_4 = ["badc", "baba"]
expected_output_4 = False


try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    assert function(input_4) == expected_output_4, f"Test Case 4 Failed"
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))