#Write a Python program to find the first appearance of the substring
def get_result(string):
    if string.find("not") != -1:
        start = string.find("not")
        end = string.find("poor",start,len(string))
        end += 4
        result_string = string[:start] + "good" + string[end:]
        return result_string 
    else:
        return string
    
string = input()
print(get_result(string))
        
