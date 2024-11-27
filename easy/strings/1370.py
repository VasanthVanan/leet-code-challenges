# 1370. Increasing Decreasing String
# https://leetcode.com/problems/increasing-decreasing-string/description/

def function(inputs):
    def append(hashmap, order):
        appended = ""
        for i in sorted(hashmap.keys(), reverse=order):
            if(hashmap[i]): 
                appended += i
                hashmap[i] = int(hashmap[i]) - 1
        return [appended, hashmap]
    # create a dictionary of letters and their corresponding values
    hashmap = {}
    strings = ""
    for i in inputs:
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] += 1
    while(sum(list(hashmap.values()))):
        # append ASCII characters to the string in ascending order
        temp, hashmap = append(hashmap, False)
        strings += temp
        # append ASCII characters to the string in descending order
        if(sum(list(hashmap.values()))):
            temp, hashmap = append(hashmap, True)
            strings += temp
    return strings


# Test Case 1
input_1 = "aaaabbbbcccc"
expected_output_1 = "abccbaabccba"

# Test Case 2
input_2 = "rat"
expected_output_2 = "art"

# Test Case 3
input_3 = "leetcode"
expected_output_3 = "cdelotee"

try:
    assert function(input_1) == expected_output_1, f'Test Case 1 Failed'
    assert function(input_2) == expected_output_2, f'Test Case 2 Failed'
    assert function(input_3) == expected_output_3, f'Test Case 3 Failed'
    print('\033[92m All test cases passed! \033[0m')
except AssertionError as e:
    print('\033[91m Error: {}\033[0m'.format(e))