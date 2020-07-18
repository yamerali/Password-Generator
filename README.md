# Password-Generator

Password vulnerabilities consist of an array of guessing attacks, such as observing the target, brute force guessing, etc.

Most passwords fall under one of two categories, each with their own pros and cons.

The first are passwords with personal information, such as a childs name and birthdate or phone number (or any combination of this information). These passwords may be easy to remember, but it can also be easy for an attacker to guess these passwords, either by observing or researching the target.

EXAMPLES = {Micheal0432, 1January1900, MyDog123}

The second type are random passwords consisting of different character types. Although these passwords are much harder to guess by any means, they are also much harder for a user to remember which means they will often be written down on paper, which is a huge vulnerability.

EXAMPLE = R(@#asdruEq

I believe that the best password is a combination of these two types, consisting of easy to remember words or phrases but also including characters of different types (upper and lower case letters, numbers, and symbols). The password should also be suffeciently long such that it is difficult to be guessed by bruteforce attacks.

My criteria for a strong password is as follows:
• Be at least 8 characters long
• Include at least one of each of the following: uppercase letter, lowercase letter, number, symbol.
• Be easily ”readable” so that it is easy to remember and users wont need to write it down. (i.e. ”H3[p” could be pronounced ”HELP”)

The way my password generator works is by asking the user for a desired length and then selecting an english word from the dictionary (my program only chooses from 20 words, but it can be easily scaled by using a larger set of words). The program then randomly swaps some letters from the word for other characters that look like the letter, examples for the letter ”a” are @ and A. After the characters have been swapped, the program will check if the criteria for characters has been met (does it include at least one of each), if not it will add the required characters. The program then checks for length requirements. If the password is too short, then random characters are added to the password. If the password is too long, then random characters are removed from the password. The program then checks again to see if the password contains all the characters. I would improve this in the future by appending more words together to meet the length requirement for words that are too short, but this would require a wider range of words to choose from.

SAMPLE OUTPUT
Enter a length for password (>= 8): 8
deadwood
D3@d/o0d

NOTE
This is a proof of concept for generating strong passwords. If I ever use this in a project I would optimize the code and increase the dictionary size as well as the symbols available to swap.
