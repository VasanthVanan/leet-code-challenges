# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/description/

def function(inputs):
    str_1 = inputs[0]
    str_2 = inputs[1]
    letter_hash = {}

    if(len(str_1)!= len(str_2)):
        return False
    
    if(len(str_1) <= 1 or len(str_2) <= 1):
        return True

    # iterate through the strings
    for i in range(len(str_1)):

        # check the hash value is not equal to the current character
        if((str_1[i] in letter_hash and letter_hash[str_1[i]] != str_2[i]) or (str_1[i] == str_2[i])):
            return False
        
        # check if the character is not present in the hash
        if(str_1[i] not in letter_hash):
            letter_hash[str_1[i]] = str_2[i]

    return True


# Test Case 1
input_1 = ["egg","add"] 
expected_output_1 = True
assert function(input_1) == expected_output_1, f"Test Case 1 Failed"

# Test Case 2
input_2 = ["foo", "bar"]
expected_output_2 = False
assert function(input_2) == expected_output_2, f"Test Case 2 Failed"

# Test Case 3
input_3 = ["paper", "title"]
expected_output_3 = True
assert function(input_3) == expected_output_3, f"Test Case 3 Failed"

# Test Case 4
input_4 = ["badc", "baba"]
expected_output_4 = False
assert function(input_4) == expected_output_4, f"Test Case 4 Failed"

print("All test cases passed!")