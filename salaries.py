import csv

with open("salaries.csv") as csvfile:
    rows = list(csv.reader(csvfile))

    # Rows is now a list of lists containing the rows of the CSV

    # For example

    # rows[0] is the first row of the file
    # rows[0][0] is the first value in the first row

    # Complete the program so that it produces the expected output
