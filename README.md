QNO.1
Write a Python program that takes a list of numbers and:
Print the numbers in the list but skip numbers that are divisible by 5.
Stops the loop if a number greater than 50 is encountered.

QNO.2
Write a Python program that takes a string as input and returns a new string where every alternate word is reversed while keeping the order of the words intact.
Example Input/Output:
Input: "Python is an amazing programming language"
Output: "Python si an gnizama programming egaugnal” 

QNO.3
Write a Python program that takes a list of words and finds all words that appear more than once, storing them in a dictionary with their frequency count.
Example Input/Output:
Input: ["apple", "banana", "apple", "orange", "banana", "banana"]
Output: {'apple': 2, 'banana': 3}

QNO.4
Create a dictionary called books where the keys are book titles (strings) and the values are the number of copies available for each book (integers). 
For example:
books = {
    'Book1': 5,
    'Book2': 6,
    'Book3': 10,  # You can add more books
}

Write a Python program that does the following:
Prompts the user to enter the name of the book they want.
Prompts the user to enter the number of copies they want to buy.
Checks if the book exists in the books dictionary.
Prints the following messages based on availability:
- "Available": If the book is in the dictionary and there are enough copies to fulfill the user's request.
- "Partially Available": If the book is in the dictionary, but there are fewer copies than the user wants.
- "Unavailable": If the book is not in the dictionary.
Important: Your program should handle the case where the user might enter something that is not a valid number of copies (e.g., letters, a blank input). Provide a clear message to the user if this happens and ask for number of copies again if the input by user is not an integer type



QNO.5
Write a program in python which takes a list of words as input and store the frequency of each word in dictionary  
Input [“This”,”is”,”good”,”is”]
Output {“this”:1,”is”:2}


QNO.6
Write a function largest_word(sentence) that takes a sentence as input and returns the longest word in the sentence. If there are multiple words of the same length, return the first one that appears.
Hint: Split the sentence into words using .split(), then compare the lengths of the words to find the longest one.
largest_word("Python programming is awesome") 
# Output: "programming"

QNO.7  
Write a function to_title_case(sentence) that takes a sentence as input and returns the sentence in title case, where the first letter of each word is capitalized.

to_title_case("hello world from python") 
# Output: "Hello World From Python"
