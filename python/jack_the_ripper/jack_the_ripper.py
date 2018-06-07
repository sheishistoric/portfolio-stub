#DO NOT run this file as is

#Get this CSV file onto your computer.
#(to do this, you have to be in the command line! go to the directory you want to be in, mkdir ~name~, and then curl ~website > ~name-of-new-file.csv)

#Successfully read in the CSV and prove that you did it by printing out the column headings.
import csv

with open('ripper.csv', 'r') as csvfile2:
    our_reader2 = csv.reader(csvfile2)
    headers = [row for row in our_reader2]

print(headers[0])

#Get all the texts of the press reports and store it in a variable called 'all_texts'. Print this variable out.
with open('ripper.csv', 'r') as csvfile3:
        our_reader3 = csv.reader(csvfile3)
        all_text = [row[4] for row in our_reader3]

print(all_text)

#What is the earliest date that an article was published?
with open('ripper.csv', 'r') as csvfile4:
        our_reader4 = csv.reader(csvfile4)
        dates = [row[3] for row in our_reader4]

print(min(dates))

#Write a new CSV with all the same data as the original CSV, but lowercase all the texts for the press reports.

with open('ripper.csv', 'r') as csvfile5:
    our_reader5 = csv.reader(csvfile5)
    new_results = [row for row in our_reader5]

for row in new_results:
    row[4] = row[4].lower()

with open('ripper2.csv', 'w') as csvfile5_1:
    writer = csv.writer(csvfile5_1)
    for row in new_results:
        writer.writerow(row)
