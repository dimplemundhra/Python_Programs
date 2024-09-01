# Write a program to enter a string. Calculate the length of the string. Find the substring country. Count the occurences of each word in the given sentence.
# If the String as input is India is my motherland. I love my country. Capital of India is New Delhi.

def string_inp():
    str1="India is my motherland. I love my country. Capital of India is New Delhi"
    print("Length of string= ",len(str1))
    if 'country' in str1:
        print("'country' is present in the string")
    else:
        print("'country' is not present in the string")

    words=str1.split()
    word_count={}
    for word in words:
        word=word.strip(".,") #Remove Punctuations
        if word in word_count:
           word_count[word] +=1
        else:
           word_count[word]=1
    print("Word occurences:- ")
    for word,count in word_count.items():
        print(word,":",count)
string_inp()

# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically. 
# Suppose the following input is supplied to the program: without,hello,bag,world Then, the output should be: bag,hello,without,world.

def str_input():
    str= "without,hello,bag,world"
    words=str.split(',')    
    words.sort()
    sorted_words=(','.join(words))
    print(sorted_words)

str_input()

# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized. 
# Suppose the following input is supplied to the program: Hello world Practice makes perfectThen, the output should be:HELLO WORLD PRACTICE MAKES PERFECT

def upper_str():
    lines= [
        "Hello World", 
        "Practice makes perfect"
    ]
    upper_str1=[lines.upper() for line in lines]
    for line in upper_str1:
        print(line)
upper_str()                    #something is wrong in this snippet

#  Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again Then, the output should be:
# again and hello makes perfect practice world

def duplic_remove():
    str1="hello world and practice makes perfect and hello world again"
    str2=str1.split()
    uniq_str2=sorted(set(str2))
    result=' '.join(uniq_str2)
    print(result)

duplic_remove()

# # Write a program that accepts a sentence and calculate the number of letters and digits.Suppose the following input is supplied to the program:
# # hello world! 123 Then, the output should be:LETTERS 10 DIGITS 3

def letDig():
    inp_str= "hello world! 123"
    letters=sum(c.isalpha() for c in inp_str)
    digits=sum(c.isdigit() for c in inp_str)
    print(f"LETTERS= {letters}")
    print(f"DIGITS= {digits}")
letDig()

# # Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes" , otherwise print "No".

def str_check():
    str1=input("Enter a string: ")
    if str1.lower()== "yes":
        print("Yes")
    else:
        print("No")
str_check()

# Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only. Example:
# If the following words is given as input to the program:2 cats and 3 dogs. Then, the output of the program should be:
# ['2','3'].... In case of input data being supplied to the question, it should be assumed to be a console input.

def check_digs_only():
    str2="2 cats and 3 dogs"
    words=str2.split()
    dig_words= [word for word in words if word.isdigit()]
    print(dig_words)

# check_digs_only()

# write a program which count and print the numbers of each character in a string input by console. Example:
# If the following string is given as input to the program:
# abcdefgabc  Then, the output of the program should be:
# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1

def check_string():
    str1="abcdefgabc"
    char_count={}
    for char in str1:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
    for char,count in char_count.items():
        print(char,":",count)

# check_string()

# Write a program that accepts a string :-
# I. 1.reverses it.
# II. 2.checks whether it is a palindrome.
# III. 3.checks whether it ends with a specific substring.
# IV. 4.capitalize the first letter of each word in a string
# V. 5.check if a string is anagram of another string
# VI. 6.remove vowels from string
# VII. 7.find length of the longest word in a sentence

def string_commands():
    str3= "hello mummaa"
   # I
    rev_str=str3[ : :-1]
    print("Reversed String= ",rev_str)

    #II
    if(rev_str==str3):
        print(rev_str,"is a Palindrome string..")
    else:
        print(rev_str,"Is not a palindrome string..")

    #III
    str_substring = "Mummaa"
    ends_with_substring = str3.endswith(str_substring)
    print(f"Ends with '{str_substring}': {ends_with_substring}")

    #IV
    capitalized_string = str3.title()
    print(f"Capitalized sentence is : {capitalized_string}")

    #V
    new_str="aammum olleh"
    is_anagram=sorted(str3)==sorted(new_str)
    print(f"Is anagram of '{new_str}' : {is_anagram}")

    #VII
    words = str3.split()
    longest_word_length = max(len(word) for word in words)
    print(f"Length of the longest word: {longest_word_length}")

string_commands()

     