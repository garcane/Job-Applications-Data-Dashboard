import pandas as pd
from datetime import datetime, timedelta
import random

# Load the uploaded CSV file
file_path = r'C:\Users\Student\Job Application\job_applications_final.csv'

# Try alternative encodings
data = pd.read_csv(file_path, encoding='latin1')  # Use 'latin1' to handle special characters

# Define the range for artificial dates
start_date = datetime(2024, 1, 5)
end_date = datetime(2024, 11, 28)

# Function to generate a random date between the start and end dates
def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

# Update date formatting and fill in missing dates
def standardize_date(date_str):
    if isinstance(date_str, float) or pd.isnull(date_str):
        return None  # Return None for non-string or missing values
    try:
        # Try parsing date in "August 18, 2024" format
        date_obj = datetime.strptime(date_str, "%B %d, %Y")
    except ValueError:
        try:
            # Try parsing date in "19/08/2024" format
            date_obj = datetime.strptime(date_str, "%d/%m/%Y")
        except ValueError:
            return None  # Mark as missing if not parseable
    return date_obj.strftime("%d %B %Y")

# Convert the 'Date' column to strings to handle mixed types
data['Date'] = data['Date'].astype(str)

# Apply the standardization function and generate random dates for "N/A"
data['Date'] = data['Date'].apply(
    lambda x: standardize_date(x) if x != 'N/A' and x != 'nan' else random_date(start_date, end_date).strftime("%d %B %Y")
)

# Save the updated data to a new CSV file
output_path = r'C:\Users\Student\Job Application\job_applications_updated.csv'
data.to_csv(output_path, index=False, encoding='utf-8')  # Save using UTF-8 encoding
print(f"Updated file saved at: {output_path}")
