import glassdoor_scraper as gs
import pandas as pd

df = gs.get_jobs("data scientist", 2000, False)

df.to_csv('glassdoor_jobs.csv', index = False)