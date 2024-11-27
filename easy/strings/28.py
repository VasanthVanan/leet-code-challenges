# 28. Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

def function(inputs):
    haystack, needle = inputs[0], inputs[1]
    haystack_length = len(haystack)
    needle_length = len(needle)

    # Naive Method
    if(haystack_length >= needle_length):
        for i in range(len(haystack)):
            if(haystack[i] == needle[0]):
                # check if the substring is the same
                sliced_str = haystack[i:i+needle_length]
                if(sliced_str == needle):
                    return i             
    
    return -1

    # Python Inbuilt Method
    # return haystack.find(needle)


# Test Case 1
input_1 = ["sadbutsad", "sad"]
expected_output_1 = 0

# Test Case 2
input_2 = ["leetcode", "leeto"]
expected_output_2 = -1

# Test Case 3
input_3 = ["a", "a"]
expected_output_3 = 0

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))