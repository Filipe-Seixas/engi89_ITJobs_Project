from app.database import Database
from bs4 import BeautifulSoup
import requests
import sqlite3
from datetime import date


# Get today's date and create Database class object
today = date.today()
formatted_date = today.strftime("%d/%m/%Y")
data_bs = Database()


# --- SCRAPING --- #

# Get URL
url_text = requests.get("https://www.itjobswatch.co.uk/").text

# Create BeautifulSoup object
soup = BeautifulSoup(url_text, 'lxml')

# Get the main table with the job results
results = soup.find('table', class_='results')
# Find all table entries
jobs = results.find_all('tr')

# Find all table entries but use '[1:]' to skip the first entry which is the column titles and they don't share the
# same classes we're looking for
jobs = results.find_all('tr')[1:]
sep = " "

# Iterate through the table listings
for job in jobs:
    # Get the required data but only the text, also replace any unwanted special characters
    title = job.find('td', class_='c2').text.replace(" ", "_").replace("#", "_Sharp").replace(".", "dot_").replace("-", "_").replace("(", "").replace(")", "").replace("+", "_Plus")
    rank = job.find('td', class_='c3').text
    med_salary = float(job.find('td', class_='c5').text.replace("£", "").replace(",", ""))
    hist_ads = job.find('td', class_='c7').text.replace(",", "").split(sep, 1)[0]
    live_jobs = job.find('td', class_='c8').text.replace(",", "")
    # # Print it out
    # print(f'''
    #     Job Title: {title}
    #     Rank: {rank}
    #     Salary: {med_salary}
    #     Median Salary: {median_salary_change}
    #     Historical Permanent Job Ads: {hist_ads}
    #     Live Jobs: {live_jobs}
    #     ''')

    data_bs.database_initialise(title)
    data_bs.add_jobs(formatted_date, title, rank, med_salary, hist_ads, live_jobs)

data_bs.db.close()
