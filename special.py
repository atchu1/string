string = input("Please Enter your Own String : ")
special = alphabets= digits=0

for i in range(len(string)):
    if(string[i].isalpha()):
        alphabets = alphabets + 1
    elif(string[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1
      
print("Total Number of Special Characters in this String :  ", special)
