#there is a package called nltk. load it for this file.
import nltk

def open_file_and_get_text(filename):
    #given a filename, open it as a read-only file named 'our_file'
    with open(filename, "r") as our_file:
    #read the file's content and store it
        text = our_file.read()
    return text

def clean_tokens(tokens):
    #given some tokens, lowercase them all
    #create an empty list called clean_words
    clean_words = []

    #loop over every word item in the tokens list
    for word in tokens:
        #make each word lowercase and append it to the new list.
        clean_words.append(word.lower())
    return clean_words


#starting with a file: set a variable 'our_file' to eyre.txt
our_file = "eyre.txt"

#use method open_file_and_get_text
text = open_file_and_get_text(our_file)

#print the first 100 characters of the variable 'our_file'
print(text[0:100])

#take a long string and break it into words
words = nltk.word_tokenize(text)
clean_words = clean_tokens(words)

#print the first 30 words from clean_words.def clean_tokens(cleanwords):
print(clean_words[0:30])

word_counts = nltk.FreqDist(clean_words)
print(word_counts.most_common(10))
print("'Jane' appears " + str(word_counts['jane']) + " times in the text." )
nltk.Text(clean_words).dispersion_plot(['he', 'she', 'jane', 'tony'])"
