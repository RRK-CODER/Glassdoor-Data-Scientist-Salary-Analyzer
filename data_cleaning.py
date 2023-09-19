import pandas as pd
df = pd.read_csv('glassdoor_jobs.csv')

#Salary Parsing 
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1']

Salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = Salary.apply(lambda x: x.replace('K', '').replace('$', '').replace(' ', ''))
min_hr = minus_kd.apply(lambda x: x.lower().replace('perhour','').replace('employerprovidedsalary:', ''))

df['min_salary']=min_hr.apply(lambda x:round(float(x.split('-')[0])))
df['max_salary']=min_hr.apply(lambda x:round(float(x.split('-')[-1])))
df['avg_salary']= (df.min_salary+df.max_salary)/2

#Company Name , Text Only
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] ==-1 else x['Company Name'][:-3], axis=1)

#state field
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[-1])
df.job_state.value_counts()

#age of company
df['age'] = df.Founded.apply(lambda x: x if x<1 else 2023-x)

#parsing the job description (python etc.)
#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python_yn.value_counts()
#analysis/analyse/analysis
df['analysis_yn'] = df['Job Description'].apply(lambda x: 1 if 'analyse' in x.lower() or 'analytics' in x.lower() or 'analysis' in x.lower() else 0)
df.analysis_yn.value_counts()
#spark
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()
#aws
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() or 'amazon web services' in x.lower() else 0)
df.aws.value_counts()
#excel
df['Excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() or 'ms excel' in x.lower() or 'msexcel' in x.lower() else 0)
df.Excel.value_counts()


df.to_csv('salary_data_cleaned.csv', index=False)