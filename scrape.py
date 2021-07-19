from bs4 import BeautifulSoup
import requests

# Get URL
url_text = requests.get("https://www.itjobswatch.co.uk/").text

# Create BeautifulSoup object
soup = BeautifulSoup(url_text, 'lxml')

# Get the main table with the job results
results = soup.find('table', class_='results')

# Find all table entries but use '[1:]' to skip the first entry which is the column titles and they don't share the
# same classes we're looking for
jobs = results.find_all('tr')[1:]

# Iterate through the table listings
for job in jobs:
    # Get the required data but only the text
    title = job.find('td', class_='c2').text
    rank = job.find('td', class_='c3').text
    salary = job.find('td', class_='c5').text
    median_salary = job.find('td', class_='c6').text
    hist_ads = job.find('td', class_='c7').text
    live_jobs = job.find('td', class_='c8').text

    # Print it out
    print(f'''
    Job Title: {title}
    Rank: {rank}
    Salary: {salary}
    Median Salary: {median_salary}
    Historical Permanent Job Ads: {hist_ads}
    Live Jobs: {live_jobs}
    ''')
