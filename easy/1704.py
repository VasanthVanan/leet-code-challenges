# 1704. Determine if String Halves Are Alike
# https://leetcode.com/problems/determine-if-string-halves-are-alike/description/ 

def function(s):
    dicts = {'a', 'e', 'i', 'o', 'u'}
    a_count, b_count = 0, 0

    s = s.lower()

    # split the string into two halves
    a = s[:len(s)//2]
    b = s[len(s)//2:]

    for i,j in zip(a,b):
        # count the number of vowels in each half
        if i in dicts: a_count += 1
        if j in dicts: b_count += 1

    # return True if the number of vowels in each half is equal
    return True if b_count == a_count else False

# Test Case 1
input_1 = "book"
expected_output_1 = True

# Test Case 2
input_2 = "textbook"
expected_output_2 = False

# Test Case 3
input_3 = "MerryChristmas"
expected_output_3 = False

try:
    assert function(input_1) == expected_output_1, f"Test Case 1 Failed"
    assert function(input_2) == expected_output_2, f"Test Case 2 Failed"
    assert function(input_3) == expected_output_3, f"Test Case 3 Failed"
    print("\033[92m All test cases passed!\033[0m")
except AssertionError as e:
    print("\033[91m Error: {}\033[0m".format(e))