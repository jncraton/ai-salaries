import pandas

df = pandas.read_csv("https://ai-jobs.net/salaries/download/salaries.csv")

df = df[(df.work_year == 2024) & (df.company_location == 'US') & (df.employment_type == 'FT') & (df.experience_level.isin(['EN', 'MI']))]

df = df.groupby('experience_level').apply(lambda x: x.sample(n=100)).reset_index(drop=True)

df = df.drop(["salary", "salary_currency"], axis=1)

df.to_csv("salaries.csv", index=False)
