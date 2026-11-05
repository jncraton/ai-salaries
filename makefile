all: salaries.csv

survey_results_public.csv:
	wget https://github.com/StackExchange/Survey/raw/refs/heads/main/packages/archive/2026/survey_results_public.csv

salaries.csv: survey_results_public.csv
	python3 convert.py

format:
	uvx black .

clean:
	rm -f survey_results_public.csv
