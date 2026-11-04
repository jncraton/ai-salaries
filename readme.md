AI Salaries
===========

This project provides and exploration of salaries in the Software Engineering, AI, ML, and data science fields. Salary data comes from the [Stack Overflow Developer Survey](https://github.com/StackExchange/Survey/tree/main/packages/archive/2026).

Learning Objectives
-------------------

After completing this assignment, students will be able to:

1. Access data from CSV files using the `csv` module
2. Work with data stored in nested lists
3. Apply filtering and aggregate functions to compute basic descriptive statistics

Data
----

A small subset of simplified data columns from the Stack Overflow Developer Survey is provided in `salaries.csv`. A desciption of the full dataset is [provided by StackExchange](https://github.com/StackExchange/Survey/tree/main/packages/archive/2026).

Here is a small sample from salaries.csv:

```csv
Role,WorkSetting,WorkExp,Industry,JobSat,Compensation
Developer,Remote,26,Government,9,195000
Architect,Remote,28,Retail,8,184000
Software engineer,Remote,16,IT services,4,300000
```

CSV Module
----------

The CSV module can be used to read rows from a CSV file as lists. This is demonstrated in the handout code in [salaries.py](salaries.py). This is the recommended starting point for reading data from [salaries.csv](salaries.csv).

Tasks
-----

Create a Python program that will output the following information:

1. The total number of salaries in the file (remember not to include the header row)
2. The average (mean) salary for entry-level positions
3. The average (mean) salary for entry-level positions with a Data Scientist Title
4. The highest salary for a fully remote, entry-level position
5. The average (mean) salary for all mid-level positions
6. A descriptive statistic of your choice calculated from this dataset

Here is roughly what the program should output when run:

```
There are 200 salaries in the file
Entry-level mean salary: $111k
Entry-level mean salary for Data Scientist job title: $121k
Highest entry-level remote salary: $177k
Mid-level mean salary: $166k
{A descriptive statistic of your choice}
```

Resources
---------

The following resources may help you to complete this assignment:

- [Python CSV module documentation](https://docs.python.org/3/library/csv.html)
- [PY4E Chapter 8: Lists](https://www.py4e.com/html3/08-lists)
- Functions such as [sum](https://docs.python.org/3/library/functions.html#sum) and [len](https://docs.python.org/3/library/functions.html#len)
