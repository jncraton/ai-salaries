all: salaries.csv

salaries.csv:
	python3 download.py

clean:
