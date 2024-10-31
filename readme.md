AI Salaries
===========

This project provides and exploration of salaries in AI, ML, and data science fields. Salary data comes from [ai-jobs.net](https://ai-jobs.net/).

Learning Objectives
-------------------

After completing this assignment, students will be able to:

1. Access data from CSV files using the `csv` module
2. Work with data stored in nested lists
3. Apply filtering and aggregate functions to compute basic descriptive statistics

Data
----

The following data dictionary is provided to understand the meaning of the underlying data. Note that the dataset ([salaries.csv](salaries.csv)) provided with this assignment is a subset of a [larger dataset](https://ai-jobs.net/salaries/download/). It includes only a sample of full-time, entry-level and mid-level jobs for 2024 in the United States.

```
0. work_year
    The year the salary was paid.

1. experience_level
    The experience level in the job during the year with the following possible values:

    EN        Entry-level / Junior
    MI        Mid-level / Intermediate
    SE        Senior-level / Expert
    EX        Executive-level / Director

2. employment_type
    The type of employement for the role:

    PT        Part-time
    FT        Full-time
    CT        Contract
    FL        Freelance

3. job_title
    The role worked in during the year.

4. salary_in_usd
    The salary in USD (FX rate divided by avg. USD rate of respective year) via statistical data from the BIS and central banks.

5. employee_residence
    Employee's primary country of residence in during the work year as an ISO 3166 country code.

6. remote_ratio
    The overall amount of work done remotely, possible values are as follows:

    0         No remote work (less than 20%)
    50        Partially remote/hybird
    100       Fully remote (more than 80%)

7. company_location
    The country of the employer's main office or contracting branch as an ISO 3166 country code.

8. company_size
    The average number of people that worked for the company during the year:

    S        less than 50 employees (small)
    M        50 to 250 employees (medium)
    L        more than 250 employees (large)
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
