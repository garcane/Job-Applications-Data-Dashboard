# Job Applications Data Analysis

This project documents the process of analyzing data related to job applications, highlighting the data cleaning, transformation, and analysis steps performed to create a structured dataset for insights.

## Overview

The primary goal of this project was to transform unstructured data from a Word document into a clean and structured CSV file, suitable for further analysis. This dataset represents job applications, with details such as company, position, application date, location, and salary.

## Process

1. **Data Collection**:
   - Manually scraped job application details from the following websites, Gradcracker, Otta, Indeed, Totaljobs, Reed, Linkedin, CV Library. These are saved them in a Word document.

2. **Initial Cleaning in Word**:
   - Removed irrelevant text, including:
     - "No longer accepting applications"
     - "View cover letter"
     - "Job closed or expired on Indeed"
     - "This employer typically responds within X days"
     - Other redundant phrases are found in `Removed Target Words.txt`.
    
       

3. **Conversion to Text and CSV**:
   - Converted the cleaned Word document into a plain text file.
   - The Notion Job tracker had the predefined columns: `Company`, `Stage`, `Position`, `Applied`, `Date`, `Salary`, `Location`.
   - Using ChatGPT to transform the text into a CSV format with predefined columns: `Company`, `Stage`, `Position`, `Applied`, `Date`, `Salary`, `Location`.

4. **Manual Adjustments**:
   - Corrected column inconsistencies where job titles were placed under the `Company` column and vice versa.
   - Standardised date formats for consistency using 
   - For missing dates, generated random dates within the job hunting period using Excel.

5. **Salary Adjustments**:
   - Calculated mean averages for roles with salary ranges.
   - Research averaged salary using Glasssdoor and ChatGPT
   - Filled missing salary values through prompt engineering and Excel scripts such as
  
```excel
=RANDBETWEEN(lower_limit, upper_limit)
```


## Tools and Technologies
- **Microsoft Word**: Initial data cleaning.
- **ChatGPT**: Conversion of text data into CSV format.
- **Gemini**: Minor Excel formulas
- **Microsoft Excel**: Random date generation and manual adjustments.
- **Python**: Random date generator and automation.

## Files

- **`Application Document Analysis.docx`**: The initial cleaned Word document.
- **`Application Document Analysis (Cleaned).txt`**: Text version of the cleaned data.
- **`job_applications_final.csv`**: Final processed CSV file.

## Insights and Challenges

- The process revealed the importance of data consistency when dealing with unstructured formats.
- Automation with tools like ChatGPT significantly reduced manual effort.
- Handling missing data required a combination of statistical methods and logical inference.

## Future Work

- Automate the entire pipeline using Python scripts for scraping, cleaning, and transformation.
- Visualize the dataset using tools like Power BI or Tableau to identify application trends and success rates.
