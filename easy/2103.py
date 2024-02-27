# 2103. Rings and Rods
# https://leetcode.com/problems/rings-and-rods/description/ 

def function(s):
    hashmap, result = {}, 0
    # iterate every pair incrementing by 2
    for i in range(0,len(s), 2):
        # add the pair to the hashmap if it doesn't exist
        if s[i+1] not in hashmap:
            hashmap[s[i+1]] = s[i]
        # if the pair exists, append the new letter to the existing pair
        else:
            hashmap[s[i+1]] = hashmap[s[i+1]] + s[i]
    
    # iterate through the hashmap and check if 'B', 'G', 'R' is present in the hashmap
    for key in hashmap:
        if all(x in hashmap[key] for x in 'BGR'):
            # increment the result 
            result += 1
    
    return result

# Test Case 1
input_1 =  "B0B6G0R6R0R6G9"
expected_output_1 = 1

# Test Case 2
input_2 = "B0R0G0R9R0B0G0"
expected_output_2 = 1

# Test Case 3
input_3 = "G4"
expected_output_3 = 0

# Test Case 4
input_4 = "G3R3R7B7R5B1G8G4B3G6"
expected_output_4 = 1

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    assert function(input_4) == expected_output_4, f'Test Case 4 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))