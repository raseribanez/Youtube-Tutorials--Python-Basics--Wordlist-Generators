# Ben Woodfield
# Version used for Youtube Tutorials and examples
# Uses shell window to gather user input and saves the list to a text document

#### THE TEXT DOCUMENT WILL SAVE IN THE SAME FOLDER AS THIS PYTHON PROGRAM IS SAVED AND RUN FROM ####
#### REMEMBER TO TYPE THE FILENAME WITH THE .TXT EXTENSION ####
#### USE (CTRL+C) TO KILL THE PROGRAM ####

#### IF YOU SET THE REQUIREMENTS TOO LONG YOU WILL BE WAITING A LONG TIME FOR YOUR RESULTS ####
#### THIS PROGRAM IS AUTOMATICALLY SET TO THE FULL ALPHABET IN LOWER CASE, AND ALSO NUMBERS ####
#### IF YOU CHOOSE LENGTH ANY LONGER THAN 3 THE RESULTS WILL TAKE A LONG TIME AND USE UP RAM AND PROCESSING POWER ####
#### SEE LINE 28 TO CHANGE THE LIST RESULT CHARACTERS ####

import time

print ("Welcome to List Generator!");
print ("");
print ("Press ^C to exit");
print ("---------------------------------------------------");
length=int(raw_input("Enter the maximum of characters: "))
name=raw_input("Enter destination file name with extension (.txt): ")
tic = time.clock()
print ("---------------------------------------------------");
print ("Running, Please Wait!");
print ("---------------------------------------------------");
lista=[0 for x in xrange(length)]
x=length-1
string="abcdefghijklnmopqrstuvwxyz1234567890" # Add/edit your list results preferences here
list_of_results=[]
file1=file(name,"w")
while(x>-1):
    result=""
    if lista[x]==len(string)-1:
        for z in xrange(length):
            result+=string[lista[z]]
        lista[x]=0
        x-=1
    elif x==length-1:
        for z in xrange(length):
            result+=string[lista[z]]
        lista[x]+=1
    else:
        for z in xrange(length):
            result+=string[lista[z]]
        lista[x]+=1
        if x>0:
            x+=1
        else:
            x=length-1
    file1.write(result+"\n")
toc = time.clock()
ttn = toc - tic
print ("Done! in "+str(ttn)+" seconds.");
print ("Please check "+str(name)+" in your directory");
print ("---------------------------------------------------");
