import pandas as pd

# 1. Load the dataset
df = pd.read_csv("data.csv")
print("--- 1. Raw Data Overview ---")
print(df)
print("\nMissing values before cleaning:\n", df.isnull().sum())

# 2. Standardize column names (lowercase with underscores)
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# 3. Remove duplicate rows (removes duplicate Employee ID 102 - Priya Patel)
df = df.drop_duplicates(subset=["employee_id"], keep="first")

# 4. Handle missing values
# Fill missing categorical data with 'Unknown'
df["department"] = df["department"].fillna("Unknown")

# Fill missing numerical data with column median
df["age"] = df["age"].fillna(df["age"].median())
df["salary"] = df["salary"].fillna(df["salary"].median())

# 5. Convert data types & create derived columns
df["age"] = df["age"].astype(int)
df["join_date"] = pd.to_datetime(df["join_date"])
df["join_year"] = df["join_date"].dt.year

# 6. Perform aggregation / summary analysis
dept_summary = (
    df.groupby("department", as_index=False)
    .agg(
        employee_count=("employee_id", "count"),
        avg_age=("age", "mean"),
        avg_salary=("salary", "mean"),
        total_salary=("salary", "sum"),
    )
    .round(2)
)

print("\n--- 2. Cleaned Dataset ---")
print(df)

print("\n--- 3. Department-Wise Summary ---")
print(dept_summary)

# 7. Export processed results
df.to_csv("cleaned_data.csv", index=False)
dept_summary.to_csv("department_summary.csv", index=False)
print("\nSaved 'cleaned_data.csv' and 'department_summary.csv' successfully.")
