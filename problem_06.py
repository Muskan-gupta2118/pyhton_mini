def palindrome(string):
    string_value=string.lower().replace(" ","");
    if string_value==string_value[::-1]:
        print("your current string is a palindrome");
    else:
        print("Your current string is not a palindrome ");
  
palindrome('women');          

    