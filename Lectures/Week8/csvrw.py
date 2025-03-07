from csv import writer
from csv import reader
outfile = open("chp7_b_stu_perform.csv", "w")
csvWriter = writer(outfile)

csvWriter.writerow(["Name", "Id", "Class", "Average"])
csvWriter.writerow(["John Smith", 1607, "Senior", 3.28])
csvWriter.writerow(["Mary Leigh", 2030, "Senior", 4.0])
csvWriter.writerow([])

outfile.close()

##
#  This program reads data from a csv file that contains movie information,
#  filters out unwanted data, and produces a new csv file.
#

from csv import reader, writer

# Open the two csv files.
infile = open("chp7_b_movies.csv", encoding="utf-8")
csvReader = reader(infile)

outfile = open("chp7_b_filtered_movies.csv", "w",encoding="utf-8" )
csvWriter = writer(outfile)

# Add the list of column headers to the csv file.
headers = ["Name","Year","Actors"]
csvWriter.writerow(headers)

# Skip the row of column headers in the reader.
next(csvReader)

# Filter the rows of data.
for row in csvReader :
  year = int(row[1])
  if year >= 1990 and year <= 1999 :
    newRow = [row[0], row[1], row[4]]
    csvWriter.writerow(newRow)

infile.close()
outfile.close()