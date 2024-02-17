# 2325. Decode the Message
# https://leetcode.com/problems/decode-the-message/description/ 

def function(inputs):
    key, message = inputs[0], inputs[1]
    # create a hashmap of unique alphabets with their corresponding indices
    hashmap, counter = {}, 0
    for character in key:
        if character not in hashmap and character.isalpha():
            hashmap[character] = counter
            counter += 1

    # iterate every character of cipher and find the corresponding character in hashmap
    # if the character is not in the hashmap, then it is a space
    decoded = ""
    for character in message:
        if character in hashmap:
            decoded += chr(hashmap[character] + 97)
        else:
            decoded += " "
    return decoded

# Test Case 1
input_1 = ["the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"]
expected_output_1 = "this is a secret"

# Test Case 2
input_2 = ["eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"]
expected_output_2 = "the five boxing wizards jump quickly"

# Test Case 3
input_3 = []
expected_output_3 = []

try:
    assert function(input_1) == expected_output_1, f"Test Case 1 Failed"
    assert function(input_2) == expected_output_2, f"Test Case 2 Failed"
    #assert function(input_3) == expected_output_3, f"Test Case 3 Failed"
    print("\033[92m\nAll test cases passed!\n\033[0m")
except AssertionError as e:
    print("\033[91m\nError: {}\033[0m".format(e))