Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
    "X-DSPAM-Confidence:    0.8475"
Count these lines and extract the floating point values from each of the lines and compute the average of those values and
produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
# Use the file name mbox-short.txt as the file name


# 1st method, without using SUM() function
count=0
total=0.0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continuen
    else:
        count=count+1
        x=line[20:]
        y=float(x)
        total=total+y
print("Average spam confidence:",total/count)

------------------------------------------------------------------------------

# 2nd method, if we can use the SUM() function

alist=list()
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        x=line[20:]
        y=float(x)
        alist.append(y)
print("Average spam confidence:",sum(alist)/len(alist))
