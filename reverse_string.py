list = (input().split('.'))             #inputting he string and splitting it into words after each dot
list = list[::-1]                       #order of the created list is reversed
for words in list[:(len(list)-1)]:      #iterate through list to the secondlast word
    print(words,end='.')                #printing the output and statement is ended by dot
print(list[-1])                         #last word in the loop is printed
