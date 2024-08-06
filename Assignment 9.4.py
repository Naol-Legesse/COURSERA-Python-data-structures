#Assignment 9.4

#Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

#-------------------------------------------------------------------

#name = input("Enter file: ")
#if len(name) < 1:
    #name = "mbox-short.txt"
#fname=open(name)

words = list()
coll = dict()
file = open("mbox-short.txt")
for line in file:
    if line.startswith("From "):
        line=line.rstrip()
        nline=line.split()
        words.append(nline[1])
    else:
        continue
for word in words:
    if word not in coll:
        coll[word]=1
    else:
        coll[word]=coll[word]+1

largevalue=None
largeword=None
for key,value in coll.items():
    if largevalue is None or value>largevalue:
        largevalue=value
        largeword=key
print(largeword,largevalue)