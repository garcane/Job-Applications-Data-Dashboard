# Job Applications Dashboard
This project documents the process of cleaning data related to job applications, highlighting the data cleaning, transformation particularly from semi structured data into structured dats, and analysis steps performed to create a structured dataset for insights.
![Job Application Dashboard-1](https://github.com/user-attachments/assets/82195a76-a031-42a2-9719-f70bf93d07af)


## Overview
The primary goal of this project was to transform semi-structured data from a Word document to a cleaned text file into a clean and structured CSV file, suitable for further analysis. This dataset represents job applications, with details such as company, position, application date, location, and salary.

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
   - Using ChatGPT to transform the text into a CSV format with predefined columns: `Company`, `Stage`, `Position`, `Applied`, `Date`, `Salary`, `Location`. using this prompt:


I have these text document which contain all the job applications I have applied for. They have mixed formats for example this

```
Coding Trainee Placement Programme

Location: Nationwide

ITonlinelearning

16/01/2024 (20:55)
```

```
Trainee Business Analyst

LocalJobs4U

Salary: £25,000 - £27,000/annum

Location: WC2N, Charing Cross, Greater London

19/08/2024 (11:32)

```

or 

```
Data Analyst

Probus Recruitment Ltd

16/08/2024 (09:43)
```

or 

```
Data Scientist

Datasource

London

18/10/24
```

## Task Description

 I need you to create a CSV file from the text using the following headings
 
- **Company**
- **Stage**
- **Position**
- **Applied**
- **Date**
- **Salary**
- **Location**

If the job entry lacks **Location**, **Salary**, or **Stage**, fill those columns with `N/A`. The output should resemble the format:

```
Gracye, Rejected, Data Graduate, London, 12 August 2024, £26,800, London
```

### Deliverables

A downloadable CSV file.

The downloadable CSV file was then merged into the Notion CSV database.


4. **Manual Adjustments**:
   - Corrected column inconsistencies where job titles were placed under the `Company` column and vice versa.
   - Standardised date formats for consistency using 
   - For missing dates, generated random dates within the job hunting period using Excel.
   - Companies with the same corporation but had different names was standardised by using the official company name from the website


5. **Salary Adjustments**:
   - Calculated mean averages for roles with salary ranges.
   - Research averaged salary using Glassdoor and ChatGPT
   - Filled missing salary values through prompt engineering and Excel scripts such as
  
```excel
=RANDBETWEEN(lower_limit, upper_limit)
```


## Tools and Technologies
- **Microsoft Word**: Initial data cleaning.
- **ChatGPT**: Conversion of text data into CSV format.
- **Gemini**: Minor Excel formulas.
- **Claude**: Minor string reformatting.
- **Microsoft Excel**: Random date generation and manual adjustments.
- **Python**: Random date generator and automation.

## Files
- **`Application Document Analysis.docx`**: The initial cleaned Word document.
- **`Notion Job Tracker Applications Copy`**: The Notion Job Tracker
- **`Application Document Analysis (Cleaned).txt`**: Text version of the cleaned data.
- **`job_applications_final.csv`**: Final processed CSV file.
- **`Removed Target Words.txt`**: Key words removed from the Word document 

## Insights and Challenges
- The process revealed the importance of data consistency when dealing with unstructured formats.
- Automation with tools like ChatGPT significantly reduced manual effort.
- Handling missing data required a combination of statistical methods and logical inference.

## Methodology: Data Visualization and Analysis
1. **Data Preparation and Source**  
   - The data for this Power BI report was derived from a CSV file containing the following fields: `ID`, `Company`, `Stage`, `Position`, `Date`, `Salary`, and `Location`. This dataset captures key details of job applications, including the progress through various stages, positions applied for, corresponding salaries, and geographical locations.

2. **Report Creation**  
   - A comprehensive visual report was developed to provide a clear overview of the job application trends and outcomes. The report incorporates dynamic slicers to allow interactive filtering by important dimensions such as application stage, position, and date. These slicers enable users to drill down into specific subsets of the data for detailed insights.

3. **Visualization Design**  
   - Various visual elements were used to illustrate the data effectively:
     - A **KPI summary** at the top of the dashboard highlights key metrics such as the number of distinct locations, total job applications, average salary, and the total number of companies.
     - A **bar chart** displays the breakdown of job applications by stage, showcasing outcomes such as "Ghosted," "Rejected," and "Offered" for a quick overview of application success rates.
     - A **clustered bar chart** maps the number of companies and average salary by location, providing insights into the geographical distribution of job opportunities and associated remuneration.
     - A **line chart** tracks the number of job applications over time, revealing trends in monthly application activity.
     - An **interactive Sankey diagram** connects dimensions such as location, position, and company to show the flow of applications and associated outcomes.

4. **Insights and Recommendations**  
   - The visualizations are designed to deliver actionable insights. For instance, users can identify cities or companies with higher salary offerings, analyze the most common stages where applications are rejected, and observe trends in application volume to optimize job-seeking strategies.
   - Filtering by position (e.g., "Data Analyst") or location (e.g., "London, Greater London") enables targeted analysis, helping to refine strategies for job searching in specific sectors or areas.

5. **Enhancing Company Performance and Decision-Making**  
   - The insights provided by this dashboard can guide users or organizations in improving their application processes, focusing efforts on promising locations, and tailoring strategies to align with observed trends in hiring practices. 
