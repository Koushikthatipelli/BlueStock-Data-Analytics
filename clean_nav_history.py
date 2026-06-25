import pandas as pd
import os

# Read dataset
df = pd.read_csv("data/raw/nav_history.csv")

print("========== ORIGINAL DATA ==========")
print(df.head())

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort data
df = df.sort_values(
    by=["amfi_code", "date"]
)

# Remove duplicate rows
df = df.drop_duplicates()

# Remove invalid NAV values
df = df[df["nav"] > 0]

# Fill missing NAV values
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Create processed folder
os.makedirs("data/processed", exist_ok=True)

# Save cleaned file
df.to_csv(
    "data/processed/nav_history_cleaned.csv",
    index=False
)

print("\n✅ Cleaning Completed Successfully")
print(df.head())