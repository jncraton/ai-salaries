import csv
import requests

download = requests.get("https://ai-jobs.net/salaries/download/salaries.csv")

decoded_content = download.content.decode('utf-8')

with open('salaries.csv', 'w') as outcsv:
    writer = None

    for row in csv.DictReader(decoded_content.splitlines(), delimiter=','):
        if not writer:
            writer = csv.DictWriter(outcsv, fieldnames = row.keys())
            writer.writeheader()
            
        if row['work_year'] == '2023'  and row['company_location'] == 'US' and row['employment_type'] == 'FT' and row['experience_level'] in ('EN', 'MI'):
            writer.writerow(row)

print(f"Downloaded complete")

