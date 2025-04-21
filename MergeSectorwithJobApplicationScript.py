import pandas as pd

# Load CSVs with encoding that handles BOM
applications_df = pd.read_csv(r"C:\Users\Student\Job-Applications-Data-Dashboard\job_applications_final.csv", encoding='latin1')
sectors_df = pd.read_csv(r"C:\Users\Student\Job-Applications-Data-Dashboard\Company Name with Sector.csv", encoding='utf-8')

# Clean and standardise column names
applications_df.columns = applications_df.columns.str.strip()
sectors_df.columns = sectors_df.columns.str.strip()

# Check for the correct company name column
if 'ï»¿Company Name' in sectors_df.columns:
    sectors_df.rename(columns={'ï»¿Company Name': 'Company'}, inplace=True)
elif 'Company Name' in sectors_df.columns:
    sectors_df.rename(columns={'Company Name': 'Company'}, inplace=True)

# Also rename company column in applications if needed
if 'Company' not in applications_df.columns:
    applications_df.rename(columns={'Company Name': 'Company'}, inplace=True)

# Standardise casing for merging
applications_df['Company'] = applications_df['Company'].str.strip().str.lower()
sectors_df['Company'] = sectors_df['Company'].str.strip().str.lower()

# Merge on Company
merged_df = pd.merge(
    applications_df,
    sectors_df[['Company', 'Sector']],
    on='Company',
    how='left',
    suffixes=('', '_from_sectors')
)

# Fill existing 'Sector' column or add it if it didn’t exist
if 'Sector' in applications_df.columns:
    merged_df['Sector'] = merged_df['Sector'].fillna(merged_df['Sector_from_sectors'])
    merged_df.drop(columns=['Sector_from_sectors'], inplace=True, errors='ignore')
else:
    merged_df.rename(columns={'Sector_from_sectors': 'Sector'}, inplace=True)

# Replace any remaining blank/NaN sectors with 'Unknown'
merged_df['Sector'] = merged_df['Sector'].fillna('Unknown')



# Save the result
merged_df.to_csv(r"C:\Users\Student\Job-Applications-Data-Dashboard\job_applications_final_updated_with_sector.csv", index=False)
print("✅ Merge completed and saved to 'job_applications_final_updated_with_sector.csv'")
