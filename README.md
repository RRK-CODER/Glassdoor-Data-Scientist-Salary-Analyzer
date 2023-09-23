###  Glassdoor Data Scientist Salary Analyzer 

- Developed a salary estimation tool with a Mean Absolute Error (MAE) of approximately $11,000, aimed at assisting data scientists in optimizing their income negotiations upon securing employment.
- Employed Python and Selenium to systematically extract and analyze data from more than 1,500 live job listings on Glassdoor.
- Utilized advanced text analysis techniques to derive quantitative insights from the content of each job description, thereby assessing the significance companies attribute to proficiencies in Python, Excel, AWS, and Spark.
- Employed GridsearchCV to fine-tune Linear, Lasso, and Random Forest Regressors, optimizing model performance to achieve superior predictive accuracy.
- Developed a user-friendly client-facing API using Flask, facilitating seamless interaction with the salary estimation tool.

## Web Scraping
Tweaked the web scraper github repo (above) to scrape 1500 job postings from glassdoor.com. With each job, we got the following:
- Job title
- Salary Estimate
- Job Description
- Rating
- Company Name
- Location
- Size
- Founded
- Type of Ownership
- Industry
- Sector
- Revenue

## Data Cleaning
After scraping the data, conducted a data preprocessing phase to ensure its suitability for our model. Below are the modifications made and the variables created:

- Parsed numeric data out of salary
- Made columns for employer provided salary and hourly wages
- Removed rows without salary
- Parsed rating out of company text
- Made a new column for company state
- Added a column for if the job was at the company’s headquarters
- Transformed founded date into age of company
- Made columns for if different skills were listed in the job description:
    - Python
    - R
    - Excel
    - AWS
    - Spark
- Column for simplified job title and Seniority
- Column for description length

## Exploratory Data Analysis (EDA)
Conducted a comprehensive examination of data distributions and performed a detailed analysis of value counts for the diverse categorical variables. Presented below are select key insights gleaned from the pivot tables.
![Alt text](<EDA 1.png>) ![Alt text](<eda 2.png>) ![Alt text](<eda 3.png>)

## Model Building
Initially, categorical variables underwent a transformation into dummy variables. Subsequently, the dataset was partitioned into training and test sets, employing a test size of 20%.

Three distinct models were then employed, and their performance was assessed utilizing the Mean Absolute Error (MAE) metric. The selection of MAE was predicated on its ease of interpretation and the fact that it is less sensitive to outliers, aligning with the characteristics of this specific modeling context.

I tried three different models:

- Multiple Linear Regression – Baseline for the model
- Lasso Regression – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
- Random Forest – Again, with the sparsity associated with the data, I thought that this would be a good fit.

## Model performance
The Random Forest model far outperformed the other approaches on the test and validation sets.

- Random Forest : MAE = 11.22
- Linear Regression: MAE = 18.86
- Ridge Regression: MAE = 19.67

## Productionization
In this step, built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary.