import requests
import pandas as pd
import os

# Create data/raw folder if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

# Mutual Fund API URL
url = "https://api.mfapi.in/mf/125497"

# Fetch data
response = requests.get(url)

# Convert JSON to Python dictionary
data = response.json()

# Print Fund Name
print("Fund Name:", data["meta"]["scheme_name"])

# Convert NAV history into DataFrame
nav_df = pd.DataFrame(data["data"])

# Save CSV
scheme_name = data["meta"]["scheme_name"]

file_name = scheme_name.replace(" ", "_").replace("/", "_") + ".csv"

output_path = f"data/raw/{file_name}"
nav_df.to_csv(output_path, index=False)

print(f"\nData saved successfully to: {output_path}")
print(nav_df.head())