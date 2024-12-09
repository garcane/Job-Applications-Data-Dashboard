# Generated from ChatGPT
import pandas as pd
import re

# Load the text file content
file_path = '/mnt/data/Application Document Analysis (Cleaned).txt'
with open(file_path, 'r') as file:
    content = file.read()

# Define a function to extract job application details from text
def extract_jobs(text):
    # Split entries using double newlines as delimiter
    entries = text.split("\n\n")
    
    job_data = []
    for entry in entries:
        # Extract company, position, date, salary, and location
        position = re.search(r"^(.*?)(?=\n|$)", entry)  # First line as position
        company = re.search(r"(?<=\n)(.*?)(?=\n|$)", entry)  # Second line as company
        date = re.search(r"(\d{2}/\d{2}/\d{4})", entry)  # Extract date
        salary = re.search(r"Salary: ([^\n]*)", entry)  # Extract salary
        location = re.search(r"Location: ([^\n]*)", entry)  # Extract location
        
        # Add extracted details to list, filling missing values with 'N/A'
        job_data.append({
            'Position': position.group(0).strip() if position else 'N/A',
            'Company': company.group(0).strip() if company else 'N/A',
            'Date': date.group(1).strip() if date else 'N/A',
            'Salary': salary.group(1).strip() if salary else 'N/A',
            'Location': location.group(1).strip() if location else 'N/A',
            'Stage': 'N/A'  # Default stage to N/A unless specified in the data
        })
    return job_data

# Extract job applications from the text content
jobs = extract_jobs(content)

# Create a DataFrame and reorder columns
df = pd.DataFrame(jobs)
df = df[['Company', 'Stage', 'Position', 'Applied', 'Date', 'Salary', 'Location']]
df['Stage'] = 'N/A'  # Ensure the "Stage" column exists as default 'N/A'


# Save to CSV
output_path = '/mnt/data/job_applications.csv'
df.to_csv(output_path, index=False)
output_path
