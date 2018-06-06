#there is a package called nltk. load it for this file.
import nltk

#starting with a file: set a variable 'filename' to eyre.txt
filename = "eyre.txt"

#given a filename, open it as a read-only file named 'our_file'
with open(filename, "r") as our_file:
    #read the file's content and store it
    text = our_file.read()

#print the first 100 characters of the variable text
print(text[0:100])
