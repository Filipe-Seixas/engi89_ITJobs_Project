from bs4 import BeautifulSoup
import requests

# Get URL
url_text = requests.get("https://www.itjobswatch.co.uk/").text

# Create BeautifulSoup object
soup = BeautifulSoup(url_text, 'lxml')
# print(soup.prettify())
# tags = soup.find_all('td')  # Find all tags 'td'
# print(tags)

results = soup.find_all('table', class_='results')
print(results)
for result in results:
    job_salary = result.td
    print(job_salary)
    # print(result)
