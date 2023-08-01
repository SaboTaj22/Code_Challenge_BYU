#CHALLENGE 1
#Find out if two sentences are anagrams.

#EXPLANATION OF SOLUTION
# They are anagrams given that they are the same letters, just rearranged.
# You solve this by first removing the spaces.
# Then you loop through the strings and compare the lengths using a for loop.
# If they are actually anagrams, then I would write a conditional statement with the boolean value of true for similar length, and false for different lengths.
# I would then pass those phrases into a dictionary to compare the character counts. If the dictionaries are equal, then the phrases are anagrams.

# def are_anagrams(phrase1, phrase2):
#     # Remove spaces and convert to lowercase
#     phrase1 = phrase1.replace(" ", "").lower()
#     phrase2 = phrase2.replace(" ", "").lower()
#
#     # Check if the lengths are equal
#     if len(phrase1) != len(phrase2):
#         return False
#
#     # Convert the phrases to dictionaries with character counts
#     char_count1 = {}
#     char_count2 = {}
#     for char in phrase1:
#         char_count1[char] = char_count1.get(char, 0) + 1
#     for char in phrase2:
#         char_count2[char] = char_count2.get(char, 0) + 1
#
#     # Check if the dictionaries are equal
#     return char_count1 == char_count2
#
# # Test with the given phrases
# phrase1 = "Tom Marvolo Riddle"
# phrase2 = "I am Lord Voldemort"
#
#
# if are_anagrams(phrase1, phrase2):
#     print("The phrases are anagrams.")
# else:
#     print("The phrases are not anagrams.")

#Challenge 2
# Find the length of the last word in a string

#EXPLANATION OF SOLUTION
#To solve for this problem I would create a function where you pass in the sentence you would like to get the length of the last word.
# I would then remove the spaces within the sentence and split the string into a list of words.
# You can retrieve the last word by using len(word[-1]). This retrieves the last elements length within the list.
# You would then return this value as the output.


# def length_of_last_word(s):
#     # Remove trailing spaces
#     s = s.rstrip()
#
#     # Split the string by spaces
#     words = s.split()
#
#     # Check if there are any words
#     if not words:
#         return 0
#
#     # Return the length of the last word
#     return len(words[-1])
#
#
# # Test the function
# sentence = "Hello, how are you?"
# print(length_of_last_word(sentence))  # Output: 4 (last word is "you?")


#CHALLENGE 3
# Given an array of numbers, find the lowest and highest values.

#EXPLANATION OF SOLUTION
# To solve for this problem, I would first create a function that takes in the array of numbers as an input.
# I would then create two variables, "highest" and "lowest", indicating the highest and lowest value starting with the first value within the array.
# Using a for loop, you can then iterate through the array and compare each value with the "highest" and "lowest" value variables with conditional statements.
# After iterating through the array, you will be left with the lowest and highest values of which you can return as an output.

def find_lowest_and_highest(arr):
    if not arr:
        return None, None  # If the array is empty, return None for both min and max

    min_val = arr[0]  # Initialize min_val with the first element of the array
    max_val = arr[0]  # Initialize max_val with the first element of the array

    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    return min_val, max_val

# Test the function
numbers = [4, 1, 7, -3, 9, 5]
lowest, highest = find_lowest_and_highest(numbers)
print("Lowest value:", lowest)
print("Highest value:", highest)
