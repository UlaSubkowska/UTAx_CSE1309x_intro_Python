Assignment2 from: Introduction to Programming Using Python (UTAx: CSE1309x) edx

In this assignment you are asked to write a spell checker (corrector). This assignment includes 3 parts. In the first part you are asked to write a function to to compare two strings and return 0 if they match, return 1 if they mismatch in one character and return 2 if they mismatch by more than one character.
In the second part you are asked to write a function to check if a string can match another string by either inserting or deleting a character.
In the third part you are asked to write a function to correct spelling of a string (sentence) by using a list of correct words. This third function uses the first two functions as helper functions. 


1. Write a function named find_mismatch that accepts two strings as input arguments and returns:
    0 if the two strings match exactly.
    1 if the two strings have the same length and mismatch in only one character.
    2 if the two strings do not have the same length or mismatch in two or more characters.
Capital letters are considered the same as lower case letters. 

2.  Write a function named single_insert_or_delete that accepts two strings as input arguments and returns:
    0 if the two strings match exactly.
    1 if the first string can become the same as the second string by inserting or deleting a single character. Notice that inserting and deleting a character is not the same as replacing a character.
    2 otherwise
Capital letters are considered the same as lower case letters.

3.  Write a function named spelling_corrector that accepts two arguments. The first argument is a sentence (string) and the second argument is a list of words (correct_spells). Your function should check each word in the input string against all the words in the correct_spells list and return a string such that:
    If a word in the original sentence matches exactly with a word in the correct_spells then the word is not modified and it should be directly copied to the output string.
    if a word in the sentence can match a word in the correct_spells list by replacing, inserting, or deleting a single character, then that word should be replaced by the correct word in the correct_spelled list.
    If neither of the two previous conditions is true, then the word in the original string should not be modified and should be directly copied to the output string.
Notes:
    Do not spell check one or two letter words (copy them directly to the output string).
    In case of a tie use the first word from the correct_spelled list.
    Ignore capitalization, i.e. consider capital letters to be the same as lower case letters.
    All characters in the output string should all be in lower case letters.
    Assume that the input string only includes alphabetic characters and spaces. (a-z and A-Z)
    Remove extra spaces between the words.
    Remove spaces at the start and end of the output string.