#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
string = input()
char = string[0]
result_string = char + string[1:].replace(char,'$')
print(result_string)

#ALternate Code
s=input()
s=s[0]+s[1:].replace(s[0],'$')
print(s)
