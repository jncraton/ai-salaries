import csv

with open("salaries.csv") as csvfile:
    rows = list(csv.reader(csvfile))

    # `rows` is now a list of lists containing the rows of the CSV

    # For example

    # rows[0] is the first row of the file
    # rows[0][0] is the first value in the first row

    # Compute and display the following items as detailed in the readme

    # 1. The total number of salaries in the file (remember not to include the header row)

    # 2. The average (mean) salary for entry-level positions

    # 3. The average (mean) salary for entry-level positions with a Data Scientist Title

    # 4. The highest salary for a fully remote, entry-level position

    # 5. The average (mean) salary for all mid-level positions
