# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/description/

def function(inputs):
    str_1 = inputs[0]
    str_2 = inputs[1]
    letter_hash = {}

    # iterate through the strings
    for i in range(len(str_1)):
        # check if the character is not present in the hash
        if(str_1[i] not in letter_hash):
            letter_hash[str_1[i]] = str_2[i]
        # check the hash value is not equal to the current character
        elif(str_1[i] in letter_hash and letter_hash[str_1[i]] != str_2[i]):
            return False

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

print("All test cases passed!")