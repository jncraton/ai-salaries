import pandas as pd

df = pd.read_csv("survey_results_public.csv")

df = df[
    [
        "Age",
        "CodeMain",
        "Employment",
        "WorkSetting",
        "YearsCode",
        "WorkExp",
        "Role",
        "OrgSize",
        "Industry",
        "JobSat",
        "Country",
        "Currency",
        "Compensation",
    ]
]

# Compensation is filtered to greater than 5000 to drop folks who entered their comp assuming it was expected to be in thousand (e.g. 150 instead of 150000)
df = df[
    (df["Employment"] == "Employed")
    & (df["Country"] == "United States of America")
    & (df["Currency"] == "USD United States dollar")
    & (df["Compensation"] > 5000.0)
    & (df["YearsCode"] > 0.0)
]

df = df[["Role", "WorkSetting", "WorkExp", "Industry", "JobSat", "Compensation"]]
df = df.dropna()

num_cols = df.select_dtypes(include="number").columns
df[num_cols] = df[num_cols].astype(int)

df["WorkSetting"] = (
    df["WorkSetting"].str.replace(r"\s*\([^)]*\)", "", regex=True).str.strip()
)
df["Role"] = df["Role"].str.replace(r"\s*\([^)]*\)", "", regex=True).str.strip()
df["Role"] = df["Role"].str.replace(r",.*$", "", regex=True).str.strip()
df["Industry"] = df["Industry"].str.replace(r",.*$", "", regex=True).str.strip()

df.to_csv("salaries.csv", index=False)

print(df["Role"].unique())
