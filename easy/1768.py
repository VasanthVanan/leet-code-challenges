# 1768. Merge Strings Alternately
# https://leetcode.com/problems/merge-strings-alternately/

def function(inputs):
    word1, word2 = inputs[0], inputs[1]
    len1, len2 = len(word1), len(word2)
    flag, merged = True, ""
    # iterate till any of the string length is zero
    while len1 or len2:
        # toggle flag to merge strings alternately
        if flag:
            merged += word1[0]
            word1 = word1[1:]
            len1 -= 1
            if len2 > 0: flag = False
        else:
            merged += word2[0]
            word2 = word2[1:]
            if len1 > 0: flag = True
            len2 -= 1
        
    return merged


# Test Case 1
input_1 = ["abc", "pqr"]
expected_output_1 = "apbqcr"

# Test Case 2
input_2 = ["ab","pqrs"]
expected_output_2 = "apbqrs"

# Test Case 3
input_3 = ["abcd", "pq"]
expected_output_3 = "apbqcd"

try:
    assert function(input_1) == expected_output_1, f"Test Case 1 Failed"
    assert function(input_2) == expected_output_2, f"Test Case 2 Failed"
    assert function(input_3) == expected_output_3, f"Test Case 3 Failed"
    print("All test cases passed!")
except AssertionError as e:
    print("Error: {}".format(e))