# 1859. Sorting the Sentence
# https://leetcode.com/problems/sorting-the-sentence/description/

def function(inputs):
    if(inputs):
        # split the string into a list of strings and a list of indices
        index_list = (list(filter(str.isdigit, inputs)))
        str_list = [c[:-1] for c in inputs.split()]

        # create a hash map of indices and strings
        hashmap = (dict(zip(index_list, str_list)))

        # return the sorted string
        return (' '.join([ hashmap[str(i)] for i in range(1,len(str_list)+1)]))


# Test Case 1
input_1 = "is2 sentence4 This1 a3"
expected_output_1 = "This is a sentence"

# Test Case 2
input_2 = "Myself2 Me1 I4 and3"
expected_output_2 = "Me Myself and I"

# Test Case 3
# input_3 = []
# expected_output_3 = []
# assert function(input_3) == expected_output_3, f"Test Case 3 Failed"

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    # assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))