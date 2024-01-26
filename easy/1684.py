# 1684. Count the Number of Consistent Strings
# https://leetcode.com/problems/count-the-number-of-consistent-strings/description/

def function(inputs):

    def checkCharacter(allowed, word):
    # check if the character is in the allowed list
        for c in word:
            if c not in allowed:
                return False
        return True

    allowed, words = inputs[0], inputs[1]
    # iterate through the words and count the number of words that are consistent
    return len(list(filter(lambda x: checkCharacter(allowed, x), words)))


# Test Case 1
input_1 = ["ab",["ad","bd","aaab","baa","badab"]] 
expected_output_1 = 2
assert function(input_1) == expected_output_1, f"Test Case 1 Failed"

# Test Case 2
input_2 = ["abc",["a","b","c","ab","ac","bc","abc"]]
expected_output_2 = 7
assert function(input_2) == expected_output_2, f"Test Case 2 Failed"

# Test Case 3
input_3 = ["cad", ["cc","acd","b","ba","bac","bad","ac","d"]]
expected_output_3 = 4
assert function(input_3) == expected_output_3, f"Test Case 3 Failed"

print("All test cases passed!")